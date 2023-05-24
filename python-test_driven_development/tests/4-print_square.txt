>>> print_square = __import__('4-print_square').print_square

(int as input)
>>> print_square(4)
####
####
####
####

(str as input)
>>> print_square("4")
Traceback (most recent call last):
    ...
TypeError: size must be an integer

(float as input)
>>> print_square(4.0)
Traceback (most recent call last):
	...
TypeError: size must be an integer

(negative int as input)
>>> print_square(-4)
Traceback (most recent call last):
    ...
ValueError: size must be >= 0

(zero as input)
>>> print_square(0)


(no input)
>>> print_square()
Traceback (most recent call last):
    ...
TypeError: print_square() missing 1 required positional argument: 'size'

(nan as input)
>>> print_square(float('nan'))
Traceback (most recent call last):
    ...
TypeError: size must be an integer

(inf as input)
>>> print_square(float('inf'))
Traceback (most recent call last):
    ...
TypeError: size must be an integer

(tuple as input)
>>> print_square((4, ))
Traceback (most recent call last):
    ...
TypeError: size must be an integer