# 도구 불러오기(이미지 처리도구, 수학도구)
import cv2
import numpy as np

# sample.jpg 이미지 로드하기
image = cv2.imread('sample.jpg')

# RGB에서 HSV(색상,채도,명도) 변환하기
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색 범위 기준 정하기
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 빨간색만 통과하는 거름망 만들기
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = mask1 + mask2 # 두 개의 마스크를 합침

# 원본 이미지에서 빨간색 부분만 남기기
result = cv2.bitwise_and(image, image, mask=mask)

# 결과 이미지 출력
cv2.imshow('Original', image)
cv2.imshow('Red Filtered', result)
cv2.waitKey(0)
cv2.destroyAllWindows()