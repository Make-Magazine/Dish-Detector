import sys
import cv

size=(640,480)
hsv_frame = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
thresholded = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)
thresholded2 = cv.CreateImage(size, cv.IPL_DEPTH_8U, 1)

def detect_and_draw( img ):

    storage = cv.CreateMat(img.width, 1, cv.CV_32FC3)      
    cv.CvtColor(img,hsv_frame, cv.CV_BGR2GRAY)
    cv.HoughCircles(hsv_frame, storage, cv.CV_HOUGH_GRADIENT, 1, thresholded.height/4, 100, 40, 20, 200)
    Radius = 0
    x = 0
    y = 0

    for i in range(storage.width - 1):

            print i
            if storage[i,2] >Radius:
                Radius = storage[i, 2]
                x = storage[i, 0]
                y = storage[i, 1]
                center=(x,y)
                print x,y,Radius
            else:
                print "no circle"

                cv.Circle(thresholded, center,Radius, (0, 0, 255), 3, 8, 0)


    cv.ShowImage( "result", thresholded)

if __name__ == '__main__':

	img = cv.LoadImage("test3.jpg")
        detect_and_draw(img)
        cv.WaitKey(0)
