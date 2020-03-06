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


def main():
	file_path = input("Where is the image stored:")
	image = cv2.imread(file_path)
	if(image is None):
		print("whoopsiedaisie")
		return
	test(image)
	


if __name__ == "__main__":
	main()