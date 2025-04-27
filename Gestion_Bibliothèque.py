# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
from pickle import Unpickler, Pickler

# Le module de la bibliothèque
from Bibliothèque import*
# Définition/ Récupération de l'objet bibliothèque
BASE_DIR = os.path.dirname(__file__)
SAVE_FILE = os.path.join(BASE_DIR, "Sauvegarge.txt")
def ma_bibliotheque () :
    from pickle import Unpickler
    import os
    # fichier_stock = "c:/Users/Hp/Gestionnaire_Biblio/Data/Memoire.txt"
    if os.path.exists(fichier_stock) :
        with open(fichier_stock, "rb") as doc :
            m_ub = Unpickler(doc)
            donne = m_ub.load()
            livre.num = donne[1]
            abonner.mat = donne[2] 
            return donne[0]
    else :
        return Bibliotheque("Principal")

biblio=ma_bibliotheque()

# Enregistrement et récupération des donnés
def G_save(bibliotheque_princ) :
    import os
    # Attention le dossier contenant la memoire est à définir
    # doss_stock_1 = "C:/Users/HP/Gestionnaire_Biblio"
    if os.path.exists(doss_stock_1) :
        # doss_stock_2 = "C:/Users/HP/Gestionnaire_Biblio/Data"
        if os.path.exists(doss_stock_2) :
            # fichier_stock = "c:/Users/Hp/Gestionnaire_Biblio/Data/Memoire.txt"
            import pickle
            # liste contenant la bibliotheque principal,
            # le numéro du dernier livre,
            # le dernier matricule
            donne = [bibliotheque_princ, livre.num, abonner.mat]
            with open(fichier_stock, "wb") as doc :
                m_p = pickle.Pickler(doc)
                m_p.dump(donne)
        else :
            os.mkdir(doss_stock_2)
            return G_save()
    else :
        os.mkdir("doss_stock_1")
        return G_save()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Bibliothèque")
root.geometry("800x1200")
root.configure(bg="#F5F5F5")

# Le Menu Latérale
menu_frame = tk.Frame(root, bg="blue", width=150)
menu_frame.pack(side="left", fill="y")

# Icone du Menu
menu_slide = tk.Frame(menu_frame, width=150)
menu_slide.pack(side="top", fill="y")
menu_icone = tk.Button(menu_slide, text="  ≡        ", font=("Times New Roman", 16, "bold"))
menu_icone.pack(pady=10, side="left")
menu_label = tk.Label(menu_slide, text="      Menu     ", font=("Times New Roman", 16, "bold"))
menu_label.pack(pady=10, side="right")

# La zone principale
main_frame = tk.Frame(root)
main_frame.pack(expand=True, fill="both")
bienvenue = tk.Label(main_frame, text="Bienvenue dans la bibliothèque Principal\n Que pouvons nous faire pour vous ?", font=("Times New Roman", 18))
bienvenue.pack(fill="both", expand=True, side="top")


# Les fonctions du menu
def home() :
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    bienvenue = tk.Label(main_frame, text="Bienvenue dans la bibliothèque Principal\n Que pouvons nous faire pour vous ?", font=("Times New Roman", 18))
    bienvenue.pack(fill="both", expand=True, side="top")    
# option1 = Afficher les livres
def affichage_livre():
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Listes des livres Enregistrer", font=("Times New Roman", 16))
    Affich_1.pack()
    # Tableau avec treeview
    colonnes = ("Titre", "Auteur", "Année", "Numéro", "Nombre d'exemplaire")
    Table=ttk.Treeview(main_frame, columns=colonnes, show="headings")
    # Définitions des en_têtes
    for col in colonnes :
        Table.heading(col, text=col)
        Table.column(col, width=150, anchor="center")
    # Ajout de livres
    t_livres=[]
    for book in biblio.Livres :
        donne = (book.titre, book.auteur, book.annee, book._numero, book.nbr_exemplaire)
        t_livres.append(donne)
    for livre in t_livres :
        Table.insert("", "end", values=livre)
    
    # Placement du tableau
    Table.pack(expand=True, fill="both")

