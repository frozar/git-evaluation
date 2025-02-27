import re
import sys


#Mise en place de programme 
while True:
    #Mise en place de l'entrée d'élément de la part de l'utilisateur
    try:
        operation = input("> " if sys.stdin.isatty() else "")

        # Si deux signe d'opération se suivent alors on lance une erreur
        if not re.match(r"^\s*\d+(\.\d+)?\s*[-+*/]\s*\d+(\.\d+)?\s*$", operation):
            raise SyntaxError(f"Erreur de syntaxe pour le calcul: \"{operation}\"")
        #Gestion des différentes opérations possibles
        if '+' in operation:
            int1, int2 = operation.split('+')
            result = int(int1.strip()) + int(int2.strip())
        elif '-' in operation:
            int1, int2 = operation.split('-')
            result = int(int1.strip()) - int(int2.strip())
        elif '*' in operation:
            int1, int2 = operation.split('*')
            result = int(int1.strip()) * int(int2.strip())
        elif '/' in operation:
            int1, int2 = operation.split('/')
            #Si on essaye de diviser par 0 on lance une erreur
            if int(int2.strip()) == 0:
                raise ZeroDivisionError("Division par zéro")
            result = int(int1.strip()) / int(int2.strip())
        else :
            raise SyntaxError(f"Erreur de syntaxe pour le calcul: \"{operation}\"")
        #Affichage du résultat calculé
        print(result)
    #Si le programme rencontre une erreur ou un arrêt souhaiter alors affiche le message et/ou l'erreur
    except (KeyboardInterrupt, EOFError):
        if sys.stdin.isatty():
            print("\n Fin des calculs :)")
        sys.exit(0)
    except Exception as e:
        print(e)
        sys.exit(1)