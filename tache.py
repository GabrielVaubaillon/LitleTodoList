import dates

class Tache:

    # Constructeur :
    #---------------
    def __init__(self, id):
        # This is what identifies the task, it must be unique:
        self.id = id

        # Default Values :
        # Attributs explained with their respective "set" method below
        self.name = ""

        self.deadline = None
        self.duration = 0
        self.nextDeadline = None
        # Note : maybe add smthing like self.nbRepetition

        self.description = ""
        self.priorite = 5

        self.subTasks = []

    # set Attributs :
    #----------------

    # The Name is what the user will see the most, it summarize what the task
    # is about. It shall be rather short and descriptive
    # type : String
    def set_name(self, name):
        self.name = name

    # The deadline is the date at which the task MUST be done
    # I use my own format for dates, further help can be found in the dates.py files
    # type : Date (from dates.py) or None
    def set_deadline(self, date):
        # TODO :The date shall not be after the deadline of a Higher task (see ParentTask)
        self.date = date

    # The duration represent the time the user think will be needed to
    # perform the task in hours.
    # type : float
    def set_duration(self, time):
        self.duration = time

    # This attribute is usefull for recurring task only. It allows to set a new
    # deadline once the task is done, so it can repeat itself. If the task isn't
    # a reccurent task, it's value is set to None. If the task is a perpetual
    # task without deadline, its value is set to "perpetual"
    # expr is one of the expressions decodable by dates.dateFromString()
    # type : string or None
    def set_nextDeadline(self, expr):
        self.nextDeadline = expr

    # La description permet de détailler un peu plus ce qu'il faut faire pour
    # completer la tache.
    # type : string
    def set_description(self, description):
        self.description = description

    # The task priority allows us to sort task, and promote those who really
    # need to be put first
    # We code the priority between 0 and 10, with 5 neutral, 10 extra important
    # and 0 not important at all
    # type : int (between 0 and 10, 5 by default)
    def set_priorite(self, p):
        # NOTE: verify p is between 0 and 10
        self.priorite = p

    # subTask is a list of the id of subtask of the current task. Every subtask
    # must be completed in order to be able to finish the current task. There
    # is no real limits on how much levels and subtask of subtasks you can have
    # But it is forbidden to create loop, there cannot be a parent task in the
    # subTasks

    # Function to add a sub task to the current task
    # It perform a check to avoid subTask/ParentTask loops
    def add_subTask(self, id):
        # NOTE: The deadline of the subTask must be before the deadline of the parent task
        self.subTasks.append(id)

    # Function to remove a sub task from the current task
    def remove_subTask(self, idTask):
        # NOTE: faire une fonction trouver id dans list pour idTask ??
        found = False
        i = 0
        while not(found) and i < len(self.subTasks):
            found = idTask == self.subTasks[i]
            i += 1

        if found:
            # Minus one because id get incremented one time after we found it
            del self.subTasks[i - 1]


    # Methods :
    #----------

    # return False si il faut garder la tache, True si il faut la supprimmer
    # NOTE: Peut etre pas un booleen en sortie ?
    def done(self):
        if self.nextDeadline != None:
            if self.nextDeadline != "perpetual":
                self.deadline = dateFromString(self.nextDeadline)
            return False
        return True

    def __str__(self):
        c = "[" + str(self.id) + "] " + str(self.name) + " ; "
        if self.deadline != None:
            c += str(self.deadline) + " ; "
        c += str(self.subTasks)
        return c

    def strall(self):
        # NOTE: maybe display categories too
        string = "Task :" + self.id + "\n"
        string += "name :" + self.name + "\n"
        string += "deadline :" + self.deadline + "\n"
        string += "duration :" + self.duration + "\n"
        string += "nextDeadline :" + self.nextDeadline + "\n"
        string += "priorite :" + self.priorite + "\n"
        string += "subTasks :" + self.subTasks + "\n"
        string += "description :" + self.description + "\n"
        return string

    def strSave(self):
        string = self.id + ";"
        string += self.name + ";"
        string += self.deadline + ";"
        string += self.duration + ";"
        string += self.nextDeadline + ";"
        string += self.priorite + ";"
        for i in self.subtasks:
            string += str(i) + ","
        string += ";"
        string += self.description + "\n"
        return string


def taskFromSave(string):
    string = string.split(";")
    task = Tache(int(string[0]))

    task.set_name(string[1])
    task.set_deadline(dateFromString(string[2]))
    task.set_duration(float(string[3]))
    task.set_nextDeadline(string[4])
    task.set_priorite(int(string[5]))
    for i in [int(id) for id in string[6].split(",")]:
        task.add_subTask(i)
    task.set_description(str[7][:-1])
    
    return task
