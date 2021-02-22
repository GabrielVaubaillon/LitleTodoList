
class Category:

    def __init__(self, name):

        self.name = name

        self.tasks = []

    def addTask(self, id):
        # NOTE : vérifier que l'on a pas déjà la tache dans la catégorie
        self.tasks.append(id)

    def removeTask(self, idTask):
        # NOTE: faire une fonction trouver id dans list pour idTask ??
        found = False
        i = 0
        while not(found) and i < len(self.tasks):
            found = idTask == self.tasks[i]
            i += 1

        if found:
            # Minus one because id get incremented one time after we found it
            del self.tasks[i - 1]

    def __str__(self):
        string = self.name + " : "
        string += str(self.tasks)
        return string

    def strSave(self):
        string = str(self.name) + ";"
        for idTask in self.tasks:
            string += str(idTask) + ","
        string += "\n"
        return string


def importFile(fileName, categoriesList):
    f = open(fileName, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        categoriesList.append(categoryFromSave(line))

def save(fileName, categoriesList):
    f = open(fileName, "w")
    for category in categoriesList:
        f.write(category.strSave())
    f.close()

def categoryFromSave(string):
    string = string.split(";")
    name = string[0]
    cat = Category(name)
    if len(string[1]) > 1:
        idtasks = string[1].split(",")
        idtasks = idtasks[:-1] # on retire le \n
        idtasks = [int(id) for id in idtasks]
        for i in idtasks:
            cat.addTask(i)
    return cat
