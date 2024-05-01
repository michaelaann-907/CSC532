from PIL import Image
import io
import numpy as np
import os

"""
Using functions inbuilt into Pillow, we can easily see JPEG image compression through any filetype, as long as
the filetype is conversed to RGB, which we do in our compress_JPEG function.
"""


def compress_JPEG(inputImage, outputImage, imageQuality=85):
    """
    Function compresses any image type into the JPEG format using inbuilt functionality.
    :param inputImage: Image to be compressed.
    :param outputImage: Compressed image.
    :param imageQuality: Desired quality (1-100) of the resulting image.
    :return:
    """
    # Open the image file
    with Image.open(inputImage) as img:
        # Convert the image to RGB mode
        img = img.convert('RGB')
        with io.BytesIO() as buffer:
            img.save(buffer, 'JPEG', quality=imageQuality)
            compressed_img = Image.open(buffer)
            # Save the compressed image
            compressed_img.save(outputImage, 'JPEG')
        return outputImage


def decompress_JPEG(inputImage, outputImage):
    """
    This Function is less important for tests, but used input functionality to decompress our inbuilt compress function.
    :param inputImage: a compressed JPEG image
    :param outputImage: a decompressed JPEG image
    :return:
    """
    # Open the compressed image file we just compressed
    with Image.open(inputImage) as img:
        # Get the file format of the input image
        img_format = img.format
        # Save the image to the output path with the same format as input
        img.save(outputImage, img_format)

def get_image_properties(image_path):
    with Image.open(image_path) as img:
        image_array = np.array(img)
        shape = img.size
        dtype = image_array.dtype
        size = os.path.getsize(image_path)
        mean = np.mean(image_array)
        std = np.std(image_array)
    return shape, dtype, size, mean, std


def main():
    inputImage = 'Images/TestingImages/TI2.png'  # Path to the input image file
    compressedImage = 'Images/JPEG/CompressedTI2JPEG.png'

    original_shape, original_dtype, original_size, original_mean, original_std = get_image_properties(inputImage)


    # Compress the image
    compressedImage = compress_JPEG(inputImage, compressedImage)

    compressed_shape, compressed_dtype, compressed_size, compressed_mean, compressed_std = get_image_properties(compressedImage)

    # Decompress the image
    decompressedImage = 'Images/JPEG/DecompressedTI2JPEG.png'  # Path to save the decompressed image file
    decompress_JPEG(compressedImage, decompressedImage)



    # Print comparison information
    print("Original Image Properties:")
    print("Dimensions:", original_shape)
    print("Data type:", original_dtype)
    print("File size:", original_size, "bytes")
    print("Mean pixel value:", original_mean)
    print("Standard deviation:", original_std)
    print("\nCompressed Image Properties:")
    print("Dimensions:", compressed_shape)
    print("Data type:", compressed_dtype)
    print("File size:", compressed_size, "bytes")
    compression_ratio = original_size / compressed_size
    print("Compression ratio:", compression_ratio)
    print("Mean pixel value:", compressed_mean)
    print("Standard deviation:", compressed_std)


if __name__ == '__main__':
    main()
