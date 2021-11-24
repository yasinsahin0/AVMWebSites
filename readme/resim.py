import cv2


img = cv2.imread("images/old/yag-duyuru.jpg")
img1 = cv2.resize(img,(700,400),interpolation=cv2.INTER_AREA)

img2 = cv2.imread("images/old/sabun-duyuru.jpg")
img2 = cv2.resize(img2,(700,400),interpolation=cv2.INTER_AREA)

img3 = cv2.imread("images/old/baharat-duyuru.jpg")
img3 = cv2.resize(img3,(700,400),interpolation=cv2.INTER_AREA)


cv2.imwrite("images/yag-resize.jpg",img1)
cv2.imwrite("images/sabun-resize.jpg",img2)
cv2.imwrite("images/baharat-resize.jpg",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
