from __future__ import print_function
import sys
import math
in_stream = sys.stdin
def max_stack(num_ants, weights):
    max_num_ants = 0
    min_weight = list()
    min_weight_for_1_ant = list()
    for i in range(num_ants):
        if(i == 0):
            min_weight_for_1_ant.append(weights[i])
        else:
            min_weight_for_1_ant.append(min(min_weight_for_1_ant[i-1], weights[i]))
        max_num_ants = 1
    min_weight.append(min_weight_for_1_ant)
    for num_in_stack in range(1, num_ants):
        min_weight_for_num_ants = list()
        for i in range(num_ants):
            if(i + 1 < num_in_stack + 1):
                min_weight_for_num_ants.append(-1)
            elif(i+1 == num_in_stack + 1):
                if(min_weight[num_in_stack-1][i-1] != -1 and min_weight[num_in_stack-1][i-1] <= 6 * weights[i]):
                    min_weight_for_num_ants.append(min_weight[num_in_stack-1][i-1] + weights[i])
                    max_num_ants = num_in_stack + 1
                else:
                    min_weight_for_num_ants.append(-1)
            else:
                if(min_weight[num_in_stack-1][i-1] != -1 and min_weight[num_in_stack-1][i-1] <= 6 * weights[i]):
                    current_ant = min_weight[num_in_stack-1][i-1] + weights[i]
                else:
                    current_ant = -1
                old_ant = min_weight_for_num_ants[i-1]
                if(current_ant == -1 and old_ant == -1):
                    min_weight_for_num_ants.append(-1)
                elif(current_ant == -1):
                    min_weight_for_num_ants.append(old_ant)
                    max_num_ants = num_in_stack + 1
                elif(old_ant == -1):
                    min_weight_for_num_ants.append(current_ant)
                    max_num_ants = num_in_stack + 1
                else:
                    min_weight_for_num_ants.append(min(old_ant, current_ant))
                    max_num_ants = num_in_stack + 1
        min_weight.append(min_weight_for_num_ants)
    return max_num_ants
def main(args):
    T = int(in_stream.readline().strip())
    for x in range(T):
        in_data = in_stream.readline().split()
        N = int(in_data[0])
        weights_str = in_stream.readline().split()
        weights = list()
        for i in range(N):
            weight = int(weights_str[i])
            weights.append(weight)
        max_num_ants = max_stack(N, weights)
        print("Case #%d: %d" % (x+1, max_num_ants))
if(__name__ == '__main__'):
    ret = main(sys.argv)
    sys.exit(ret);