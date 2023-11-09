import itertools
import fitz

FILE_INPUT = "mac-paper.pdf"
FILE_OUTPUT = "dcrypt.pdf"
CAR = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
DICTIONNAIRE = "dict.txt"


def foo(l, n=3):
		yield from itertools.product(*([l] * n)) 
def all_config_car(nb_car):
	p = []
	for x in foo(CAR, nb_car):
		p.append(''.join(x))
	return p

def test(passwords, pdf):
	for password in passwords:
		print("Trying password: " + password)
		if pdf.authenticate(password):
			pdf.save(FILE_OUTPUT)
			if pdf.save:
				print('Password is: ' + password)
				return 1
	return 0

def test_brute_force():
	pdf = fitz.open(FILE_INPUT)

	for i in range(15):
		# List of passwords to try
		passwords = all_config_car(i)

		if test(passwords, pdf) == 1:
			break

def test_dictionnaire():
	pdf = fitz.open(FILE_INPUT)
	passwords = open(DICTIONNAIRE, 'r').read().split('\n')
	test(passwords, pdf)

# test_brute_force()
test_dictionnaire()


