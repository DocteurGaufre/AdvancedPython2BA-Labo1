import math
import scipy.integrate as spi
import scipy.optimize as opt

def fact(n):
	"""Computes the factorial of a natural number.
	
	Pre: -
	Post: Returns the factorial of 'n'.
	Throws: ValueError if n < 0
	"""
	fact = 1

	if n < 0 :
		return ValueError

	for chiffre in range(1, n + 1):
		fact = fact * chiffre

	return fact

def roots(a, b, c):
	"""Computes the roots of the ax^2 + bx + x = 0 polynomial.
	
	Pre: -
	Post: Returns a tuple with zero, one or two elements corresponding
		to the roots of the ax^2 + bx + c polynomial.
	"""
	Delta = (b**2) - (4*a*c)

	if Delta < 0 :
		return(())
	if Delta == 0 :
		x1 = (-b)/(2*a)
		return((x1))
	if Delta > 0 :
		x1 = (-b + math.sqrt(Delta)) / (2*a)
		x2 = (-b - math.sqrt(Delta)) / (2*a)
		return((x1,x2))


def integrate(function, lower, upper):
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	if lower > upper:
		return ValueError

	f = lambda x: eval(function)
	resultat, erreur = spi.quad(f, -1, 1)

	return resultat

if __name__ == '__main__':
	print(fact(5))
	print(roots(-1, -9, 20))
	print(integrate('x ** 2 - 1', -1, 1))