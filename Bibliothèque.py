# -*- coding:utf-8 -*-
"""Gestionnaire de Bibliothèque 
    Menu
1- Ajouter un livre
2 - S'aboner
3- Rechercher des livre
4- Emprunter un livre
5- Retourner un livre
6- Supprimer un livre
7 Afficher les livres
8- Afficher les abonnées
9- Quitter
    Caractéristiques du livres
- Numéro unique (entier)
- Un titre
- nom d'auteur
- Année de publication
        Autres aspect
- Affichage claire et détaillé
- Le menu sera toujours afficher

"""
from rich.table import Table
from rich.console import Console

console = Console()
# Définition des livres

class livre :
    num = 100
    def __init__ (self, titre, auteur, annee, nbr_exemplaire) :
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.nbr_exemplaire = nbr_exemplaire
        livre.num += 1
        self._numero = livre.num
    
    def __str__ (self) :
        return (f"{self.titre} de {self.auteur}, publié en {self.annee}.")

 
#  On défini les abonné
class abonner :
    mat = 1014
    """Seul les abonné peuvent emprunter les livres"""
    def __init__ (self, nom, prenom ):
        self.nom = nom
        self.prenom = prenom
        self.val = nom + " " + prenom
        self.livre_emprunt = []
        abonner.mat += 1
        self.matricule = abonner.mat
    def emprunter(self) :
        if len(self.livre_emprunt) == 0 :
            return "Pas de livre emprunté"
        else :
            return f"{len(self.livre_emprunt)} livre(s) emprunté(s)"
    def affiche_livre (self) :
        for book in self.livre_emprunt :
            print(book)
    def __str__ (self) :
        return f"{self.val}, matricule : {self.matricule}, {self.emprunter()}"

    
