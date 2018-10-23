x=int(input())
def f(x):
    for i in range(x):
        num=int(input())
        if num>0 and num<10001:
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        print("NIE")
                        break
                else:
                        print("TAK")

            else:
                print("NIE")
        else:
            f(x)
f(x)