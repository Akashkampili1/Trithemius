# Steganographic Framework with AES-256 Encryption

![Team Phoenix](https://img.shields.io/badge/Created%20by-Team%20Phoenix-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

This Python script provides a comprehensive Steganographic Framework with AES-256 Encryption. The framework supports hiding information within various media types such as text, images, audio, and videos. It employs the AES-256 encryption algorithm to secure the hidden data.

![](trithemius.png)

## Features

- Text Encryption and Decryption using AES-256
- Image Steganography (LSB method)
- Audio Steganography
- Video Steganography

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - PIL (Pillow)
  - stegano
  - pyaes
  - opencv-python
  - numpy

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Akashkampili1/TrithemiusCli
   ```

2. Navigate to the project directory:

   ```bash
   cd TrithemiusCli
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Requirements

Make sure to install the required dependencies by running:

```bash
pip install -r requirements.txt
```

- pyaes==1.6.1
- stegano==0.11.2
- Pillow==10.1.0
- numpy==1.26.2
- opencv-python==4.8.1.78

## Usage

1. Run the script and choose the desired operation from the main menu.
2. For text encryption/decryption, enter the text when prompted.
3. For image, audio, or video operations, provide the necessary file names and follow the instructions.


### Encryption

1. **Text Encryption:**
   - You can encrypt text using AES-256 encryption. The encrypted text will be displayed in hexadecimal format.

2. **Choose Parameter:**
   - After entering the text, you can choose the type of media to hide the encrypted text.
   - Options include Image, Audio, and Video.

3. **Image Encryption:**
   - Specify the image filename (with extension) and the data to be encoded.
   - The new image will be saved with the specified name.

4. **Audio Encryption:**
   - Specify the audio filename (with extension) and the text to be encoded.
   - The modified audio file will be saved.

5. **Video Encryption:**
   - Specify the video filename (with extension) and enter the message to be encoded.
   - The output will be saved as "Embedded_Video.mp4."

### Decryption

1. **Choose Parameter:**
   - After selecting decryption, you can choose the type of media from which to extract hidden information.
   - Options include Text, Image, Audio, and Video.

2. **Text Decryption:**
   - Enter the encrypted text in hexadecimal format.
   - The decrypted text will be displayed.

3. **Image Decryption:**
   - Specify the image filename (with extension) from which to extract hidden text.
   - The decoded text will be displayed.

4. **Audio Decryption:**
   - Specify the audio filename (with extension) from which to extract hidden text.
   - The decoded text will be displayed.

5. **Video Decryption:**
   - Specify the video filename (with extension) from which to extract hidden text.
   - The decoded text will be displayed.


## Credits

This framework is created by Team Phoenix.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
