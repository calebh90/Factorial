from math import factorial
from cmath import cos

fact = factorial
fact2 = cos
n = int(input("Hi! What number do you want to factor? "))
print("The factor of", n , "is" , fact(n))

Quest = input("Do you also want to do know the cosine of " + str(n) + "? ").lower()
def cosfunc(x):
	if x == "yes":
		return ("Ok, the cosine of "+ str(n) + " is " + str(fact2(n)))
	else:
		return "Ok... have a good day! :)"

print(cosfunc(Quest))