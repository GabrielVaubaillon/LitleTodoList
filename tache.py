import datetime as dt

class Tache:

    # Constructeur :
    #---------------
    def __init__(self, name, deadline=None, description = " ",
                    priorite=5):
        self.name = name
        self.deadline = deadline
        self.description = description
        self.priorite = priorite

    def setName(self, name):
        self.name = name

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setDescription(self, description):
        self.description = description

    def setPriorite(self, priorite):
        self.priorite = priorite

    # Méthodes :
    #-----------
    def getName(self):
        return self.name

    def getDate(self):
        return self.deadline

    def strDeadline(self):
        if self.deadline != None:
            return self.deadline.strftime("%A %d %B")

    #Retourne la chaine de caractere de sauvegarde de la tache
    def strSave(self):
        ch = self.name + "\\"
        ch += self.deadline.isoformat() + "\\"
        ch += str(self.priorite) + "\\"
        ch += self.description + "\\"
        return ch


#Retourne la Tache correspondant à la chaine de caractere de sauvegarde
def fromSaveToTache(save):
    save = save.split("\\")
    name = save[0]
    t = Tache(name)
    t.setDeadline(dt.date.fromisoformat(save[1]))
    t.setPriorite(int(save[2]))
    t.setDescription(save[3])
    return t
