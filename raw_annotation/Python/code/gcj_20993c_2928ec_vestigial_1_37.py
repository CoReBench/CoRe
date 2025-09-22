def vestigial(pinax):
	size = len(pinax[0])
	result = []
	row_digits = []
	column_digits = []
	for i in range(0, size):
		column_digits.append([])
	same_row_counter = 0 
	same_column_counter = [0]*size
	trail = 0
	for row in range(0, size):
		del row_digits[:]
		for column in range(0, size):
			if(row==column):
				trail += pinax[row][row]
			if(len(row_digits)==column):
				for i in range(0, len(row_digits)+1):
					if (i ==(len(row_digits))): 
						row_digits.append(pinax[row][column])
						break
					elif (row_digits[i] == pinax[row][column]):
						same_row_counter +=1
						break
			for i in range(0, len(column_digits[column])+1):
				if(i== len(column_digits[column])):
					column_digits[column].append(pinax[row][column])
					break
				elif(column_digits[column][i] == pinax[row][column]):
					same_column_counter[column] =1
					break
	sumC = 0
	for i in range(0, size):
		sumC += same_column_counter[i]
	result.append(trail)	
	result.append(same_row_counter)
	result.append(sumC)
	return result
def main():
	testCases = int(raw_input())
	for i in range(0, testCases):
		size = int(raw_input())
		pinax = [[]]*size
		for j in range(0, size):
			pinax[j] = list(map(int, raw_input().split()))
		result = vestigial(pinax)
		print("Case #" + str(i) + ": " + str(result[0]) + " " + str(result[1]) + " " + str(result[2]) )
main()