# option2 = afficher les abonner
def affichage_abonner():
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Listes des abonnés", font=("Times New Roman", 16))
    Affich_1.pack()
    # Tableau avec treeview
    colonnes = ("Nom", "Prenom", "Matricule", "Nbr de livre emprunter", "Premier livre", "Second livre")
    Table=ttk.Treeview(main_frame, columns=colonnes, show="headings")
    # Définitions des en_têtes
    for col in colonnes :
        Table.heading(col, text=col)
        Table.column(col, width=150, anchor="center")
    # Ajout de livres
    t_livres=[]
    for ab in biblio.Abonnement :
        donne = (ab.nom, ab.prenom, ab.matricule, len(ab.livre_emprunt), (ab.livre_emprunt[0] if len(ab.livre_emprunt)>=1 else "None"), (ab.livre_emprunt[1] if len(ab.livre_emprunt)==2 else "None"))
        t_livres.append(donne)
    for livre in t_livres :
        Table.insert("", "end", values=livre)
    
    # Placement du tableau
    Table.pack(expand=True, fill="both")
    # return biblio.Afficher_abonner()

# option3 = Abonnement
def affichage_abonnement() :
    def get_inform() :
        global main_frame
        for widget in main_frame.winfo_children() :
            widget.destroy()
        Affich_1 = tk.Label(main_frame, text="Procédures d'Abonnement", font=("Times New Roman", 16))
        Affich_1.pack()
        # Le nom
        nom_frame = tk.Frame(main_frame)
        nom_frame.pack(fill="x")
        nom=tk.StringVar()
        nom_label=tk.Label(nom_frame, text="Nom : ", font=("Times New Roman", 18)).pack(side="left")
        nom_saisie = tk.Entry(nom_frame, font=("Times New Roman", 14), textvariable=nom).pack(side="left")
        # Prénom
        prenom_frame = tk.Frame(main_frame)
        prenom_frame.pack(fill="x")
        prenom=tk.StringVar()
        prenom_label=tk.Label(prenom_frame, text="Prénom : ", font=("Times New Roman", 18)).pack(side="left")
        prenom_saisie = tk.Entry(prenom_frame, font=("Times New Roman", 14), textvariable=prenom).pack(side="left")
        # Soumission
        def soumission() :
            name = nom.get().strip()
            first_name = prenom.get().strip()
            for widget in main_frame.winfo_children() :
                if widget != Affich_1 :
                    widget.destroy()
                    
            if not biblio.Abonnement :
                nouveau = abonner(name, first_name)
                biblio.Abonnement.append(nouveau)
                message = tk.Label(main_frame, text="Vous êtes entregistrer avec succès", font=("Times New Roman", 18), background="green")
                message.pack()
                      
            else :
                val = name + " " + first_name
                for personne in biblio.Abonnement :
                    if personne.val.lower() == val.lower() :
                        message = tk.Label(main_frame, text="Vous êtes dejà entregistrer !", font=("Times New Roman", 18), background="red")
                        message.pack()
                        return 0
                nouveau = abonner(name, first_name)
                biblio.Abonnement.append(nouveau)
                message = tk.Label(main_frame, text="Vous êtes  entregistrer avec succès !", font=("Times New Roman", 18), background="green")
                message.pack()
            G_save(biblio)   
        # Bouton de soumission/ exécute soumission()
        sommettre = tk.Button(main_frame, text="Soumettre", font=("Times New Roman", 18), bg="green", command=soumission).pack()
    
    get_inform()

