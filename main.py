

#------------------------------------------------------------------------------
#       Imports :
#------------------------------------------------------------------------------

import dates
import tache
import tasklist
import categories
#from help.py import help

#------------------------------------------------------------------------------
#       Config :
#------------------------------------------------------------------------------

# TODO : rassembler les fichiers de sauvegarde, surtout saveID
saveID = "hopeThisGetFixedSoon.txt"
saveFileName = "todo.txt"
saveCategories = "catSave.txt"


# TODO : clean that please
f = open(saveID)
NEWID = int(f.readline())
f.close()

#------------------------------------------------------------------------------
#       Functions
#------------------------------------------------------------------------------

# NOTE: -pt <id> (possibilité de choisir une tache parente)
# create Test de Math -p 8 -d nw -dc test d'algebre et de proba -st 43
def createTask(tasklist, command):

    global NEWID #TODO : clean that

    command = command.split("-")

    id = NEWID + 1 # TODO : Clean that
    NEWID += 1
    task = tache.Tache(id)

    # NOTE: ce qu'il y a après ressemble beaucoup à la fonction modif, peut
    # être moyen de les rassembler en une seule fonction
    task.set_name(command[0])
    command = command[1:]

    for com in command:
        com = com.split(" ",1)

        if com[0] == "d" or com[0] == "date":
            task.set_deadline( dates.dateFromString( com[1] ) )

        if com[0] == "du" or com[0] == "duration":
            d = float(com[1])
            task.set_duration(d)

        if com[0] == "nd" or com[0] == "nextdate":
            if com[1] == "None ":
                task.set_nextDeadline(None)
            else:
                # On enleve l'espace de fin
                task.set_nextDeadline(com[1][:-1])

        if com[0] == "dc" or com[0] == "description":
            task.set_description(command[1])

        if com[0] == "p" or com[0] == "priorite":
            p = int(com[1])
            task.set_priorite(p)

        if com[0] == "st" or com[0] == "subtask":
            com[1] = com[1].split(" ")
            for id in com[1]:
                task.add_subTask(int(id))

    tasklist.addTask(task)

def removeTask(command):
    idTask = int(command)
    tasklist.removeTask(idTask)

def modifTask(tasklist, command):
    command = command.split("-")

    idTask = int(command[0])

    task = tasklist.get_task(idTask)

    # NOTE: ce qu'il y a après ressemble beaucoup à la fonction modif, peut
    # être moyen de les rassembler en une seule fonction
    command = command[1:]

    for com in command:
        com = com.split(" ",1)

        if com[0] == "n" or comm[0] == "name":
            task.set_name(comm[1])

        if com[0] == "d" or com[0] == "date":
            task.set_deadline( dates.dateFromString( com[1] ) )

        if com[0] == "du" or com[0] == "duration":
            d = float(com[1])
            task.set_duration(d)

        if com[0] == "nd" or com[0] == "nextdate":
            if com[1] == "None ":
                task.set_nextDeadline(None)
            else:
                # On enleve l'espace de fin
                task.set_nextDeadline(com[1][:-1])

        if com[0] == "dc" or com[0] == "description":
            task.set_description(command[1])

        if com[0] == "p" or com[0] == "priorite":
            p = int(com[1])
            task.set_priorite(p)

        if com[0] == "st" or com[0] == "subtask":
            com[1] = com[1].split(" ")
            for id in com[1]:
                task.add_subTask(int(id))

def printTask(tasklist, command):
    id = int(command)
    task = tasklist.get_task(id)
    print(task)

def printList(tasklist):
    print(tasklist)

def taskDone(tasklist, command):
    id = int(command)
    needToDelete = (tasklist.get_task(id)).done()
    if needToDelete:
        tasklist.remove(id)

def createCategory(categoriesList, command):
    cat = Category(command)
    categoriesList.append(cat)

def removeCategory(categoriesList, command):
    # peut etre faire une fonction pour trouver la catégorie dans la liste
    name = command
    i = 0
    found = False
    while not found and i < len(categoriesList):
        found = name == categoriesList[i].name
        i += 1
    if found:
        del categoriesList[i - 1]

def linkTaskCategory(command):
    command = command.split(" ")
    idTask = int(command[0])
    # peut etre faire une fonction pour trouver la catégorie dans la liste
    name = command[1]
    i = 0
    found = False
    while not found and i < len(categoriesList):
        found = name == categoriesList[i].name
        i += 1
    categoriesList[i - 1].addTask(idTask)

def unLinkTaskCategory(command):
    command = command.split(" ")
    idTask = int(command[0])
    # peut etre faire une fonction pour trouver la catégorie dans la liste
    name = command[1]
    i = 0
    found = False
    while not found and i < len(categoriesList):
        found = name == categoriesList[i].name
        i += 1
    categoriesList[i - 1].removeTask(idTask)


#------------------------------------------------------------------------------
#       Exectution
#------------------------------------------------------------------------------

#Petit message de bienvenue
print("\n\nLitleTodoList :)\n------------\n\n")

tasklist = tasklist.Tasklist()
tasklist.importFile(saveFileName)

categoriesList = []
categories.importFile(saveCategories, categoriesList)


running = True
while running:
    command = input("> ")

    # command = [ "main command" , "options"]
    command = command.split(" ", 1)

    if command[0] == "exit":
        tasklist.save(saveFileName)

        running = False

    if command[0] == "save":
        tasklist.save(saveFileName)

    if command[0] == "create":
        createTask(tasklist, command[1])

    if command[0] == "rm":
        removeTask(command[1])

    if command[0] == "ch":
        modifTask(command[1])

    if command[0] == "cat-create":
        createCategory(categoriesList, command[1])

    if command[0] == "cat-remove":
        removeCategory(categoriesList, command[1])

    if command[0] == "done":
        taskDone(tasklist, command[1])

    if command[0] == "ls":
        if len(command) > 1:
            printTask(tasklist, command[1])
        printList(tasklist)

    if command[0] == "cat":
        linkTaskCategory(command[1])

    if command[0] == "catrm":
        unLinkTaskCategory(command[1])
