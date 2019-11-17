# Using this function to do the preprocessing and cleaning
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
import nltk; nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

# THis fun do all the preproccessing and cleaning
def CLEANING(string):
    string = string.lower() 
    tokenizer = RegexpTokenizer("[\w']+")  
    clean_text = tokenizer.tokenize(string)
    clean_words = []
    for word in clean_text:
        if word not in stop_words:
            clean_words.append(word)
    lemmatizer = WordNetLemmatizer() 
    lemmat = [lemmatizer.lemmatize(wor) for wor in clean_words]
    ps = PorterStemmer()
    bagofword = [ps.stem(w) for w in lemmat]
    return bagofword
