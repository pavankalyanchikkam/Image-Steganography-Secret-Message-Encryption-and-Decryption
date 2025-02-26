"""
encryption.py
-------------
Contains the core logic to embed a secret message into an image
using a basic steganographic technique. Recommended to use
lossless formats (e.g., PNG) to preserve pixel data.
"""

import cv2

# Create dictionaries for character <-> numeric mapping
CHAR_MAP = {chr(i): i for i in range(256)}
NUM_MAP = {i: chr(i) for i in range(256)}

def encrypt_image(
    cover_path: str,
    secret_message: str,
    passcode: str,
    output_image: str = "encryptedImage.png",
    metadata_file: str = "metadata.txt"
) -> None:
    """
    Embeds the secret_message into the cover image at cover_path
    and saves the result as output_image. Writes the passcode and
    message length to metadata_file.
    """

    # Load the cover image
    image = cv2.imread(cover_path)
    if image is None:
        raise FileNotFoundError(f"Could not open image at {cover_path}")

    # Basic dimension checks
    rows, cols, channels = image.shape
    if len(secret_message) * 3 > rows * cols:
        raise ValueError("Message too long to fit in the provided image.")

    # Embed the message
    r, c, chan = 0, 0, 0
    for ch in secret_message:
        image[r, c, chan] = CHAR_MAP[ch]
        r += 1
        c += 1
        chan = (chan + 1) % channels

    # Save encrypted image
    cv2.imwrite(output_image, image)

    # Write metadata
    with open(metadata_file, "w", encoding="utf-8") as meta:
        meta.write(f"{len(secret_message)}\n{passcode}\n")

    print(f"Encryption complete. Encrypted image saved as: {output_image}")
    print(f"Metadata saved to: {metadata_file}")

# Example usage (Uncomment to run standalone):
# if __name__ == "__main__":
#     cover = "mypic.png"
#     msg = "HelloWorld"
#     pwd = "abc123"
#     encrypt_image(cover, msg, pwd)
