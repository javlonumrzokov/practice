import cv2

image = cv2.imread("cat.jpg")
# cv2.imshow("CAT", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print("shape", image.shape)  # natija : height, width, number of channels(RGB)
print("Height", image.shape[0])
print("Width", image.shape[1])
print("Channels", image.shape[2])  # BGR Blue Green Red in OPENCV da

(b, g, r) = image[100, 70]
print("Blue:", b, "Green:", g, "Red:", r)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("CAT", gray)
# cv2.waitKey(0)

resized = cv2.resize(gray, (300, 300))
# print("shape", resized.shape)
# cv2.imshow("CAT", resized)
# cv2.waitKey(0)

cropped = gray[100:350, 150:400]
# print("shape", cropped.shape)
# cv2.imshow("CAT", cropped)
# cv2.waitKey(0)

rotated = cv2.rotate(gray, cv2.ROTATE_180)
# cv2.imshow("CAT", rotated)
# cv2.waitKey(0)

flipped = cv2.flip(gray, 1)
# cv2.imshow("CAT", flipped)
# cv2.waitKey(0)

cv2.imwrite("flipped_gray_cat.jpg", flipped)
flipped_gray_cat = cv2.imread("flipped_gray_cat.jpg")
cv2.imshow("CAT", flipped_gray_cat)
cv2.waitKey(0)
