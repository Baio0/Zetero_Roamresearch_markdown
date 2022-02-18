# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:39:38 2021

@author: laoba
"""

import markdown
import json
import os 
import os.path
# importing required modules 
from zipfile import ZipFile 
import re
import math
#import BeautifulSoup
import pypandoc




#get the list of all folder and files 
#download file
download_path='./download/'
ext_path='./extract/'
if not os.path.isdir(ext_path):
    os.mkdir(save_path)


filelist=os.listdir(download_path)
#search the roam-export folder

for name in filelist[:]:
    if 'export' not in name.lower() or '.zip' not in name:
        filelist.remove(name)

if len(filelist)>=1:
    zip_name=filelist[0]

    # opening the zip file in READ mode 
    ext_path='./extract/'
    if not os.path.isdir(ext_path):
        os.mkdir(ext_path)
        #clean the extract folder before we use it. 
        filelist_de=os.listdir(ext_path)
    for file in filelist_de:
        os.remove(ext_path+file)



    with ZipFile(download_path+zip_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 

        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall(ext_path) 
        print('Done!') 
    


#Convert it to a markdown
# clear the output folder
save_path_md='./output_md/'
if not os.path.isdir(save_path_md):
    os.mkdir(save_path_md)

convert_path_md='./convert_md/'
if not os.path.isdir(convert_path_md):
    os.mkdir(convert_path_md)
    
#filelist_de=os.listdir(save_path_md)
#for file in filelist_de:
#    os.remove(file)

#get the list of markdown file
filelist1=os.listdir(ext_path)

for name in filelist1[:]:
    if '.md' not in name:
        filelist1.remove(name)

for name in filelist1:
    with open(ext_path+name, 'r',encoding='UTF-8') as f:
        text = f.read()
    #convert 
    text=text.replace('$$','$')# Change the math enviroment 
    for i in range(6):
        bullet_sign1='\n'+i*4*' '+'- '
        if i==0: # Move all the bullet to left
            bullet_sign2='\n'
        else:
            bullet_sign2='\n'+(i-1)*4*' '+'- '
        text=text.replace(bullet_sign1,bullet_sign2)

    #while '\n\n' in text:
    #    text=text.replace('\n\n','\n')
    text=text.replace('- ![]','![]') # Remove the bullet symbol of picture 
    while ' \n' in text:
        text=text.replace(' \n','\n')# remove all the space before the enter
    text=text.replace('[[','**')
    text=text.replace(']]','**')
    
    
    #print(text)

    completename=os.path.join(save_path_md,name)
    with open(completename, 'w',encoding='UTF-8') as f:
        f.write(text)
    #convert markdown to pdf 

#    output = pypandoc.convert_file(completename, 'pdf','md', outputfile=convert_path_md+name[0:-3]+'.pdf')
#    assert output == ""

def findbracket(text,left_symbol='[[',right_symbol=']]'):
    left_symbol_length=len(left_symbol)
    right_symbol_length=len(right_symbol)
    local1=text.find(left_symbol)
    local2=A[local1+left_symbol_length-1].text.find(right_symbol)
    symbol_extract=A[local1:local2+right_symbol_length]
    A[local1:local2+right_symbol_length]=None


    

#Latex function area

def envolope(body,begin=None,end=None,cover=None):
    if cover==None:
        if begin!=None:
            body=begin+body
        if end!=None:
            body=body+end
        return body
    else:
        if begin!=None:
            loc_begin=cover.find(begin)+len(begin)
            body=cover[0:loc_begin]+body+cover[loc_begin:]
        elif end!=None:
            loc_end=cover.find(end)
            body=cover[0:loc_end]+body+cover[loc_end:]
        return body


def Str_repeat(a=' ',n=1):
    c=''
    for i in range(n):
        c=c+a
    return c

def Str_depth(text):
    K=[]
    S=[]
    D={}
    for n in range(200):
        C1=Str_repeat(' ',n)+'- '
        C0='\n'+C1
        if C0 in text:
            K.append(n)
            S.append(C0)
            D[n]=C0
        elif C1 not in text:
            break
    K=sorted(K)
    return [K,S,D]


def get_block(text,Str):
    str_loc=text.find(Str)
    if str_loc!=-1:
        [depth_list,depth_str_list,depth_dict]=Str_depth(text)  
        #find block end        
        block_end=len(text)
        for depth_str in depth_str_list:
            end=text.find(depth_str,str_loc)
            if end!=-1:
                block_end=min(block_end,end)
        #find begin and level
        begin=0
        level=-1
        for depth in depth_list:
            depth_str='\n'+Str_repeat(' ',depth)+'- '
            loc=text.rfind(depth_str,0,block_end)
            if loc!=-1 and loc>=begin:
                begin=loc
                level=depth
        #find level end
        level_end=len(text)
        for depth in depth_list:
            depth_str='\n'+Str_repeat(' ',level)+'- '
            end=text.find(depth_str,str_loc)
            if depth<=level and end!=-1:
                level_end=min(level_end,text.find(depth_str,str_loc))
        return [str_loc, level, begin+level+3, block_end,level_end]

def Str_replace(text,Str,begin=None,end=None):
    if begin==None:
        begin=end
    elif end==None:
        end=begin
    return text[0:begin]+Str+text[end:]


    
def Str_findall(text,Str,begin=0,end=None):
    if end==None:
        end=len(text)
    K=[]
    loc=text.find(Str,begin,end)
    while loc!=-1:
        K.append(loc)
        begin=loc+len(Str)
        loc=text.find(Str,begin,end)
    return K

    
def Str_cut(body):
    while body[0] in [' ']:
        body=body[1:]
    while body[-1] in [' ']:
        body=body[0:-1]
    return body

                 
            

# for text convert
def reference_convert(obj):
    ref=''
    ref_L=''
    while '[[Ref' in obj:
        ref=term_convert(obj,['[[Ref. ',']]'])[0]
        if ref in citation_data:
            ref1=citation_data[ref]
        obj=term_convert(obj,['[[Ref. ',']]'],['\\cite{','}'],term_re=ref1)
    return obj



#def obj_check_name(obj):
def In_Structure_check(text,loc,Struc=['[',']']):
    if Struc[0]!=Struc[1]:
        loc0=text.rfind(Struc[0],0,loc)
        if loc0!=-1 and Struc[1] in text[loc0:loc]:
            return False
        elif loc0!=-1 and Struc[1] not in text[loc0:loc]:
            return True
        elif loc0==-1:
            return False
        
    elif Struc[0]==Struc[1]:
        #get the occurence of one string
        occ_num=len(Str_findall(text,Struc[0],0,loc))
        if occ_num%2 ==0: #even number
            return False
        else:
            return True
    
def bound_find(obj,Struc=['[',']'],bound_str=':'):
    bound=obj.find(bound_str)
    if bound!=-1:
        while bound!=-1:
            if not In_Structure_check(obj,bound,Struc):
                return bound
            else:
                bound=obj.find(bound_str,bound+len(bound_str))
        bound=-1
        return bound
           
def term_convert(obj,struc_orig=['(',')'],struc_new=None,Type='in',end=None,term_re=None):
    '''either replace a structure or find a structure, replace a special term with replaced term, orig_term,replace should be 2-d list of string'''
    if end==None:
        end=len(obj)
    if struc_new==None:
        struc_new=struc_orig

    term_begin=obj.find(struc_orig[0])
    if Type=='de':
        term_end=obj.rfind(struc_orig[1],term_begin,end)
    elif Type=='in':
        term_end=obj.find(struc_orig[1],term_begin+len(struc_orig[0]),end)
    
    term=obj[term_begin:term_end] #This is the original term, if we use the final version, we may made empty term to be non-empty one. 
    if term_re!=None:
        term_new=struc_new[0]+term_re+struc_new[1]
        term=term[len(struc_orig[0]):]
    elif term_re==None and term!='':
        term=term[len(struc_orig[0]):]
        term_new=struc_new[0]+term+struc_new[1]
    elif term_re==None and term=='':
        term_new=''
    obj=Str_replace(obj,term_new,term_begin,term_end+len(struc_orig[1]))
    return [obj,term]

def bullet_convert1(body):
    depth_list=Str_depth(body)[0]
    if len(depth_list)==0:# it does not contain any structure. 
        return body
    elif len(depth_list)>=1: 
        depth=depth_list[0]
        bullet_str='\n'+Str_repeat(' ',depth)+'- '
        #bullet_begin=body.find(bullet_str)
        bullet_list=body.split(bullet_str)
        bullet_list[0]=bullet_list[0]+'\\begin{itemize}'
        for i in range(1,len(bullet_list)):
            item=bullet_list[i]
            bullet_list[i]='  '+bullet_convert1(item)
        body='\n\\item '.join(bullet_list)+'\n\\end{itemize}'
        return body
    
def bullet_convert2(body):
    depth_list=Str_depth(body)[0]
    if len(depth_list)==0:# it does not contain any structure. 
        return body
    elif len(depth_list)>=1:
        depth=depth_list[0]
        bullet_str='\n'+Str_repeat(' ',depth)+'- '
        bound=body.find(bullet_str)
        pre=body[0:bound]
        bullet=body[bound:]
        for i in range(len(depth_list)):
            depth=depth_list[i]
            bullet_str='\n'+Str_repeat(' ',depth)+'- '
            bullet_str_new='\n'+Str_repeat(' ',i+1)+'\\'+str(i+1)+' '
            bullet=bullet.replace(bullet_str,bullet_str_new)
        body=pre+'\\begin{outline}'+bullet +'\\end{outline}'
        return body

class Complex:
    def __init__(self, a):
        a=a+1
        
    
    

def Theorem_convert(text,Str='Theorem',div_str='**'):
    Str1=div_str+Str
    # find the Theom_begin
    [Thm_loc,level,block_begin,block_end,level_end]=get_block(text,Str1)
    Thm_begin=Thm_loc
    #find theorem end
    if text[block_end-1] in [':']:
        end1=level_end
    elif text[block_end-1] in ['.','$']:# '$' means we use math formula to end. In this case, we can not use '.' to end. 
        end1=block_end
    elif text[block_end-1] in [')','}']:
        loc1=text.rfind('.',block_begin,block_end)
        loc2=text.rfind(':',block_begin,block_end)
        if loc1>=loc2:
            end1=block_end
        else:
            end1=level_end
    end2=text.rfind('$\square$',Thm_begin,level_end)
    print(text[block_begin:block_end])
    if end2==-1:
        Thm_end=end1
    else:
        Thm_end=min(end1,end2)
    #get the Theorem
    obj=text[Thm_begin:Thm_end]
    
    #get the bound between head and body
    bound=0
    for struc in struc_list:
        bound=max(bound,bound_find(obj,struc))
    #get the head
    head=obj[0:bound]
    loc1=head.find(div_str,len(Str1))
    name1=head[loc1+3:]
    [c1,name2]=term_convert(head,['(',')'],['(',')'],'de',bound)
    if len(name2)<=1/2*len(name1):
        name=name1
    else: 
        name=name2
    name_L=''
    if name!='':
        name_L='['+name+']'
    #get the body: 
    body=obj[bound+1:]
    body_level=get_block(body,body)[3]
    if body_level==0:
        body='We have: '+body
    #[Thm_loc,level,block_begin,block_end,level_end]=get_block(obj,body)

    body=bullet_convert2(body)
    # construct latex verstion
    obj_L='\\begin{'+Str.lower()+'}'+name_L+'\n'+body+'\n\\end{'+Str.lower()+'}\n'
    text=Str_replace(text,obj_L,Thm_begin,Thm_end)
    # delete the level of theorem
    text=text[0:block_begin-level-2]+text[block_begin-2:]
    return text


    
def proof_convert(text):
    [Pf_loc,level,block_begin,block_end,level_end]=get_block(text,'__Proof')
#    print('before')
#    print(block_begin)
    #get the beginning of the proof
    Pf_begin=block_begin
    if block_begin<Pf_loc:
        begin_str_list=['\n','.']
        for begin_str in begin_str_list:
            begin1=text.rfind(begin_str,block_begin,Pf_loc)
            Pf_begin=max(Pf_begin,begin1)
    #get the end of the proof
    end2=text.rfind('$$\\square$',Pf_loc,level_end)
    if end2!=-1:
        Pf_end=end2
    else:
        Pf_end=level_end
    Pf=text[Pf_begin:Pf_end]

    #get the boundary of the proof
    bound=0
    for struc in struc_list:
        bound=max(bound,bound_find(Pf,struc))
    name=Pf[0:bound]
    name=name.replace('__','')
    List=name.split(' ')
    if len(List)<=1:
        name=''
    else:
        name='['+name+']'
    body=Pf[bound+1:]
    #convert body
    #body=bound_convert(body)
    body=bullet_convert2(body)

    Pf_L='\\begin{proof}'+name+'\n'+body+'\n\\end{proof}\n'
    text=Str_replace(text,Pf_L,Pf_begin,Pf_end)

    # delete the level of proof
    text=text[0:block_begin-level-2]+text[block_begin-2:]
    return text
    



    
# #Convert it to latex

# #get the list of markdown file
# filelist_ext=os.listdir(ext_path)
# #need to use \\ to represent \ in a String
# save_path_L='./output_latex/'
# if not os.path.isdir(save_path_L):
#     os.mkdir(save_path_L)


# zotero_path='./output_zotero/'
# if not os.path.isdir(zotero_path):
#     os.mkdir(zotero_path)
    
# with open(save_path_L+'head.tex','r',encoding='UTF-8') as f:
#     head_L=f.read()    
# with open(save_path_L+'Citation_F.json','r',encoding='UTF-8') as f:
#     citation_data = json.load(f)
    

# for filename in filelist_ext[:]:
#     if '.md' not in name:
#         filelist_ext.remove(name)
# for filename in filelist_ext:
#     with open(ext_path+filename, 'r',encoding='UTF-8') as f:
#         text = f.read()
#     #pre-convert 
#     text=text.replace('$$','$')
#     while '\n\n' in text:
#         text=text.replace('\n\n','\n')
#     #delete all the space in end of block
#     while ' \n' in text:
#         text=text.replace(' \n','\n')
#     #delete all the space in the begining of block
#     while '-  ' in text:
#         text=text.replace('-  ','- ')
    
#     # pre-convert for latex
#     text='\n'+text
#     text=text.replace('$\\begin{aligned}','\\begin{align*}')
#     text=text.replace('\\end{aligned}$','\\end{align*}')
    
    
#     # Convert reference 
#     while '[[Ref' in text:
#         ref=term_convert(text,['[[Ref. ',']]'],['[[Ref. ',']]'])[1] #get the reference 
#         if ref in citation_data:
#             ref=citation_data[ref]
#         text=term_convert(text,['[[Ref. ',']]'],['\\cite{','}'],term_re=ref)[0] #convert the reference

#     #delete all the pyerlink
#     while '([[' in text and ']])' in text:
#         text=term_convert(text,['([[',']])'],['',''],term_re='')[0]
#     #delete all the double linkd
#     while '[[' in text and ']]' in text:
#         text=term_convert(text,['[[',']]'],['\\emph{','}'])[0]

    
#     struc_list=[['\\cite{','}'] #for citation
#                 ,['(',')'] # for math
#                 ,['[[',']]']] #for hyperlink
#     text1=text

 
#     #convert theorem
#     Part_list=['Theorem','Corollary','Proposition','Lemma','Definition']
#     div_str='**'
#     for Str in Part_list:
#         while div_str+Str in text:
#             text=Theorem_convert(text,Str,div_str)
#     while '__Proof' in text:
#         text=proof_convert(text)
    
#     # we make all the defintion, theorem, proof to be the first level
#     textlist=text.split('\n- ')
#     for i in range(len(textlist)):
#         part=textlist[i]
#         part=bullet_convert1(part)

#         textlist[i]=part
#     text='\n'.join(textlist)
#     text=envolope(text,end='%document_end',cover=head_L)

    

#     filename=save_path_L+filename[0:-3]+'.tex'
#     with open(filename, 'w',encoding='UTF-8') as f:
#         f.write(text)
    

    

        
        



    
    
    
        
            




    