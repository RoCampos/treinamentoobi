import sys

def factorial (N):
    fat = 1
    for i in range (1,N+1):
        fat = fat * i
    return fat

def main(N):
    factorials = []
    for i in range(1, N):
        fat = factorial(i);
        if fat > N:
            break
        else:
            factorials.append (fat);
    amount = 0
    
    i = len(factorials)-1 #last position

    # number os factorials
    k = 0

    while amount != N:
        amount = amount + factorials[i]
        k = k + 1
        if amount == N:
            break
        elif amount > N:
            amount = amount - factorials[i]
            i = i - 1
            k = k - 1

    print (k)

if __name__ == '__main__':
    N = int(input())
    main(N)