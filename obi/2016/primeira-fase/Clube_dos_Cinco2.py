
# https://olimpiada.ic.unicamp.br/pratique/p1/2016/f1/clube/


N = int(input ())
answers = list(map(int,input().split ()))

A = answers[0] - (answers[3] + answers[4])
B = answers[1] - (answers[3] + answers[5])
C = answers[2] - (answers[4] + answers[5])

verdade = sum (answers[3:7])

if (A + B + C) > (N - verdade):
	print ('S')
else:
	print ('N')


