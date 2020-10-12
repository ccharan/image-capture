import cv2
import time

# capturing the image and waiting for 1 sec
cam = cv2.VideoCapture(0)
time.sleep(1)

# reading the image by calling the read method, read returns 2 values
# so selecting second returned value by indicating [1].
img = cam.read()[1]

# saving the image and releasing the camera
cv2.imwrite('capturedImage.jpg', img)
cam.release()

# displaying the captured image & waiting until window is closed
cv2.imshow('Captured Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
