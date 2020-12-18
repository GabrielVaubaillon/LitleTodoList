# LitleTodoList
Petite gestion en ligne de commandes de ma todo list. Deadlines, taches recurentes, priorités et catégories

### Commandes
 - list : (list) : liste l'ensemble des taches
 - add : (add [name] [parametres]) : ajoute/créé une nouvelle tache
    - parametres : [cmd]=[value] ; les parametres non précisés recevrons une valeur par défaut  
    cmd:
        - d or date : d=2020-12-24 : donne la deadline de la tache
        - dc or description : dc=Penser_à_faire_ça_comme_ceci : une courte description pour mieux comprendre la tache
        - p or priorite : p=[entier] : 5 par défaut, les plus importantes à 10, les moins importantes à 0
 - modif : (modif [id] [parametres]) : permet de modifier les caracteristiques de la ID, voir les parametres de la commande add  
    - parametre supplémentaire par rapport à add :
        - name : permet de changer le nom
 - remove : (remove [id]) : retire la tache correspondant à l'id
 - save : (save) : Met à jour le fichier de sauvegarde (peut etre faire ça après chaque modif, à réfléchir)
