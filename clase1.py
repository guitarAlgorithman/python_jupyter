import cv2
import imutils

#Cargo las imagenes de referencias
original=cv2.imread("./images/20000a.jpg")
camara=cv2.VideoCapture(0)


while(True):
    ret,frame=camara.read()
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1):
        break
camara.release()
cv2.destroyAllWindows()