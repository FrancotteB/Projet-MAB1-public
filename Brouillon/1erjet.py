# -*- coding: utf-8 -*-
"""
@author: bastien
"""

import pandas as pd
import matplotlib.pyplot as plt
import holidays




# Charger le fichier CSV dans un DataFrame
data = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\NivreHourlyDataWithNBBedroom.csv')


be_holidays = holidays.Belgium(years=2022)

# Filtrer les données pour afficher uniquement les conso de l'appartement 'A001'
data_appart = data[data['apartName'] == 'A203']


# Filtrer les données pour chque type de chambre
data_1chbre = data[data['nbBedroom'] == 1]
data_2chbre = data[data['nbBedroom'] == 2]
data_3chbre = data[data['nbBedroom'] == 3]

print(data_appart)


liste_noms_appartements = data['apartName'].unique()


print(liste_noms_appartements)


liste_compteur = data['meterType'].unique()

print(liste_compteur)



data_elec = data_appart[data_appart['meterType'] == 'Compteur ECS 1']

conso = data_elec['consumption']
time = data_elec['datetime']

#plt.plot(time.iloc[:24],conso.iloc[:24])
#plt.show()


data_elec['datetime'] = pd.to_datetime(data_elec['datetime'])

# Créer une colonne 'date' avec la date
data_elec['date'] = data_elec['datetime'].dt.date

# Créer une colonne 'time' avec l'heure
data_elec['time'] = data_elec['datetime'].dt.time


print(data_elec)



data_1chbre['datetime'] = pd.to_datetime(data_1chbre['datetime'])

# Créer une colonne 'date' avec la date
data_1chbre['date'] = data_1chbre['datetime'].dt.date

# Créer une colonne 'time' avec l'heure
data_1chbre['time'] = data_1chbre['datetime'].dt.time





donnees_temporaires = []

# Boucler sur chaque heure unique
for heure in data_1chbre['time'].unique():
    # Filtrer les lignes où 'time' est égal à l'heure en cours
    valeurs_a_moyenner = data_1chbre.loc[data_1chbre['time'] == heure, 'consumption']
    
    # Calculer la moyenne des valeurs filtrées
    moyenne = valeurs_a_moyenner.mean()
    
    # Ajouter l'heure et la moyenne à la liste des données temporaires
    donnees_temporaires.append({'Heure': str(heure), 'Moyenne': moyenne})
    
# Créer un DataFrame à partir de la liste des données temporaires
moyennes_par_heure = pd.DataFrame(donnees_temporaires)

moyennes_par_heure = moyennes_par_heure.sort_values(by='Heure')

print(moyennes_par_heure)



plt.plot(moyennes_par_heure['Heure'], moyennes_par_heure['Moyenne'])
plt.xlabel('Heure')
plt.ylabel('Moyenne de la consommation')
plt.title('Moyenne de la consommation par heure')
plt.xticks(rotation=45)  
plt.grid(True) 
plt.show()
