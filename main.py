import cv2
img = cv2.imread("src/umi_small.jpg", 0)

def onTrackbar(position):
	global threshold
	threshold = position
cv2.namedWindow("img")
threshold = 100
cv2.createTrackbar("track", "img", threshold, 255, onTrackbar)
while True:
	ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
	cv2.imshow("img", img_th)
	cv2.imshow("src", img)
	# Escキーで抜ける
	if cv2.waitKey(10) == 27:
		break
cv2.destroyAllWindows()
