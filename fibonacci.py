def main():
    max_num=100
    dict_fib=dict.fromkeys(range(max_num))
    dict_fib[0],dict_fib[1] = 0, 1
    for i in range(2,max_num):
        dict_fib[i] = dict_fib[i-1]+dict_fib[i-2]
    n = input("a num < 12345678:")
    return True if n in dict_fib.values() else False

main()