#  On défini la bibliothèque 
class Bibliotheque :
    def __init__ (self, nom_bibliotheque) :
        self.nom_bibliotheque = nom_bibliotheque
        self.Livres = []
        self.Abonnement = []
    
    def Ajouter (self, titre, auteur, annee, nbr_exemplaire) :
        # S'il n'y a pas de livres
        if not self.Livres :
            nv_livre = livre(titre, auteur, annee, nbr_exemplaire)
            self.Livres.append(nv_livre)
            print((f"{nv_livre} a été ajouté avec succès\n"))
            return None
            
        for book in self.Livres :
            if book.titre.lower()==titre.lower() and book.auteur.lower()==auteur.lower() and book.annee==annee :
                print(f"Ce livre existe déjà :\n{book}\n")
                indice = self.Livres.index(book)
                ajout = False
                break
            else :
                ajout = True
        if ajout :
            nv_livre = livre(titre, auteur, annee, nbr_exemplaire)
            self.Livres.append(nv_livre)
            print(f"{nv_livre} a été ajouté avec succès\n")
        else :
            r = input("Voulez vous ajoutez des exemplaires ? (o/n)  ")
            if r.lower().strip() == "o" :
                n = "a"
                while type(n) != int :
                    try :
                        n= int(input("Veuillez entrer le nbr d'exemplaire à ajouter : "))
                    except (TypeError, ValueError) :
                        print("Veuillez entrez un entier !\n")
                self.Livres[indice].nbr_exemplaire += n
                print(f"Mise à jour :\n{self.Livres[indice]}")
            else :
                print("On ne peut pas définir le même livre 2 fois \n")
    
    def sabonner (self, nom, prenom) :
        # si 0 abonné
        if not self.Abonnement :
            nouveau = abonner(nom, prenom)
            self.Abonnement.append(nouveau) 
            print (f"Abonnement avec suxxès\n {nouveau}")
            return 0
            
        val = nom + " " + prenom
        for personne in self.Abonnement :
            if personne.val.lower() == val.lower() :
                print(f"Vous êtes déjà enregistrer\n{personne}\n")
                return 0
        nouveau = abonner(nom, prenom)
        self.Abonnement.append(nouveau) 
        print(f"Abonnement avec suxxès\n {nouveau}")
        return 0

            
    def Rechercher_livre (self, donnee) :
        result=[]
        for book in self.Livres :
            if type(donnee)==int :
                if book.annee == donnee:
                    result.append(book)
            else :
                if (donnee.lower().strip()==book.titre.lower()) or (donnee.lower().strip()==book.auteur.lower()) :
                    result.append(book)
        return result
         
    def Emprunter (self, donnee, identité) :
        # On vérifier s'il es abonné
        for ident in self.Abonnement :
            if ident.val.lower() == identité.lower() :
                indice = self.Abonnement.index(ident)
                v1=True
                break
            else :
                v1 = False
        if not v1 :
            print("Dsl, vous n'êtes pas abonné !\nSeul les abonnés peuvent emprunter les livres\n")
        # On vérifie le nbre de livre dejà emprunter
        if v1 :
            if  len(self.Abonnement[indice].livre_emprunt)==2 :
                print("Dsl, vous ne pouvez pas emprunter plus de 2 livres\n")
                print(f"Vous avez déjà emprunter :\n{self.Abonnement[indice].livre_emprunt[0]} et \n{self.Abonnement[indice].livre_emprunt[1]}\n")
                v2 = False
            elif len(self.Abonnement[indice].livre_emprunt)==1 :
                print(f"Vous aviez emprunter :\n {self.Abonnement[indice].livre_emprunt[0]} \n")
                print("Vous pouvez encore emprunter 1 livre\n")
                v2 = True
            elif len(self.Abonnement[indice].livre_emprunt)==0 :
                print("Vous pouvez emprunter 2 livre \n")
                v2 = True
                
        # Emprunt
        if v2 :
            books = self.Rechercher_livre(donnee)
            if len(books) == 0 :
                print("Aucun livre ne correspond à ce que vous voulez !\n")
            elif len(books) == 1 and books[0].nbr_exemplaire>0 :
                print(f"Voulez vous vraiment emprunter {books[0]} ? (o/n) : ")
                qq=input()
                if qq.lower().strip() == "o" :
                    (self.Abonnement[indice].livre_emprunt).append(books[0])
                    books[0].nbr_exemplaire -= 1
                    print("Vous avez emprunter un livre avec succès.\n")
                else :
                    print("D'accord emprunt annulé\n")
            elif len(books)==1 and not books[o].nbr_exemplaire>0 :
                print(f"Dsl {books[0]} n'est pas disponible")
            elif len(books)>1 :
                for i, elt in enumerate(books) :
                    print(i+1, " : ", elt, "\n")
                qq="bj"
                while type(qq) != int :
                    try :
                        qq=int(input("Veuillez confirmer l'emprunt en entrant le numero du livre correspondant (0 pou annuler) :  "))
                    except (TypeError, ValueError) :
                        print("Veuiller entrer un entier !\n")
                if qq==0 or qq>=len(books):
                    print("D'accord, emprunt annulé \n")
                else :
                    if books[qq-1].nbr_exemplaire>0 :
                        (self.Abonnement[indice].livre_emprunt).append(books[qq-1])                       
                        books[qq-1].nbr_exemplaire -= 1
                        print("Vous avez emprunter un livre avec succès.\n")
                    else :
                            print("Dsl ! Ce livre n'est pas diponible")
            
    def Retourner (self, donnee, identité) :
        for ident in self.Abonnement :
            if ident.val.lower() == identité.lower() :
                indice = self.Abonnement.index(ident)
                v1=True
                break
            else :
                v1 = False
        if not v1 :
            print("Dsl, vous n'êtes pas abonné !\nSeul les abonnés peuvent emprunter et retourner des livres\n")
        # On vérifie si le livre correspond
        if v1 :
            if  len(self.Abonnement[indice].livre_emprunt)== 0:
                print("Vous n'avez pas  emprunter de livre \n")
                v2=False
            else :
                v2=True
        if v2 :
            books = self.Rechercher_livre(donnee)
            if len(books) == 0:
                print("Aucun livre ne correspond \n")
                v3 = False
            elif len(books)>=1 :
                for elt in books :
                    if elt in self.Abonnement[indice].livre_emprunt :
                        print(f"Voulez vous Retourner {elt} ? (o/n)  ")
                        z = input()
                        if z.lower() == "o" :
                            (self.Abonnement[indice].livre_emprunt).remove(elt)
                            elt.nbr_exemplaire += 1
                            print(f"Mises jou avec succès : {self.Abonnement[indice]}")
                        else :
                            print("Retour Annuler !\n")
                    else :
                        print(f"Vous n'avez pas emprunter {books}")    

    def Supprimer (self, donnee):
        books = self.Rechercher_livre(donnee)
        
        if len(books) == 0:
            return "Aucun livre ne correspond\n"
        elif len(books)>=1 : 
            for elt in books :
                print(f"Voulez vous vraiment supprimer {elt} ? (o/n)  ")
                qq = input()
                if qq.lower() == "o" :
                    self.Livres.remove(elt)
                    print("Livre supprimer avec succès !\n")
                else :
                    print("Suppression annulé !\n")
  
    def Afficher_livres (self) :
        if not self.Livres :
            return ("Aucun Livre n'es enregistrer pour le moment")
        else :
            table_livre = Table(title="Liste des Livres")
            table_livre.add_column("Titre", style="cyan")
            table_livre.add_column("Auteur", style="magenta")
            table_livre.add_column("Année", style="green")
            table_livre.add_column("Numéro", style="cyan")
            table_livre.add_column("Nombre d'exemplaire", style="green")
            for elt in self.Livres :
                table_livre.add_row(elt.titre, elt.auteur, str(elt.annee), str(elt._numero), str(elt.nbr_exemplaire) )
            return console.print(table_livre)
                    
    def Afficher_abonner (self):
        if not self.Abonnement :
            print("Aucun abonné enregistrer !\n")
        else :
            table_abonner = Table(title="Liste des abonné")
            table_abonner.add_column("Nom", style="cyan")
            table_abonner.add_column("Prenom", style="magenta")
            table_abonner.add_column("Matricule", style="green")
            table_abonner.add_column("Nombre de Livres emprunter", style="cyan")
            table_abonner.add_column("Livres", style="magenta")
            table_abonner.add_column("Livres", style="green")
            for elt in self.Abonnement :
                table_abonner.add_row(elt.nom, elt.prenom, str(elt.matricule), str(len(elt.livre_emprunt)), (str(elt.livre_emprunt[0]) if len(elt.livre_emprunt)>=1 else ""), (str(elt.livre_emprunt[1]) if len(elt.livre_emprunt)==2 else ""))
            console.print(table_abonner)
    
        
# Fin Module