def WORD_COUNT(word , doc):
    count = 0
    for w in doc:
        if w == word:
            count+=1              
    return count
    
    # Using this function to do the preprocessing and cleaning
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
import nltk; nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(nltk.corpus.stopwords.words('english'))

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
    
    
    
def inverted_index (clean_df,dic_of_vocab):  
  no =[]
  inverted_index ={}
  for i in clean_df.index:
      for word in clean_df.loc[i,'text']:
          if dic_of_vocab[word] not in inverted_index.keys():
              inverted_index[dic_of_vocab[word]] = []
          if word in dic_of_vocab.keys() :
              inverted_index[dic_of_vocab[word]].append('doc_' +str(i))
          elif word not in dic_of_vocab.keys() : 
              no.append(word)
    return  inverted_index , no       

import pickle 

pickle.dump( inverted_index  , open( "inverted_index_in_PART", "wb"))
pickle.dump( vocabulary  , open( "vocabulary_in_PART", "wb" ))
pickle.dump( dic_of_term_id  , open( "dic_of_term_id_in_PART", "wb"))
pickle.dump( dic_of_vocab  , open( "dic_of_vocab_in_PART", "wb" ))
