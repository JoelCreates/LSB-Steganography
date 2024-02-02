# Overview
This project presents a sophisticated steganography tool implemented in Python, utilising the Least Significant Bit (LSB) technique. The tool capitalises on the characteristic end-of-file marker (FFD9) in JPEG images to append hidden data. This approach enables the embedding of various forms of data, including text, executables, and even entire images, without perceptible changes to the host image. An intuitive graphical user interface (GUI) facilitates the injection and extraction of hidden content, maintaining the secrecy and integrity of the data.

# Features
- Data Embedding: Embed text, executables, or images into JPEG files.
- Data Extraction: Extract the embedded data from the modified image without leaving any trace.
- Imperceptibility: Ensures that changes made to the host image are visually indiscernible.
- User-Friendly GUI: Easy-to-use interface for embedding and extracting data seamlessly.

# Installation
## Prerequisites
- Python 3.x
- Required Python libraries: [List any specific libraries or frameworks used]

## Setup
Clone the repository:
```git clone [repository URL]```

## Install dependencies:
```pip install -r requirements.txt```

# Usage
1. Launch the Application: Run the GUI application through the Python script.
2. Embed Data: Select an image and choose the type of data (text, executable, or another image) to embed.
3. Extract Data: Open a previously modified image to extract the hidden data.

# How It Works
- End-of-File Marker Exploitation: Utilises the JPEG EOF marker (FFD9) to append data without affecting the image display.
Contributing
