# Using this function to do the preprocessing and cleaning
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
import nltk; nltk.download('stopwords')
from nltk.corpus import stopwords
form index_utils import CLEANING

# collect intro and plot in same place and the cleaning them, beside that I've made a list of unique words for each doc

clean_df = pd.DataFrame()
for i in df.index:
    clean_df.loc[i,'text'] =' '.join(df[['intro', 'plot']].loc[i].dropna())
clean_df['unique_words'] = clean_df['text'].map(set)
clean_df['text'] = clean_df['text'].map(CLEANING) 

# bagofword containing a list of all words

bagofword = CLEANING(script)

# It's a set of unique words 
all_vocab = set(bagofword)

# term_id and vocab These dict save the term and term id 
dic_of_term_id = {}
dic_of_vocab = {}
for i,j in enumerate(all_vocab):
    num = 'term_' + str(i)
    dic_of_vocab[j] = num
    dic_of_term_id[num] = j

    
clean_df = pd.DataFrame()
for i in df.index:
    
    clean_df.loc[i,'text'] =' '.join(df[['intro', 'plot']].loc[i].dropna())   
    no = []

# here I made a dict of term_id and doc_ic which shows each word exists in which doc
vocabulary = {}
for i in clean_df.index:
    for word in clean_df.loc[i,'unique_words']:
        if dic_of_vocab[word] in vocabulary.keys():
            vocabulary[dic_of_vocab[word]].append('doc_' + str(i))
        elif dic_of_vocab[word] not in vocabulary.keys():
            vocabulary[dic_of_vocab[word]] = ['doc_' + str(i)]
        else:
            no.append(word)
    
