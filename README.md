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

### Scénario 1 : Utilisation intéractive

Un exemple d'utilisation :
```
1. $ ./main
2. > 3+9
3. 12
4. > 
5. Fin des calculs :)
6. $ echo $?
7. 0
8. $ 
```

A la ligne `1`, le programme `main` est appelé. Noterez l'utilisation d'un `$` en début de ligne pour indiquer l'utilisation du prompt du terminal.  
A la ligne `2`, le calcul `3+9` est demande au programme. Noterez l'utilisation d'un `>` en début de ligne pour indiquer l'utilisation du prompt du programme `main`.  
A la ligne `3`, le programme affiche le résultat du calcul.  
A la ligne `4`, on sort du programme `main` grâce à la combinaison de touche `Ctrl + D` qui envoie [le signal](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) `End-Of-File` au programme.  
A la ligne `5`, le programme afficher un message de sorti `Fin des calculs :)`.  
A la ligne `6`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `main`.  
A la ligne `7`, on voit le code de sortie `0`.  
A la ligne `8`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. Vous noterez que malgré le fait qu'un signal soit utiliser pour sortir du programme, le code de sortie retourné est `0`, ce qui indique que le programme s'est exécuté normalement.

**Remarque :** Toutes les écritures du programme `main` se font sur la sortie standard `STDOUT`.

### Utilisation en lisant STDIN

Dans le but d'automatiser l'utilisation du programme `main`, il doit pouvoir lire sur l'entrée standard `STDIN`.

Il y a généralement 2 utilitaires pour envoyer des données à travers un pipe : `echo` et `cat`.

#### Scénario 2 : STDIN : utilisation de echo

Un exemple d'utilisation :
```
1. $ echo "3+12" | ./main
2. 15
3. $ echo $?
4. 0
5. $ 
```

A la ligne `1`, on envoie la chaine de caractère "3+12" dans le programme `main` à l'aide d'un pipe.
A la ligne `2`, le programme main écrit son résultat.  
A la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `main`.  
A la ligne `4`, on voit le code de sortie `0`.  
A la ligne `5`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. On peut noter qu'il est plus court que le scénario interactif et qu'il n'y a pas de message à la sortie du programme.

#### Scénario 3 : STDIN : utilisation de cat

Dans ce dépôt, vous trouverez le fichier `good-expression.txt` qui contient 10 expressions calculables avec les 4 opérations à gérer. En utilisant ce fichier:
```
 1. $ cat good-expression.txt | ./main
 2. 4
 3. 11
 4. 35
 5. -4
 6. 12
 8. 90
 9. 4.0
10. 8.0
11. 10
12. 4
13. $ echo $?
14. 0
15. $ 
```
A la ligne `1`, on envoie le contenu du fichier `good-expression.txt` dans le programme  `main` à l'aide d'un pipe.
De la ligne `2` à `12`, le programme `main` écrit le résultat des calculs sur la sortie standard `STDOUT`.  
A la ligne `13`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `main`.  
A la ligne `14`, on voit le code de sortie `0`.  
A la ligne `15`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. On peut noter qu'avec la capacité de lecture sur le pipe, il possible au programme `main` de traiter un grand nombre de données.

### Gestion d'erreurs

La gestion d'erreur fait partie intégrante du travail du développeur. Si les cas limites ne sont pas traités, le programme est généralement utilisable. La gestion des erreurs est identique que le programme `main` soit utilisé en mode intéraction ou en mode lecture depuis `STDIN`.

#### Erreur de syntaxe

Si la ligne de calcul comporte une erreur de syntaxe, voici le comportement du programme `main` :
```
1. $ echo "3+*12" | ./main
2. Erreur de syntaxe pour le calcul: "3+*12"
3. $ echo $?
4. 1
5. $ 
```

A la ligne `1`, on envoie la chaine de caractère "3+*12" dans le programme `main` à l'aide d'un pipe.
A la ligne `2`, le programme main écrit son message d'erreur en rappelant le calcul concerné.  
A la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `main`.  
A la ligne `4`, on voit le code de sortie `1`.  
A la ligne `5`, on est de retour dans le terminal.  

On peut noter que le message d'erreur rappelle la ligne de calcul qui a provoqué l'erreur. On peut aussi voir que le code de sortie est différent de 0, ce qui indique que le programme ne s'est pas exécuté correctement.

