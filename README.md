# Minitrice

Ce projet consiste à créer un programme qui permet de faire les 4 opérations arithmétiques (`+`, `-`, `*` et `/`) entre deux nombres. 

## Introduction

Ce projet qui sert de support pour l'évaluation du module gestionnaire de version est un travail de groupe.

La liste des groupes:
 - Groupe 1
   - Dewen Bidois
   - Beriche Chahalane
   - Olivier Grondin
   - Lenaic Honorine
 - Groupe 2
   - Camille Javel
   - Julien Lenormand
   - Luc Maillet
   - Nicolas Maillot
 - Groupe 3
   - Pauline Moncoiffe-Brisset
   - Miguel Pourny
   - Aina Rakotonaivo
   - Dimitri Ratane
 - Groupe 4
   - Nandraina Razafindraibe
   - Alexandre Tam-Hui
   - Mathilde Vingadessin
   - Lucas Xitra

**L'objectif** : le groupe démontrera son abilité à manipuler des branches git et à réaliser des Pull Resquest. Ce travail est collectif, le nombre de commits par personne devrait être sensiblement le même.

## Le fond

Le programme a été sera utilisable à travers un terminal. Vous utiliserez votre langage de programmation favori.

Le programme prend en entrée une chaine de caractère qui contient 2 nombres séparés par une des opérations `+`, `-`, `*` ou `/`. Après la validation d'une ligne, en appuyant sur la touche `Entrée`, votre programme affiche le résultat du calcul indiqué par la chaîne de caractère.

L'exécutable représentant le programme, sera désigne par `main` dans la suite de ce document. Il doit être utilisable de façon intéraction ou en lisant l'entrée standard, `STDIN`.

### Utilisation intéractive 

Un exemple d'utilisation :
```
1. $ ./main
2. > 3+9
3. 12
4. > ^D
```

A la ligne `1`, le programme `main` est appelé. Noterez l'utilisation d'un `$` en début de ligne pour indiquer l'utilisation du prompt du terminal.  
A la ligne `2`, le calcul `3+9` est demande au programme. Noterez l'utilisation d'un `>` en début de ligne pour indiquer l'utilisation du prompt du programme `main`.  
A la ligne `3`, le programme affiche le résultat du calcul.  
A la ligne `4`, on sort du programme `main` grâce à la combinaison de touche `Ctrl + D` qui envoie [le signal](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) `End-Of-File` au programme.  

### Utilisation par STDIN 

Un exemple d'utilisation :
```
1. $ echo "3+9" | ./main
2. 12
4. $
```


Lorsque vous appelez votre programme
utilisable de façon intéractive
utilisable avec stdin (`pipe`)


## La forme

Les nombres que ce programme doit supporter sont des nombres de tailles raisonnable : pas d'overflow ou d'erreur de calcul dû la taille des nombres manipulée. 

# Le barème

# Le rendu


# Astuce

Pour les utilisateurs de Windows, je vous recommande d'installer WSL pour avoir accès à un terminal similaire à un terminal Unix.

