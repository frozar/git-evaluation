import re

while True:
    try:
        operation = input("> ")

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
            result = int(int1.strip()) / int(int2.strip())
        else :
            raise SyntaxError(f"Erreur de syntaxe pour le calcul: \"{operation}\"")
        
        print(result)

    except Exception as e:
        print(f"Erreur: {e}")