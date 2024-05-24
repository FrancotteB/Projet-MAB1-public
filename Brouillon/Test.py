# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 11:51:37 2024

@author: basti
"""

import pandas as pd
import matplotlib.pyplot as plt
from utils import *

n_appart = 'A101'

data = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\NivreHourlyDataWithNBBedroom.csv')

da102=dappart(data, n_appart)
d2=dnchbre(data, 2)

da102elec = delec(da102)
da102ecs = decs(da102)

d2elec = delec(d2)
d2ecs = decs(d2)


d2elechiver, d2elecprin, d2elecete, d2elecaut = saison(d2elec)
da1023sem = filtre(da102elec, '2022-11-28', 3)
d102h, d102p, d102e, d102a = saison(da102elec)

d2f, d2o = holids(d2elechiver, 2022)
#da102f, da102o = holids(da1023sem)
da102f, da102o = holids(d102h, 2022)





#%%
print("\n\n\n")
print("Pas normalise :")
ma102 = moytemp(da102elec)
m2 = moytemp(d2elec)
#affim(m2)
comp(ma102, m2)
Rmse = cvrmseM(ma102, m2)
Nmbe = nmbeM(ma102, m2)

#%%
ma102h = moytemp(d102h)
#ma102h = moytemp(da1023sem)
m2h = moytemp(d2elecprin)
#affim(m2h)
comp(ma102h, m2h)
Rmseh = cvrmseM(ma102h, m2h)
Nmbeh = nmbeM(ma102h, m2h)

#%%
ma102f = moytemp(da102f)
m2f = moytemp(d2f)
#affim(m2f)
comp(ma102f, m2f)
Rmsef = cvrmseM(ma102f, m2f)
Nmbef = nmbeM(ma102f, m2f)


ma102o = moytemp(da102o)
m2o = moytemp(d2o)
#affim(m2o)
comp(ma102o, m2o)
Rmseo = cvrmseM(ma102o, m2o)
Nmbeo = nmbeM(ma102o, m2o)


#%%
print("\n")
print("Normalise methode 1:")
nma102 = norm(ma102)
nm2 = norm(m2)
comp(nma102, nm2)
rmseN1 = cvrmseM(nma102, nm2)
NmbeN1 = nmbeM(nma102, nm2)

nma102h = norm(ma102h)
nm2h = norm(m2h)
comp(nma102h, nm2h)
rmseN1h = cvrmseM(nma102h, nm2h)
NmbeN1h = nmbeM(nma102h, nm2h)

nma102f = norm(ma102f)
nm2f = norm(m2f)
comp(nma102f, nm2f)
rmseN1f = cvrmseM(nma102f, nm2f)
NmbeN1f = nmbeM(nma102f, nm2f)

nma102o = norm(ma102o)
nm2o = norm(m2o)
comp(nma102o, nm2o)
rmseN1o = cvrmseM(nma102o, nm2o)
NmbeN1o = nmbeM(nma102o, nm2o)

#%%
print("\n")
print('Normalise methode 2:')
nma102_2 = norm2(ma102)
nm2_2 = norm2(m2)
comp(nma102_2, nm2_2)
rmseN2 = cvrmseM(nma102_2, nm2_2)
NmbeN2 = nmbeM(nma102_2, nm2_2)

#%%
nma102h2 = norm2(ma102h)
nm2h2 = norm2(m2h)
comp(nma102h2, nm2h2)
rmseN2h = cvrmseM(nma102h2, nm2h2)
NmbeN2h = nmbeM(nma102h2, nm2h2)

nma102f2 = norm2(ma102f)
nm2f2 = norm2(m2f)
comp(nma102f2, nm2f2)
rmseN2f = cvrmseM(nma102f2, nm2f2)
NmbeN2f = nmbeM(nma102f2, nm2f2)

nma102o2 = norm2(ma102o)
nm2o2 = norm2(m2o)
comp(nma102o2, nm2o2)
rmseN2o = cvrmseM(nma102o2, nm2o2)
NmbeN2o = nmbeM(nma102o2, nm2o2)

#%%
print("\n")
print('Normalise methode 3:')
nma102_3 = norm3(ma102)
nm2_3 = norm3(m2)
comp(nma102_3, nm2_3)
rmseN2 = cvrmseM(nma102_3, nm2_3)
NmbeN2 = nmbeM(nma102_3, nm2_3)

nma102h3 = norm3(ma102h)
nm2h3 = norm3(m2h)
comp(nma102h3, nm2h3)
rmseN2h = cvrmseM(nma102h3, nm2h3)
NmbeN2h = nmbeM(nma102h3, nm2h3)

nma102f3 = norm3(ma102f)
nm2f3 = norm3(m2f)
comp(nma102f3, nm2f3)
rmseN2f = cvrmseM(nma102f3, nm2f3)
NmbeN2f = nmbeM(nma102f3, nm2f3)

nma102o3 = norm3(ma102o)
nm2o3 = norm3(m2o)
comp(nma102o3, nm2o3)
rmseN2o = cvrmseM(nma102o3, nm2o3)
NmbeN2o = nmbeM(nma102o3, nm2o3)


