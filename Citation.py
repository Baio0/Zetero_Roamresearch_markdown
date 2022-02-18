# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 14:56:53 2021

@author: laoba
"""

import json
import os 
import os.path
dict = {
'Entropic optimal transport is maximum-likelihood deconvolution' : 'rigollet2018entropic',
'hello':'yes'
}
json = json.dumps(dict)
    
save_path_L='./output_latex/'
if not os.path.isdir(save_path_L):
    os.mkdir(save_path_L)

with open(save_path_L+'Citation_F.json', 'w') as f:
    f.write(json)
