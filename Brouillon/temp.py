# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import pandas as pd
import matplotlib.pyplot as plt
from utils import *

da101=dappart('A101')

d2=dnchbre(2)

da101elec = delec(da101)

da101ecs = decs(da101)

#Da101elec=todt(da101elec)

#Da101ecs=todt(da101ecs)

d2elec = delec(d2)

#D2elec=todt(d2elec)

m=moytemp(da101elec)

m2=moytemp(da101ecs)

m3=moytemp(d2elec)



d1803 = dj(da101elec, '2022-03-18')
affi(d1803)
#test = dsum(d1803)
#plt.plot(test)
#plt.show()

affim(m)
affim(m2)
affim(m3)

A1, A2 = holids(d2elec)

M1 = moytemp(A1)
M2 = moytemp(A2)

affim(M1)
affim(M2)

B = saison(d2elec)

