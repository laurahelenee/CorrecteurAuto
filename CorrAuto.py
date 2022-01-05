# -*- coding: utf-8 -*-

import os

#Faire en sorte qu'on est bien dans le bon chemin 
path_file = input("Entrez le chemin vers le dossier du devoir : ")
os.chdir(path_file)

#vérifier dans quel chemin on est 
path = os.getcwd()
print("Vous vous trouvez dans le dossier " + path)


#La première fonction demande à l'utilisateur de rentrer le chemin du fichier en input et de transformer
#tous les mots du texte en une liste 
def get_lect_file():
    """
    

    Returns
    -------
    txtmts : TYPE
        DESCRIPTION.

    """
    txt_corr= input("Entrez le chemin absolu du fichier à inspecter : ") #Input pour que l'user entre le chemin
    print ("Fichier chargé!")
    with open(txt_corr,'r') as txt: #ouverture du fichier en mode lecture
        txtlist = txt.read()  #création d'une variable qui lit le contenu
        txtmts = txtlist.split() #création d'une liste avec tous les éléments/mots 
        for i in range(len(txtmts)):
            txtmts[i]=txtmts[i].lower() #insensibilité à la casse 
        txt.close() #fermeture obligatoire du fichier
    return txtmts


#création d'une fonction de lecture pour le dictionnaire et transfo en liste
def lect_dict(): 
    """
    

    Returns
    -------
    dico_eng : TYPE
        DESCRIPTION.

    """
    with open("dico_eng.txt",'r') as dico: #Ouverture du dico via son chemin en mode lecture
        dicolist = dico.read() #Lecture du fichier
        dico_eng = dicolist.split() #Séparation des différents éléments inclus dans le fichier en élément de liste
        dico.close() #Fermeture du fichier
    return dico_eng



"""
Volonté : vérifier si le mot est dans le dictionnaire : 
    - Si le mot est dans le dictionnaire, on va append l'élément dans une nouvelle liste
    - Si le mot n'est pas dans le dictionnaire, on demande à l'utilisateur de rentrer un input qu'on appellera choix:
        - Choix = 0 à (x>0), append le ième élément du choix pour b élément du dictionnaire
        - Choix = -1, append i tel quel 
        - Choix = -2, entrer un input qu'on va append dans la liste 

La nouvelle liste contiendra ce que l'utilisateur aura choisi et on pourra créer un nouveau document texte 

"""


def corr_autom_tst(txtmts,dico_eng):
    bon = [] #liste vide pour copier tous les mots bons et/ou corrigés
    for i in txtmts:
        if i in dico_eng: #si le mot est bien dans le dico anglais on ajoute l'élément dans la bonne liste
            bon.append(i)
        elif i not in dico_eng: 
            litodi = [] #litodi pour list to dictionnary, liste qui va se transfo en dico
            dicto = {} #pour créer un dictionnaire
            print("Erreur détectée : " + str(i)) #on affiche à l'user le mot hors dico
            wd = str(i) #stockage du mot erroné pour l'utiliser si jamais il ne veut pas le changer
            for i in dico_eng:
                if i.startswith(wd[:3]): #condition de selection : si les 3 premières lettres communes
                    litodi.append(i) 
                for i in range(0,len(litodi)): #pour tous les résultats possibles on append un dictionnaire à partir de litodi
                    dicto[i]=litodi[i]
            if len(dicto)==0 : #si le dictionnaire n'a pas de contenu retourner à l'user un msg d'erreur pour qu'il choisisse soit -1 ou -2
                print("Aucune alternative n'a été trouvée.")
            else : print(dicto)
            choix = int(input("Quel est votre choix ? ")) #l'user entre un choix numérique 
            if choix >=0 : #condition : si le choix est supérieur ou égal à 0 on pioche dans les valeurs du dico
                bonmt = list(dicto.values()) #on crée une liste de mots avec les valeurs (2e mot) du dico
                wdchoice = bonmt[choix] #on retourne l'élément de la liste que l'on souhaite avoir et stock dans une variable
                bon.append(wdchoice) #on ajoute ce mot à la liste
                print("Votre mot a été corrigé.")
            if choix == -1:
                print("Vous avez choisi de garder le mot intact.")
                bon.append(wd) #vu qu'on a stocké la variable erronnée au début ça peut nous servir si le mot est correct mais juste pas dans le dico
            if choix == -2:
                corr_perso = input("Veuillez entrer votre correction : ") #l'user entre son mot qui est stocké dans une variable 
                bon.append(corr_perso) #append ce mot
                print("Votre mot a été corrigé.")
    return bon

def crea_fich(fich_liste):
    joined_fich_l = " ".join(fich_liste) #si on ne fait pas ça les mots ne seront pas espacés 
    print("Un fichier est créé avec vos modifications !")
    nom_fich = input("Comment voulez-vous appeler votre fichier ? (N'oubliez pas l'extension .txt) : ")
    new_file = open(nom_fich,"w") #création d'un nouveau fichier new_file en mode write (curseur au début)
    for i in joined_fich_l:
        new_file.write(i)
    new_file.close()
    return
               