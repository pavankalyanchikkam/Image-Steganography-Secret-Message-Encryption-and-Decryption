import cv2

def decrypt_message():
    # Load the encrypted image (PNG format now).
    image = cv2.imread("encryptedImage.png")
    if image is None:
        print("Error: Encrypted image not found. Please check the path.")
        return

    # Retrieve metadata (the message length and original passcode).
    try:
        with open("metadata.txt", "r") as meta:
            lines = meta.readlines()
            msg_length = int(lines[0].strip())
            original_key = lines[1].strip()
    except Exception as e:
        print("Error reading metadata:", e)
        return

    entered_key = input("Enter passcode for decryption: ")
    if entered_key != original_key:
        print("Access Denied: Incorrect passcode.")
        return

    # Create a reverse mapping from numeric values to characters.
    num_to_char = {i: chr(i) for i in range(255)}

    recovered = ""
    row, col, channel = 0, 0, 0
    for _ in range(msg_length):
        recovered += num_to_char[image[row, col, channel]]
        row += 1
        col += 1
        channel = (channel + 1) % 3

    print("Decrypted message:", recovered)

if __name__ == "__main__":
    decrypt_message()
