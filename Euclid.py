#-*- coding:utf-8 -*-
width=1680
height=640
if height>width :
	max=height
	min=width
else :
	max=width
	min=height
while(max != min):
	while(max>min):
		max-=min
	tmp=min
	min=max
	max=tmp
print "the width: ",width," height: ",height," rectangle transform square and the border length is:",min