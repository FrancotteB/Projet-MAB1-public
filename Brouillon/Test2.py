# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:33:20 2024

@author: basti
"""

import pandas as pd
import matplotlib.pyplot as plt
from utils import *

datanum = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\ApartmentNBBedroom.csv')
data2 = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\NivreHourlyData2023.csv')
data2023 = pd.merge(data2, datanum, on='apartName')
data2022 = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\NivreHourlyDataWithNBBedroom.csv')


#Split en fct du nbre cde chbre
d22_1=dnchbre(data2022, 1)
d22_2=dnchbre(data2022, 2)
d22_3=dnchbre(data2022, 3)

d23_1=dnchbre(data2023, 1)
d23_2=dnchbre(data2023, 2)
d23_3=dnchbre(data2023, 3)


#Split elec, ecs, ef, chauff
d22_1elec = delec(d22_1)
d22_1ecs = decs(d22_1)
d22_1ef = deef(d22_1)
d22_1chau = dchau(d22_1)

d22_2elec = delec(d22_2)
d22_2ecs = decs(d22_2)
d22_2ef = deef(d22_2)
d22_2chau = dchau(d22_2)

d22_3elec = delec(d22_3)
d22_3ecs = decs(d22_3)
d22_3ef = deef(d22_3)
d22_3chau = dchau(d22_3)


d23_1elec = delec(d23_1)
d23_1ecs = decs(d23_1)
d23_1ef = deef(d23_1)
d23_1chau = dchau(d23_1)

d23_2elec = delec(d23_2)
d23_2ecs = decs(d23_2)
d23_2ef = deef(d23_2)
d23_2chau = dchau(d23_2)

d23_3elec = delec(d23_3)
d23_3ecs = decs(d23_3)
d23_3ef = deef(d23_3)
d23_3chau = dchau(d23_3)
