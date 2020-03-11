import numpy as np
import cv2

def test(image):
	image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	ret, thresh = cv2.threshold(image_gs, 127, 255, 0)
	contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#print(contours, image2)
	cv2.drawContours(image, contours, -1, (0, 255, 0), thickness=3)
	cv2.imshow("test", image)
	cv2.waitKey(0)

def test2(image):
	hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
	lower_red = np.array([30,150,50]) 
	upper_red = np.array([255,255,180]) 
	mask = cv2.inRange(hsv, lower_red, upper_red) 
	res = cv2.bitwise_and(image,image, mask= mask) 
	cv2.imshow('Original',image) 
	edges = cv2.Canny(image,100,200) 
	cv2.imshow('Edges',edges)
	cv2.waitKey(0)
	cv2.destroyAllWindows()  



def test4():
	pass

def main():
	file_path = input("Where is the image stored:")
	image = cv2.imread(file_path)
	if(image is None):
		print("whoopsiedaisie")
		return
	image1 = image.copy()
	image2 = image.copy()
	image3 = image.copy()
	test(image1)
	test2(image2)


if __name__ == "__main__":
	main()



