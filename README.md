This is used to extract top keywords from a transcript of an audio file.
This uses NLTK kit from python.
Fore more information, please read code comments

It has two functionalities
1. Return the top 10 keywords with the count (number of occurences)
2. Return the top 10 keywords with the timestamp at which they occurred

Usage:

If the name of text file is 'sample.txt'

To get the word count json:
keywords_with_word_count('sample', 'sample_output')

Sample output for word count json:
{"data": [["phone", 18], ["thing", 17], ["car", 17], ["time", 12], ["distraction", 10], ["way", 9], ["voice", 9], ["android", 8], ["task", 7], ["lot", 7], ["experience", 7], ["today", 7], ["auto", 6], ["people", 6], ["platform", 6]]}

###############################################################################################

To get the timestamp json:
keywords_with_timestamps('sample', 'sample_output')

Sample output for timestamp json:
{"data": [{"timestamps": ["466.500000", "469.590000", "491.970000", "493.860000", "533.100000", "570.790000", "578.050000"], "keyword": "task"}]}



