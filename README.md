# LitleTodoList
Petite gestion en ligne de commandes de ma todo list. Deadlines, taches recurentes, priorités et catégories

## Actual README

### Commandes
 - list : (list) : liste l'ensemble des taches
 - add : (add [name] [deadline]) : ajoute/créé une nouvelle tache
 - remove : (remove [id]) : retire la tache correspondant à l'id
 - save : (save) : Met à jour le fichier de sauvegarde (peut etre faire ça après chaque modif, à réfléchir)


## Notes de développement

**deadline :  20-decembre (2020)**

### TODO next time
 - tri des taches dans dates croissantes
 - Dates sans l'année en param de add
 - gestion de add intelligente (pas besoin de tout préciser à chaque fois)
 - ajout de l'attribut priorité

### Idées pour le programme todo list
 - interface style console "todo add title=Exercice 3 priority=High cat=Signaux date=18-11"
 - ajouter des taches
 - categories (Polytech/Hobby/Famille/Santé...)
 - priorités (Hyper Important)
 - taches interompues car manque qqchose, en dehors de mon scope
	(a afficher qd meme pour pouvoir les reprendre des que possible)
 - recherche par date
 - prevision de faire telle tache tel jour
 - rappel des taches à faire ce jour au demarrage du systeme
 - couleurs si possible
 - afficher un calendrier lorsque l'on choisi la date
 - taches meres/filles/dependantes/diviser en plus petites taches
 - possibilité de faire des taches recurrentes
 - attribuer une durée prévue pour les taches
 - fonction donne une tache random par rapport à la durée donnée, dans une certaine
    catégorie, avec plus de chance de tomber sur les taches haute priorité
 - ~~Ce serait cool en C ou en shell, mais python marchera tout aussi bien je pense~~ On va partir sur du python, possibilité de refaire ça autrement une autre fois
 - recherche par mot clef?? si je finis en avance, peut etre ...
 - archive des taches effectuées

 - Fichier avec header contenant toutes les infos importantes
    Premiere ligne nom/description en une phrase/attributs
    reste, description précise/avancée

### En cours/Prévision/Ordre

 - faire fonctionner avec juste les fonctionnalités de bases (nom/description/deadline/ajout/suppression)
 - ajout des fonctionnalités dans cet ordre :
    - affichage par dates
    - priorités
    - catégories
    - date prévue d'execution
    - standbye
    - recurrente
    - durée prévue
    - hierarchie des taches (division/dependantes)
    - random tache
    - archive
    - recherche par mot clef??

### Idées d'amélioration
