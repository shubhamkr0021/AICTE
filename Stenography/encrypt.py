import cv2
import os

# Load the image
img = cv2.imread("pic.png")
if img is None:
    print("Error: Image not found.")
    exit()

# Get user inputs
msg = input("Enter secret message: ") + "\0"  # Add termination character
password = input("Enter a passcode: ")

# Validate message fits in the image
max_length = img.shape[0] * img.shape[1] * 3 // 3 
if len(msg) > max_length:
    print(f"Error: Message too long. Max allowed: {max_length}")
    exit()


char_to_int = {chr(i): i for i in range(256)}

# Embed message into pixels
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = char_to_int[char]
    n += 1
    m += 1
    z = (z + 1) % 3

# Save as PNG to avoid compression
cv2.imwrite("encryptedImage.png", img)
print("Image encrypted as 'encryptedImage.png'")

with open("encryption_info.txt", "w") as f:
    f.write(password)