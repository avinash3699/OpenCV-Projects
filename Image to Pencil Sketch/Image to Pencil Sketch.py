import cv2
import os

inputImagePath = input("Enter the image's name with it's absolute path ").strip()

try:
    image = cv2.imread(inputImagePath)
    
    image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    image_inversion = cv2.bitwise_not(image_grayscale)
    
    image_blurred = cv2.GaussianBlur(image_inversion, (21, 21), sigmaX = 0, sigmaY = 0)
    
    final_image = cv2.divide(image_grayscale, 255 - image_blurred, scale = 256)
    
    filename = os.path.splitext(os.path.basename(inputImagePath))[0]
    
    cv2.imwrite("outputs\%s-sketched.jpg" % filename, final_image)
    
    print("Check the output folder for your sketched image!")

except:
    print("Sorry :/ We cannot process your image. It may be due to one of the following reasons.")
    print("1. Your image's path is wrong.")
    print("2. Image's name or extension is wrong.")
    print("3. The image does not exists.")