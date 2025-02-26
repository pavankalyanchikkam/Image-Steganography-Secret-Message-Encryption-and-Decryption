import cv2
import os

def encrypt_message():
    # Load the base image (ensure 'mypic.jpg' is in the same folder)
    image = cv2.imread("mypic.jpg")
    if image is None:
        print("Error: Image file not found. Please check the path.")
        return

    secret = input("Enter your secret message: ")
    key = input("Enter a passcode: ")

    # Create mapping dictionaries for conversion between characters and their numeric values.
    char_to_num = {chr(i): i for i in range(255)}
    
    # Embed each character into a pixel value.
    row, col, channel = 0, 0, 0
    for ch in secret:
        image[row, col, channel] = char_to_num[ch]
        row += 1
        col += 1
        channel = (channel + 1) % 3

    # Save the encrypted image in PNG (lossless format).
    cv2.imwrite("encryptedImage.png", image)
    os.system("start encryptedImage.png")  # For Windows; adjust if needed

    # Write metadata (message length and passcode) to a file for later decryption.
    with open("metadata.txt", "w") as meta:
        meta.write(f"{len(secret)}\n{key}")

if __name__ == "__main__":
    encrypt_message()
