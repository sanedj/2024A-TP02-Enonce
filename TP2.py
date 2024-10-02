"""
TP2 : Système de gestion de livres pour une bibliothèque

Groupe de laboratoire : 01
Numéro d'équipe :  08
Noms et matricules : Nedjari (2400197), Kriba (2369237)
"""

########################################################################################################## 
# PARTIE 1 : Création du système de gestion et ajout de la collection actuelle
##########################################################################################################

import csv # Importation du module csv
bibliotheque = {} # Initialisation de la bibliothèque
# Ouverture du fichier csv de la collection en l'associant à une variable pour permettre la lecture de celui-ci
fichier_csv = open('C:\\Users\\Saber\\.inf1007\\2024A-TP02-Enonce\\collection_bibliotheque.csv', newline = '', encoding = 'utf-8')
lecture_csv = csv.DictReader(fichier_csv) # Permet de lire le contenu du fichier csv et de convertir chaque ligne en dictionnaire
for ligne in lecture_csv:
    cote_rangement = ligne['cote_rangement'] # Associer la valeur du cote de rangement de la ligne à une variable
    # Création d'un sous dictionnaire associé à la cote de rangement d'une certaine ligne qui contiendra les informations du livre de la ligne
    # Dans les signes suivantes, on associe l'information spécifique de la ligne (ex. nom de l'auteur) à la clé correspondante (ex. 'auteur')
    bibliotheque[cote_rangement] = {
        'titre': ligne['titre'],
        'auteur': ligne['auteur'],
        'date_publication': ligne['date_publication']
    }

fichier_csv.close() # Sauvegarder et fermer le fichier
print(f' \n Bibliothèque initiale : \n') # Vérification du dictionnaire
for key, value in bibliotheque.items():
    print(f'{key}: {value}') # Affichage des sous-dictionnaires ligne par ligne
print('') # Espace entre cette section et la prochaine

########################################################################################################## 
# PARTIE 2 : Ajout d'une nouvelle collection à la bibliothèque
########################################################################################################## 

# Ouverture du fichier csv de la nouvelle collection 
nouveau_fichier_csv = open('C:\\Users\\Saber\\.inf1007\\2024A-TP02-Enonce\\nouvelle_collection.csv', newline = '', encoding = 'utf-8')
nouvelle_lecture_csv = csv.DictReader(nouveau_fichier_csv)
for nouvelle_ligne in nouvelle_lecture_csv:
    cote_rangement = nouvelle_ligne['cote_rangement'] # Associer la valeur du cote du rangement de la ligne à une variable
    titre = nouvelle_ligne['titre'] # Associer le titre de la ligne à une variable
    auteur = nouvelle_ligne['auteur'] # Associer le nom de l'auteur de la ligne à une variable
    date_publication = nouvelle_ligne['date_publication'] # Associer la date de publication de la ligne à une variable

    if not cote_rangement in bibliotheque.keys(): # Itération vérifiant si le livre est déjà inclu dans la bibliothèque
        # Code ajoutant les nouveaux éléments dans la bibliothèque
        bibliotheque[cote_rangement] = {
            'titre': titre,
            'auteur': auteur,
            'date_publication': date_publication,
        }
        print(f"Le livre {cote_rangement} ---- {titre} par {auteur} ---- a été ajouté avec succès") # Confirmation de l'ajout
    else:
        print(f"Le livre {cote_rangement} ---- {titre} par {auteur} ---- est déjà présent dans la bibliothèque") # Ajout non réalisé

nouveau_fichier_csv.close() # Sauvegarder et fermer le fichier
print(f' \n Nouvelle bibliothèque : \n') # Vérification du dictionnaire
for key, value in bibliotheque.items():
    print(f'{key}: {value}') # Affichage des sous-dictionnaires ligne par ligne

########################################################################################################## 
# PARTIE 3 : Modification de la cote de rangement d'une sélection de livres
########################################################################################################## 

modifications = [] # Initialisation du liste vide
for cote in list(bibliotheque.keys()): # Associe la variable cote aux clés de la bibliothèque
    if cote.startswith('S'): # Vérification de la première lettre de la cote de rangement
        if bibliotheque[cote]['auteur'] == 'William Shakespeare': # Vérification de si l'auteur est Shakespeare   
            new_cote = cote.replace('S', 'WS') # Remplace la lettre S par WS dans la cote de rangement
            modifications.append((cote, new_cote)) # Ajout de l'anciennce cote et la nouvelle cote

for cote, new_cote in modifications: # Boucle permettant de lire les éléments présents dans la liste 'modifications'
    bibliotheque[new_cote] = bibliotheque.pop(cote) # Retire la vieille cote en retournant sa valeur, puis l'associe à une nouvelle cote

print(f' \n Bibliothèque avec modifications : \n') # Vérification du dictionnaire
for key, value in bibliotheque.items(): # Impression des informations de chaque livre
    print(f'{key}: {value}')

########################################################################################################## 
# PARTIE 4 : Emprunts et retours de livres
########################################################################################################## 

for clé in bibliotheque.keys():
    # Ajouter une nouvelle clé dans le dictionnaire "emprunts" qui correspond à "disponible"
    bibliotheque[clé]['emprunts'] = 'disponible'
    # Ajouter une nouvelle clé dans le dictionnaire "date_emprunt" qui est vide (correspond à '')
    bibliotheque[clé]['date_emprunt'] = ''

