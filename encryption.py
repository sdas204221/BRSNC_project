from PIL import Image
def e1(pixels,size,x,u):
	newImg=Image.new("L",(size,size),(0))
	newPixels=newImg.load()
	for i in range(size):
		for j in range(size):
			newPixels[i,j]=pixels[i,j]^int((x*(10**6))%256)
			x=u*x*(1-x)
	return newImg
