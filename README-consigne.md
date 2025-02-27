# Projet Minitrice

### Installation
Pour l'installion de notre projet il suffit de récupérer le répertoire créer avec tous les fichier et dossiers créés. Pour l'execution, il faudra, dans un terminal, executer le fichier "minitrice.py" avec l'opération souhaité. Il faudra également avoir "Python" d'installer sur votre machine.

### Execution
Exemple d'execution :
```bash
1. $ py minitrice.py
2. > 24-4
3. 0
4. >
5. Fin des calculs :)
```

Exemple de gestion d'erreur :
```bash
1. $ py minitrice.py
2. > 20/0
3. Erreur: Division par zéro
```
### Generator
Le générateur génère aléatoire un nombre de d'opérations fournis lors de l'appelle a la fonction. On a fait en sorte de gérer l'erreur de la division par 0 en limitant le choix des nombres de 1 à 1000. Pour les erreurs possibles de syntaxe tout est géré depuis le fichier minitrice.

Exemple d'execution du fichier "generator.py"
```bash
1. $ py generator.py 2
2. 242 * 250
3. 752 * 876
```
Exemple d'execution du fichier "generator.py" avec "minitrice.py"
```bash
1. $ py generator.py 2 | py minitrice.py
2. 665
3. 327
```

### Publication
https://youtu.be/QJj5j2jYu5k

