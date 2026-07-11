# 도구 불러오기(이미지 처리도구, 수학도구)
import cv2
import numpy as np



# sample.jpg 이미지 로드하기
image = cv2.imread('sample.jpg')



# RGB에서 HSV(색상,채도,명도) 변환하기
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)



#빨간색 처리
min_red1 = np.array([0, 100, 100])
max_red1 = np.array([15, 255, 255])
min_red2 = np.array([165, 100, 100])
max_red2 = np.array([180, 255, 255])

red_mask1 = cv2.inRange(hsv, min_red1, max_red1)
red_mask2 = cv2.inRange(hsv, min_red2, max_red2)
red_mask = red_mask1 + red_mask2

red_result = cv2.bitwise_and(image, image, mask=red_mask)




# 초록색 처리
min_green = np.array([40, 100, 100])
max_green = np.array([70, 255, 255])

green_mask = cv2.inRange(hsv, min_green, max_green)

green_result = cv2.bitwise_and(image, image, mask=green_mask)



# 파란색 처리
min_blue = np.array([100, 100, 100])
max_blue = np.array([130, 255, 255])

blue_mask = cv2.inRange(hsv, min_blue, max_blue)

blue_result = cv2.bitwise_and(image, image, mask=blue_mask)



# 결과 이미지 출력
cv2.imshow('Original', image)
cv2.imshow('Red Filtered', red_result)
cv2.imshow('Green Filtered', green_result)
cv2.imshow('Blue Filtered', blue_result)
cv2.waitKey(0)
cv2.destroyAllWindows()