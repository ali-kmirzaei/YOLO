import math
import cv2 as cv
import numpy as np
import imutils


def find_degree(src):
    # Edge detection
    dst = cv.Canny(src, 50, 200, None, 3)
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    # Standard Hough Line Transform
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)
    # Draw the lines
    degree = 0
    # print(lines)
    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
            pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
            angle = np.arctan2(pt2[1]-pt1[1], pt2[0]-pt1[0]) * 180. /np.pi
            angle_abs = abs(angle)
            # print(angle)
            if angle_abs < 45:
                cv.line(cdst, pt1, pt2, (0,0,255), 3, cv.LINE_AA)

                if angle_abs > degree:
                    degree = angle
    else:
        return "Please insert a better image!"

    while cv.waitKey(1) != ord('0'):
        cv.imshow("lines", cdst)

    # print(degree)
    if degree > 80:
        return 0
    return degree

def rotate(src, degree):
    rotated = imutils.rotate(src, degree)
    while cv.waitKey(1) != ord('0'):
        cv.imshow("Rotated", rotated)
    return rotated

