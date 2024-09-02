import pandas as pd
from matplotlib import pyplot as plt

__author__ = 'SORO DOBA ISSIAKA AND DOHOUN AMOIN MAEVA'

# LECTURE DES DONNEES

# Question 2.1  Charger les données et afficher les dimensions, noms des colonnes, et types des colonnes

## Charger les données
df = pd.read_csv('palmerpenguins.csv')

## Afficher les dimensions (nombre de lignes et de colonnes)
print(f"Dimensions : {df.shape}")

print("="*100)

## Afficher les noms des colonnes
print(f"Noms des colonnes : {df.columns.tolist()}")

print("="*100)

## Afficher les types des colonnes
print(f"les types des colonnes: {df.dtypes}")

print("*"*100)

# ANALYSE DES DONNEES

# Question 2.2 Afficher le poids moyen (en grammes) par sexe

## Calculer le poids moyen par sexe
poids_moyen = df.groupby('sex')['body_mass_g'].mean()

## Afficher le résultat
print(poids_moyen)

print("="*100)

# Question 2.3 : Afficher le nombre d'individus renseignés par espèce et par île

# Compter le nombre d'individus par espèce et par île
nombre = df.groupby(['species', 'island']).size()

# Afficher le résultat
print(nombre)

print("="*100)

# Question 2.4 : Afficher le nombre d'espèces différentes par île

## Compter le nombre d'espèces différentes par île
nombre_especes = df.groupby('island')['species'].nunique()

## Afficher le résultat
print(nombre_especes)

print("="*100)

# TRAITEMENT DES VALEURS MANQUANTES

# Question 2.5 : Afficher le nombre de valeurs manquantes par colonne

## Compter les valeurs manquantes par colonne
valeurs_manquante = df.isnull().sum()

## Afficher le résultat
print(valeurs_manquante)

print("="*100)

# Question 2.6 : Supprimer les colonnes ayant plus de 10% de valeurs manquantes

# Calculer le seuil de 10% du nombre de lignes
seuil = 0.1 * len(df)

# Supprimer les colonnes ayant plus de 10% de valeurs manquantes
df = df.dropna(thresh=len(df) - seuil, axis=1)

# Vérifier le nombre de valeurs manquantes par colonne après suppression
valeurs_manquantes = df.isnull().sum()
print(valeurs_manquantes)

print("="*100)

# Question 2.7 : Supprimer les lignes restantes contenant encore des valeurs manquantes

## Supprimer les lignes contenant des valeurs manquantes
df = df.dropna()

## Afficher les dimensions de la DataFrame après suppression des lignes
print(f'Dimensions après suppression des lignes : {df.shape}')

print("="*100)

# Question 2.8 : Définir la colonne num comme index de la DataFrame

# Définir la colonne 'num' comme index
df = df.set_index('num')

# Afficher les premières lignes pour vérifier le nouvel index
df.head()

print("="*100)

# Question 2.9 : Séparer la variable cible ('species') et les variables explicatives

## Séparer la variable cible dans df_y
df_y = df['species']

# Séparer les variables explicatives dans df_X
df_X = df.drop(columns=['species'])

# Afficher les premières lignes pour vérifier
print(df_X.head())
print(df_y.head())

print("="*100)

# CONVERSION DES DONNEES CATEGORIELLE

# Question 2.10 : Conversion des données catégorielles (One Hot Encoding)

# Effectuer le one hot encoding sur les colonnes catégorielles de df_X
df_X = pd.get_dummies(df_X, drop_first=True)

# Afficher les premières lignes pour vérifier
print(df_X.head())

print("="*100)

# NORMALISATION DES DONNEES

# Normaliser les données (centrage et réduction)
norm = (df_X - df_X.mean()) / df_X.std()

# Afficher les statistiques descriptives pour vérifier
print(norm.describe())

print("="*100)

# VISUALISATION AVEC MATPLOTLIB

# Tracer l'histogramme de la colonne 'body_mass_g'
plt.hist(df['body_mass_g'], bins=20, color='blue', edgecolor='black')

# Tracer la ligne verticale représentant la moyenne
plt.axvline(df['body_mass_g'].mean(), color='yellow', linestyle='dashed', linewidth=1)

# Ajouter des labels et un titre
plt.xlabel('Body mass g')
plt.ylabel('les Frequences')
plt.title('Histogramme de la masse corporelle des manchots')

# Afficher le graphique
plt.show()





