from copy import deepcopy
def FindNewWord(w_list):
	w_list.sort()
	L = len(w_list[0])
	if len(w_list) == 1 or L ==1:
		return "-"
	prefix_index = [0]
	N = len(w_list)
	last_prefix = w_list[0][0]
	for i in range(1, N):
		if w_list[i][0] != last_prefix:
			last_prefix = w_list[i][0]
			prefix_index.append(i)
	prefix_index.append(N)
	curr_word = ""
	for p in range(1, L):
		available_letters = {w_list[0][p]}
		for k in range(1, N):
			available_letters.add(w_list[k][p])
		n_prefixes = len(prefix_index)
		isFound=False
		new_prefix_index = []
		for n_prefix in range(n_prefixes -1):
			start_index = prefix_index[n_prefix]
			end_index   = prefix_index[n_prefix+1]
			letters_in_prefix = {w_list[start_index][p]}
			last_letter = w_list[start_index][p]
			new_prefix_index.append(start_index)
			for item in range(start_index + 1, end_index):
				letter = w_list[item][p]
				if letter != last_letter:
					last_letter =letter
					letters_in_prefix.add(w_list[item][p])
					new_prefix_index.append(item)
			remaining_letters = available_letters.difference(letters_in_prefix)
			if len(remaining_letters) > 0:
				letter = next(iter(remaining_letters))
				curr_word = w_list[start_index][:p] + letter
				isFound = True
				break
		if isFound:
			break
		new_prefix_index.append(N)
		prefix_index = deepcopy(new_prefix_index)
	if not isFound:
		return "-"
	size_p = len(curr_word)
	for p in range(size_p, L):
		curr_word+= w_list[0][p]
	return  curr_word
def solve_jam():
	T = int(input())
	output = []
	for i in range(T):
		data = str(raw_input()).split()
		N = int(data[0])
		L = int(data[1])
		w_list = []
		for p in range(N):
			w_list.append(str(raw_input()))
		out = FindNewWord(w_list)
		output.append(out)
	return output
def save_output(output):
	for index, value in enumerate(output):
		print "Case #"+ str(index + 1)+ ": " + str(value)
out = solve_jam()
save_output(out)