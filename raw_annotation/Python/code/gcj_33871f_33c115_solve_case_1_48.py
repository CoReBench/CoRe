def solve_case(in_times, edges):
    latencies = [10**6]*len(edges)
    edges = [(a-1, b-1) for (a,b) in edges]
    abs_times = [10**6]*len(in_times)
    for index, i in enumerate(in_times):
        if i > 0:
            abs_times[index] = i
    pos_times = []
    for index, i in enumerate(in_times):
        if i < 0:
            pos_times.append( (abs(i), index) )
    pos_times.sort()
    current_time = 0    
    received = 1        
    while pos_times:
        if pos_times[0][0] == received:
            current_time += 1
            new_received = 0
            while pos_times and pos_times[0][0] == received:
                new_received += 1
                a,b = pos_times[0]
                abs_times[b] = current_time
                pos_times = pos_times[1:]
            received += new_received
        else:
            next_times = []
            for i in abs_times:
                if i > current_time:
                    next_times.append(i)
            current_time = min(next_times)
            received_count = 0
            for i in abs_times:
                if i <= current_time:
                    received_count += 1
    abs_times = [0] + abs_times
    sorted_receipt = [(i, ind) for ind, i in enumerate(abs_times)]
    sorted_receipt.sort()
    for time, comp in sorted_receipt[1:]:
        for index, (A, B) in enumerate(edges):
            if A == comp:
                if abs_times[A] > abs_times[B]:
                    latencies[index] = abs_times[A] - abs_times[B]
                    break
            if B == comp:
                if abs_times[B] > abs_times[A]:
                    latencies[index] = abs_times[B] - abs_times[A]
                    break
    return ' '.join(map(str, latencies))
def main():
    T = int(raw_input())
    for case_no in xrange(1, T+1):
        num_comps, num_edges = map(int, raw_input().split(' '))
        in_times = map(int, raw_input().split(' '))
        edges = []
        for edge_no in xrange(num_edges):
            edges.append(tuple(map(int, raw_input().split())))
        ans = solve_case(in_times, edges)
        print "Case #{}: {}".format(case_no, ans)
main()