# option4 = Ajouter Livre
def affichage_ajout() :
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Procédure pour ajouter un livre", font=("Times New Roman", 18))
    Affich_1.pack()
    affich_2 = tk.Label(main_frame, text="Les informations du livre à ajouté", font=("Times New Roman", 14))
    affich_2.pack()
    # Le Titre
    titre_frame = tk.Frame(main_frame)
    titre_frame.pack(fill="x")
    titre=tk.StringVar()
    titre_label=tk.Label(titre_frame, text="Titre : ", font=("Times New Roman", 14)).pack(side="left")
    titre_saisie = tk.Entry(titre_frame, font=("Times New Roman", 14), textvariable=titre).pack(side="left")
    # Auteur
    auteur_frame = tk.Frame(main_frame)
    auteur_frame.pack(fill="x")
    auteur=tk.StringVar()
    auteur_label=tk.Label(auteur_frame, text="Auteur : ", font=("Times New Roman", 18)).pack(side="left")
    auteur_saisie = tk.Entry(auteur_frame, font=("Times New Roman", 14), textvariable=auteur).pack(side="left")
    # Année
    annee_frame = tk.Frame(main_frame)
    annee_frame.pack(fill="x")
    annee=tk.StringVar()
    annee_label=tk.Label(annee_frame, text="Année : ", font=("Times New Roman", 18)).pack(side="left")
    annee_saisie = tk.Entry(annee_frame, font=("Times New Roman", 14), textvariable=annee).pack(side="left")
    # Nbre d'exemplaire
    nbr_frame = tk.Frame(main_frame)
    nbr_frame.pack(fill="x")
    nombre=tk.StringVar()
    nbr_label=tk.Label(nbr_frame, text="Nbre d'exemplaires : ", font=("Times New Roman", 18)).pack(side="left")
    nbr_saisie = tk.Entry(nbr_frame, font=("Times New Roman", 14), textvariable=nombre).pack(side="left")
    
    def ajouter() :
        T = titre.get().strip()
        aut = auteur.get().strip()
        try :
            anne = int(annee.get())
            nbr = int(nombre.get())
        except :
            from tkinter import messagebox
            messagebox.showerror("Erreur", "L'année et le nbre de livres doivent être des entier")
            return 0
        
        # Ajout
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 :
                    widget.destroy()
        if not biblio.Livres :
            nv = livre(T, aut, anne, nbr)
            biblio.Livres.append(nv)
            message = tk.Label(main_frame, text=f"Livre ajouter avec succès: {nv} ", font=("Times New Roman", 18), background="green")
            message.pack()
            G_save(biblio)
        else :
            for book in biblio.Livres :
                if book.titre.lower()==T.lower() and book.auteur.lower()==aut.lower() and int(book.annee)==anne :
                    message = tk.Label(main_frame, text=f"Ce livre existe dejà:\n {book} ", font=("Times New Roman", 18), background="green")
                    message.pack()
                    # option pour ajout d'exemplaire
                    quest = tk.Label(main_frame, text="Voulez vous ajouter des exemplaires ?", font=("Times New Roman", 18)).pack()
                    reponse = tk.Frame(main_frame)
                    reponse.pack()
                    # pas d'ajout d'exemplaire
                    def non() :
                        for widget in main_frame.winfo_children() :
                            if widget != Affich_1 :
                                widget.destroy()
                        message = tk.Label(main_frame, text=f"Daccord \n On ne peut pas ajouer un livre qui existe djà", font=("Times New Roman", 18), background="green")
                        message.pack() 
                    # Ajou d'exemplaire
                    def oui() :
                        for widget in main_frame.winfo_children() :
                            if widget != Affich_1 :
                                widget.destroy()
                        message = tk.Label(main_frame, text=f"Combien de livre voulez vous ajouter ?", font=("Times New Roman", 18), background="green")
                        message.pack() 
                        exemp = tk.StringVar()
                        tk.Entry(main_frame, font=("Times New Roman", 14), textvariable=exemp).pack()
                        # Pour ajouter
                        def ajout():
                            try :
                                exemplaire = int(exemp.get())
                            except :
                                from tkinter import messagebox
                                messagebox.showerror("Erreur", "Le nbre d'exemplaire à ajouter doit être un entier !")
                                return 0
                            for widget in main_frame.winfo_children() :
                                if widget != Affich_1 :
                                    widget.destroy()
                            book.nbr_exemplaire += exemplaire
                            message = tk.Label(main_frame, text=f"Livres mis à jour : \n {book}", font=("Times New Roman", 18), background="green")
                            message.pack()
                            G_save(biblio)
                                
                            # Bouton pour ajout
                        tk.Button(main_frame, text="Ajouter", font=("Times New Roman", 18), command=ajout).pack()
                                
                    oui = tk.Button(reponse, text="Oui", background="blue", command=oui).pack(side="left")
                    non=tk.Button(reponse, text="NON", background="yellow", command=non).pack(side="left")
                    return 0
            nv = livre(T, aut, anne, nbr)
            biblio.Livres.append(nv)
            message = tk.Label(main_frame, text=f"Livre ajouter avec succès :\n {nv} ", font=("Times New Roman", 18), background="green")
            message.pack()
            G_save(biblio)
            return 0  
            
    
    # Bouton de soumission
    sommettre = tk.Button(main_frame, text="Soumettre", font=("Times New Roman", 18), bg="green", command=ajouter).pack()

