
#------------------------------------------------------------------------------
#       Imports :
#------------------------------------------------------------------------------

# Fichiers :
import tache
import fichiers
import dates

#------------------------------------------------------------------------------
#       Config :
#------------------------------------------------------------------------------

#Le chemin du fichier de sauvegarde des taches
nameFichier = "todo.ltdl"



#------------------------------------------------------------------------------
#       Fonctions
#------------------------------------------------------------------------------

#Permet de récupérer l'emplacement de la tache id dans la liste
#param : id, entier positif, l'identifiant de la tache recherchée
#return : entier, l'indice de la tache dans la liste des taches,
#       -1 si non trouvé
def getIndiceTache(id):
    indice = -1
    i = 0
    while (indice == -1) and (i < len(listeTaches)):
        if listeTaches[i].getId() == id:
            indice = i
        i += 1
    return indice




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
                date = dates.dateFromString(param[1])
                if date != None:
                    t.setDeadline(date)
                else:
                    print("Date non valide")

            if param[0] in ["p", "priorite"]:
                t.setPriorite(int(param[1]))

            if param[0] in ["dc", "description"]:
                t.setDescription(param[1])

    listeTaches.append(t)

#Modifie la tache choisie
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
                date = dates.dateFromString(param[1])
                if date != None:
                    t.setDeadline(date)
                else:
                    print("Date non valide")

            if param[0] in ["p", "priorite"]:
                t.setPriorite(int(param[1]))

            if param[0] in ["dc", "description"]:
                t.setDescription(param[1])




#Supprime les tache id de la liste des taches :
def removeTache(commande):
    #TODO : creer une corbeille, la vider automatiquement au bout d'un certain
    #temps

    for i in  range(1, len(commande)):
        indice = getIndiceTache(int(commande[i]))
        if indice == -1:
            print("La Tache " + commande[i] + " n'existe pas")

        else :
            print("Effectuer la suppression de ",listeTaches[indice].getName(), "? [O/n] :  ", end="")
            if input() in ["O","o","","Y","y","yes"]:
                del listeTaches[indice]


#Affiche les taches en les filtrant/triant selon les parametres
def listTaches(commande):
    listeAffichage = listeTaches[:]
    #On trie puis filtre la liste des taches en fonction des parametres :
    if len(commande) > 1 and commande[1] == "date":
        listeAffichage.sort(key= lambda tache : tache.getDate())

    #On affiche la liste triée :
    for i in range(len(listeAffichage)):
        t = listeAffichage[i]
        print("-",t.getId(),":",t.getName(), "   ", t.strDeadline())


#------------------------------------------------------------------------------
#       Variables globales
#------------------------------------------------------------------------------

#Liste de toutes les taches :
listeTaches = []
fichiers.readTaches(listeTaches, nameFichier)

#On stocke dans cette variable globale le plus grand identifiant dispo
#Les identifiants changent à chaque recharge de la sauvegarde. On ne fait
#que les augmenter durant toute l'execution, meme si suppressions
NEWID = len(listeTaches)

#------------------------------------------------------------------------------
#       Exectution
#------------------------------------------------------------------------------

#Petit message de bienvenue
print("\n\nLitleTodoList :)\n------------\n\n")


running = True
while running:
    commande = input("> ")
    #On découpe la commande en coupant aux espaces
    #Note : ça veut dire, qu'il ne faut pas d'espaces dans les noms des taches,
    # ni dans leurs descriptions
    commande = commande.split(" ")

    if commande[0] in ["q","exit","quit"]:
        #On sauvegarde
        fichiers.write(listeTaches, nameFichier)
        #On quitte le programme
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
