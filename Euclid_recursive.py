def Eclid(max,min):
	if max == min :
		return max
	else:
		max-=min
		if max < min:
			tmp=min
			min=max
			max=tmp
		return Eclid(max,min)

border=Eclid(1680,640)
print border