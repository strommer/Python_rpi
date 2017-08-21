import pprint


def scan_data(file_):
	f = open(file_).readlines()
	dictionary_mesh = {}
	for line in f:
		dictionary_mesh[line.partition(';')[0]] = line.partition(';')[2].strip('\n')
	pprint.pprint(dictionary_mesh)


def isa(a,b):
	dictionary = scan_data('mtr_smp.txt')
	print (dictionary[b] in dictionary[a])
		


if __name__ == "__main__":
	isa("Salmonella Food Poisoning", "Bacterial Infections")
	isa("Tularemia", "Bacterial Infections")
	isa("Mucormycosis", "Bacterial Infections")