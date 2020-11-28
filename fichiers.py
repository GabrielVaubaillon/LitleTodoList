import tache


#Initialise la liste des taches à partir du nom du fichier source :
def readTaches(liste, fichier):
    f = open(ficher, "r")
    
    f.close()

#Sauvegarde la liste des taches dans un fichier :
def write(liste, fichier):

    f = open(fichier, "w")

    for t in liste:
        f.write("START" + t.strSave() + "END")

    f.close()
