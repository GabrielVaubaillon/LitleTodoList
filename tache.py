import dates

class Tache:

    # Constructeur :
    #---------------
    def __init__(self, name, id, deadline=None, description = " ",
                    priorite=5):
        self.id = id
        self.name = name
        self.deadline = deadline
        self.description = description
        self.priorite = priorite

    # set Attributs :
    #---------------
    def setName(self, name):
        self.name = name

    def setDeadline(self, deadline):
        self.deadline = deadline

    def setDescription(self, description):
        self.description = description

    def setPriorite(self, priorite):
        self.priorite = priorite

    # get Attributs :
    #-----------
    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getDate(self):
        return self.deadline

    # Formats :
    #---------------
    def strDeadline(self):
        if self.deadline != None:
            return str(self.deadline)

    #Retourne la chaine de caractere de sauvegarde de la tache
    def strSave(self):
        ch = self.name + "\\"
        if self.deadline != None:
            ch += self.deadline.strSave() + "\\"
        else:
            ch+= "None" + "\\"
        ch += str(self.priorite) + "\\"
        ch += self.description + "\\"
        return ch
#END class Tache

#Retourne la Tache correspondant à la chaine de caractere de sauvegarde
def fromSaveToTache(save, id):
    save = save.split("\\")
    name = save[0]
    t = Tache(name, int(id))
    
    if save[1] != "None":
        t.setDeadline(dates.dateFromTxt(save[1]))
    t.setPriorite(int(save[2]))
    t.setDescription(save[3])
    return t
