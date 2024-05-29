# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:05:35 2024

@author: basti
"""

import pandas as pd
import matplotlib.pyplot as plt
from utils import *
import os

datanum = pd.read_csv('path_number_bedroom')
data2 = pd.read_csv('path_data2023_wonb')
data2023 = pd.merge(data2, datanum, on='apartName')
data2022 = pd.read_csv('path_data_2022_wnb')



#%%
D22, P22 = gene(data2022, 2022)
D23, P23 = gene(data2023, 2022)



#%%
import os


folder_name = 'profils'
# Créez le dossier s'il n'existe pas déjà
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Exporter chaque DataFrame en fichier .csv dans le dossier spécifié
for name, df in P22.items():
    file_path = os.path.join(folder_name, f'{name}.csv')
    df.to_csv(file_path, index=False)

print(f'All files have been saved in the folder: {folder_name}')

#%%

# Exemple de comparaison

acomp22 = P22['db1_ef_f_aut_mnorm']
acomp23 = P23['db1_ef_f_aut_mnorm']
acompapp = papp['db1_ef_f_aut_mnorm']

comp(acomp23, acomp22)
rmse = cvrmseM(acomp23, acomp22)
Nmbe = nmbeM(acomp23, acomp22)







