import pprint


def scan_data(file_):
	f = open(file_).readlines()
	dictionary_mesh = {}
	for line in f:
		dictionary_mesh[line.partition(';')[0]] = line.partition(';')[2].strip('\n')
	return(dictionary_mesh)


def dictionary_maker(file__):
	dictionary_term = scan_data(file__)
	dictionary_num = {}
	for i in dictionary_term:
		dictionary_num[i] = dictionary_term[i].split('.')
	return (dictionary_num)


def dictionary_maker2(dictionary_num2):
	dict1 = {}
	for i in sorted(dictionary_num2.values()):
		branch = dict1
		for part in i:
			if part in branch:
				branch = branch[part]
			else:
				branch[part] = {}
	pprint.pprint(dict1)
	return(dict1)

	
def isa(a,b):
	dictionary = scan_data("mtr_smp.txt")
	# a1 = dictionary[a]
	# b1 = dictionary[b]
	# dictionary2 = dictionary_maker2(dictionary)
	# return (dictionary2[b1[-1]] in dictionary2[a1[-1]])
	return(dictionary[b] in dictionary[a])
		


if __name__ == "__main__":
	dictionary = dictionary_maker('mtr_smp.txt')
	dictionary_maker2(dictionary)
	print(isa("Salmonella Food Poisoning", "Bacterial Infections"))
	print(isa("Tularemia", "Bacterial Infections"))
	print(isa("Mucormycosis", "Bacterial Infections"))
	# scan_data('mtr_smp.txt')
	