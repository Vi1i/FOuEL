def eval(equation, x, y):
	if(equation == 0):
		return rosenbrockBanana(x, y)
	elif(equation == 1):
		return goldsteinPrice(x, y)
	else:
		print("ERROR")

def rosenbrockBanana(x, y):
	result = 0;
	result = ((1 - x) ** 2) + (100 * ((y - (x ** 2)) ** 2))
	return result

def goldsteinPrice(x, y):
	result = 0;
	result = ((((x + y + 1) ** 2) * (19 - (14 * x) + (3 * (x ** 2)) - (14 * y) + (6 * x * y) + (3 * (y ** 2)) ) + 1) * ((((2 * x) - (3 * y)) ** 2) * (18 - (32 * x) + (12 * (x ** 2)) + (48 * y) - (36 * x * y) + (27 * (y ** 2)) ) + 30))
	return result