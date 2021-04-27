"""
These states encode the surname, first name, middle initial,
date of birth, and sex
"""

def get_soundex(name):
	"""Get the soundex code for the string"""
	name = name.upper()

	soundex = ""
	soundex += name[0]

	dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

	for char in name[1:]:
		for key in dictionary.keys():
			if char in key:
				code = dictionary[key]
				if code != soundex[-1]:
					soundex += code

	soundex = soundex.replace(".", "")
	soundex = soundex[:4].ljust(4, "0")

	return str(soundex)
def name_middle_initial(name, middle_initial):
	#get soundex of given name
	sdx = get_soundex(name)


	dictionary = {"A" : "000", "B" : "060", "C" : "100"}
	#just used a to c so that the math works
	#so in the below line we only need D-Z
	alphabet = 'DEFGHIJKLMNOPQRSTUVWXYZ'
	for i in range(1, len(alphabet)):
		dictionary[alphabet[i]] = str(100 + (i * 40))

	#middle initial codes
	dict2 = {"NO" : 14, "PQ" : 15, "R" : 16, "S" : 17, "TUV" : 18, "WXYZ" : 19}
	alphabet2 = "ABCDEFGHIJKLM"

	for i in range(len(alphabet2)):
		dict2[alphabet2[i]] = i + 1

	next_3_nums = int(dictionary[name[0]]) + dict2[middle_initial]
	sdx += str(next_3_nums)
	return sdx

def get_last_nums(month, day, year, whichState, sex, sdx):
	month = str(month)
	year = str(year)

	isFemaleTrue = 0
	if sex.lower() == 'f':
		isFemale = True

	if whichState.lower() == 'illinois':
		eachMonth = 31
		if isFemale == True:
			isFemaleTrue = 6
	elif whichState.lower() == 'florida':
		eachMonth = 40
		if isFemale == True:
			isFemaleTrue = 5
	
	max_num_illinois = eachMonth * 12
	isFemale = True

	dictMonths = {"JANUARY" : 1, "FEBRUARY" : 2, "MARCH" : 3,
		"APRIL" : 4, "MAY" : 5, "JUNE" : 6, "JULY" : 7,
		"AUGUST" : 8, "SEPTEMBER" : 9, "OCTOBER" : 10,
		"NOVEMBER" : 11, "DECEMBER" : 12}

	year_sep = "-"

	year = year[-2:]
	if whichState.lower() == 'illinois':
		year = year[0] + year_sep + year[-1]

	monthEncoding = (dictMonths[month.upper()] - 1) * eachMonth + day

	if len(str(monthEncoding)) < 3:
		monthEncoding = str(monthEncoding)
		monthEncoding = monthEncoding[::-1]
		for i in range(3 - len(monthEncoding)):
			monthEncoding += '0'
		monthEncoding = monthEncoding[::-1]
	if isFemale == True:
		monthEncodingFirstNum = int(str(monthEncoding)[0])
		monthEncodingFirstNum += isFemaleTrue
		monthEncoding = str(monthEncodingFirstNum) + str(monthEncoding)[1:]

	sdx += str(year) + str(monthEncoding)
	return sdx

MyLicenseNumber = get_last_nums("March", 3, 1949, 'florida', 'f', name_middle_initial('Matthew', 'A'))
print(MyLicenseNumber)