#option5 = Emprunter un livre
def affichage_emprunt():
    from tkinter import messagebox
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Procédure pour emprunter un livre", font=("Times New Roman", 18))
    Affich_1.pack()
    Affich_2 = tk.Label(main_frame, text="NB : Seul les abonner peuvent emprunter les livres", font=("Times New Roman", 18), background="red")
    Affich_2.pack()
    # L'abonner Voulant emprunter le livre
    def info_abonne():
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in item.val.lower():
                    listebox.insert(tk.END, item.val)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Nom et prénom de l'abonner  : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Vérification du abonné
        def verifie_ab():
            val=entree.get().lower().strip()
            if not biblio.Abonnement :
                messagebox.showwarning("Attention", "vous n'êtes pas Abonné !")
            else :
                for it in biblio.Abonnement :
                    if val==it.val.lower() :
                        return info_emprunt(it)
                messagebox.showwarning("Attention", "vous n'êtes pas Abonné !")
        # Boutons entré
        tk.Button(Recher, text=" Entrer ", bg="green", command=verifie_ab).pack(side="left")
        # Les Abonnés
        elements=[]
        for it in biblio.Abonnement :
            elements.append(it)
        # Liste des abonnés
        listebox = tk.Listbox(main_frame, width=30,height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, item.val)
        # Remplir la barres de recherche en cliquant sur un élement de la liste
        def element_selectionne(event) :
            selection = listebox.curselection()
            if selection :
                valeur = listebox.get(selection[0])
                entree.delete(0, tk.END)  #effecer le champ
                entree.insert(0, valeur)  #mis à jour du champ
        listebox.bind("<Double-Button-1>", element_selectionne) 
    
    # Vérification nbre de livre emprunté
    def info_emprunt(abonné):
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        Affich_2["text"] = "Aucun Abonné ne peut Emprunter Plus de 2 Livres"
        tk.Label(main_frame, text=f"Abonné : \n {abonné}", font=("Times New Roman", 18)).pack()
        # Fonction pour envoyer l'objet abonné à la fonction infos_livres
        def vérif_em():
            return infos_livres(abonné)
        if len(abonné.livre_emprunt)==0:
            tk.Label(main_frame, text=f"Vous Pouvez encore emprunter 2 livres", bg="green", font=("Times New Roman", 14)).pack()
            tk.Button(main_frame, text=" Choisir livre ", bg="pink", font=("Times New Roman", 18), command=vérif_em).pack()
        elif len(abonné.livre_emprunt) == 1:
            tk.Label(main_frame, text=f"Livre emprunté :\n   {abonné.livre_emprunt[0]}", font=("Times New Roman", 18)).pack()
            tk.Label(main_frame, text=f"Vous pouvez encore emprunter 1 livres", bg="green", font=("Times New Roman", 14)).pack()
            tk.Button(main_frame, text=" Choisir livre ", bg="pink", font=("Times New Roman", 18), command=vérif_em).pack()
        elif len(abonné.livre_emprunt) == 2:
            tk.Label(main_frame, text=f"Livre emprunté :\n   {abonné.livre_emprunt[0]}\n    {abonné.livre_emprunt[1]}", font=("Times New Roman", 14)).pack()
            tk.Label(main_frame, text=f"Vous ne pouvez plus emprunter de livre encore", bg="red", font=("Times New Roman", 14)).pack()

    # Le livre à emprunter
    def infos_livres(abonné):
        """Seul les livres disponible seront afficher"""
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in item :
                    listebox.insert(tk.END, item)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Recherche : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        tk.Label(main_frame, text="Double clic pour Sélectionner le livre ", font=("Times New Roman", 14)).pack()
        # Les livres
        elements=[]
        for it in biblio.Livres :
            if it.nbr_exemplaire>0 :
                elements.append(it)
        # Liste des livres
        listebox = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, item)
        # Sélection du livre
        def element_selectionne(event):
            selection = listebox.curselection()
            book=listebox.get(selection[0])
            for elt in biblio.Livres :
                if book==str(elt) :
                    g_book = elt
            return go_emprunt(abonné, g_book)
        # Sélectionner le livre qu'on veut
        listebox.bind("<Double-Button-1>", element_selectionne)     
    
    # Fin emprunter le livre
    def go_emprunt(abonné, livre):
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        abonné.livre_emprunt.append(livre)
        livre.nbr_exemplaire -= 1
        G_save(biblio)
        tk.Label(main_frame, text=f"Vous : {abonné}\n Avez emprunter avec succès le livre :\n {livre}", bg="green", font=("Times New Roman", 16)).pack()
                        
    return info_abonne()
    
