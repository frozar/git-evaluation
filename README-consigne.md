# Minitrice

Ce projet consiste à créer un programme qui permet de réaliser les 4 opérations arithmétiques élémentaires (`+`, `-`, `*` et `/`) entre deux nombres positifs. 

- [Minitrice](#minitrice)
  - [Introduction](#introduction)
  - [Objectifs](#objectifs)
  - [Le fond](#le-fond)
    - [Scénario 1 : Utilisation interactive](#scénario-1--utilisation-interactive)
    - [Utilisation en lisant STDIN](#utilisation-en-lisant-stdin)
      - [Scénario 2 : STDIN : utilisation de `echo`](#scénario-2--stdin--utilisation-de-echo)
      - [Scénario 3 : STDIN : utilisation de `cat`](#scénario-3--stdin--utilisation-de-cat)
    - [Gestion d'erreurs](#gestion-derreurs)
      - [Scénario 4 : Erreur de syntaxe](#scénario-4--erreur-de-syntaxe)
      - [Scénario 5 : Division par zéro](#scénario-5--division-par-zéro)
    - [Générateur d'expression](#générateur-dexpression)
      - [Bonus : gestion d'erreur](#bonus--gestion-derreur)
  - [La forme](#la-forme)
  - [Le rendu](#le-rendu)
  - [Gource](#gource)
  - [Le barème](#le-barème)
  - [Astuces](#astuces)
    - [Windowsien](#windowsien)
    - [Langage de programmation](#langage-de-programmation)
  - [Liens utiles](#liens-utiles)


## Introduction

Ce projet sert de support pour l'évaluation du module gestionnaire de version et doit être réalisé en groupes.

Voici la liste des groupes :

 - Groupe 1 :
   - Adrien Lemettre
   - Thibault Chaumont
   - Yanis Vingadassamy
   - Thomas Comorassamy
 - Groupe 2 :
   - Aya Meziani
   - Teddy Greze
   - Aifeze Simba
 - Groupe 3 :
   - Matthieu Hoarau
   - Fanirininony Andriatombontsoa
   - Rodolphe Prevot

## Objectifs

Le groupe démontrera sa capacité à manipuler des branches git et à réaliser des *Pull Request*. Ce travail est collectif, on attend que chaque membre du groupe contribue de manière égale au dépôt. Aussi, le nombre de commits par personne devrait être sensiblement le même.

## Le fond

Le programme sera utilisable à travers un terminal. Vous utiliserez votre langage de programmation favori.

Le programme prend en entrée une chaîne de caractère qui contient 2 nombres positifs séparés par un caractère représentant l'une des opérations suivantes : `+`, `-`, `*` ou `/`. Après la validation d'une ligne, en appuyant sur la touche `Entrée`, votre programme affiche le résultat du calcul indiqué par la chaîne de caractère.

L'exécutable représentant le programme sera désigne par `minitrice` dans la suite de ce document. Il doit être utilisable de façon interactive ou en lisant l'entrée standard, `STDIN`.

### Scénario 1 : Utilisation interactive

Un exemple d'utilisation :

```bash
1. $ ./minitrice
2. > 3+9
3. 12
4. > 
5. Fin des calculs :)
6. $ echo $?
7. 0
8. $ 
```

- À la ligne `1`, le programme `minitrice` est appelé. Noterez l'utilisation d'un `$` en début de ligne pour indiquer l'utilisation du prompt du terminal.  
- À la ligne `2`, le calcul `3+9` est demande au programme. Noterez l'utilisation d'un `>` en début de ligne pour indiquer l'utilisation du prompt du programme `minitrice`.  
- À la ligne `3`, le programme affiche le résultat du calcul.  
- À la ligne `4`, on sort du programme `minitrice` grâce à la combinaison de touche `Ctrl + D` qui envoie [le signal](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) `End-Of-File` au programme.  
- À la ligne `5`, le programme afficher un message de sorti `Fin des calculs :)`.  
- À la ligne `6`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `minitrice`.  
- À la ligne `7`, on voit le code de sortie `0`.  
- À la ligne `8`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. Vous noterez que malgré le fait qu'un signal soit utilisé pour sortir du programme, le code de sortie retourné est `0`, ce qui indique que le programme s'est exécuté normalement.

**Remarque :** Toutes les écritures du programme `minitrice` se font sur la sortie standard `STDOUT`.

### Utilisation en lisant STDIN

Dans le but d'automatiser l'utilisation du programme `minitrice`, il doit pouvoir lire sur l'entrée standard `STDIN`. Dans [la tradition d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix), tout programme devrait présenter une interface *texte*, l'interface universelle, lui permettant de recevoir ses entrées depuis la sortie d'un autre programme sous forme de chaîne de caractères. Ainsi, le programme peut être composé avec d'autres programmes pour en fabriquer de nouveaux. Pour composer deux programmes, il faut utiliser [un pipe (ou tube)](https://en.wikipedia.org/wiki/Pipeline_(Unix)), représenté par le caractère `|`. Par exemple :

```bash
programme1 | programme2 | programme3
```

`programme3` lit son entrée depuis la sortie de `programme2`, et `programme2` lit son entrée depuis la sortie de `programme1`. On peut dire que `programme1 | programme2 | programme3 ` est un nouveau programme, *composé* à partir de 3 autres programmes.

Il y a généralement 2 utilitaires (programmes) pour envoyer des données à travers un pipe : `echo` et `cat`.

#### Scénario 2 : STDIN : utilisation de `echo`

Un exemple d'utilisation :
```
1. $ echo "3+12" | ./minitrice
2. 15
3. $ echo $?
4. 0
5. $ 
```

- À la ligne `1`, on envoie la chaîne de caractère "3+12" dans le programme `minitrice` à l'aide d'un pipe.
- À la ligne `2`, le programme `minitrice` écrit son résultat.  
- À la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `minitrice`.  
- À la ligne `4`, on voit le code de sortie `0`.  
- À la ligne `5`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. On peut noter qu'il est plus court que le scénario interactif et qu'il n'y a pas de message à la sortie du programme.

#### Scénario 3 : STDIN : utilisation de `cat`

Dans ce dépôt, vous trouverez le fichier `good-expression.txt` qui contient 10 expressions calculables avec les 4 opérations à gérer. En utilisant ce fichier :
```bash
 1. $ cat good-expression.txt | ./minitrice
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
- À la ligne `1`, on envoie le contenu du fichier `good-expression.txt` dans le programme  `minitrice` à l'aide d'un pipe.
De la ligne `2` à `12`, le programme `minitrice` écrit le résultat des calculs sur la sortie standard `STDOUT`.  
- À la ligne `13`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `minitrice`.  
- À la ligne `14`, on voit le code de sortie `0`.  
- À la ligne `15`, on est de retour dans le terminal.  

Ce scénario décrit un exemple d'utilisation du programme à réaliser. On peut noter qu'avec la capacité de lecture sur le pipe, il possible au programme `minitrice` de traiter un grand nombre de données.

### Gestion d'erreurs

La gestion d'erreurs fait partie intégrante du travail du développeur·se. Si les cas limites ne sont pas traités, le programme est généralement inutilisable. La gestion des erreurs est identique que le programme `minitrice` soit utilisé en mode interactif ou en mode lecture depuis `STDIN`.

#### Scénario 4 : Erreur de syntaxe

Si la ligne de calcul comporte une erreur de syntaxe, voici le comportement du programme `minitrice` :

```bash
1. $ echo "3+*12" | ./minitrice
2. Erreur de syntaxe pour le calcul: "3+*12"
3. $ echo $?
4. 1
5. $ 
```

- À la ligne `1`, on envoie la chaîne de caractère "3+*12" dans le programme `minitrice` à l'aide d'un pipe.
- À la ligne `2`, le programme main écrit son message d'erreur en rappelant le calcul concerné.  
- À la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `minitrice`.  
- À la ligne `4`, on voit le code de sortie `1`.  
- À la ligne `5`, on est de retour dans le terminal.  

On peut noter que le message d'erreur rappelle la ligne de calcul qui a provoqué l'erreur. On peut aussi voir que le code de sortie est différent de `0`, ce qui indique que le programme ne s'est pas exécuté correctement.

#### Scénario 5 : Division par zéro

La division par zéro est un grand classique des erreurs à traiter dans le cadre de calcul. Voici le comportement du programme `minitrice` dans ce cas de figure :

```bash
1. $ echo "3/0" | ./minitrice
2. Division par zéro
3. $ echo $?
4. 1
5. $ 
```

- À la ligne `1`, on envoie la chaîne de caractère "3/0" dans le programme `minitrice` à l'aide d'un pipe.
- À la ligne `2`, le programme main écrit son message d'erreur.  
- À la ligne `3`, de retour dans le terminal Unix, on demande le code de sortie suite à l'exécution du program `minitrice`.  
- À la ligne `4`, on voit le code de sortie `1`.  
- À la ligne `5`, on est de retour dans le terminal.  

On peut noter que le message d'erreur ne donne pas d'information sur le calcul qui a provoqué ce message (ce qui est moins pratique pour débugguer). On peut aussi voir que le code de sortie est différent de 0, ce qui indique que le programme ne s'est pas exécuté correctement.

### Générateur d'expression

Le programme `minitrice` ayant la capacité de lire des entrées depuis un pipe, `|`, il est maintenant possible de le relier à la sortie d'un autre programme : `generator`.

Le programme `generator` génére des expressions calculable de façon aléatoire. Deux nombres choisi aléatoirement dans l'interval `[1, 1000]` sont utilisé pour générer les expressions. Le choix de l'opération à réaliser entre ces deux nombres est aussi aléatoire. Ce programme prend un entier comme premier argument qui désigne le nombre d'expression à générer. Exemple d'utilisation :

```bash
1. $ ./generator 2
2. 7-9
3. 84/12
4. $
```

- À la ligne `1`, le programme `generator` est appelé avec l'argument `2`. Noterez l'utilisation d'un `$` en début de ligne pour indiquer l'utilisation du prompt du terminal.  
- À la ligne `2`, on voit que l'expression `7-9` a été générée.  
- À la ligne `3`, on voit que l'expression `84/12` a été générée.  
- À la ligne `4`, on est de retour dans le terminal.  

Le programme `generator` peut se composé avec le programme `minitrice` à l'aide d'un pipe (en imaginant que les mêmes expresions que précédemment soit générées) :

```bash
1. $ ./generator 2 | ./minitrice
2. -2
3. 7.0
4. $
```

#### Bonus : gestion d'erreur

Le programme `generator` est simple, mais cela n'empêche pas le fait qu'il y a des erreurs qui peuvent se produirent. Cette partie représente le bonus de ce sujet. Vous êtes libre de programmer le ou les erreurs que vous choisissez de gérer. Pour chaque erreur implémentée, vous devez la décrire dans le `README.md`. Vous devez aussi décrire les étapes pour provoquer le ou les erreurs.

## La forme

Les nombres que le programme `minitrice` doit supporter sont des nombres positifs de tailles raisonnable : pas d'overflow ou d'erreur de calcul dû la taille des nombres manipulée. Donc pas de piège ici.

Les espaces à gauche et à droite d'une ligne de calcul ne génèrent pas d'erreurs.

Pour l'affichage du résultat de calcul, il doit être arrondi à 2 chiffres après la virgule lorsque sa partie décimale est grande.

## Le rendu

Utilisez ce dépôt, `frozar/git-evaluation`, comme template pour initialiser votre dépôt de travail avec le bouton `Use this template` sur la page d'accueil de ce dépôt.

Vous devez faire un dépôt github public, avec un nom de dépôt de la forme `git-evaluation_groupe-<numéro>` en fonction de votre numéro de groupe. Par exemple pour le groupe 3, le nom du dépôt est `git-evaluation_groupe-3`.

> [!TIP]
> Si vous avez "forké" ce dépôt, `frozar/git-evaluation`, dépuis Github pour créer votre dépôt de travail, vous devriez supprimer le lien de parenté avec le dépôt d'origine pour éviter des désagréments lors de la création de Merge Request.  

Vous devez rédiger un `README.md` qui contiendra les sections suivantes :
 - Installation : Ce qu'il faut faire pour pouvoir lancer votre programme. Si des logiciels tiers (compilateur par exemple) doivent être installé, les procédures d'installation doivent être décrite ici. Il en est de même pour les bibliothèques,  
 - Exécution : Un exemple d'utilisation de votre programme, avec la sortie attendue, comme ce qui fait dans ce document,  
 - Générator : Description de la gestion des erreurs que vous avez mis en place sur le programme `generator`. La ou les procédures pour reproduire le ou les erreurs doivent être renseignées,  
 - Publication : Le lien Youtube de votre vidéo gource associée à l'activité sur votre dépôt (plus de renseignements dans la section suivante),  
 - Liens utiles : Une liste de ressources en ligne qui vous a été utile pour réaliser ce projet. Cette liste doit être sous la même forme que la section [Liens utiles](#liens-utiles) de ce document.  

Les exécutables `minitrice` et `generator` doivent être présents à la racine de votre dépôt. Dans le cas où ces programmes sont générés, à la fin de leur génération, ces programmes doivent être présents à la racine de votre dépôt.

Dans un dossier `results` à la racine de votre dépôt, vous stockerez les résultats de votre programme `minitrice` sur les fichiers contenus dans le dossier `test`. Les noms de fichiers contenant les résultats correspondront au nom de fichier d'origine suffixé par `-result`, par exemple `00-addition-result.txt`.

**Date de rendu du projet** : Vous devez m'envoyer un mail contenant l'adresse URL de votre dépôt public GitHub avant jeudi 26 février 2026, 23h59. Vous perdrez un point par jour de retard.

Mon adresse mail : fabien.rozar@gmail.com

<ins>Remarque :</ins> Je vous encourage vivement de mettre vos collègues en copie du mail de rendu.

## Gource

Pour installer `gource` sous linux, vous pouvez simplement utiliser la commande suivante :

```bash
sudo apt install gource
```

Vous aurez aussi besoin de l'utilitaire [`ffmpeg`](https://ffmpeg.org/) pour convertir le fichier généré par `gource`.
```bash
sudo apt install ffmpeg
```

Pour apprendre à utiliser `gource`, je vous recommande cette [article](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0). Très récemment, j'ai personnellement utilisé cette commande pour créer une vidéo à l'aide de `gource` :

```bash
gource -s 2 -r 60 --file-font-size 8 --title git-evaluation --filename-time 2 --stop-at-end --hide date,usernames -o video1.ppm && \
  ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i video1.ppm -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 video2.mp4
```

A la suite de cette commande, que vous devrez exécuter depuis la racine de votre dépôt, vous devriez obtenir les fichiers `video1.ppm` et `video2.mp4`. C'est le fichier `video2.mp4` que vous devez publier sur YouTube.

Assurez-vous que votre dépôt et votre vidéo sont accessibles par n'importe qui (public) et non uniquement par vous-même.

## Le barème

 - La rédaction du `README.md` conforme à la consigne : 1 points,
 - Respect des noms de programmes et fichiers pour les travaux réalisés : 2 points,
 - Exécution correcte de votre programme sur les fichiers du répertoire `test` :  1 points,
 - Présence du répertoire `results` contenant les différents fichiers de résultat avec le contenu attendu : 1 points,
 - Exécution correcte de votre programme sur les scénarios dans ce document : 1 points,
 - La création du programme `generator` et son exécution correcte : 1 point,
 - Gestion et explication des erreurs gérées par `generator` : 1 point **(bonus)**,
 - Exécution correcte de votre programme sur un grand fichier (environ 10000 lignes) qui n'est pas fournis : 1 point,
 - Chaque message commit doit avoir un sujet court (< 70 caractères) et doit décrire correctement le travail réaliser par le commit. Si votre décription est plus longue, utilisez le corps du message de commit : 2 points,
 - Votre historique de commit doit être similaire à l'historique produit par le [workshop 3](https://github.com/frozar/git-workshop-3/blob/main/img/historique-final.png) : 5 points,
 - Pour chaque progression sur votre projet, l'utilisation des *Pull Request* sur Github avec des descriptions explicites du contenu de la *Pull Request* : 3 points,
 - Publication de la vidéo générée par l'utilitaire [gource](https://gource.io/) correspondante à votre activité sur ce dépôt : 2 points.

## Astuces

### Windowsien

Pour les utilisateur·ices de Windows, je vous recommande d'installer WSL2 pour avoir accès à un terminal similaire à un terminal Unix.

### Langage de programmation

Bien que je vous laisse le choix du langage de programmation, je vous recommande vivement d'utiliser Python. Python vous permettra de lire l'entrée avec la function `input()`, d'évaluer une ligne de calcul la function `eval` et de gérer les erreurs avec un bloc `try/except`. Vous aurez besoin de gérer les exceptions `EOFError`, `SyntaxError` et `ZeroDivisionError`. Vous pouvez aussi facilement savoir si le pipe est utilisé ou pas avec un programme python grâce à [ce lien](https://stackoverflow.com/questions/33871836/find-out-if-there-is-input-from-a-pipe-or-not-in-python).


## Liens utiles

 - [Organisation du développement collaboratif](https://slides.com/frozar/git) : le support de cours pour git/github,
 - [How to capture Control+D signal?](https://stackoverflow.com/questions/1516122/how-to-capture-controld-signal) : discussion sur l'interception du signal `End Of File`,
 - [Find out if there is input from a pipe or not in Python?](https://stackoverflow.com/questions/33871836/find-out-if-there-is-input-from-a-pipe-or-not-in-python) : discussion sur la détection de l'utilisation d'un pipe en Python,
 - [My Gource video production pipeline](https://dev.to/voieducode/my-gource-video-production-pipeline-5eb0) : décrit un exemple d'utilisation de gource,
 - [Philosophie d'Unix](https://fr.wikipedia.org/wiki/Philosophie_d%27Unix) : description de la philosophie Unix,
 - [Pipeline (Unix)](https://en.wikipedia.org/wiki/Pipeline_(Unix)) : description du pipe,
 - [Pipe: How the System Call That Ties Unix Together Came About](https://thenewstack.io/pipe-how-the-system-call-that-ties-unix-together-came-about/) : décrit l'histoire de la création du pipe.
