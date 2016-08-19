#Exercise 1
#Write a function to calculate the greatest common divisor of two numbers

def common_divisor(number1, number2):
	if number1 % number2 == 0:
		print number2
	elif number2 % number1 == 0:
		print number1
	return common_divisor(number2,(number1 % number2))
	
	


	
	
	
	






















#Exercise 2
#Write a function that returns prime numbers less than 121

#Exercise 3
#Write a function that gives a solution to Tower of Hanoi game
#https://www.mathsisfun.com/games/towerofhanoi.html



