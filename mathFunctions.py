import random
import math

#Constants represeting value corresponding to level
ADD = 0
SUB = 1
MULT = 2
DIV = 3
POW = 4
ROOT = 5
ALG = 6
TRIG = 7
DER = 8
INT = 9


class basicProblem:
    def __init__(self, mathType, level):
        self.mathType = mathType
        self.level = level

    #Returns a tuple of the question(as a string), and the int value of the correct answer
    def executeProblem(self):
        if self.mathType == ADD:
            ans = addition(self.level)
        elif self.mathType == SUB:
            ans = subtraction(self.level)
        elif self.mathType == MULT:
            ans = multiplication(self.level)
        elif self.mathType == DIV:
            ans = division(self.level)
        elif self.mathType == POW:
            ans = power(self.level)
        elif self.mathType == ROOT:
            ans = root(self.level)
        else:
            ans = root(self.level)
        return ans

def addition(level):
    if level == 0:
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
    elif level == 1:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    else:
        num1 = random.randint(1, 2000)
        num2 = random.randint(1, 1000)
    #Output numbers
    #print(num1, " + ", num2)
    return (str(num1)+" + "+str(num2)), num1 + num2

def subtraction(level):
    if level == 0:
        num2 = random.randint(1,9)   
        num1 = random.randint(num2,10)
    elif level == 1:
        num2 = random.randint(1, 10)
        num1 = random.randint(1, 100)
    else:
        num2 = random.randint(-100, 100)
        num1 = random.randint(-100, 100)
    #Output numbers
    #print(num1, " - ", num2)
    return (str(num1)+" - "+str(num2)), num1 - num2

def multiplication(level):
    if level == 0:
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)
    elif level == 1:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 9)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
    #Output numbers
    #print(num1, " x ", num2)
    return (str(num1)+" x "+str(num2)), num1 * num2

def division(level):
    if level == 0:
        num2 = random.randint(1,9)
        num1 = num2*random.randint(1,10)
    elif level == 1:
        num1 = random.randint(1, 20) 
        num2 = random.randint(1, 9)
    else:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
    #Output Numbers
    #print(num1, " / ", num2)
    #Decimal point amount
    return (str(num1)+" / "+str(num2)), int((num1/num2)+0.5)

def power(level):
    if level == 0:
        num1 = random.randint(2,20)
        num2 = 2
    else:
        num1 = random.randint(3, 20)
        num2 = random.randint(2, 3)

    #Output numbers
    #print(num1, " ^ (", num2, ")")
    return (str(num1)+" ^ ("+str(num2) + ")"), num1 ** num2

def root(level):
    if level == 0:
        root = 2
        x = random.randint(1,15)**root
    else:
        root = 3
        x = random.randint(1,15)**root
    #Output numbers
    #print(x, " ^ (1/", root, ")")
    return (str(x)+" ^ (1/"+str(root) + ")"), x ** (1/root)

#Future implementation
def functionCreate(level):#creates the function string for alg, deriv and integrals
    functStr=''
    coeff1 = 0 #First term
    coeff2 = 0
    coeff3 = 0
    power1 = 0
    power2 = 0
    const = 0
    if level == 1:
        coeff1 = random.randint(2,10)
        const = random.randint(2, 10)
        functStr = str(coeff1)+'x +' + str(const)
    if level == 2:
        coeff1 = random.randint(2, 10)
        power1 = 2
        coeff2 = random.randint(2, 10)
        const = random.randint(2, 10)
        functStr = str(coeff1)+'x^' +str(power1) +" + " + str(coeff2) + "x + " + str(const)
    if level == 3:
        coeff1 = random.randint(2, 10)
        power1 = 3
        coeff2 = random.randint(2, 10)
        power2 = 2
        coeff3 = random.randint(2, 10)
        const = random.randint(2, 10)
        functStr = str(coeff1) + 'x^ ' + str(power1) + " + " + str(coeff2) + 'x^ ' + str(power2) + " + " + str(coeff3) + "x + " + str(const)
    return functStr, coeff1, const, coeff2, power1, coeff3, power2

#returns the greatest answer
def quadraticFormula(a, b, c):
    x1 = ((-b + math.sqrt(b**2 - (4 * a * c))) / (2 * a))
    x2 = ((-b - math.sqrt(b**2 - (4 * a * c))) / (2 * a))
    if x1 >= x2:
        return x1
    else:
        return x2

#future implementation
def algebra(level):
    answer = 0
    if level == 0:
        y = random.randint(1,30)
        funct = functionCreate(1)
        coeff = funct[1]
        const = funct[2]
        answer = round(((y - const) / coeff), 1)
    else:
        y = 0
        funct = functionCreate(2)
        coeff1 = funct[1]
        const = funct[2]
        coeff2 = funct[3]
        answer = quadraticFormula(coeff1, coeff2, const)
    return (str(y) + " = " + funct[0]), answer
