def get_xor(num):
	temp = [num,1,num+1,0]
	return temp[num%4]

def answer(start,length):
	skip = length-1
	if start == 0:
		ans = get_xor(start+skip)
	else:
		ans = get_xor(start+skip)^get_xor(start-1)
        
	while skip:
		start += length
		skip -= 1
		row_end = start+skip
		ans ^= get_xor(start-1)^get_xor(row_end)
    return ans