#### Division par zéro

La division par zéro est un grand classique des erreurs à traiter dans le cadre de calcul. Voici le comporte du programme `main` dans ce cas de figure :
```
1. $ echo "3/0" | ./main
2. Division par zéro
3. $ echo $?
4. 1
5. $ 
```

A la ligne `1`, on envoie la chaine de caractère "3/0" dans le programme `main` à l'aide d'un pipe.
A la ligne `2`, le programme main écrit son message d'erreur.  
A la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `main`.  
A la ligne `4`, on voit le code de sortie `1`.  
A la ligne `5`, on est de retour dans le terminal.  

On peut noter que le message d'erreur ne donne pas d'information sur le calcul qui a provoquer ce message (ce qui est moins pratique pour débugguer). On peut aussi voir que le code de sortie est différent de 0, ce qui indique que le programme ne s'est pas exécuté correctement.

## La forme

Les nombres que ce programme doit supporter sont des nombres de tailles raisonnable : pas d'overflow ou d'erreur de calcul dû la taille des nombres manipulée. Donc pas de piège ici.

Les espaces à gauche et à droite d'une ligne de calcul ne génére pas d'erreurs.

Les nombres avec une partie décimal importante seront arondi à 2 chiffres après la virgule.

## Le rendu

Vous devez faire un dépôt git public, avec un nom sous le format `git-evaluation_groupe-<numéro>` en fonction de votre numéro de groupe. Par exemple pour le groupe 3, le nom du dépôt est `git-evaluation_groupe-3`.

Vous devez rédiger un README.md qui contiendra :
 - les instructions pour pouvoir lancer votre programme : potentiellement, l'installation de dépendences, compilateur ou autre dans une section du README,
 - le lien youtube de votre vidéo gource associé à l'activité sur votre dépôt (plus de renseignements dans la section suivante).

Votre dépôt contiendra également les résultats du programme `main` sur les fichiers `good-expression.txt`, `bad-expression.txt` et `mixed-expression.txt`. Les noms de fichiers contenant les résultats correspondront au nom de fichier d'origine suffixé par `-result`, par exemple `bad-expression-result.txt`

## Gource

Pour installer `gource` sous linux, vous pouvez simplement utiliser la commande suivante :
```
sudo apt install gource
```

Vous aurez aussi besoin de l'utilitaire `ffmpeg` pour convertir le fichier généré par gource.

Pour apprendre à utiliser gource, je vous recommande cette [article](). Très récemment, j'ai personnellement utilisé cette commande pour créer une vidéo à l'aide de gource :
```
gource -s 2 -r 60 --file-font-size 8 --title git-evaluation --filename-time 2 --stop-at-end --hide date,usernames -o video1.ppm && \
  ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i video1.ppm -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 video2.mp4
```

A la suite de cette commande que vous devriez exécuter depuis la racine de votre dépôt, vous devriez obtenir les fichiers `video1.ppm` et `video2.mp4`. C'est le fichier `video2.mp4` que vous devez publié sur youtube.

Assurer que votre vidéo est accessible par n'importe qui et non uniquement par vous-même.

## Le barème

 - Exécution correcte de votre programme sur les scénarios dans ce document.
 - Exécution correcte de votre programme les fichiers de tests fournis.
 - Exécution correcte de votre programme sur un grand fichier (environ 10000 lignes) qui n'est pas fournis.
 - Un historique git propre
 - Une bonne utilisation des Pull Request sur github avec des descriptions explite du contenu de la Pull Request
 - Respect de l'ensemble des consignes sur les travaux réalisés.
 - Publication du vidéo de votre activité sur ce dépôt à l'aide de la commande [gource](https://gource.io/)


## Astuces

### Windowsien

Pour les utilisateurs de Windows, je vous recommande d'installer WSL pour avoir accès à un terminal similaire à un terminal Unix.

### Langage de programmation

Bien que je vous laisse le choix du langage de programmation, je vous recommande vivement d'utiliser python. Python vous permettra de lire l'entrée avec la function `input()`, d'évaluer une ligne de calcul la function `eval` et de gérer les erreurs avec un bloc `try/except`. Vous pouvez aussi savoir facilement si le pipe est utilisé ou pas avec un programme python grâce à [ce lien](https://stackoverflow.com/questions/33871836/find-out-if-there-is-input-from-a-pipe-or-not-in-python).
