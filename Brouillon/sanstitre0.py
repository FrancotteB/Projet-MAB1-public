# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 12:55:28 2024

@author: basti
"""
import pandas as pd
import matplotlib.pyplot as plt
import holidays
from utils import *


be_holidays = holidays.Belgium(years=2022)

# Créer un DataFrame pour l'année 2022
dates = pd.date_range(start='2022-01-01', end='2022-12-31')

# Créer un DataFrame à partir des dates
df_jours = pd.DataFrame({'date': dates})

# Ajouter une colonne pour les jours fériés
df_jours['ferie'] = df_jours['date'].isin(be_holidays)

# Ajouter une colonne pour les jours ouvrables
df_jours['ouvrable'] = ~df_jours['date'].isin(be_holidays)

# Afficher le DataFrame avec les jours fériés et ouvrables
print(df_jours)