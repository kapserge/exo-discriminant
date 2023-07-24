import random
def generation_aleatoire():
    option1 = random.randint(1, 10)
    option2 = random.randint(1, 10)
    option3 = random.randint(1, 10)
    return option1, option2, option3
    
def calcul_descriminant(a, b, c):
    return b**2 - 4*a*c

numbers = generation_aleatoire()
descriminant = calcul_descriminant(*numbers)
while descriminant <= 0:
   numbers = generation_aleatoire()
   descriminant = calcul_descriminant(*numbers)
output = f"""le descriminant de l'équation:
            {str(numbers[0])}x2 + {str(numbers[1])}x + {str(numbers[2])} est: {str(descriminant)}"""
print(output)

while descriminant != 0:
   numbers = generation_aleatoire()
   descriminant = calcul_descriminant(*numbers)
output = f"""le descriminant de l'équation:
            {str(numbers[0])}x2 + {str(numbers[1])}x + {str(numbers[2])} est: {str(descriminant)}"""
print(output)

while descriminant >= 0:
   numbers = generation_aleatoire()
   descriminant = calcul_descriminant(*numbers)
output = f"""le descriminant de l'équation:
            {str(numbers[0])}x2 + {str(numbers[1])}x + {str(numbers[2])} est: {str(descriminant)}"""
print(output)