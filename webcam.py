import cv2

cap = cv2.VideoCapture(0)

# load cascade file into a variable
cascade = cv2.CascadeClassifier("public/haarcascade_frontalface_default.xml")


while True:
    success,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow("webcam",frame)
        if cv2.waitKey(1) & 0xFF ==ord("s"):
            break

cap.release()