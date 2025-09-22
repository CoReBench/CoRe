def solve(L):
	sorted_list = sorted(L)
	done = False
	lengthList = len(L)
	while not done:
		done = True
		i = 0
		while i < lengthList-2:
			if L[i] > L[i+2]:
				done = False
				tmp = L[i]
				L[i] = L[i+2]
				L[i+2] = tmp
			i+=1
	c = 0
	while c < lengthList:
		expected = sorted_list[i]
		if L[i] != expected:
			return i
		c+=1
	return -1
def main():
	tc = input()
	i = 0
	while i < tc:
		n = input()
		l = [ int(n) for n in raw_input().split() ]
		result = solve(l)
		buffer = "OK"
		if result >= 0:
			buffer = "%d" % result
		i += 1
		print "Case #%d: %s" % (i,buffer)
main()