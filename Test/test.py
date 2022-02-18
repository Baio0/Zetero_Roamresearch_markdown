# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:54:36 2021

@author: laoba
"""

import json



def search(Data, searchfor):
    if type(Data)==str:
        if searchfor in Data:
            return Data
        else:
            return None
    elif type(Data)==list:
        for item in Data:
            C=search(item, searchfor)
            if C!=None:
                return C
    elif type(Data)==dict:
        for key in Data:
            if searchfor in key:
                return dict[key]
            else: 
                C=search(Data[key],searchfor)
                if C!=None:
                    return C
    return None 


with open('roam-export.json',encoding='utf-8') as f:
  data = json.load(f)[0]

author=search(data,'Author')
#loc_au=author_d.find('::')
author=author.replace('[[','[[Au: ')
author=author.replace('::',':')



link=search(data,'links')
loc1_Zlink=link.find('Local')+14
loc2_Zlink=link.find('Web')-3
Zlink='[local library]'+link[loc1_Zlink:loc2_Zlink]

loc_pdflink=link.find('pdf')+4
pdflink='[link]'+link[loc_pdflink:]


with open('roam.json', 'w') as new_f:
    new_f.writelines("%s\n" % title)
    new_f.writelines("%s\n" % author)
    new_f.writelines("%s\n" % Zlink)
    new_f.writelines("%s\n" % pdflink)
    
    

