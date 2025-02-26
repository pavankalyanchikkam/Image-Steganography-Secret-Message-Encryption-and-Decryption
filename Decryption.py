"""
decryption.py
-------------
Contains the core logic to extract a secret message from an
encrypted image, using metadata to determine message length
and passcode verification.
"""

import cv2

# Same mapping dictionaries (must match encryption.py)
CHAR_MAP = {chr(i): i for i in range(256)}
NUM_MAP = {i: chr(i) for i in range(256)}

def decrypt_image(
    encrypted_path: str,
    user_passcode: str,
    metadata_file: str = "metadata.txt"
) -> str:
    """
    Extracts and returns the hidden message from the image at
    encrypted_path if user_passcode matches the stored passcode
    in metadata_file. Raises exceptions on error or mismatch.
    """

    # Load the encrypted image
    image = cv2.imread(encrypted_path)
    if image is None:
        raise FileNotFoundError(f"Could not open image at {encrypted_path}")

    # Read metadata for message length and original passcode
    try:
        with open(metadata_file, "r", encoding="utf-8") as meta:
            lines = meta.readlines()
            msg_length = int(lines[0].strip())
            original_passcode = lines[1].strip()
    except Exception as e:
        raise IOError("Failed to read metadata file") from e

    if user_passcode != original_passcode:
        raise PermissionError("Incorrect passcode. Access denied.")

    # Extract the hidden message
    r, c, chan = 0, 0, 0
    recovered = []

    rows, cols, channels = image.shape
    for _ in range(msg_length):
        if r >= rows or c >= cols:
            raise ValueError("Decryption exceeded image boundaries.")
        val = image[r, c, chan]
        recovered.append(NUM_MAP[val])
        r += 1
        c += 1
        chan = (chan + 1) % channels

    hidden_text = "".join(recovered)
    return hidden_text

# Example usage (Uncomment to run standalone):
# if __name__ == "__main__":
#     enc_path = "encryptedImage.png"
#     pwd = "abc123"
#     message = decrypt_image(enc_path, pwd)
#     print("Decrypted Message:", message)
