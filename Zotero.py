# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:08:17 2021

@author: laoba
"""

from pyzotero import zotero
import os 
import os.path
import json

title=input()

def init():
    global zot
    global alldata
    global Z_link_Pre
    Z_link_Pre='zotero://select/library/items/'
    global pdf_link_Pre
    pdf_link_Pre='zotero://open-pdf/library/items/'
    library_id='6046496'
    api_key='NGt2DzfSOMS31n6WFTo1xCJ4'
    library_type='user'
    zot = zotero.Zotero(library_id, library_type, api_key)
    alldata= zot.everything(zot.top())
    global symbol_list
    symbol_list=['\\','?',':','']
    return 

'''class Zotero():
    def __init__(self):
        global zot
        global alldata
        global Z_link_Pre='zotero://select/library/items/'
        global pdf_link_Pre='zotero://open-pdf/library/items/'
        library_id='6046496'
        api_key='NGt2DzfSOMS31n6WFTo1xCJ4'
        library_type='user'
        zot = zotero.Zotero(library_id, library_type, api_key)
        alldata= zot.everything(zot.top())
        return 
'''
init()
    
# extract informations from article 
class Zotero_ref():              
    def __init__(self,title):
        #super().__init__()
        self.search_object(title)
        #get item_id
        self.id=self.object['key']
        #make the zotero link 
        self.Zlink=Z_link_Pre+self.id
        self.title=self.object['data']['title']
        self.itemtype=self.object['data']['itemType']
        #get the author list
        self.author()
        self.date=self.object['data']['date']
        #get the year
        self.year()
        #get the item type
        self.itemtype=self.object['data']['itemType']
        self.publication()  
        self.label()

        
    def search_object(self,title): #search object by title
        for item in alldata:
            if title.lower()==item['data']['title'].lower():
                self.object=item
                return self.object
        for item in alldata:
            if title.lower() in item['data']['title'].lower():
                self.object=item
                return self.object
        

            
                

    def author(self):
        author_d=self.object['data']['creators']
        self.authors=[]
        for item in author_d:
            author=item['lastName']+', '+item['firstName']
            self.authors.append(author)
    def year(self):
        if self.date!='':
            for i in range(len(self.date)):
                year=self.date[i:i+4]
                if year.isdigit():
                    self.year=year
                    break
                
    def publication(self):
        if self.itemtype=='conferencePaper':
            self.publication={
#                'pages':self.object['data']['pages'],
                'conference name':self.object['data']['conferenceName'],
                'publisher':self.object['data']['publisher'],
                }
        elif self.itemtype=='journalArticle':
            self.publication={
                'journaltitle':self.object['data']['publicationTitle'],
                'volume':self.object['data']['volume'],
                'pages':self.object['data']['pages'],
                }
        elif self.itemtype in ['book','bookSection']:
            self.publication={
                'edition':self.object['data']['edition'],
                'publisher':self.object['data']['publisher']
                }
        else:
            self.publication={}
        return 
    
    def label(self):
        part1=self.authors[0].split(', ')[0]
        part2=self.year
        List=self.title.split(' ')
        word_list=['a','an','the','from']
        for word in List:
            if word.isalpha() and word.lower() not in word_list:
                part3=word
                break 
        self.label=part1+part2+part3
        
            
        
 

dict1_note={'conferencePaper':['booktitle','pages','organization','inprocessings'],
     'joirnalArticle':['journaltitle','Volume','pages','article'],
     'book':['publisher','book']
     }

save_path_zotero='./output_zotero/'
if not os.path.isdir(save_path_zotero):
    os.mkdir(save_path_zotero)

        

class Zotero_attach():
    def __init__(self,object_id):
        super().__init__()
        self.search_attatch(object_id)
        self.link()
    
    def search_attatch(self,object_id): # search attatchment by id 
        self.attatch=zot.children(object_id,itemType='attachment',sort='dateAdded',direction='asc')
        
    def link(self):
        self.links=[]
        for item in self.attatch:
            item_key=item['key']
            item_type=item['data']['contentType']
            if item_type =='application/pdf':
                link=pdf_link_Pre+item_key
            else:
                link=Z_link_Pre+item_key
            self.links.append(link)
#        self.links=attatch_link
   




                

class Roam_convert():
    def __init__(self,ref,attach):
        # Title:  
        self.title='Title: '+ref.title
        # Author:
        self.authors='Authors: '+'[[Au. '+']],[[Au. '.join(article.authors)+']]'
        # get year 
        self.year='Year: '+ref.year
        # get link to local library
        self.Zlink='[local library]('+ref.Zlink+')'
        #get item type 
        self.itemtype='Type: '+ref.itemtype
        # get link for attatchment
        self.link(attach)
        self.filename='Ref. '+ref.label+'.md'
        # get the publication
        self.publication(ref)
        self.write_markdown()
        
    
    def link(self,attach):
        self.links=[]
        for link in attach.links:
            if 'pdf' in link:
                link_R='[Pdf link]('+link+')'
            else:
                link_R='[Other link]('+link+')'
            self.links.append(link_R)
            
    def publication(self,ref):
        self.publication=[]
        for info in ref.publication:
            info_R=info+': '+ref.publication[info]
            self.publication.append(info_R)
    
        
    
    def write_markdown(self):
        with open(save_path_zotero+self.filename, 'w',encoding='UTF-8') as new_f:
            new_f.writelines("%s\n" %self.title)
            new_f.writelines("%s\n" %self.authors)
            new_f.writelines("%s\n" %self.year)
            new_f.writelines("%s\n" %self.Zlink)
            for link in self.links:
                new_f.writelines("%s\n" % link)
            new_f.writelines("%s\n" %self.itemtype)
            for info in self.publication:
                new_f.writelines("%s\n" % info)
                
      

    


        
        
        
#attatch_d=zot.children(data_id,itemType='attachment',sort='dateAdded',direction='asc')
    
            
    
        
        
        






#extract inforamtion form Zotero 
article=Zotero_ref(title)
attach=Zotero_attach(article.id)
roam=Roam_convert(article,attach)


#Convert information 


'''

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
    
    


#local_link='zotero://select/library/items/'
pdf_link='zotero://open-pdf/library/items/'



if 'Ref. ' in search_name:
    search_name=search_name.replace('Ref.  ','')
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


'''