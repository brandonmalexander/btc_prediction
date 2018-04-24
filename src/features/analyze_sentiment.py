from textblob import TextBlob
import pandas as pd
import re


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


def clean_text(s):
    """ Remove non alphabetic characters. E.g. 'B:a,n+a1n$a' becomes 'Banana' """

    s = re.sub("[^a-z A-Z]", "", s)
    s = s.replace(' n ', ' ')
    return s


read = 'raw_reddit_data_final.csv'

rawtextdata = pd.read_csv(filepath_or_buffer=read, infer_datetime_format=True)
rawtextdata = rawtextdata.set_index(rawtextdata.columns[0])

cleanedtextdata = rawtextdata.fillna('0')

sentimentdata = cleanedtextdata.applymap(lambda x: TextBlob(x).sentiment.polarity)

sentimentdata.to_csv(path_or_buf='reddit_sentiment_data_final.csv')
