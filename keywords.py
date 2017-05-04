import nltk
import sys
import json
import os.path
import collections
from nltk.tokenize import regexp_tokenize
from nltk.util import ngrams
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from collections import Counter
from collections import OrderedDict
from nltk.corpus import stopwords


def get_lemmatize_pos(tag):
    if tag.startswith('N'):
        return 'n'
    elif tag.startswith('V'):
        return 'v'
    elif tag.startswith('J'):
        return 'a'
    elif tag.startswith('R'):
        return 'r'
    else:
        return ''

def keywords_with_word_count(filename):
    if os.path.isfile(filename+'.json') and os.path.isfile(filename+'.txt'):
        # To prevent unicode errors
        reload(sys)
        sys.setdefaultencoding("utf-8")

        # Extract top 10 keywords from text file
        keywords_wc = keywords_all(filename+'.txt')
        value = map(list, keywords_wc.items())
        value = sorted(value, key = lambda x: int(x[1]), reverse=True)
        wc_json = {}
        wc_json['data'] = value

        # Write to output file
        with open(filename+'.wc.json', 'w') as output_file:
            json.dump(wc_json, output_file)


def keywords_with_timestamps(filename):
    if os.path.isfile(filename+'.json') and os.path.isfile(filename+'.txt'):
        # To prevent unicode errors
        reload(sys)
        sys.setdefaultencoding("utf-8")

        # Read json input file
        json_file = open(filename+'.json').read()
        json_data = json.loads(json_file)
        json_keywords = json_data['words'] #List of json
        #ts_json = {}

        # Extract top 10 keywords
        keywords_wc = keywords_all(filename+'.txt') #Dictionary

        # Created the require output
        result_json_value = []
        for ele in keywords_wc.items():
            ts_json = {}
	    ts_values = []
            for key in json_keywords:
                if ele[0] == key['name']:
                    ts_values.append(key['time'])
            ts_json["keyword"] = ele[0]
            ts_json["timestamps"] = ts_values
            result_json_value.append(ts_json)
        result_json = {}
        result_json['data'] = result_json_value

        #Write to the output file
        with open(filename+'.ts.json', 'w') as output_file:
            json.dump(result_json, output_file)





def keywords_all(filename):

    f = open(filename, 'r')
    result = []
    wlem = WordNetLemmatizer()
    # Remove stop words and pronouns and articles
    result_tagged = []
    for line in f.readlines():
        if not line.startswith("SPEAKER:"):
            line = unicode(line, errors='ignore')
            line = regexp_tokenize(line, pattern='\w+')
            result_tagged.append(pos_tag(line))

    #Extract only nouns and foreign words
    result_stoplist=[]
    for line in result_tagged:
        for l in line:
            if l[1]=='FW' or l[1].startswith('N'):
                result_stoplist.append(l)

    #Lemmatize the extracted words
    result_lemmatize= []
    for ele in result_stoplist:
        if len(ele[1]) != 1:
            if get_lemmatize_pos(ele[1]) != '':
            #print ele[0] + " " + wlem.lemmatize(ele[0], get_lemmatize_pos(ele[1]))
                result_lemmatize.append(wlem.lemmatize(ele[0], get_lemmatize_pos(ele[1])))
            else:
                result_lemmatize.append(ele[0])

    # Get the count of all words
    count = Counter(result_lemmatize)

    # Sort in descending order
    sorted_by_count = sorted(count, key=count.get, reverse=True)
    keyword_wc = {}
    for key in sorted_by_count:
        keyword_wc[key] = count[key]
    sorted_keyword = OrderedDict(sorted(keyword_wc.items(), key=lambda x:x[1], reverse=True))

    # Return only the top 10 words
    top_10_sorted_keyword = collections.Counter(sorted_keyword).most_common(10)
    return dict(top_10_sorted_keyword)

keywords_with_word_count('sample2')
keywords_with_timestamps('sample2')
