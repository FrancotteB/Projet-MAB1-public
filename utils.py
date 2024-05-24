# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 17:47:51 2024

@author: basti
"""

import pandas as pd
import matplotlib.pyplot as plt
import holidays
import numpy as np
from datetime import datetime
from scipy.interpolate import interp1d


data = pd.read_csv('C:\\Users\\basti\\Documents\\UNIF\\MAB1\\Projet\\NivreHourlyDataWithNBBedroom.csv')


def dappart (data,num):
    dappart = data[data['apartName'] == num]
    return dappart

def dnchbre (data,nbre):
    dnchbre = data[data['nbBedroom'] == nbre]
    return dnchbre


def delec (db):
    elec = ['Compteur electrique coffret', 'Compteur electrique double-flux']
    dt = db[db['meterType'].isin(elec)]
    dtype = todt(dt)
    dtype = dand(dtype)
    
    return dtype

def decs (db):
    ecs = ['Compteur ECS 1', 'Compteur ECS 2']
    dt = db[db['meterType'].isin(ecs)]
    dtype = todt(dt)
    dtype = dand(dtype)
    return dtype

def deef (db):
    ecs = ['Compteur EF']
    dt = db[db['meterType'].isin(ecs)]
    dtype = todt(dt)
    dtype = dand(dtype)
    return dtype

def dchau (db):
    ecs = ['Compteur chauffage']
    dt = db[db['meterType'].isin(ecs)]
    dtype = todt(dt)
    dtype = dand(dtype)
    return dtype


def todt (db):
    db['datetime'] = pd.to_datetime(db['datetime'])
    
    # Filtrer les lignes où les minutes et les secondes sont égales à zéro
    db = db[(db['datetime'].dt.minute == 0) & (db['datetime'].dt.second == 0)]

    # Créer une colonne 'date' avec la date
    db['date'] = db['datetime'].dt.date

    # Créer une colonne 'time' avec l'heure
    db['time'] = db['datetime'].dt.time
    
    return db


def dj (dbo, jour):
    db = dbo.copy()
    db['date'] = pd.to_datetime(db['date'])
    dj = db[db['date'].dt.date == pd.to_datetime(jour).date()]
    return dj



def custom_and(series):
    return set(series)

def dand(db):
    donnees_aggreges = db.groupby(['apartName', db['datetime']]).agg({'consumption': 'sum', 'index': 'first', 'unit': 'first', 'meterID': 'first', 'apartName': 'first', 'nbBedroom': 'first', 'datetime': 'first', 'date': 'first', 'time': 'first', 'meterType': custom_and})
    return donnees_aggreges


#def dsum (db):
    donnees_aggreges = db.groupby(db['datetime'].dt.hour)['consumption'].sum()
    return donnees_aggreges
    

def moytemp (db):
    donnees_temporaires = []
    
    unité = db['unit'].iloc[0]

    for heure in db['time'].unique():
        
        valeurs_a_moyenner = db.loc[db['time'] == heure, 'consumption']
        
        moyenne = valeurs_a_moyenner.mean()
        
        donnees_temporaires.append({'Heure': str(heure), 'Moyenne': moyenne.round(4), 'Unité': unité})
        
    moyennes_par_heure = pd.DataFrame(donnees_temporaires)

    moyennes_par_heure = moyennes_par_heure.sort_values(by='Heure')
    
    moyennes_par_heure = Ftre(moyennes_par_heure, unité)
    
    return moyennes_par_heure


def affi (conso):
    plt.plot(conso['datetime'], conso['consumption'])
    plt.xlabel('Heure')
    plt.ylabel('consommation')
    plt.title('consommation par heure')
    plt.xticks(rotation=45)  
    plt.grid(True) 
    plt.show()


def affim (moy):
    unité = moy['Unité'].iloc[0]
    
    plt.plot(moy['Heure'], moy['Moyenne'])
    plt.xlabel('Heure')
    plt.ylabel(f'Moyenne de la consommation ({unité})')
    plt.title('Moyenne de la consommation par heure')
    plt.xticks(rotation=45)  
    plt.grid(True) 
    plt.show()
    
    
    
def get_holidays_multiple_years(start_year, end_year, country='BE'):
    all_holidays = []
    for year in range(start_year, end_year + 1):
        country_holidays = holidays.CountryHoliday(country, years=year)
        all_holidays.extend(country_holidays)
    return all_holidays




    
    
def holids (dbo, année) :
    
    db = dbo.copy()
    
    start_year = année-1
    end_year = année+1
    
    be_holidays = get_holidays_multiple_years(start_year, end_year)
    
    db['date'] = pd.to_datetime(db['date'])
    
    # Ajouter une colonne pour les jours fériés
    db['ferie'] = db['date'].isin(be_holidays)
    
    # Ajouter une colonne pour les weekends
    db['weekend'] = db['date'].dt.weekday >= 5
    
    db['we_ferie'] = db['ferie'] | db['weekend']
    
    
    db.drop('ferie', axis=1, inplace=True)
    db.drop('weekend', axis=1, inplace=True)
    
    
    db_ouvrables = db[db['we_ferie'] == False]
    db_feries = db[db['we_ferie'] == True]

    # Afficher le DataFrame avec les jours fériés et ouvrables
    #print(db_feries,db_ouvrables)
    return db_feries,db_ouvrables




def filtre (dbo, date, sem) :
    
    db = dbo.copy()
    db['date'] = pd.to_datetime(db['date'])
    
    # Sélectionner la date de début et de fin de la plage de 3 semaines
    date_debut = date
    date_fin = pd.to_datetime(date_debut) + pd.DateOffset(weeks=sem)

    # Filtrer les données pour la plage de 3 semaines
    db_plage_3_semaines = db[(db['date'] >= date_debut) & (db['date'] < date_fin)]
    
    # Afficher les données de la plage de 3 semaines
    return db_plage_3_semaines
    
    
def comp (moya, moyb) :
    
    unité = moya['Unité'].iloc[0]
    
    db_moyennes = pd.DataFrame()
    # Calculer la différence entre les deux moyennes
    #db_moyennes['Difference'] = moya['Moyenne'] - moyb['Moyenne']
    
    # Fusionner les DataFrames sur la colonne 'Heure'
    merged_df = pd.merge(moya, moyb, on='Heure', suffixes=('_moya', '_moyb'))
    
    # Calculer la différence entre les colonnes 'Moyenne_x' et 'Moyenne_y'
    db_moyennes['Difference'] = merged_df['Moyenne_moya'] - merged_df['Moyenne_moyb']
    
    db_moyennes['Heure'] = moya['Heure']
    db_moyennes = db_moyennes.sort_values(by='Heure')
    
    
    # Tracer les moyennes originales
    plt.plot(moya['Heure'], moya['Moyenne'], label='Moyenne Réelle', marker='o')
    plt.plot(moyb['Heure'], moyb['Moyenne'], label='Moyenne Estimée', marker='o')
    
    plt.xlabel('Heure')
    plt.ylabel('Moyennes normalisées')
    plt.title('Moyennes originales')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # Tracer la différence entre les moyennes
    plt.plot(db_moyennes['Heure'], db_moyennes['Difference'], label='Différence', marker='o')
    
    # Configurer le graphique
    plt.xlabel('Heure')
    plt.ylabel('Différence')
    plt.title('Comparaison des moyennes')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
def compdd (moya, moyb) :
    
    db_moyennes = pd.DataFrame()
    # Calculer la différence entre les deux moyennes
    #db_moyennes['Difference'] = moya['consumption'] - moyb['consumption']
    db_moyennes['time'] = moya['time']
    
    moya['Heure'] = moya['datetime'].apply(time_to_float)
    moyb['Heure'] = moyb['datetime'].apply(time_to_float)
    
    # Tracer les moyennes originales
    plt.plot(moya['Heure'], moya['consumption'], label='consumption Réelle', marker='o')
    plt.plot(moyb['Heure'], moyb['consumption'], label='consumption Estimée', marker='o')
    
    plt.xlabel('time')
    plt.ylabel('consumption')
    plt.title('consumption originales')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
    """
    # Tracer la différence entre les moyennes
    plt.plot(db_moyennes['time'], db_moyennes['Difference'], label='Différence', marker='o')
    
    # Configurer le graphique
    plt.xlabel('time')
    plt.ylabel('Différence')
    plt.title('Comparaison des consumption')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.show()
    """
    
def saison (db) :
    
    db['mois'] = db['datetime'].dt.month
    
    # Diviser les données en fonction des saisons
    db_hiver = db[(db['mois'] == 12) | (db['mois'] <= 2)]  # Décembre, Janvier, Février
    db_printemps = db[(db['mois'] >= 3) & (db['mois'] <= 5)]  # Mars, Avril, Mai
    db_ete = db[(db['mois'] >= 6) & (db['mois'] <= 8)]  # Juin, Juillet, Août
    db_automne = db[(db['mois'] >= 9) & (db['mois'] <= 11)]  # Septembre, Octobre, Novembre
    
    # Afficher les DataFrame pour chaque saison
    """print("Hiver:")
    print(db_hiver)
    print("\nPrintemps:")
    print(db_printemps)
    print("\nÉté:")
    print(db_ete)
    print("\nAutomne:")
    print(db_automne)"""
    
    return db_hiver, db_printemps, db_ete, db_automne


def cvrmseM (dbvraie, dbesti) :
    
    
    valeurs_reelles = dbvraie['Moyenne']
    valeurs_predites = dbesti['Moyenne']
    
    # 1. Calcul des écarts entre les valeurs réelles et les valeurs prédites
    ecarts = np.subtract(valeurs_reelles, valeurs_predites)
    #print(ecarts)
    
    # 2. Élévation au carré des écarts
    ecarts_carre = np.square(ecarts)
    #print(ecarts_carre)
    
    # 3. Calcul de la moyenne des écarts au carré
    mse = np.mean(ecarts_carre)
    #print(mse)
    
    # 4. Calcul de la racine carrée de la MSE pour obtenir le RMSE
    rmse = np.sqrt(mse)
    
    #print("RMSE :", rmse)
    
    y_mean = np.mean(valeurs_reelles)
    cv_rmse = (rmse / y_mean)*100
    
    print("CV(RMSE) :", cv_rmse)
    return cv_rmse

def nmbeM (dbvraie, dbesti) :
    
    
    valeurs_reelles = dbvraie['Moyenne']
    valeurs_predites = dbesti['Moyenne']
    
    # 1. Calcul des écarts entre les valeurs réelles et les valeurs prédites
    ecarts = np.subtract(valeurs_reelles, valeurs_predites)
    #print(ecarts)
    
    # 2. Calcul de la moyenne des écarts
    mbe = np.mean(ecarts)
        
    y_mean = np.mean(valeurs_reelles)
    nmbe = (mbe / y_mean)*100
    
    print("NMBE :", nmbe)
    return nmbe



def norm (dbo) :
    
    db = dbo.copy()
    

    # Calcul des valeurs min et max de la colonne "Moyenne"
    min_value = db['Moyenne'].min()
    max_value = db['Moyenne'].max()
    
    # Normalisation de la colonne "Moyenne"
    db['Moyenne'] = (db['Moyenne'] - min_value) / (max_value - min_value)
    
    # Affichage de la base de données normalisée
    #print(db)
    return db
    
def norm2 (dbo) :
    
    db = dbo.copy()
    
    unité = db['Unité'].iloc[0]
    
    # Calcul de la moyenne de la colonne "Moyenne"
    mean_value = db['Moyenne'].mean()
    #print(mean_value)
    
    # Normalisation de la colonne "Moyenne"
    db['Moyenne'] = db['Moyenne'] / mean_value
    
    db[f'Facteur de normalisation ({unité})'] = mean_value
    
    # Affichage de la base de données normalisée
    #print(db)
    return db

def norm4 (dbo) : 

    db = dbo.copy()
    
    # Calculer la moyenne et l'écart-type de la colonne 'Moyenne'
    moyenne = db['Moyenne'].mean()
    ecart_type = db['Moyenne'].std()
    
    # Appliquer la normalisation z-score à la colonne 'Moyenne'
    db['Moyenne'] = (db['Moyenne'] - moyenne) / ecart_type
    return db

def norm5 (dbo) : 

    db = dbo.copy()
    # Appliquer la normalisation par plage de fréquences à la colonne 'Moyenne'
    db['Moyenne'] = pd.qcut(db['Moyenne'], q=10, labels=False, duplicates='drop') / 10.0
    
    return db

def norm3 (dbo) : 

    db = dbo.copy()
    decimales = 4
    db['Moyenne'] = np.log(db['Moyenne'] + 1)
    
    return db


def Ftre (dbo, unité) :
    
    db = dbo.copy()
    # Calculer la moyenne et l'écart-type
    moyenne = db['Moyenne'].mean()
    ecart_type = db['Moyenne'].std()
    
    # Définir le nombre d'écart-types pour déterminer les valeurs aberrantes (par exemple, 3 écart-types)
    nb_ecart_types = 2
    
    # Calculer le seuil statistique en prenant en compte l'écart absolu
    seuil_statistique = np.abs(db['Moyenne'] - moyenne).mean() + nb_ecart_types * ecart_type
    
    # Détection des valeurs aberrantes (simple exemple avec un seuil)
    valeurs_aberrantes = np.abs(db['Moyenne'] - moyenne) > seuil_statistique
  
    # Convertir la colonne 'Heure' en datetime
    db['Heure'] = pd.to_datetime(db['Heure'], format='%H:%M:%S') 
    # Convertir 'Heure' en nombre pour l'interpolation (en secondes depuis le début de la journée)
    db['Heure_numeric'] = db['Heure'].dt.hour * 3600 + db['Heure'].dt.minute * 60 + db['Heure'].dt.second
    
    # Appliquer l'interpolation quadratique pour remplacer les valeurs aberrantes
    interpolator = interp1d(db['Heure_numeric'][~valeurs_aberrantes], db['Moyenne'][~valeurs_aberrantes], kind='quadratic', fill_value="extrapolate")
    
    # Remplacer les valeurs aberrantes par les valeurs interpolées
    db.loc[valeurs_aberrantes, 'Moyenne'] = interpolator(db['Heure_numeric'][valeurs_aberrantes])
    
    # Supprimer la colonne temporaire 'Heure_numeric'
    db.drop(columns=['Heure_numeric'], inplace=True)
    
    # Convertir la colonne 'Heure' de datetime à string
    db['Heure'] = db['Heure'].dt.strftime('%H:%M:%S')
    
    return db

def affseu (dbo) :
    
    db = dbo.copy()
    
    # Calculer la moyenne et l'écart-type
    moyenne = db['Moyenne'].mean()
    ecart_type = db['Moyenne'].std()    
    
    # Définir le nombre d'écart-types pour déterminer les valeurs aberrantes (par exemple, 3 écart-types)
    nb_ecart_types = 2
    
    # Calculer le seuil statistique
    seuil_statistique = np.abs(db['Moyenne'] - moyenne).mean() + nb_ecart_types * ecart_type
    
    # Tracer le graphique
    plt.figure(figsize=(10, 6))
    plt.plot(db['Moyenne'], label='Valeurs', marker='o', color='blue')
    plt.axhline(y=moyenne + seuil_statistique, color='red', linestyle='--', label=f'Seuil statistique (3 écart-types)')
    plt.axhline(y=moyenne - seuil_statistique, color='red', linestyle='--')    
    plt.xlabel('Index')
    plt.ylabel('Valeurs')
    plt.title('Représentation graphique des valeurs et du seuil statistique')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    
    
def gene (db, année) :
    
    l_db = {}
    nl1 = ['db1', 'db2', 'db3']


    for name, i in zip (nl1, range(1, 4)):
        df = dnchbre(db, i)  
        if not df.empty:     
            l_db[name] = df
    
    
    
    ldb_elec = {}
    ldb_ecs = {}
    ldb_ef = {}
    ldb_chau = {}
    ldb_type = {}
    i = 0
    
    for key, db0 in l_db.items() :
        ldb_elec[f"{key}{'_elec'}"] = delec(db0)
        ldb_ecs[f"{key}{'_ecs'}"] = decs(db0)
        ldb_ef[f"{key}{'_ef'}"] = deef(db0)
        ldb_chau[f"{key}{'_chau'}"] = dchau(db0)
        i=i+1
        if i == len(l_db):
            ldb_type = {**ldb_elec, **ldb_ecs, **ldb_ef, **ldb_chau}
            i = 0
           
             
    
    ldb_o = {}
    ldb_f = {}
    ldb_jfo = {}
    
    
    
    
    for key, dtb in ldb_type.items() :
        jf, jo = holids(dtb, année)
        ldb_o[f"{key}{'_o'}"] = jf
        ldb_f[f"{key}{'_f'}"] = jo
        i=i+1
        if i == len(ldb_type):
            ldb_jfo = {**ldb_o, **ldb_f}
            i = 0
        
         
    ldb_hiver = {}
    ldb_prin = {}
    ldb_ete = {}
    ldb_auto = {}
    ldb_sai = {}
     
    for key, Dtb in ldb_jfo.items() :
        dh, dp, de, da = saison(Dtb)
        ldb_hiver[f"{key}{'_hiv'}"] = dh
        ldb_prin[f"{key}{'_prin'}"] = dp
        ldb_ete[f"{key}{'_ete'}"] = de
        ldb_auto[f"{key}{'_aut'}"] = da
        i=i+1
        if i == len(ldb_jfo):
            ldb_sai = {**ldb_hiver, **ldb_prin, **ldb_ete, **ldb_auto}
            i = 0


    proftypes = {}
    
    for key, dtb in ldb_sai.items() :
        proftypes[f"{key}{'_mnorm'}"] = norm2(moytemp(dtb))
    
    return ldb_sai, proftypes 


def time_to_float(dt):
    epoch = datetime(1970, 1, 1)
    delta = dt - epoch
    return delta.total_seconds() / (24 * 3600)
    
