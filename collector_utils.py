import os
def WRITER(i , soup):
  save_path = os.getcwd()
  f = open( os.path.join(save_path+'article_'+str(i)+'.html','w'))
  f.write(str(soup.encode('ascii').decode('ascii')))
  f.close()
