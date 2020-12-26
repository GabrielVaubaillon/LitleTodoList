WEEKDAY = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]
MONTHSNAME = ["janvier","février","mars","avril","mai","juin","juillet",
                "août","septembre","octobre","novembre","décembre"]
MONTHSDAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
NO_MONTH = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]#pour le calendrier perpetuel

#On suppose que toutes les dates sont ultérieures à 1582, ça simplifie pas mal
#de choses


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        #un entier entre 0 et 6, de Lundi à Dimanche
        self.weekday = findweekday(day, month, year)

    # ==
    def __eq__(self, other):
        if not isinstance(other, Date):
            return False
        return self.day == other.day and self.month == other.month and self.year == other.year

    # !=
    def __ne__(self, other):
        return not (self == other)

    # <
    def __lt__(self, other):
        if not isinstance(other, Date):
            return False

        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False

    # <=
    def __le__(self, other):
        return not (self > other)

    # >
    def __gt__(self, other):
        if not isinstance(other, Date):
            return False

        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        else:
            return False

    # >=
    def __ge__(self, other):
        return not (self < other)

    def getWeekDay(self):
        return self.weekday

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def strWeekday(self):
        return WEEKDAY[self.weekday]

    def strMonth(self):
        return MONTHSNAME[self.month - 1]

    def __str__(self):
        ch = self.strWeekday() +" "+ str(self.day) + " " + self.strMonth()
        if TODAY.year != self.year:
            ch += " " + str(self.year)
        return ch

    def strSave(self):
        return str(self.year)+"-"+str(self.month)+"-"+str(self.day)

    def updateWeekDay(self):
        self.weekday = findweekday(self.day, self.month, self.year)

    def isEndOfYear(self):
        return self.month == 12 and self.day == 31

    def isEndOfMonth(self):
        if self.month == 2 and isBissextile(self.year):
            return self.day == 29
        return self.day == MONTHSDAY[self.month - 1]

    def addDay(self):
        if self.isEndOfYear():
            self.day = 1
            self.month = 1
            self.year = self.year + 1
        elif self.isEndOfMonth():
            self.day = 1
            self.month = self.month + 1
        else:
            self.day = self.day + 1

        self.weekday = (self.weekday + 1) % 7

    def addDays(self,n):
        for i in range(n):
            self.addDay()

    def addYear(self):
        self.year = self.year + 1
        self.updateWeekDay()


def dateFromTxt(ch):
    #yyyy-mm-dd
    ch = ch.split("-")
    return Date(int(ch[2]), int(ch[1]), int(ch[0]))


def initToday():
    from datetime import date
    today = date.today()
    return Date(today.day, today.month, today.year)

def isBissextile(annee):
    return (annee%4==0 and annee%100!=0) or annee%400==0

#Les fonctions suivantes permettent de trouver le jour de la semaine
#J'utilise des ressources sur le calendrier perpetuel de M. Moret
def nb_seculaire(annee):
    siecle = annee // 100
    no_seculaire = 3
    for i in range(15, siecle + 1):
        if i % 4 == 0:
            no_seculaire = (no_seculaire - 1) % 7
        else:
            no_seculaire = (no_seculaire - 2) % 7
    return no_seculaire

def nb_annuel(annee):
    an = annee % 100
    return (an + (an // 4) - 5) % 7

def nb_mensuel(annee, mois):
    if isBissextile(annee):
        if mois == 1:
            return 3
        elif mois == 2:
            return 6
    return NO_MONTH[mois - 1]


def findweekday(jour, mois, annee):
    #Note : Cet algorithme ne marche qu'après le 20 decembre 1582 !!!!

    nday = nb_seculaire(annee) + nb_annuel(annee) + nb_mensuel(annee, mois)
    nday += jour % 7

    #-1 car ici on commence le tableau à 0 et pas à 1
    return (nday%7) - 1

TODAY = initToday()