# option6 = Retourner Livre
def affichage_retourLivre():
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Procédure pour Retourner un livre emprunté", font=("Times New Roman", 18))
    Affich_1.pack()
    Affich_2 = tk.Label(main_frame, text="NB : Vous ne povez pas retourner un livre que vous n'avez pas emprunté", font=("Times New Roman", 18), background="red")
    Affich_2.pack()
    # L'abonner Voulant retourner le livre
    def info_abonne():
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in item.val.lower():
                    listebox.insert(tk.END, item.val)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Nom et prénom de l'abonner  : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Vérification du abonné
        def verifie_ab():
            val=entree.get().lower().strip()
            if not biblio.Abonnement :
                messagebox.showwarning("Attention", "vous n'êtes pas Abonné !")
            else :
                for it in biblio.Abonnement :
                    if val==it.val.lower() :
                        return info_emprunt(it)
                messagebox.showwarning("Attention", "vous n'êtes pas Abonné !")
        # Boutons entré
        tk.Button(Recher, text=" Entrer ", bg="green", command=verifie_ab).pack(side="left")
        # Les Abonnés
        elements=[]
        for it in biblio.Abonnement :
            elements.append(it)
        # Liste des abonnés
        listebox = tk.Listbox(main_frame, width=30,height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, item.val)
        # Remplir la barres de recherche en cliquant sur un élement de la liste
        def element_selectionne(event) :
            selection = listebox.curselection()
            if selection :
                valeur = listebox.get(selection[0])
                entree.delete(0, tk.END)  #effecer le champ
                entree.insert(0, valeur)  #mis à jour du champ        
        listebox.bind("<Double-Button-1>", element_selectionne)     

    # Vérification des livres empruntés par l'abonner
    def info_emprunt(abonné):
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        Affich_2["text"] = "Aucun Abonné ne peut Emprunter Plus de 2 Livres"
        tk.Label(main_frame, text=f"Abonné : \n {abonné}", font=("Times New Roman", 18)).pack()
        # Fonction pour envoyer l'objet abonné à la fonction infos_livres
        if len(abonné.livre_emprunt)==0:
            tk.Label(main_frame, text="Vous n'avez emprunter aucun livre", bg="green", font=("Times New Roman", 14)).pack()
        elif len(abonné.livre_emprunt) == 1:
            tk.Label(main_frame, text=f"Livre emprunté :\n   {abonné.livre_emprunt[0]}", font=("Times New Roman", 18)).pack()
            tk.Label(main_frame, text=f"Voulez vous vraiment retourner ce livre ?", bg="green", font=("Times New Roman", 14)).pack()
            oui_non=tk.Frame(main_frame)
            oui_non.pack()
            # Fonction pour échapper à l'exécution de go_retour au démarrage/ éviter des ereurs
            def détour_go():
                return go_retour(abonné, abonné.livre_emprunt[0])
            tk.Button(oui_non, text=" OUI ", bg="pink", font=("Times New Roman", 18), command=détour_go).pack(side="left")
            tk.Button(oui_non, text=" Non ", bg="pink", font=("Times New Roman", 18), command=N_retour).pack(side="left")
        elif len(abonné.livre_emprunt) == 2:
            tk.Label(main_frame, text=f"Livre emprunté : ", font=("Times New Roman", 14)).pack()
            tk.Label(main_frame, text=f"Veuillez sélecctionner le livre que vous voulez retourner ", font=("Times New Roman", 16)).pack()
            livre_emprunter = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 14))
            livre_emprunter.pack()
            for item in abonné.livre_emprunt :
                livre_emprunter.insert(tk.END, item)
            # fonction pour livre sélectionner
            def element_selectionne(event):
                selection = livre_emprunter.curselection()
                book=livre_emprunter.get(selection[0])
                for elt in biblio.Livres :
                    if book==str(elt) :
                        g_book = elt
                return go_retour(abonné, g_book)
            livre_emprunter.bind("<Double-Button-1>", element_selectionne)
    
    # Fonction pas de retour
    def N_retour():
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        tk.Label(main_frame, text="Daccord, A la prochaine", bg="silver", font=("Times New Roman", 14)).pack()
        
    # Fin retourner livre
    def go_retour(abonné, livr) :
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 and widget != Affich_2 :
                widget.destroy()
        # proccessus de retour de livre
        abonné.livre_emprunt.remove(livr)
        livr.nbr_exemplaire += 1
        G_save(biblio)
        tk.Label(main_frame, text=f"{livr} a été retourné avec succès ", bg="silver", font=("Times New Roman", 14)).pack()
    
    return info_abonne()

