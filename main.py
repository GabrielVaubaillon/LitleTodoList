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

#Permet de récupérer l'emplacement de la tache id dans la liste
def getIndiceTache(id):
    i = 0
    while listeTaches[i].getId() != id:
        i += 1
    return i


#Créée une tache à partir de la commande, l'ajoute dans la liste des taches
def addTache(commande):
    global NEWID

    name = commande[1]
    t = tache.Tache(name = name, id = NEWID)
    NEWID += 1

    for i in range(1, len(commande)):

        param = commande[i].split("=")

        if param[0] in ["d", "date"]:
            if param[1] == "today":
                t.setDeadline(dt.date.today())
            else:
                t.setDeadline(dt.date.fromisoformat(param[1]))

        if param[0] in ["p", "priorite"]:
            t.setPriorite(int(priorite))

        if param[0] in ["dc", "description"]:
            t.setDescription(param[1])

    listeTaches.append(t)

#Modifie les caracteristiques de la tache choisie et dans la liste des taches
def modifTache(commande):
    indice = getIndiceTache(int(commande[1]))

    t = listeTaches[indice]

    for i in range(1, len(commande)):

        param = commande[i].split("=")

        if param[0] in ["n","name"]:
            t.setName(param[1])

        if param[0] in ["d", "date"]:
            if param[1] == "today":
                t.setDeadline(dt.date.today())
            else:
                t.setDeadline(dt.date.fromisoformat(param[1]))

        if param[0] in ["p", "priorite"]:
            t.setPriorite(int(priorite))

        if param[0] in ["dc", "description"]:
            t.setDescription(param[1])




#Supprime la tache en ieme position dans la liste générale :
def removeTache(commande):
    indice = getIndiceTache(int(commande[1]))
    print("Effectuer la suppression de ",listeTaches[indice].getName(), "? [O/n] :  ", end="")
    if input() in ["O","o",""]:
        del listeTaches[indice]


#Affiche toutes les taches
def listTaches(commande):
    listeAffichage = listeTaches[:]
    if len(commande) > 1 and commande[1] == "date":
        listeAffichage.sort(key= lambda tache : tache.getDate())

    for i in range(len(listeAffichage)):
        t = listeAffichage[i]
        print("-",t.getId(),":",t.getName(), "   ", t.strDeadline())


#------------------------------------------------------------------------------
#       Exectution
#------------------------------------------------------------------------------
#Petit message de bienvenue
print("\n\nLitleTodoList :)\n------------\n\n")


#Liste de toutes les taches :
listeTaches = []
fichiers.readTaches(listeTaches, nameFichier)

#On stocke dans cette variable globale le plus grand identifiant dispo
#Les identifiants changent à chaque recharge de la sauvegarde. On ne fait
#que les augmenter durant toute l'execution, meme si suppressions
NEWID = len(listeTaches)


running = True
while running:
    commande = input("> ")
    #On découpe la commande en coupant aux espaces
    commande = commande.split(" ")

    if commande[0] in ["q","exit","quit"]:
        fichiers.write(listeTaches, nameFichier)
        running = False

    if commande[0] in ["list", "ls"]:
        listTaches(commande)

    if commande[0] == "add":
        addTache(commande)

    if commande[0] == "modif":
        modifTache(commande)

    if commande[0] in ["remove","rm"]:
        removeTache(commande)

    if commande[0] == "save":
        fichiers.write(listeTaches, nameFichier)
