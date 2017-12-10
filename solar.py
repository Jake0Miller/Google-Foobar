def answer(xs):
	xs.sort()
	ans = xs.pop()
	pos = [x for x in xs if x > 1]
	neg = [x for x in xs if x < 0]
	while pos:
		ans *= pos.pop()
	while len(neg) > 1:
		ans *= neg.pop(0)*neg.pop(0)
	return str(ans)