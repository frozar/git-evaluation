import re
import sys

while True:
    try:
        operation = input("> " if sys.stdin.isatty() else "")

        if not re.match(r"^\s*\d+(\.\d+)?\s*[-+*/]\s*\d+(\.\d+)?\s*$", operation):
            raise SyntaxError(f"Erreur de syntaxe pour le calcul: \"{operation}\"")
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
            if int(int2.strip()) == 0:
                raise ZeroDivisionError("Division par zéro")
            result = int(int1.strip()) / int(int2.strip())
        else :
            raise SyntaxError(f"Erreur de syntaxe pour le calcul: \"{operation}\"")
        
        print(result)

    except (KeyboardInterrupt, EOFError):
        if sys.stdin.isatty():
            print("\n Fin des calculs :)")
        sys.exit(0)
    except Exception as e:
        print(f"Erreur: {e}")
        sys.exit(1)