# Evaluation of Steganography

This project presents the basic concepts, history, techniques, and evaluation of **steganography**, with a focus on **image steganography using the Least Significant Bit (LSB) technique**.

## About the Project

Steganography is the practice of hiding information inside another medium so that the existence of the hidden information is not easily noticed.

This project is based on the reference paper:

**View of Ancient and Modern Steganography**

The project covers both the historical development of steganography and modern digital techniques.

## Topics Covered

* Introduction to steganography
* Difference between cryptography and steganography
* Ancient steganography techniques
* Modern steganography
* Text steganography
* Image steganography
* Audio steganography
* Video steganography
* Protocol steganography
* LSB-based image steganography
* Steganalysis
* Security
* Capacity
* Image quality
* Advantages and disadvantages

## Practical Demonstration

The practical part demonstrates how a secret message can be embedded into an image by modifying the **Least Significant Bit (LSB)** of pixel values.

The basic process is:

```text
Cover Image + Secret Message
          ↓
      Embedding
          ↓
      Stego Image
          ↓
      Extraction
          ↓
    Secret Message
```

Only small changes are made to pixel values, so the resulting image can look very similar to the original image.

## Evaluation

The steganography technique can be evaluated using three main factors:

1. **Security** – How difficult it is to detect the hidden information.
2. **Capacity** – How much information can be hidden.
3. **Image Quality** – How much the image changes after embedding.

## Repository Contents

```text
presentation/
    Presentation PowerPoint
    Speaking Script PDF

reference/
    Reference paper

demo/
    Original carrier image
    Stego image
    Difference image

code/
    LSB steganography implementation
```

## Reference

The main reference used for this academic project is:

*View of Ancient and Modern Steganography*

## Purpose

This repository was created for academic learning and classroom presentation of steganography concepts and a practical image-based demonstration.
