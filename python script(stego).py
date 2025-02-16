import cv2
import os
import string

img = cv2.imread("doggie.jpg") # Replace with the correct image path

msg = input("Enter secret message: ") #enter the message that wants to be embedded
password = input("Enter a passcode: ") #enter the encryption password
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(msg)): #encyption technique
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage(3).jpg", img)
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ") #decryption technique
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message: ", message)
else:
    print("YOU ARE NOT autheriozed to open this ")
