
N = int(input ())
answers = list(map(int,input().split ()))

a = sum(answers[0:3])
b = sum(answers[3:6])

if (a-b) > (N):
	print ('S')
else:
	print ('N')

