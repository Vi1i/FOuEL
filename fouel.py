import random
import struct
from bitstring import BitArray

def rosenbrockBanana(x, y):
	result = 0;
	result = ((1 - x) ** 2) + (100 * ((y - (x ** 2)) ** 2))
	return result

def goldsteinPrice(x, y):
	result = 0;
	result = ((((x + y + 1) ** 2) * (19 - (14 * x) + (3 * (x ** 2)) - (14 * y) + (6 * x * y) + (3 * (y ** 2)) ) + 1) * ((((2 * x) - (3 * y)) ** 2) * (18 - (32 * x) + (12 * (x ** 2)) + (48 * y) - (36 * x * y) + (27 * (y ** 2)) ) + 30))
	return result

def to_binary(num):
	return BitArray(float=num, length=64).bin

def to_float(num):
	return BitArray("0b"+ num).float

def initPop(pops, r):
	population = {}
	for pop in range(0, pops):
		_x = random.uniform(r[0], r[1])
		_y = random.uniform(r[0], r[1])
		x = to_binary(_x)
		y = to_binary(_y)
		# An example of taking a float into binary, and a binary into a float
		population[pop] = (x, y)

	return population

def selector(population, count):
	result = random.sample(population, count)

	return result

def eval(equation, x, y):
	_x = to_float(x)
	_y = to_float(_y)
	if(equation == 0):
		return rosenbrockBanana(_x, _y)
	elif(equation == 1):
		return goldsteinPrice(_x, _y)
	else:
		print("ERROR")

# Set the seed for the random generator
random.seed(0)

#create the population
population = initPop(100, (-2, 2))

selection = selector(population, 5)
print(selection)