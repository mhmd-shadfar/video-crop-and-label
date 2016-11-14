import cv2
import numpy as np

source = cv2.imread("pic.jpg")
template = cv2.imread("subpic.jpg")

side_size = template.shape[0]

result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
y, x = np.unravel_index(result.argmax(), result.shape)

cv2.rectangle(source, (x, y), (x + side_size, y + side_size), (255, 255, 255))

cv2.imwrite('out.jpg', source)