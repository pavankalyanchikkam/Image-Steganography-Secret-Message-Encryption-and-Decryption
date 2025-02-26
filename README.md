# Image Steganography: Secret Message Encryption and Decryption

This project demonstrates a simple image-based steganography technique using Python and OpenCV. It was developed during the AICTE-IBM internship and showcases a basic method for embedding a secret message within an image file and retrieving it later using a passcode.

## Table of Contents
- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Overview
This project consists of two separate Python scripts:
1. **encryption.py**: Reads an input image, embeds a secret message into the image pixel values, and saves the modified image in PNG format. It also creates a metadata file that stores the length of the secret message and a passcode.
2. **decryption.py**: Reads the encrypted image and the metadata file, then retrieves and prints the secret message if the correct passcode is provided.

## Project Structure