# option7 = Supprimer Livre
def suppression_livre():
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Procédure pour supprimer définitivement un livre", font=("Times New Roman", 18))
    Affich_1.pack()
    tk.Label(main_frame, text="Veuillez sélectionner le livre que vous voulez supprimer ", bg="silver", font=("Times New Roman", 16)).pack()
    # choix du livre à supprimer
    def infos_livres():
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in str(item).lower():
                    listebox.insert(tk.END, item)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Recherche : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Les livres
        elements=[]
        for it in biblio.Livres :
            elements.append(it)
        # Liste des livres
        listebox = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, str(item))
        # La sélection de livre
        def element_selectionne(event):
            selection = listebox.curselection()
            val=listebox.get(selection[0])
            for item in biblio.Livres :
                if val == str(item) :
                    book = item
            return go_supprimer(book)         
        listebox.bind("<Double-Button-1>", element_selectionne)
    
    # fin supprimer le livre
    def go_supprimer(livr):
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 :
                widget.destroy()
        # suppression
        biblio.Livres.remove(livr)
        G_save(biblio)
        tk.Label(main_frame, text=f"{livr} \n a été supprimer avec succès", bg="green", font=("Times New Roman", 16)).pack()
        
    return infos_livres()

# option8 = Supprimer un Abonner
def suppression_abonne():
    from tkinter import messagebox
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Procédure pour supprimer définitivement un abonné", font=("Times New Roman", 18))
    Affich_1.pack()
    tk.Label(main_frame, text="Veuillez sélectionner l'abonné' que vous voulez supprimer ", bg="silver", font=("Times New Roman", 16)).pack()
    # choix de l'abonné à supprimer
    def info_abonne():
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in str(item).lower():
                    listebox.insert(tk.END, item)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Recherche : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Les Abonnés
        elements=[]
        for it in biblio.Abonnement :
            elements.append(it)
        # Liste des livres
        listebox = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, item)
        # sélection de l'abonné
        def element_selectionne(event):
            selection = listebox.curselection()
            val = listebox.get(selection[0])
            for item in biblio.Abonnement :
                if val==str(item):
                    abonn = item
            return go_supprimer(abonn)            
        listebox.bind("<Double-Button-1>", element_selectionne)    
    
    # fin supprimer abonné
    def go_supprimer(abonné) :
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 :
                widget.destroy()
        # suppression
        biblio.Abonnement.remove(abonné)
        G_save(biblio)
        tk.Label(main_frame, text=f"{abonné} \n a été supprimer avec succès", bg="green", font=("Times New Roman", 16)).pack()
    
    return  info_abonne()  
     
