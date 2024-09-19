def catMap(x,y,size):
	xNew=(2*x+y)%size
	yNew=(x+y)%size
	return xNew,yNew
