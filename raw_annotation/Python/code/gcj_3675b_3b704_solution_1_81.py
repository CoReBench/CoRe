def solution(number_of_signs):
    a_to_b = []
    for i in range(number_of_signs):
        sign = raw_input()
        d, a, b = sign.split()
        d = int(d)
        a = int(a)
        b = int(b)
        a_to_b.append((d + a, d - b))
    N = None
    M = None
    maximum_set_size = 1
    number_of_maximum_set_sized = 0
    current_set_size = 1
    a_for_comparision, b_for_comparision = a_to_b.pop(0)
    is_finish = False
    while not is_finish and len(a_to_b) > 0:
        for index, tup in enumerate(a_to_b):
            if index == len(a_to_b) - 1:
                is_finish = True
            a, b = tup
            if N is not None and M is None:
                if a != a_for_comparision:
                    M = b
                    b_for_comparision = b
                current_set_size += 1
            elif M is not None and N is None:
                if b != b_for_comparision:
                    N = a
                    a_for_comparision = a
                current_set_size += 1
            elif M is not None and N is not None:
                if b != b_for_comparision and a != a_for_comparision:
                    if current_set_size > maximum_set_size:
                        maximum_set_size = current_set_size
                        number_of_maximum_set_sized = 1
                    elif current_set_size == maximum_set_size:
                        number_of_maximum_set_sized += 1
                    current_set_size = 1
                    N = None
                    M = None
                    a_to_b = a_to_b[index:]
                    break
                    a_for_comparision = a
                    b_for_comparision = b
                else:
                    current_set_size+=1
            elif a == a_for_comparision and b == b_for_comparision:
                if (N is None):
                    a_for_comparision = a
                if (M is None):
                    b_for_comparision = b
                current_set_size += 1
                continue
            elif a == a_for_comparision and b != b_for_comparision:
                if (N is None):
                    N = a
                    a_for_comparision = N
                b_for_comparision = b
                current_set_size += 1
            elif b == b_for_comparision and a != a_for_comparision:
                if (M is None):
                    M = b
                    b_for_comparision = b
                a_for_comparision = a
                current_set_size += 1
            elif b != b_for_comparision and a != a_for_comparision:
                if len(a_to_b) > index:
                    if a == a_to_b[index+1][0]:
                        N = a_to_b[index +1][0]
                        a_for_comparision = a_to_b[index +1][0]
                        M = b_for_comparision
                        current_set_size+=1
                    else:
                        M = a_to_b[index +1][1]
                        b_for_comparision = a_to_b[index +1][1]
                        N = a_for_comparision
                        current_set_size+=1
                else:
                    current_set_size += 1
    return maximum_set_size, number_of_maximum_set_sized
def read_input():
    number_of_tests = raw_input()
    for test_number in range(int(number_of_tests)):
        number_of_signs = raw_input()
        try:
            print_output(solution(int(number_of_signs)), test_number + 1)
        except Exception as exc:
            pass
def print_output(answer, test_case):
    print "Case #{0}: {1} {2}".format(test_case, answer[0], answer[1])
read_input()