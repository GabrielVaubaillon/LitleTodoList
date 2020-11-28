import tache
import fichiers
import os #Pour écrire/supprimer les fichiers, TODO : surement une meilleure technique

#------------------------------------------------------------------------------
#       Config :
#------------------------------------------------------------------------------

#Le fichier de sauvegarde des taches
nameFichier = ""



#------------------------------------------------------------------------------
#       Fonctions
#------------------------------------------------------------------------------

#Créée une tache à partir de la commande, l'ajoute dans la liste des taches
def addTache(commande):
    #commande de la forme ["add", "name", "deadline"]
    name = commande[1]
    description = commande[2]
    listeTaches.append(tache.Tache(name, description))


#Affiche toutes les taches
def listTaches(commande):
    for t in listeTaches:
        print(tache.getName())


#------------------------------------------------------------------------------
#       Exectution
#------------------------------------------------------------------------------
#Petit message de bienvenue
print("\n\nLitleTodoList :)\n------------\n\n")


#Liste de toutes les taches :
listeTaches = []
fichiers.readTaches(listeTaches, nameFichier)


running = True
while running:
    commande = input("> ")
    #On découpe la commande en coupant aux espaces
    commande = commande.split(" ")

    if commande[0] in ["q","exit","quit"]:
        running = False

    if commande[0] == "list":
        listTaches(commande)

    if commande[0] == "add":
        addTache(commande)
