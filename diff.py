import sys
import cv
import numpy as np

def main():
  im = cv.LoadImage(sys.argv[1])
  bg = cv.LoadImage("test3.jpg")

  gray = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_8U, 1)
  graybg = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_8U, 1)
  dest = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_8U, 1)

  cv.CvtColor(im, gray, cv.CV_BGR2GRAY)
  cv.CvtColor(bg, graybg, cv.CV_BGR2GRAY)

  cv.Sub(gray, graybg, dest)

  cv.Canny(dest, gray, 100, 100 / 2, 3)

  cv.ShowImage('Circles', gray)
  cv.WaitKey(0)

if __name__ == '__main__':
  main()
