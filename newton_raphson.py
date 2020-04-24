'''This program uses the Newton-Raphson method to find the root of the polynomial
2x^3 − 9x^2 + 12x − 6.'''

#the polynomial. if changed, p1 must also be changed.
def p(x):
    return 2*x**3 - 9*x**2 + 12*x - 6

#the derivative
def p1(x):
    return 6*x**2 - 18*x + 12

#solves polynomial given in function p. guess = initial guess, epsilon = acceptable error
def solve(guess,epsilon):
    number_of_guesses = 0
    while abs(p(guess)) >= epsilon:
        number_of_guesses += 1
        #Stop division by 0 or too many steps
        if p1(guess) == 0 or number_of_guesses>10000:
            print("Try some other initial guess or acceptable error.")
            return 
        guess -= p(guess)/p1(guess)
    print(f"Root = {guess}\nNumber of guesses = {number_of_guesses}")