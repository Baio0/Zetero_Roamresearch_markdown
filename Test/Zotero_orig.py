# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:08:17 2021

@author: laoba
"""

from pyzotero import zotero
import os 
import os.path
import json

search_name='''Real and Complex Analysis'''
#class Zotero():
#    def __init__(self):
library_id='6046496'
api_key='NGt2DzfSOMS31n6WFTo1xCJ4'
library_type='user'
zot = zotero.Zotero(library_id, library_type, api_key)
data_all= zot.everything(zot.top())
     
      

def search(Data, searchfor,Type='None'):
    if type(Data)==str:
        if searchfor.lower() in Data.lower(): 
            return Data
        else:
            return None
    elif type(Data)==list:
        for item in Data:
            C=search(item, searchfor,Type)
            if C!=None:
                if Type=='list':
                    return Data
                else:
                    return C            
    elif type(Data)==dict:
        for key in Data:
            if searchfor in key:
                return Data[key]
            else:
                C=search(Data[key],searchfor,Type)
                if C!=None:
                    if Type=='dict':
                        return Data
                    else:
                        return C
    return None

def search_title(Data,searchfor):
    for item in data_all:
        if searchfor.lower() in item['data']['title'].lower():
            return item
    


local_link='zotero://select/library/items/'
pdf_link='zotero://open-pdf/library/items/'


#'''Analysis and Geometry of Markov Diffusion Operators'''
if 'Ref. ' in search_name:
    search_name=search_name.replace('Ref. ','')
data=search_title(data_all,search_name)

#data=search(data_all,search_name,Type='dict')

#get item_id
data_id=data['key']

#get item title 
#title=search(data,'title')
title=data['data']['title']
title_R='Title: '+title

#filename_R=(title+'.md').replace(':','.')

#get item_Zoterolink
Zlink=local_link+data_id
Zlink_R='[Local Library]('+Zlink+')'


# get Author 
#author_d=search(data,'author','list')
author_d=data['data']['creators']


author_list=[]
author_list_R=[]
for i in author_d:
    author=i['lastName']+', '+i['firstName']
    author_list.append(author)
    author_list_R.append('[[Au. '+author+']]')

author_R='Author(s): '+', '.join(author_list_R)

#get the year 
year_d=data['data']['date']
if len(year_d)>=1:
    for i in range(len(year_d)):
        year=year_d[i:i+4]
        if year.isdigit():
            break
else:
    year=''
year_R='Year: '+year

#get itemtype
itemtype=data['data']['itemType']
if 'article' in itemtype.lower():
    itemtype=itemtype.replace('Article',' article')
itemtype_R='Type: '+itemtype



    
#Construct a label for file name
label_1=author_list[0].split(', ')[0]
label_2=year
c=title.split(' ')[0]
if len(c)<=3:
    label_3=title.split(' ')[1]
else:
    label_3=title.split(' ')[0]
label=label_1+label_2+label_3

symbol_list=[':','/'
             ]
for symbol in symbol_list:
    if symbol in label:
        label=label.replace(symbol,'')



filename_R='Ref. '+label+'.md'





#Get the journal of publication
pub_list=['publicationTitle','bookTitle']
for item in pub_list:
    try: 
        pub_title=data['data'][item]
        break
    except:
        pub_title=''
        print(item+' do not find')


try:
    publisher_R='[['+data['data']['publisher']+']]'
except:
    publisher_R=''



#Get link of Attatchment 
attatch_d=zot.children(data_id,itemType='attachment',sort='dateAdded',direction='asc')
# can not remove item when iteratie it, so we iterate a copy of it., 
#for item in attatch_d[:]:
#    K=search(item,'linkMode')
#    if K!='imported_file':
#        attatch_d.remove(item)


attatch_link_R=[]
for item in attatch_d:
    item_key=item['key']
    C=search(item,'contentType')
    if 'pdf' in C:
        #make pdf link
        link='[Pdf link]('+pdf_link+item_key+')'
    else:
        link='[Other link]('+local_link+item_key+')'
    attatch_link_R.append(link)

save_path_zotero='./output_zotero/'
if not os.path.isdir(save_path_zotero):
    os.mkdir(save_path_zotero)

with open(save_path_zotero+filename_R, 'w',encoding='UTF-8') as new_f:
    new_f.writelines("%s\n" %title_R)
    new_f.writelines("%s\n" % author_R)
    new_f.writelines("%s\n" % year_R)
    new_f.writelines("%s\n" % Zlink_R)
    for link in attatch_link_R:
        new_f.writelines("%s\n" % link)
    new_f.writelines("%s\n"% itemtype_R)
    if pub_title!='':
        new_f.writelines('Publication: '+"%s\n" % pub_title)
    if publisher_R!='':
        new_f.writelines('Publisher: '+"%s\n" % publisher_R)

        


#make the bib
save_path_L='./output_latex/'
with open(save_path_L+'references.bib','r',encoding='UTF-8') as f:
    ref_bib=f.read()
#with open(save_path_L+'citation_F.json','r',encoding='UTF-8') as f1:
#    citation=json.load(f1)
    

#Get the type
itemtype=data['data']['itemType']
itemtype_bib=itemtype
if 'article'in itemtype.lower():
    itemtype_bib='article'



#Get the author
author_bib='author = {'+' and '.join(author_list)+'}'

#get title
title_bib='title = {'+title+'}'

#Get the year
#year=search(data,'date')[0:4] # need to make sure 
#date=data['data']['date']
#symbol_list=['/']
#end=False
#for i in range(len(date)-3):
#    year=date[i:i+4]
#    for symbol in symbol_list:
#        if symbol in year:
#            break
#        end=True
#    if end==True:
#        break
    
            
        
year_bib='year ={'+year+'}'

#get the publication:
#journal=search(data,'publicationTitle')
# pub_list=['publicationTitle','bookTitle']
# for item in pub_list:
#     try: 
#         pub_title=data['data'][item]
#         break
#     except:
#         pub_title=''
#         print(item+' do not find')

#get the publication type
if 'bookTitle' in data['data']:
    pub_pre='booktitle={'
elif itemtype_bib in ['article']:
    pub_pre='journal={'
elif 'arXiv' in pub_title:
    pub_pre='journal={'

pub_title_bib=''

if pub_title!='':
    pub_title_bib=pub_pre+pub_title+'}'
    
# get volumne and page
try:
    volume_bib='volume={'+data['data']['volume']+'}'
except:
    volume_bib=''
try:
    pages_bib='pages={'+data['data']['pages']+'}'
except:
    pages_bib=''

#get publisher 一个是出版社, 一个是期刊名字
try:
    publisher_bib='publisher={'+data['data']['publisher']+'}'
except:
    publisher_bib=''



# make the label
label_1=author_list[0].split(', ')[0].lower()
label_2=year
c=title.split(' ')[0]
if len(c)<=3:
    label_3=title.split(' ')[1].lower()
else:
    label_3=title.split(' ')[0].lower()
label_bib=label_1+label_2+label_3

print(label_bib)
#write the bib
bib_list=['@'+itemtype_bib+'{'+label_bib,title_bib,author_bib,pub_title_bib,volume_bib,pages_bib,year_bib,publisher_bib]
if title not in ref_bib:
    with open(save_path_L+'references.bib','a',encoding='UTF-8') as f:
        f.writelines("\n")
        for item in bib_list:
            if item!='':
                f.writelines('%s\n' %item)

#write the mapping dict 


# if title not in citation:
#     citation[title]=label_bib
#     json = json.dumps(citation)
#     with open(save_path_L+'citation_F.json', 'w',encoding='UTF-8') as f:
#         #json.dump({title:label_bib},f)
#         #f.write(os.linesep)
#         f.write(json)

        
        






        

    
        

    
        





    # we've retrieved the latest five top-level items in our library
    # we can print each item's item type and ID
#for item in items:
#    print('Item Type: %s | Key: %s' % (item['data']['itemType'], item['data']['key']))

