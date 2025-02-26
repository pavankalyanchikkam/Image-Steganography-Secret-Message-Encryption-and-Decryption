# Image Steganography: Secret Message Encryption and Decryption

This project demonstrates a simple image-based steganography technique using Python and OpenCV. It was developed during the AICTE-IBM internship and showcases a basic method for embedding a secret message within an image file and retrieving it later using a passcode.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)

## Overview 🚀

- **Purpose**:  
  Develop a robust and user-friendly tool for embedding and extracting secret messages within images using Python, OpenCV, and Tkinter. This project was created during the AICTE-IBM internship to showcase practical steganography techniques.

- **Key Features**:  
  - 🔒 **Secure Messaging**: Hides sensitive data within lossless PNG images to maintain data integrity.  
  - ⚙️ **Modular Architecture**: Clean separation of encryption, decryption, and GUI components for easy maintenance and scalability.  
  - 🖥️ **Intuitive GUI**: User-friendly interface built with Tkinter simplifies the process of encrypting and decrypting messages.  
  - 🔄 **Extensibility**: Structured design that facilitates future enhancements, such as advanced cryptographic methods and support for additional media formats.

## Project Structure 📁

.
├── encryption.py        🔐 Contains the logic for embedding secret messages into images.
├── decryption.py        🔍 Handles the extraction of hidden messages from images.
├── gui.py               🖥️ Provides a graphical user interface using Tkinter.
├── mypic.png            🖼️ Example cover image (recommended: use a lossless format like PNG).
├── metadata.txt         📝 Auto-generated file storing message length and passcode.
└── encryptedImage.png   📷 Output image with the embedded secret message.
