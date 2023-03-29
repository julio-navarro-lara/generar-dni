import sys, argparse
import random

def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--first', required=False, action='store', help='First')
	parser.add_argument('-l', '--last', required=False, action='store', help='Last')
	parser.add_argument('-o', '--outputfile', required=True, action='store', help='Output file')
	parser.add_argument('-q', '--quantity', required=False, action='store', help='Quantity of words')
	my_args = parser.parse_args()
	return my_args


def letra_dni(dni):
	letras="TRWAGMYFPDXBNJZSQVHLCKEO"
	valor = dni%23
	return letras[valor]


def main():
	args = get_args()
	first = args.first
	last  = args.last
	outfile = args.outputfile
	quantity = args.quantity
	dni_arr = []
	if first and last:
		for i in range(int(first),int(last)+1):
			dni_arr.append(format(i, '08d')+letra_dni(i))
	elif quantity:
		for i in range(0,int(quantity)):
			random_dni = random.randint(0,99999999)
			dni_arr.append(format(random_dni, '08d')+letra_dni(random_dni))
	
	with open(outfile, 'w') as f:
		for item in dni_arr:
			f.write("%s\n" % item)



if __name__ == "__main__":
    main()