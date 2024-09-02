from lxml import etree

__author__ = 'SORO DOBA ISSIAKA AND DOHOUN AMOIN MAEVA'

def affiche_resultat_requete(result):
    '''
    Fonction permettant d'afficher les résultats d'une requête XPath
    '''
    if isinstance(result, list):
        for el in result:
            if isinstance(el, etree._Element):
                print(etree.tostring(el, encoding='unicode'))
            else:
                print(el)
            print('.'*100)
    else:
        print(result)
        print('.'*100)


# Corps principal
###################
# on va charger le fichier XML 
arb = etree.parse('films.xml')

# on va ensuite récupérer la racine de l'arbre
root = arb.getroot()
print(root.tag)

resultat = root.xpath('//FILM')
affiche_resultat_requete(resultat)
print(resultat)

print(type(resultat[0]))

resultat2  = root.xpath('//@*')
affiche_resultat_requete(resultat2)
print(type(resultat2[0]))

# Question 1.1
#Affichage du titre des films de genre "Science-fiction"

affichage_titre = root.xpath("//FILM[GENRE='Science-fiction']/TITRE")

#Question 1.2
#Affichage du nom de l'acteur qui a joué le rôle 'Van Gogh'
nom_acteur=root.xpath("//ACTEUR[ROLES/ROLE='Van Gogh']/NOM")

print("="*100)

#Question 1.3
#Afiichage du titre du ou des films dont le résumé contient l'année de naissance de Tony Scott

affichage=root.xpath("//FILM[contains(RESUME, //ARTISTE[NOM='Tony Scott']/ANNEENAISS)]/TITRE")


