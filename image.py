import cv2

# load cascade file into a variable
face_xml = cv2.CascadeClassifier("public/haarcascade_frontalface_default.xml")

# read image
img = cv2.imread("public/multiple_faces.png")

# convert RGB to gray
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# the thing what we want to detect
detect = face_xml.detectMultiScale(img_gray,1.1,4)

# bounding box
for (x,y,w,h) in detect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

cv2.imshow("face detect", img)
cv2.waitKey(0)
