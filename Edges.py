import cv2

def Edges(img):
    simg = cv2.medianBlur(img, 5)
    # ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    # th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    th = cv2.adaptiveThreshold(simg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return cv2.Canny(th, 50, 200, None, 3)
