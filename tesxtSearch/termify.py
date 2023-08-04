import re
import stopwords

#####################################
###  Preprocess a string to a list of terms
###  This is the same version of termify used to produce the TFIDF values stored in S3

def termify(line):
    terms = []
    words = re.findall(r'[^\W_]+', line)
    for word in words:
        lowered = word.lower()
        if (len(lowered) > 1) and (lowered not in stopwords.stopwords) and (not re.search(r'^\d*$', lowered)):
            terms.append(lowered)
    return terms