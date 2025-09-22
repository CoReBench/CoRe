import math
def is_rounding_up(num):
    return round(num) > num
def solve(n, L, choices):
    left = n - sum(choices)
    to_investigate = []
    total = 0
    for i, c in enumerate(choices):
        percent = float(c) * 100 / n
        if not is_rounding_up(percent):
            to_investigate.append((i, c, percent))
        else:
            total += round(percent)
    to_investigate.sort(key=lambda x: x[2], reverse=True)
    one_unit = 1.0 / n
    if is_rounding_up(one_unit):
        total += left * round(one_unit * 100)
        return total
    for i, c, percent in to_investigate:
        decimal = (percent - round(percent))
        diff = 0.5 - decimal
        if diff < one_unit:
            min_additional_unit = 1
        else:
            min_additional_unit = math.floor(diff / one_unit)
            while min_additional_unit <= left:
                if is_rounding_up((min_additional_unit * one_unit) + diff):
                    break
                min_additional_unit += 1
        if min_additional_unit <= left:
            new_percent = float(c + min_additional_unit) * 100 / n
            total += round(new_percent)
            left -= min_additional_unit
        else:
            total += round(percent)
    if left:
        diff = 0.5 - one_unit
        if diff < one_unit:
            min_unit_req_for_higher_ = 2
        else:
            min_unit_req_for_higher_ = math.floor(diff / one_unit) + 1
            while min_unit_req_for_higher_ <= left:
                if is_rounding_up(min_unit_req_for_higher_ * one_unit):
                    break
                    min_unit_req_for_higher_ += 1
        if min_unit_req_for_higher_ <= left:
            max_comb = (left / min_unit_req_for_higher_)
            left = left - max_comb
            new_percent = float(max_comb * one_unit) * 100 / n
            total += round(new_percent)
            if left:
                total += left * round(one_unit * 100)
        else:
            total += left * round(one_unit * 100)
    return int(total)
if __name__ == '__main__':
    t = int(raw_input())  
    for case in xrange(1, t + 1):
        n, L = [int(num) for num in raw_input().split()]
        choices = [int(num) for num in raw_input().split()]
        print 'Case #{}: {}'.format(case, solve(n, L, choices))