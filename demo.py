from curses import color_content
from turtle import color
import cv2 as cv
from cv2 import cvtColor
import numpy as np


img = np.zeros((512,512,3), np.uint8)

cv.line(img,(0,0),(511,511),(255,0,0),5)
cvtColor(all, color_content)