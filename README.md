# LitleTodoList

Petite gestion en ligne de commandes de ma todo list. Deadlines, taches recurentes, priorités et catégories

## Commandes

| Commande | Syntaxe | Description |
|----|----|----|
| exit | `exit` | Ferme le programme ( Warning : pas de sauvegarde auto) |
| save | `save` | Sauvegarde l'état de la todolist dans les fichiers |
| create | `create [Name] [OPTIONS]` | Créer une nouvelle tache avec le nom *Name*. Voir section *Create / Change* pour les options |
| ls | `ls <id>` | Liste la tache id, si id non précisé : toutes les taches |
| done | `done <id>` | Marque la tache id comme faite |
| remove / rm | `rm <id>` | supprimme la tache id |
| change / ch | `ch <id> [OPTIONS]` | Permet de modifier la tache id. Voir section *Create / Change* pour les options|
| cat | `cat <idTask> <CategoryName>` | Met la tache *idTask* dans la catégorie *CategoryName* |
| catrm | `cat <idTask> <CategoryName>` | Retire la tache *idTask* de la catégorie *CategoryName* |
| cat-create | `cat-create [Name]` | Crée une catégorie avec le nom *Name* |
| cat-ls | `cat-ls` | Liste toute les catégories |
| cat-remove | `cat-remove <CategoryName>` | supprime la catégorie CategoryName |

## Détails

### Create / Change

create/change [Name/id] [OPTIONS]
Aucune option n'est obligatoire, tous les attributs ont une valeur par défaut  
OPTIONS : `-[commande] [valeur]`

Les otpions de create et change permette d'agir sur une tache :

| commande | abréviation | valeur | défaut |
|-:|-:|:-|-:|
| name | n | Le nom de la tache (Que dans la fonction change) |  |
| date | d | la deadline (voir section Dates) | None (pas de deadline) |
| duration | du | Le temps (en heures) estimé nécessaire pour la tache | 0.0 |
| nextdate | nd | pour les taches récurrentes, format implicite pour calculer la prochaine date (voir section Dates). Pour une tache perpetuelle sans deadline mettre : `perpetual`| None |
| description | dc | Une description de la tache | Vide |
| priorite | p | La priorité d'une tache est entre 0 et 10 ; 10 très important et 0 pas du tout important | 5 |
| subtasks | st | `-st id0 id1 id2`  Les sous taches qu'il faudra compléter avant de pouvoir completer celle ci | Vide |

**Exemples**
```
> create Revision Math -d 20/04 -duration 2 -dc Chapitre 3 et 4 -p 8
> create Revise Math Ch4
> create evise Math Ch3
> ch 3 -name Revise Math Ch3
> ch 1 -subtask 2 3
```

### Dates

Les dates peuvent être définies de façon implicite ou explicite

Explicite :
- yyyy/mm/dd
- dd/mm/yyyy
- dd/mm (le suivant (si aujourd'hui = 15-03-2020, alors 03-03 => 03-03-2021))

Implicite :

| pour quand | formats |
|-|-|
| Aujourd'hui | t , today |
| Demain | tm , tomorow , nd , nday , nextday |
| Semaine prochaine | w , nw , nweek , nextweek |
| Dans deux semaines | tw , tweek , twoweek |
| Le mois prochain | nm , nmonth , nextmonth |
| Dans deux mois | tmonth , twomonth |
| L'année prochaine | ny , nyear , nextyear |

## Idées de trucs à rajouter

### bugs / soucis
- sauvegarde dans un seul fichier
- éviter les crash
- sauvegarde auto
- sauvegarde dans un seul fichier

### fonctionnalités
- cat-ls <Name> pour afficher une seule catégorie, aveec toute ses taches ??
- help <commande> , afficher l'aide de la commande correspondante, ou l'aide générale si il n'y a pas de commande précisé + à afficher si ça crash
- possibilité de lister les taches avec des filtres
- mettre une tache en standby
- choisir d'une date d'execution de la tache (avant la deadline)
- abandon d'une tache
- archive des taches (taches faites, taches abandonnées)
