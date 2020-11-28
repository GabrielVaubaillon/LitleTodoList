
class Tache:

    # Constructeurs :
    #---------------

    #Constructeur complet
    def __init__(self, name, deadline, description):
        self.name = name
        self.deadline = deadline
        self.description = description

    #Constructeur à partir de la chaine de caractere de sauvegarde :
    def __init__(self, save):
        #TODO
        pass

    # Méthodes :
    #-----------
    def getName(self):
        return self.name

    def strSave(self):
        #TODO
        pass
