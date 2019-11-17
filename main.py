from itertools import chain
from  collections import Counter
import heapq

def search_engine():
    a = input("Please define which seach engine you want to use 2 or 3: ")
    if a=='2':
        search_2(query)
    
    elif a=='3':
        search_3(query)
    else:
        a= input("please insert a valid search engine 2 or 3 :")
        

def jaccard(s1, s2):
    s1 ,s2 = set(s1), set(s2) 
    intersect = s1.intersection(s2)
    return len(intersect)/(len(s1.union(s2)))

def Euclidean(s1,s2):
    return np.linalg.norm(s1-s2)
    

def WORD_COUNT(word , doc):
    count = 0
    for w in doc:
        if w == word:
            count+=1              
    return count

def COSINE_SIMIL(s1, s2): 
    return np.dot(s1,s2)/ (np.sqrt(sum(s1**2)) * np.sqrt(sum(s2**2)))    
        
        
        
def search_2(query):
  N= 30000

  query = set(CLEANING(input('Please enter your: ')))
  n = len(query)
  answer = []
  l = np.zeros(n)

  for o,q in enumerate(query):
      try:
          answer += vocabulary[dic_of_vocab[q]]
          l[o] = (WORD_COUNT(q ,query ) /n )*np.log(N/len(dic_of_vocab[q]))
      except:
          pass

  c = Counter(answer).most_common(7)
  docs_list = [x for x,y in c]

  sim= {} 
  for doc in docs_list:
      sim[doc] = np.zeros(n)
      for o,q in enumerate(query):
          try:
              sim[doc][o] = [b for a,b in inverted_index[dic_of_vocab[q]] if a == doc][0]
          except:
              pass   
              
  similarity = {}           
  for s in sim.keys():
      similarity[s] = COSINE_SIMIL(l , sim[s] ) 

  doc_num = sorted(similarity.items(), key=lambda x: x[1] , reverse=True)

  table = df.loc[[int(e.split('_')[1]) for e,r in doc_num], ['title' , 'intro','wili_urls' , 'Similarity'] ]
  table['Similarity'] = [r for e,r in doc_num]

  retrun table[['title' , 'intro','wili_urls' , 'Similarity'] ]        
        
        
def search_3(query):
    df_search = search_2(query)
   
    import heapq
    seach_3_col = ['title' , 'intro','wili_urls' , 'Similarity']
    search_3 = []
    list_info = []
    heapq.heapify(search_3)

    for wi in query:
        list_info += inverted_index_moreinfo[wi]


    cn = Counter(list_info ).most_common(15)
    docs_list_info = [x for x,y in c]    

    for ii in docs_list_info:
            heapq.heappush(search_3 , (10*jaccard(query , clean_df.loc[int(ii.split('_')[1]),'more_info']) ,ii))

    jac_info =  heapq.nlargest(5, search_3)       
    jac_simil = [int(e.split('_')[1] )for r,e in jac_info]

    indx_seach3 =[]
    for cod in jac_simil:
        if cod in df_search.index:
            df_search.loc[cod, 'Similarity'] += float(*[f for f,g in jac_info if int(g.split('_')[1]) == cod])
        else:
            indx_seach3.append(cod)


    df_search = pd.concat([ df_search, df.loc[indx_seach3, seach_3_col]], axis=0 )
    df_search.loc[ indx_seach3, 'Similarity'] =  [f for f,g in jac_info if int(g.split('_')[1]) in indx_seach3 ]                      

    return df_search.sort_values('Similarity',ascending=False)
        
        
        
        
        
        
 search_engine(query)