# option9 = Recherche
def Recherche() :
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="          RECHERCHE           ", font=("Times New Roman", 18))
    Affich_1.pack()
    Affich2 = tk.Label(main_frame, text="Que rechercher vous ? ", font=("Times New Roman", 18))
    Affich2.pack()
    opt = tk.Frame(main_frame)
    opt.pack()
    # Recherche de livres
    def recherche_livre():
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 :
                    widget.destroy()
        Affich_1["text"] = "        RECHERCHE DE LIVRE      "
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in str(item).lower():
                    listebox.insert(tk.END, item)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Recherche : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Les livres
        elements=[]
        for it in biblio.Livres :
            elements.append(it)
        # Liste des livres
        listebox = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, str(item))
            
    # Recherche d'abonner
    def recherche_abonne():
        for widget in main_frame.winfo_children() :
            if widget != Affich_1 :
                    widget.destroy()
        Affich_1["text"] = "        RECHERCHE DE D'ABONNER      "
        # Barres de recherche
        def mise_a_jour_liste(event):
            recherche = entree.get().lower()
            listebox.delete(0, tk.END)  # Efface la liste
            for item in elements:
                if recherche in str(item).lower():
                    listebox.insert(tk.END, item)  # Ajoute les éléments correspondants
        Recher = tk.Frame(main_frame)
        Recher.pack()
        tk.Label(Recher, text="Recherche : ", font=("Times New Roman", 14)).pack(side="left")
        entree = tk.Entry(Recher, width=30, font=("Times New Romane", 12))
        entree.pack(side="left", pady=10)
        entree.bind("<KeyRelease>", mise_a_jour_liste)
        # Les Abonnés
        elements=[]
        for it in biblio.Abonnement :
            elements.append(it)
        # Liste des livres
        listebox = tk.Listbox(main_frame, width=60, height=20, font=("Times New Romane", 12))
        listebox.pack()
        for item in elements:
            listebox.insert(tk.END, str(item))
    
    # soumission choix : livre / abonné
    livre_opt = tk.Button(opt, text="  LIVRE  ", font=("Times New Roman", 18), background="green", command=recherche_livre).pack(side="left")
    abonne_opt=tk.Button(opt, text="  ABONNER  ", font=("Times New Roman", 18), background="green", command=recherche_abonne).pack(side="left")

