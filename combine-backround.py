from rembg import remove
from PIL import Image
import cv2


original_img_path = "images/IMG_5358.png"

input = Image.open(original_img_path)
output = remove(input)
output.save("combine/remove_bg.png")

mask_img_path = "combine/remove-bg.png"
mask_a = cv2.imread(mask_img_path, cv2.IMREAD_UNCHANGED)
mask_a = mask_a[:, :, 3]
cv2.imwrite("combine/mask.png", mask_a)

gray_img = cv2.imread(original_img_path)
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_BGR2GRAY)
gray_img = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
cv2.imwrite("combine/gray.png", gray_img)

gray_img_path = "images/gray.png"
mask_path = "images/mask.png"
paste_img = Image.open(gray_img_path)
base_img = Image.open(original_img_path)
mask = Image.open(mask_path)
im = Image.composite(paste_img, base_img, mask)
im.save("combine/composite.png")
