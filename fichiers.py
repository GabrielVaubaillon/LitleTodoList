import tache


#Initialise la liste des taches à partir du fichier source :
def readTaches(liste, fichier):
    f = open(fichier, "r")
    lignes = f.readlines()
    f.close()

    for ligne in lignes:
        if ligne != "\n":
            liste.append(tache.fromSaveToTache(ligne[:-1]))


#Sauvegarde la liste des taches dans un fichier :
def write(liste, fichier):

    f = open(fichier, "w")

    #On stocke une tache par ligne
    for t in liste:
        f.write(t.strSave() + "\n")

    f.close()
