import cv2
import numpy as np

img = np.zeros((600, 800, 3), np.uint8)

print(img[:10])
print(len(img))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
