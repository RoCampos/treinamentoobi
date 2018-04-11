import sys

def fatorial (N):
    fat = 1
    for i in range (1,N+1):
        fat = fat * i
    return fat

def main(N):
    
    fatoriais = []
    for i in range(1, N):
        fat = fatorial(i);
        if fat > N:
            break
        else:
            fatoriais.append (fat);
    soma = 0

    i = len(fatoriais)-1 #last position
    saida = 0
    while soma != N:
        soma = soma + fatoriais[i]
        saida = saida + 1
        if soma == N:
            break
        elif soma > N:
            soma = soma - fatoriais[i]
            i = i - 1
            saida = saida - 1

    print (saida)

if __name__ == '__main__':
    N = int(input())
    # N = int(sys.argv[1])
    main(N)