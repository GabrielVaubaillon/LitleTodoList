# LitleTodoList
Petite gestion en ligne de commandes de ma todo list. Deadlines, taches recurentes, priorités et catégories

### Commandes
- list (or ls): liste les taches
  - ls date : taches triées par date croissantes
- add : (add [name] [parametres]) : ajoute/créé une nouvelle tache
  - parametres : [cmd]=[value] ; les parametres non précisés recevrons une valeur par défaut  
cmd:
   - d or date : d=2020-12-24 : donne la deadline de la tache
   - dc or description : dc=Penser_à_faire_ça_comme_ceci : une courte description pour mieux comprendre la tache
   - p or priorite : p=[entier] : 5 par défaut, les plus importantes à 10, les moins importantes à 0
- modif : (modif [id] [parametres]) : permet de modifier les caracteristiques de la ID, voir les parametres de la commande add
  - parametre supplémentaire par rapport à add :
   - name : permet de changer le nom
- remove (or rm): (remove *[id]) : retire les tache correspondant à l'id
- save : (save) : Met à jour le fichier de sauvegarde (peut etre faire ça après chaque modif, à réfléchir)
- exit (or q, or quit) : Sort du programme en sauvegardant les taches

#### Formats dates

**Formats explicites**
- yyyy-mm-dd
- dd-mm-yyyy
- dd-mm (le suivant (si aujourd'hui = 15-03-2020, alors 03-03 => 03-03-2021 ))

**Formats implicites**
- Aujourd'hui : t , today
- Demain : tm, tomorow, nd, nday, nextday
- Semaine prochaine : w, nw, nweek, nextweek
- Dans deux semaines : tw, tweek, twoweek
- Le mois prochain : nm, nmonth, nextmonth
- Dans deux mois : tmonth, twomonth
- L'année prochaine : ny, nyear, nextyear


### Exemples

today = 30-12-2020
```
> ls
> add DM_math date=15-01 priorite=8 dc=exercices_moodle
> add DM_Physique d=tm p=8
> ls
- 0 : DM_math    vendredi 15 janvier 2021
- 1 : DM_Physique    samedi 31 decembre
> modif 1 name=DM_PysiqueChimie
> ls date
- 1 : DM_PhysiqueChimie    samedi 31 decembre
- 0 : DM_math    vendredi 15 janvier 2021
> rm 0
Effectuer la suppression de DM_math ? [O/n] :  o
> ls
- 1 : DM_PhysiqueChimie    samedi 31 decembre
> exit
```
