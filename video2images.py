import cv2
import numpy as np

cap = cv2.VideoCapture('data/video.mp4')

filename = 'output/video-{0:05d}.jpg'
number = 1

while cap.isOpened():
	ret, frame = cap.read()
	cv2.imwrite(filename.format(number), frame)
	
	print('Saving frame', number, 'to', filename.format(number))

	number += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()