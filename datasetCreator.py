import cv2

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)

userID = raw_input("Enter user ID: ")
sampleNum = 0

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataset/user." + str(userID) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.waitKey(100)

    cv2.imshow('Face', img)
    cv2.waitKey(1)

    if sampleNum >= 10:
        break

cam.release()
cv2.destroyAllWindows()
