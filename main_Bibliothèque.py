from Bibliothèque import*
import os
from pickle import Unpickler, Pickler

# Numero des livres

# Enregistrement et récupération des donnés
BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(BASE_DIR, "Sauvegarge.txt")
def save(bibliotheque_princ) :
    # liste contenant la bibliotheque principal,
    # le numéro du dernier livre,
    # le dernier matricule
    donne = [bibliotheque_princ, livre.num, abonner.mat]
    with open(SAVE_FILE, "wb") as doc :
        m_p = Pickler(doc)
        m_p.dump(donne)
       
# Définition/ Récupération de l'objet bibliothèque
def ma_bibliotheque () :
    if os.path.exists(SAVE_FILE) :
        with open(SAVE_FILE, "rb") as doc :
            m_ub = Unpickler(doc)
            donne = m_ub.load()
            livre.num = donne[1]
            abonner.mat = donne[2] 
            return donne[0]
    else :
        return Bibliotheque("Principal")

def Menu():    
    biblio = ma_bibliotheque()
    option = [
        "1- Ajouter un livre",
        "2 - S'aboner",
        "3- Rechercher des livre",
        "4- Emprunter un livre",
        "5- Retourner un livre",
        "6- Supprimer un livre",
        "7 Afficher les livres",
        "8- Afficher les abonnées",
        "9- Quitter"
    ]
    while True :
        save(biblio)
        print("\n_____________Menu de Gestion Bibliotheque_______________")
        for elt in option :
            print(f"{elt}")
        
        
        print()
        choix="dz"
        while type(choix) != int :
            try :
                choix = int(input("Veuillez choisir une option : "))
            except (TypeError, ValueError) :
                print("Veuillez entrer un entier !\n")
        
        if choix==1 :
            print()
            titre = input("Veuillez entrer le titre du livre :  ")
            auteur = input("Veuillez entrer l'auteur :  ")
            annee = input("Veuillez entrer l'année de publication du livre :  ")
            nbr_exemplaire = "bh"
            while type(nbr_exemplaire) != int :
                try :
                    nbr_exemplaire = int(input("Combien d'exemplaire voulez vous ajouter :  "))
                except (TypeError, ValueError) :
                    print("Veuillez entrer un entier !\n")
                
            biblio.Ajouter(titre.strip(), auteur.strip(), annee, nbr_exemplaire)
            print()
            
        elif choix==2 :
            print()
            nom = input("Veuillez entrer votre nom :  ")
            prenom = input("Veuillez entrer votre prenom :  ")
            biblio.sabonner(nom=nom.strip(), prenom=prenom.strip())
            
        elif choix==3 :
            print()
            don = input("Veuillez entrer une référence du livre (titre, auteur, année) : ")
            try :
                donnee = int(don)
            except (TypeError, ValueError) :
                donnee = don.strip()
            book=biblio.Rechercher_livre(donnee)
            if not book :
                print("Aucun livre trouvé\n")
            else :
                print(f"______Résultat de le recherche sur {donnee}_____")
                for li in  book :
                    print(f"{li}")
            
        elif choix==4 :
            print()
            don = input("Veuillez entrer une référence du livre (titre, auteur, année) : ")
            try :
                donnee = int(don)
            except (TypeError, ValueError) :
                donnee = don.strip()
            identite = input("Veuillez entrer votre nom + prenom : ")
            biblio.Emprunter(donnee, identite.strip())
                      
        elif choix==5 :
            print()
            don = input("Veuillez entrer une référence du livre (titre, auteur, année) : ")
            try :
                donnee = int(don)
            except (TypeError, ValueError) :
                donnee = don.strip()
            identite = input("Veuillez entrer votre nom + prenom : ")
            biblio.Retourner(donnee, identite)
            
        elif choix==6 :
            print()
            don = input("Veuillez entrer une référence du livre (titre, auteur, année) : ")
            try :
                donnee = int(don)
            except (TypeError, ValueError) :
                donnee = don.strip()
            biblio.Supprimer(donnee)
                
        elif choix==7 :
            import time
            biblio.Afficher_livres()
            time.sleep(3)
            
        elif choix==8 :
            import time
            biblio.Afficher_abonner()
            time.sleep(3)
            
        elif choix==9 :
            print("Au revoir !\nA la prochaine \n")
            from time import sleep
            sleep(3)
            break
        
        else :
            print("Option invalide ! \n")
   
if __name__ == "__main__" :
    Menu()    
