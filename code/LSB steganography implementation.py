from PIL import Image

def encode_image(input_image, output_image, message):
    image = Image.open(input_image).convert("RGB")
    pixels = list(image.getdata())

    message += "###END###"
    binary = ''.join(format(ord(char), '08b') for char in message)

    if len(binary) > len(pixels) * 3:
        raise ValueError("Message is too large for this image.")

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel
        values = [r, g, b]

        for i in range(3):
            if bit_index < len(binary):
                values[i] = (values[i] & ~1) | int(binary[bit_index])
                bit_index += 1

        new_pixels.append(tuple(values))

        if bit_index >= len(binary):
            new_pixels.extend(pixels[len(new_pixels):])
            break

    Image.new("RGB", image.size).putdata(new_pixels)