import tache
import fichiers

import dates
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
    indice = -1
    i = 0
    while (indice == -1) and (i < len(listeTaches)):
        if listeTaches[i].getId() == id:
            indice = i
        i += 1
    return indice

def dateFromCommand(strdate):
    date = dates.Date(dates.TODAY.getDay(), dates.TODAY.getMonth(), dates.TODAY.getYear())

    if strdate in ["t","today"]:
        pass

    elif strdate in ["tm","tomorow","nd","nday","nextday"]:
        date.addDays(1)

    elif strdate in ["w","nw","nweek","nextweek"]:
        date.addDays(7)

    elif strdate in ["tw","twow","twoweek"]:
        date.addDays(14)

    elif strdate in ["nm","nmonth","nextmonth"]:
        date.addDays(30)

    elif strdate in ["twomonth"]:
        date.addDays(60)

    elif strdate in ["ny","nyear","nextyear"]:
        date.addYear()

    elif ("-" in strdate) or ("/" in strdate):
        if "-" in strdate:
            param = strdate.split("-")
        else:
            param = strdate.split("/")

        if len(param) == 2:#dd-mm
            date = Date(int(param[0]), int(param[1]),dates.TODAY.getYear() )
            if date < dates.TODAY:
                date.addYear()

        elif len(param) == 3 and len(param[0] > 2):#yyyy-mm-dd
            date = Date(int(param[2]), int(param[1]), int(param[0]))
        elif len(param) == 3:#dd-mm-yyyy
            date = Date(int(param[0]), int(param[1]), int(param[2]))

    else:
        #La date n'est pas exprimée dans un fromat connu
        return None

    return date





#Créée une tache à partir de la commande, l'ajoute dans la liste des taches
def addTache(commande):
    global NEWID

    name = commande[1]
    t = tache.Tache(name = name, id = NEWID)
    NEWID += 1

    for i in range(1, len(commande)):

        param = commande[i].split("=")

        if len(param) > 1:
            if param[0] in ["d", "date"]:
                date = dateFromCommand(param[1])
                if date != None:
                    t.setDeadline(date)
                else:
                    print("Date non valide")

            if param[0] in ["p", "priorite"]:
                t.setPriorite(int(priorite))

            if param[0] in ["dc", "description"]:
                t.setDescription(param[1])

    listeTaches.append(t)

#Modifie les caracteristiques de la tache choisie et dans la liste des taches
def modifTache(commande):
    indice = getIndiceTache(int(commande[1]))

    if indice == -1:
        print("La Tache que vous voulez modifier n'existe pas")

    else :
        t = listeTaches[indice]

        for i in range(1, len(commande)):

            param = commande[i].split("=")

            if param[0] in ["n","name"]:
                t.setName(param[1])

            if param[0] in ["d", "date"]:
                date = dateFromCommand(param[1])
                if date != None:
                    t.setDeadline(date)
                else:
                    print("Date non valide")

            if param[0] in ["p", "priorite"]:
                t.setPriorite(int(priorite))

            if param[0] in ["dc", "description"]:
                t.setDescription(param[1])




#Supprime la tache en ieme position dans la liste générale :
def removeTache(commande):

    for i in  range(1, len(commande)):
        indice = getIndiceTache(int(commande[i]))
        if indice == -1:
            print("La Tache " + commande[i] + " n'existe pas")

        else :
            print("Effectuer la suppression de ",listeTaches[indice].getName(), "? [O/n] :  ", end="")
            if input() in ["O","o","","Y","y","yes"]:
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
