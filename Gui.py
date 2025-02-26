"""
gui.py
------
Provides a Tkinter-based graphical user interface that allows
users to:
    - Select a cover image and embed a secret message.
    - Select an encrypted image and retrieve the hidden message.
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import os

import cv2
from encryption import encrypt_image
from decryption import decrypt_image

# Global file path variables
cover_image_path = None
encrypted_image_path = None

def select_cover_image():
    global cover_image_path
    path = filedialog.askopenfilename(
        title="Select Cover Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if path:
        cover_image_path = path
        lbl_cover.config(text=os.path.basename(path))

def select_encrypted_image():
    global encrypted_image_path
    path = filedialog.askopenfilename(
        title="Select Encrypted Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp")]
    )
    if path:
        encrypted_image_path = path
        lbl_encrypted.config(text=os.path.basename(path))

def perform_encryption():
    if not cover_image_path:
        messagebox.showerror("Error", "Please choose a cover image first.")
        return
    
    secret_msg = entry_secret.get()
    pwd_enc = entry_pass_enc.get()
    
    if not secret_msg or not pwd_enc:
        messagebox.showerror("Error", "Please enter both secret message and passcode.")
        return

    try:
        encrypt_image(cover_image_path, secret_msg, pwd_enc)
        messagebox.showinfo("Success", "Encryption successful!\nSaved as 'encryptedImage.png'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def perform_decryption():
    if not encrypted_image_path:
        messagebox.showerror("Error", "Please choose an encrypted image first.")
        return
    
    pwd_dec = entry_pass_dec.get()
    if not pwd_dec:
        messagebox.showerror("Error", "Please enter the passcode for decryption.")
        return

    try:
        decrypted_text = decrypt_image(encrypted_image_path, pwd_dec)
        text_decrypted.delete("1.0", tk.END)
        text_decrypted.insert(tk.END, decrypted_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# --------------------- GUI Layout ---------------------
window = tk.Tk()
window.title("Image Steganography")

# ========== Encryption Frame ==========
frame_enc = tk.LabelFrame(window, text="Encryption", padx=10, pady=10)
frame_enc.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")

btn_cover = tk.Button(frame_enc, text="Load Cover Image", command=select_cover_image)
btn_cover.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lbl_cover = tk.Label(frame_enc, text="No file selected", width=30, anchor="w")
lbl_cover.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_enc, text="Secret Message:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
entry_secret = tk.Entry(frame_enc, width=30)
entry_secret.grid(row=1, column=1, padx=5, pady=2)

tk.Label(frame_enc, text="Passcode:").grid(row=2, column=0, padx=5, pady=2, sticky="w")
entry_pass_enc = tk.Entry(frame_enc, width=30, show="*")
entry_pass_enc.grid(row=2, column=1, padx=5, pady=2)

btn_encrypt = tk.Button(frame_enc, text="Encrypt", command=perform_encryption)
btn_encrypt.grid(row=3, column=0, columnspan=2, pady=10)

# ========== Decryption Frame ==========
frame_dec = tk.LabelFrame(window, text="Decryption", padx=10, pady=10)
frame_dec.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")

btn_encrypted = tk.Button(frame_dec, text="Load Encrypted Image", command=select_encrypted_image)
btn_encrypted.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lbl_encrypted = tk.Label(frame_dec, text="No file selected", width=30, anchor="w")
lbl_encrypted.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_dec, text="Passcode:").grid(row=1, column=0, padx=5, pady=2, sticky="w")
entry_pass_dec = tk.Entry(frame_dec, width=30, show="*")
entry_pass_dec.grid(row=1, column=1, padx=5, pady=2)

btn_decrypt = tk.Button(frame_dec, text="Decrypt", command=perform_decryption)
btn_decrypt.grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(frame_dec, text="Decrypted Message:").grid(row=3, column=0, padx=5, pady=2, sticky="nw")
text_decrypted = tk.Text(frame_dec, width=30, height=5)
text_decrypted.grid(row=3, column=1, padx=5, pady=2)

window.mainloop()
