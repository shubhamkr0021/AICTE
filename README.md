# Steganography Project

This project demonstrates how to hide a secret message inside an image using steganography. The project consists of two Python scripts:

- **encrypt.py**: Embeds a secret message into an image.
- **decrypt.py**: Extracts the secret message from the encrypted image.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Encrypt a Message](#step-1-encrypt-a-message)
  - [Step 2: Decrypt the Message](#step-2-decrypt-the-message)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Limitations](#limitations)

## Requirements
- Python 3.x
- OpenCV (cv2) library
- An image file (e.g., `pic.png`) to use as the base for encryption

## Installation
### Install Python:
Download and install Python from [python.org](https://www.python.org/).

### Install OpenCV:
Install the OpenCV library using pip:
```bash
pip install opencv-python
```

### Download the Project Files:
Clone or download this repository to your local machine.

## Usage
### Step 1: Encrypt a Message
1. Place the image you want to use (e.g., `pic.png`) in the same directory as the scripts.
2. Run the encryption script:
   ```bash
   python encrypt.py
   ```
3. Enter the secret message and a passcode when prompted.

   The script will:
   - Embed the message into the image.
   - Save the encrypted image as `encryptedImage.png`.
   - Save the passcode in `encryption_info.txt`.

### Step 2: Decrypt the Message
1. Run the decryption script:
   ```bash
   python decrypt.py
   ```
2. Enter the passcode when prompted.

   The script will:
   - Verify the passcode.
   - Extract the message from the encrypted image.
   - Display the decrypted message.

## How It Works
### Encryption:
- The script converts each character of the message into its corresponding ASCII value.
- These values are embedded into the pixel values of the image (Red, Green, Blue channels).
- A termination character (`\0`) is added to mark the end of the message.

### Decryption:
- The script reads the pixel values from the encrypted image.
- It converts the pixel values back into characters using their ASCII values.
- The process stops when the termination character (`\0`) is encountered.

## Troubleshooting
**Error: Image not found**
- Ensure the image file (e.g., `pic.png`) is in the same directory as the scripts.

**Error: Message too long**
- Use a larger image or a shorter message. The image must have enough pixels to store the message.

**Error: Incorrect password**
- Ensure the correct passcode is entered during decryption.

**Decrypted message is incorrect**
- Ensure the image is saved in PNG format (not JPEG) to avoid compression artifacts.
- Verify the message contains only ASCII characters.

## Limitations
- The message must fit within the pixel capacity of the image.
- The image must be in PNG format to avoid compression artifacts.
- The passcode is stored in plaintext in `encryption_info.txt`, which is not secure for sensitive applications.


