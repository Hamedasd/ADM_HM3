import csv , os, glob , random, time , codecs
import pandas as pd
import requests, urllib
from bs4 import BeautifulSoup
import requests as rq
import time
import random
from parser_utils import intro_text, plot_text

columns =[ 'title', 'intro', 'plot','Directed by','Produced by','Written by','Screenplay by','Story by','Based on','Starring','Narrated by','Music by','Cinematography','Edited by','Production','company','Distributed by','Release date','Running time','Country','Language','Budget','Box','office']
df = pd.DataFrame(columns=columns)

E = []
j = 0
for link in htmlfiles:
    try:
        html_wiki  = open(link , 'r')
        soup = BeautifulSoup(html_wiki ,'html.parser')
        
        df.loc[j , 'title'] = soup.find('h1').get_text()
        df.loc[j ,'intro'] =  intro_text(soup)
        if df.loc[j ,'intro']=='':
            try:
                df.loc[j ,'intro'] =soup.find('p').find_next_sibling('p').text.strip()
            except:
                pass    
        for x,y in  zip(soup.find('table', class_="infobox vevent").find_all('th') , soup.find('table', class_="infobox vevent").find_all('td')):
                if x.text.strip() in columns:
                    df.loc[j , x.text.strip()] = y.text.strip()

        try:
            df.loc[j ,'plot'] = plot_text(soup)
            
        except:
            pass
        
    except :
         E.append(link)
    j+=1 
# add urls to the data frame 
df['wili_urls'] = url_list 
# write whole data to CSV
df.to_csv('wiki_articles.csv', encoding='utf-8')  


for k in range(df.shape[0]):
    
    output = os.path.join('wiki_Articles_tvs' , 'article_' + str(k) + '.tsv')
    with open(output, 'wt' , encoding='utf-8') as out_file:
        tsv_writer = csv.writer(out_file, delimiter ='\t' )
        tsv_writer.writerow(df.loc[k])
        
 # make one text file of all of intro and plots

script =''
for i in df.index:
    script += ' '+' '.join( df.loc[i,['intro', 'plot']].dropna())
    
    
    
