
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

    def strSave(self):
        string = str(self.name) + ";"
        for idTask in self.list:
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

def categoryFromSave(str):
    str = str.split(";")
    name = str[0]
    idtasks = str[1].split(",")
    idtask = [int(id) for id in idTask]
    cat = Category(name)
    for i in idTask:
        cat.addTask(i)
    return cat
