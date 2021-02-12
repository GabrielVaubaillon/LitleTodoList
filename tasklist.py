import tache

class Tasklist:

    def __init__(self):

        self.list = []

    def get_task(self, taskId):
        # NOTE: faire une fonction trouver id dans list pour idTask ??
        found = False
        i = 0
        while not(found) and i < len(self.list):
            found = taskId == self.list[i].id
            i += 1

        if found:
            # Minus one because id get incremented one time after we found it
            return self.list[i - 1]
        return None

    def addTask(self, task):
        self.list.append(task)

    # Used to remove a task from the list, given it's id
    def removeTask(self, idTask):
        # NOTE: faire une fonction trouver id dans list pour idTask ??
        found = False
        i = 0
        while not(found) and i < len(self.list):
            found = idTask == self.list[i].id
            i += 1

        if found:
            # Minus one because id get incremented one time after we found it
            del self.list[i - 1]

    def save(self, fileName):
        f = open(fileName,"w")
        for task in self.list :
            f.write( task.strSave() )
        f.close()


    def importFile(self, fileName):
        f = open(fileName, "r")
        lines = f.readlines()
        f.close()
        for line in lines:
            self.list.append(tache.taskFromSave(line))

    def print(self):
        for task in self.list:
            task.print()

    def taskDone(self, id):
        # NOTE: faire une fonction trouver id dans list pour idTask ??
        found = False
        i = 0
        while not(found) and i < len(self.list):
            found = idTask == self.list[i].id
            i += 1
        i -= 1

        if found:
            needToDelete = self.list[i].done()
            if needToDelete:
                del self.list[i]

    def __str__(self):
        string = ""
        for task in self.list:
            string += str(task) + "\n"
        return string
