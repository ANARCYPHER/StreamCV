import cv2

capture = cv2.VideoCapture("http://192.168.1.67:8080/video")

while(True):
   _, frame capture.read()

   gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
   mirror = cv2.flip(gray, 1)
   cv2.imshow('livestream', mirror)

   if cv2.waitkey(1) == ord("q"):
       break

capture.release()
cv2.destroyAllWindows()