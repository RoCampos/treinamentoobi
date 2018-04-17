

N = int(input ());
fat = 1;
factorials = [];
factorials.append (1);
start = -1

for i in range(1, N):
	fat = fat * i;
	factorials.append (fat);
	if fat >= N:
		start = i-1
		break

k = 0
amount = 0;
while amount != N:
    amount = amount + factorials[start]
    k = k + 1
    if amount == N:
        break
    elif amount > N:
        amount = amount - factorials[start]
        start = start - 1
        k = k - 1

print (k)