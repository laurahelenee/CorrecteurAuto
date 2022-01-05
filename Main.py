# -*- coding: utf-8 -*-

import CorrAuto as ca
import os

def main():
    print("Bienvenue dans votre correcteur orthographique ! \n Rappel des commandes : \n - Pour sélectionner un mot, choisissez son numéro. \n - Pour laisser le mot tel quel, écrivez -1 \n - Pour choisir votre propre correction, écrivez -2.")
    print("C'est parti!")
    txtmts = ca.get_lect_file()
    dico_eng = ca.lect_dict()
    fich_liste = ca.corr_autom_tst(txtmts, dico_eng)
    ca.crea_fich(fich_liste)
    print("Analyse terminée. Vous pourrez retrouver le fichier corrigé dans le dossier suivant : " + os.getcwd())
    
main()
