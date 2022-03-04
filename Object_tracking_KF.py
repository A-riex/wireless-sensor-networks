import numpy as np
import cv2
from Kalmanfilter import KalmanFilter



kf = KalmanFilter()
img = cv2.imread("cloudy_sky.jpg")
cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.resizeWindow('img', 1000,600)

ball_position1 = [(4, 300), (61, 256), (116, 214), (170,180), (225,148), (279, 120), (332, 97),
                (383,80), (434, 66), (484, 55), (535,49) , (586,49), (634,50), (683, 58),
                (731,69), (778,82), (824,101), (870,124), (917, 148), (962, 169),
                (1006,212), (1051,249), (1093, 298)]

for pt in ball_position1:
    cv2.circle(img, pt, 20,(0, 20, 220), -1)
    predicted = kf.predict(pt[0], pt[1])

    cv2.circle(img, predicted, 15, (20, 220, 0), -1)

# for i in range(10):
#     predicted = kf.predict(predicted[0], predicted[1])
#     cv2.circle(img, predicted, 15, (20, 200, 0), 4)



cv2.imshow("img", img)
cv2.waitKey(0)

