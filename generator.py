import sys
import random

nb_expression = int(sys.argv[1])
for i in range(nb_expression):
    int1 = random.randint(1, 1000)
    int2 = random.randint(1, 1000)
    operand = random.choice(['+', '-', '*', '/'])
    print(f"{int1} {operand} {int2}")
