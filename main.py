import tache
import fichiers

import datetime as dt
import os #Pour écrire/supprimer les fichiers, TODO : surement une meilleure technique

#------------------------------------------------------------------------------
#       Config :
#------------------------------------------------------------------------------

#Le fichier de sauvegarde des taches
nameFichier = "todo.ltdl"



#------------------------------------------------------------------------------
#       Fonctions
#------------------------------------------------------------------------------

#Créée une tache à partir de la commande, l'ajoute dans la liste des taches
def addTache(commande):
    name = commande[1]
    t = tache.Tache(name = name)

    for i in range(1, len(commande)):

        param = commande[i].split("=")

        if param[0] in ["d", "date"]:
            if param[1] == "today":
                t.setDeadline(dt.date.today())
            else:
                t.setDeadline(dt.date.fromisoformat(param[1]))

        if param[0] in ["dc", "description"]:
            t.setDescription(param[1])

    listeTaches.append(t)

#Supprime la tache en ieme position dans la liste générale :
def removeTache(commande):
    id = int(commande[1])
    print("Effectuer la suppression de ",listeTaches[id].getName(), "? [O/n] :  ", end="")
    if input() in ["O","o",""]:
        del listeTaches[id]


#Affiche toutes les taches
def listTaches(commande):
    for i in range(len(listeTaches)):
        t = listeTaches[i]
        print("-",i,":",t.getName(), "   ", t.strDeadline())


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
        fichiers.write(listeTaches, nameFichier)
        running = False

    if commande[0] == "list":
        listTaches(commande)

    if commande[0] == "add":
        addTache(commande)

    if commande[0] == "remove":
        removeTache(commande)

    if commande[0] == "save":
        fichiers.write(listeTaches, nameFichier)
