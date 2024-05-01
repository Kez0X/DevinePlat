# DevinePlat ?

Ceci est un projet d'université nommé **DevinePlat** pour devinez à quel plat vous pensez à partir d'un jeu de données.

## Comment lancer le programme ?

Pour lancer le programme placez vous simplement dans le fichier __start.py__ et executez le programme.

## La création du script

La création du script, c'est tout d'abord faites par la création de notre arbre de décision. 
Le code ne contient pas directement d'arbre décisionnel pour autant nous en avons utiliser un. En effet, afin de pouvoir éliminer des solutions au fur et à mesure des questions, il a fallut imaginer un système permettant d'éliminer des solutions en fonctions des réponses aux questions tout en faisant en sorte d'avoir toujours une seule réponse à la fin.

Voici un exemple :

```
                            Q1
                            /\
                           /  \
                          /    \
                         /      \
                        /        \
                       /          \
                      Oui         Non
                      Q2          Q2
                     /  \        /  \
                    /    \      /    \
                   Oui   Non   Oui   Non
                   Q3    Q3    Q3    Q3
                   /\    /\    /\    /\
                  O  N  O  N  O  N  O  N

```

Comme vous pouvez le voir avec cet exemple avec 3 questions, on obtient 8 réponses et on peut étendre ce schéma à plus de questions.

Pour pouvoir simuler cette arborescence au lieu de creer un arbre, j'ai décidé de creer un dictionnaire contenant les réponses avec les réponses à chacunes des questions (si la réponse est postive alors je l'ai mise à True et sinon je l'ai mis à False) :

```py
"Risotto au poisson" : {
        "italien" : True,
        "riz" : True,
        "poisson" : True
    }
```

Comme vous pouvez le voir ici, le risotto au poisson contient 3 réponse vrai donc True. 
Afin de pouvoir poser les questions, j'ai creer un autre dictionnaire :

```py
questions = {
    "italien" : "Votre plat est il italien ?",
    "riz" : "Votre choix comporte t-il du riz ?",
    "poisson" : "Y a t-il du poisson dans votre plat ?"
}
```

Cela me permet de poser les questions dans l'ordre dans lequel elles viennent et de procéder par élimination.
Pour chacunes des réponses aux questions je vais éliminer toutes les plats du dictionnaires qui ne correspondent pas et au fur et à mesure le nombre des plats va réduire jusqu'à ce qu'il n'en reste qu'un. 

Par exemple :

```
>>> Votre plat est il italien ? Non
```

À cette première question comme nous répondons non, nous éliminons la moitié des possibilités. Nous passons de 8 possibilités à 4

```
>>> Votre choix comporte t-il du riz ? Oui
```

Ici, nous éliminons aussi la moitié des réponses restantes. Nous passons de 4 possibilités à 2.

```
>>> Y a t-il du poisson dans votre plat ? Non
```

Et là nous éliminons la dernière possibilités et il ne nous en reste plus qu'une.

Bien entendu, le schéma ici peut être considéré comme petit cependant en l'étendant à une zone plus grande on peut considérer ce système comme étant un arbre binaire décisionnel.

**P.S** Pour éviter de modifier le dictionnaire en cours de route nous en faisons une copie au début du programme.

```py
dicoPlat = categories.copy()
```

Nous procédons par élimination...

## Le fichier requirements.txt

Ce fichier contient tous les outils de bibliothèques nécessaires à l'utilisation du programme.
