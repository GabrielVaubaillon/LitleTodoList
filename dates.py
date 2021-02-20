
#On suppose que toutes les dates sont ultérieures à 1582, ça simplifie pas mal
#de choses

#------------------------------------------------------------------------------
#       Variables Globales
#------------------------------------------------------------------------------

WEEKDAY = ["lundi","mardi","mercredi","jeudi","vendredi","samedi","dimanche"]

MONTHSNAME = ["janvier","février","mars","avril","mai","juin","juillet",
                "août","septembre","octobre","novembre","décembre"]

MONTHSDAY = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Tableau pour le calendrier perpetuel, le calcul du jour de la semaine
NO_MONTH = [4, 0, 0, 3, 5, 1, 3, 6, 2, 4, 0, 2]

#Note : TODAY est initialisé lors du chargement de ce fichier,
# à la fin de celui-ci
TODAY = None

#------------------------------------------------------------------------------
#       Classe Date
#------------------------------------------------------------------------------
class Date:
    # Constructeur :
    #---------------
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        #un entier entre 0 et 6, de Lundi à Dimanche
        self.weekday = findweekday(day, month, year)

    # Comparaisons :
    #---------------

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

    # get Attributs :
    #----------------
    def getWeekDay(self):
        return self.weekday

    def getDay(self):
        return self.day

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    # Formats :
    #---------------
    def strWeekday(self):
        return WEEKDAY[self.weekday]

    def strMonth(self):
        return MONTHSNAME[self.month - 1]

    def __str__(self):
        ch = self.strWeekday() +" "+ str(self.day) + " " + self.strMonth()
        #Si l'année de la date est l'année en cours, on n'affiche pas l'année
        if TODAY.year != self.year:
            ch += " " + str(self.year)
        return ch

    #Sauvegarde de l'Objet dans une chaine de caractere yyyy-mm-dd
    def strSave(self):
        return str(self.year)+"-"+str(self.month)+"-"+str(self.day)

    # Booleens, date.is* :
    #---------------------
    def isEndOfYear(self):
        return self.month == 12 and self.day == 31

    def isEndOfMonth(self):
        if self.month == 2 and isBissextile(self.year):
            return self.day == 29
        return self.day == MONTHSDAY[self.month - 1]

    # Modifications :
    #----------------
    def updateWeekDay(self):
        self.weekday = findweekday(self.day, self.month, self.year)

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
#END Class Date


#------------------------------------------------------------------------------
#       From String to Date
#------------------------------------------------------------------------------

#Retourne une date, correspondant à la chaine de caracteres donnée
#param :  ch, string, chaine de caracteres, date au format "yyyy-mm-dd"
#return : Date
def dateFromTxt(ch):
    ch = ch.split("-")
    return Date(int(ch[2]), int(ch[1]), int(ch[0]))

#Retourne une date, correspondant à la chaine de caracteres donnée
#Fonctionne avec plus de formats que la fonction dateFromTxt()
#param :  strdate, string, chaine de caracteres, la date
#return : Date ou None si le format n'est pas connu
def dateFromString(strdate):
    date = Date(TODAY.getDay(), TODAY.getMonth(), TODAY.getYear())

    #Formats implicites (demain, semaine prochaine, etc.)
    if strdate in ["t","today"]:
        pass

    elif strdate in ["tm","tomorow","nd","nday","nextday"]:
        date.addDays(1)

    elif strdate in ["w","nw","nweek","nextweek"]:
        date.addDays(7)

    elif strdate in ["tw","tweek", "twoweek"]:
        date.addDays(14)

    elif strdate in ["nm","nmonth","nextmonth"]:
        date.addDays(30)

    elif strdate in ["tmonth", "twomonth"]:
        date.addDays(60)

    elif strdate in ["ny","nyear","nextyear"]:
        date.addYear()

    #Formats explicites : (yyyy-mm-dd, dd-mm, dd-mm-yyyy)
    elif ("/" in strdate):
        param = strdate.split("/")

        #dd-mm
        if len(param) == 2:
            date = Date(int(param[0]), int(param[1]),TODAY.getYear() )
            if date < TODAY:
                date.addYear()

        #yyyy-mm-dd
        elif len(param) == 3 and len(param[0] > 2):
            date = Date(int(param[2]), int(param[1]), int(param[0]))
        #dd-mm-yyyy
        elif len(param) == 3:
            date = Date(int(param[0]), int(param[1]), int(param[2]))

    #La date n'est pas exprimée dans un fromat connu
    else:
        return None

    return date

#------------------------------------------------------------------------------
#       Fonctions
#------------------------------------------------------------------------------


#Initialise la variable globale TODAY
#Note : appellé au chargement du fichier
#Note : Necessite l'utilisation du module datetime
def initToday():
    from datetime import date
    today = date.today()
    return Date(today.day, today.month, today.year)

#Retourne si une année est bissextile ou non :
def isBissextile(annee):
    return (annee%4==0 and annee%100!=0) or annee%400==0


#------------------------------------------------------------------------------
#       Calendrier Perpetuel, calcul du jour de la semaine
#------------------------------------------------------------------------------
#Note : J'utilise des ressources sur le calendrier perpetuel de M. Moret


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

#Retourne une entier entre 0 et 6 représentant le jour de la semaine,
#0 pour lundi, 6 pour dimanche
def findweekday(jour, mois, annee):
    #Note : Cet algorithme ne marche qu'après 1582

    nday = nb_seculaire(annee) + nb_annuel(annee) + nb_mensuel(annee, mois)
    nday += jour % 7

    return (nday%7) - 1

#------------------------------------------------------------------------------
#       Execution
#------------------------------------------------------------------------------

#Calcul de la variable globale TODAY
TODAY = initToday()
