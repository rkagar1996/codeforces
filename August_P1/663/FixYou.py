# https://codeforces.com/contest/1391/problem/B

t = int(input())
for test in range(t):
	n,m = map(int,input().split())
	a = []
	for i in range(n):
		a.append(list(str(input())))
	if n == 1 and m == 1:
		print(0)
	elif n == 1:
		c = 0
		for i in range(m):
			if a[0][i] == 'D':
				c += 1
		print(c)
	elif m == 1:
		c = 0
		for i in range(n):
			if a[i][0] == 'R':
				c += 1
		print(c)
	else:
		c = 0
		for i in range(m):
			if a[-1][i] == 'D':
				c += 1
		for i in range(n):
			if a[i][-1] == 'R':
				c += 1
		print(c)
