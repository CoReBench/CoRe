def calculate(arr, size):
    even_arr = [0] * (size / 2)
    odd_arr = [0] * (size - len(even_arr))
    eveni = 0
    oddi = 0
    for i in xrange(size):
        if (i+1) % 2 == 0:
            even_arr[eveni] = arr[i]
            eveni += 1
        else:
            odd_arr[oddi] = arr[i]
            oddi += 1
    even_arr.sort()
    odd_arr.sort()
    eveni = 0
    oddi = 0
    last = -1
    for i in xrange(size):
        if i == 0:
            last = odd_arr[oddi]
            oddi += 1
            continue
        if i % 2 == 1:
            if even_arr[eveni] < last:
                return str(i-1)
            last = even_arr[eveni]
            eveni += 1
        else:
            if odd_arr[oddi] < last:
                return str(i-1)
            last = odd_arr[oddi]
            oddi += 1
    return 'OK'
def main():
    t = int(raw_input())
    for i in xrange(t):
        size = int(raw_input())
        arr = map(int, raw_input().split(' '))
        ans = calculate(arr, size)
        print 'Case #' + str(i+1) + ': ' + ans
main()