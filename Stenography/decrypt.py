import cv2

img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Read password from file
try:
    with open("encryption_info.txt", "r") as f:
        stored_password = f.read().strip()
except FileNotFoundError:
    print("Error: Run encryption first.")
    exit()

# Verify password
user_password = input("Enter passcode for decryption: ")
if user_password != stored_password:
    print("Authentication failed.")
    exit()

# Create decoding dictionary
int_to_char = {i: chr(i) for i in range(256)}

message = ""
n, m, z = 0, 0, 0
while True:
    try:
        value = img[n, m, z]
        char = int_to_char[value]
        if char == "\0":  # Stop at termination character
            break
        message += char
        n += 1
        m += 1
        z = (z + 1) % 3
    except IndexError:
        break  

print("Decrypted message:", message)