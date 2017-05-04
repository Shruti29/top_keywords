This is used to extract top keywords from a transcript of an audio file.
This uses NLTK kit from python.
Fore more information, please read code comments

This extracts the top keywords from a text file
It has two functionalities
1. Return the top 10 keywords with the count (number of occurences)
2. Return the top 10 keywords with the timestamp at which they occurred

It creates a word count json in the same directory
It created a timestamp json in the same directory

Usage:

If the name of text file is 'sample2'

To get the word count json:
keywords_with_word_count('sample2')

To get the timestamp json:
keywords_with_timestamps('sample2')