fichier_modif_csv = open('C:\\Users\\Saber\\.inf1007\\2024A-TP02-Enonce\\emprunts.csv', newline = '', encoding = 'utf-8')
lecture_modif_csv = csv.DictReader(fichier_modif_csv)
for modif_ligne in lecture_modif_csv:
    cote_rangement = modif_ligne['cote_rangement'] # Associer la valeur du cote du rangement de la ligne à une variable
    date_emprunt = modif_ligne['date_emprunt'] # Associer la valeur de la date d'emprunt de la ligne à une variable

    if cote_rangement in bibliotheque.keys():
        # Remplacer la valeur "disponible" à "emprunté" si la cote de rangement est dans emprunts.csv (À travers une itération)  
        bibliotheque[cote_rangement]['emprunts'] = 'emprunté'
        # Ajouter une valeur correspondant à la date d'emprunt si le livre a bel et bien été emprunté (À travers une itération)
        bibliotheque[cote_rangement]['date_emprunt'] = date_emprunt

print(f' \n Bibliotheque avec ajout des emprunts : \n') # Vérification du dictionnaire
for key, value in bibliotheque.items(): # Impression des informations de chaque livre
    print(f'{key}: {value}')

########################################################################################################## 
# PARTIE 5 : Livres en retard 
########################################################################################################## 

import datetime
from datetime import date
current_date = datetime.date.today() # Affiche la date d'aujourd'hui soit 2024-10-??
emp_bibliotheque = {} # Initialisation d'une nouvelle bibliothèque pour les emprunts

fichier_modif_csv = open('C:\\Users\\Saber\\.inf1007\\2024A-TP02-Enonce\\emprunts.csv', newline = '', encoding = 'utf-8')
lecture_modif_csv = csv.DictReader(fichier_modif_csv) # Accéder à l'information contenu dans 'emprunts.csv'
for modif_ligne in lecture_modif_csv:
    cote_rangement = modif_ligne['cote_rangement'] # Associer la valeur de la clé 'cote_rangement' à la variable cote_rangement
    emp_bibliotheque = {
        'cote_rangement': modif_ligne['cote_rangement'],
        'date_emprunt': modif_ligne['date_emprunt'],
        'frais_retard': '', # Ajout d'une clé « frais_retard » vide pour le moment
        'livres_perdus': '' # Ajout d'une clé « livres_perdus » vide pour le moment
    }
    date_emprunt = modif_ligne['date_emprunt'] # Associer la valeur de la clé 'date_emprunt' à la variable date_emprunt

# Pour séparer date = 2024/09/27 en 2024, 09, 27 (type: int), il faut x = date.split("/"), (année, mois, journée) = (int(x[0]), int(x[1]), int(x[2]))
    date_modif = date_emprunt.split("-") # Séparer les termes de la date à '-'
    année, mois, journée = int(date_modif[0]), int(date_modif[1]), int(date_modif[2]) # Associer les valeurs de date à des variables

# Pour accéder à l'année (current_date.year), le mois (current_date.month) et la journée (current_date.day)
    b = date(année, mois, journée)
    a = date(current_date.year, current_date.month, current_date.day)
    diff_days = (a-b).days # La différence de journées entre aujourd'hui et la date de l'emprunt

# Les livres doivent être retourné dans un délai de 30 jours
# Si le livre n'est pas retourné, il y a un frais de retard de 2$ par jour, jusqu'à un montant maximum de 100$

    if 365 > diff_days > 30: # Condition vérifiant si la différence de jours est supérieur à 30 jours et inférieur à 365 jours (1 an)
        jour_retard = diff_days - 30 # Le nombre de journées de retard
        montant = jour_retard * 2 # La somme des frais
        if montant > 100:
            montant = 100 # Fixer la valeur à 100$ si le montant dépasse 100$
        emp_bibliotheque['frais_retard'] = f'{montant}' # Associer le montant de frais de retard à la clé appropriée

# Affichage de la liste des livres en retard avec leurs frais respectifs en utilisant print
    if emp_bibliotheque['frais_retard'] is not '':
        bibliotheque[cote_rangement]['frais_retard'] = emp_bibliotheque['frais_retard']
        if bibliotheque[cote_rangement]['frais_retard'] is not '':
            print(f"{cote_rangement} : {bibliotheque[cote_rangement]}") # Affichage des informations des livres

# Si aucun retour au bout d'un an, le livre est considéré comme perdu 
    elif diff_days > 365:
        emp_bibliotheque['livres_perdus'] = 'Perdus' # Identifier les livres comme étant perdus
        bibliotheque[cote_rangement]['livres_perdus'] = emp_bibliotheque['livres_perdus']
        if bibliotheque[cote_rangement]['livres_perdus'] is 'Perdus':
            print(f"{cote_rangement} : {bibliotheque[cote_rangement]}")

# Afficher la liste des livres perdus en utilisant: 
#print(f' \n Bibliotheque avec ajout des retards et frais : \n')
#for key, value in bibliotheque.items(): # Impression des informations de chaque livre
#    print(f'{key}: {value}')