#import pandas as pd
#import re                         # Regular expressions
from nltk.corpus import stopwords # Filter out stopwords, such as 'the', 'or', 'and'
#import gensim
#import wordcloud
#from collections import Counter



def textcleaner (text)    :
    #text = convert_pdf_to_txt(path) # Get the text from this

    lines = (line.strip() for line in text.splitlines()) # break into lines

    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # break multi-headlines into a line each

    #text = ''.join(chunk for chunk in chunks if chunk).encode('utf-8') # Get rid of all blank lines and ends of line
    # Now clean out all of the unicode junk (this line works great!!!)

    try:
        text = text.decode('unicode_escape').encode('ascii', 'ignore') # Need this as some websites aren't formatted
    except:                                                            # in a way that this works, can occasionally throw
         'no'                                                        # an exception
    #
    text = re.sub("[^a-zA-Z+3]"," ", text)  # Now get rid of any terms that aren't words (include 3 for d3.js)
                                             # Also include + for C++

    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text) # Fix spacing issue from merged words

    text = text.lower().split()  # Go to lower case and split them apart

    stop_words = set(stopwords.words("english")) # Filter out any stop words
    text = [w for w in text if not w in stop_words]

    text = list(set(text)) # Last, just get the set of these. Ignore counts (we are just looking at whether a term existed
                           # or not on the website)
    return text