# option10 = A propos
def propos():
    global main_frame
    for widget in main_frame.winfo_children() :
        widget.destroy()
    Affich_1 = tk.Label(main_frame, text="Information ", font=("Times New Roman", 18))
    Affich_1.pack()
    tk.Label(main_frame, text="Cette application est un projet visant à mettre en application\n Les concept d'objet en python", bg="silver", font=("Times New Roman", 16)).pack()
    tk.Label(main_frame, text="Cette application à utiliser :\n\
            ✅ Python comme language de programmation\n\
            ✅ Tkinter comme librairie pour interface graphique\n", font=("Times New Roman", 18)).pack()
    tk.Label(main_frame, text="\n \n ").pack()
    tk.Label(main_frame, text="Le projet est constituer comme suit :\n\
             ✅ Un fichier nommé Bibliothèque.py contenant la définition des classe comme : la bibliothèque, livre et abonn.\n Ces classes possèdes divers méthodes\n\
                 ✅ main_Bibliothèque.py qui défini une application console de la bibliothèque\n\
                     ✅Gestion_Bibliothèque.py qui défini l'application avec interface graphique (cette application)\n\
                         ✅Un dossier mémoir où enregistrer un objet : 'biblio' qui est la bibliothèque utilisé par l'application console et l'interface\n\
                             Ce objet isuues de classes bibliothèque est enregistrer à chaque modification et comme la classe elle contient comme attribut :\n la liste des livres et des abonné qui renferment également d'autre informeaions\n\
                                 Les autres objet 'B_abonner' et 'B_livre.py' permettent d'enregistrer le derniers numéro de livre et matricule enfin de\n maintenir le fil lors des prochaine modification\
                                     ", bg="silver", font=("Times New Roman", 14)).pack()
    tk.Label(main_frame, text="\n \n ").pack()
    tk.Label(main_frame, text="Ce projet à été dévelloppé par :\n\
        Jean DJANTA\n\
            e-mail : jeansdjanta@hotmail.com\n", font=("Times New Roman", 13)).pack(side="bottom")
    
# Les options du menus
options = [
    "Acueille",
    "Afficher les livres",
    "Afficher les abonner",
    "Abonnement",
    "Ajouter Livre",
    "Emprunter un livre",
    "Retourner Livre",
    "Supprimer Livre",
    "Supprimer un Abonner",
    "Rechercher",
    "A propos",
    "Quitter"
]

for option in options :
    # Option quitter
    if option=="Quitter" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), bg="red", relief="flat", command=root.quit )
        btn.pack(fill="x", pady=5)
    elif option ==  "Acueille" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), bg="green", relief="flat", command=home )
        btn.pack(fill="x", pady=5)
    elif option=="Afficher les livres":
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_livre)
        btn.pack(fill="x", pady=5)
    elif option=="Afficher les abonner" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_abonner)
        btn.pack(fill="x", pady=5)
    elif option=="Abonnement" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_abonnement)
        btn.pack(fill="x", pady=5)
    elif option=="Ajouter Livre" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_ajout)
        btn.pack(fill="x", pady=5)
    elif option=="Emprunter un livre" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_emprunt)
        btn.pack(fill="x", pady=5)
    elif option=="Retourner Livre" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=affichage_retourLivre)
        btn.pack(fill="x", pady=5)
    elif option=="Supprimer Livre" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=suppression_livre)
        btn.pack(fill="x", pady=5)
    elif option=="Supprimer un Abonner" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=suppression_abonne)
        btn.pack(fill="x", pady=5)
    elif option=="Rechercher" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=Recherche)
        btn.pack(fill="x", pady=5)
    elif option=="A propos" :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), relief="flat", command=propos)
        btn.pack(fill="x", pady=5)
    else :
        btn=tk.Button(menu_frame, text=option, font=("Times New Roman", 14), background="yellow", relief="flat")
        btn.pack(fill="x", pady=5)  


root.mainloop()
# Fin Code
