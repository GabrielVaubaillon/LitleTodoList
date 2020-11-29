import datetime as dt

class Tache:

    # Constructeur :
    #---------------
    def __init__(self, name, deadline=None, description = " "):
        self.name = name
        self.deadline = deadline
        self.description = description

    def setName(self, name):
        self.name = name

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setDescription(self, description):
        self.description = description

    # Méthodes :
    #-----------
    def getName(self):
        return self.name

    def strDeadline(self):
        if self.deadline != None:
            return self.deadline.strftime("%A %d %B")

    #Retourne la chaine de caractere de sauvegarde de la tache
    def strSave(self):
        ch = self.name + "\\"
        ch += self.deadline.isoformat() + "\\"
        ch += self.description + "\\"
        return ch


#Retourne la Tache correspondant à la chaine de caractere de sauvegarde
def fromSaveToTache(save):
    save = save.split("\\")
    name = save[0]
    deadline = dt.date.fromisoformat(save[1])
    description = save[2]
    return Tache(name, deadline, description)
