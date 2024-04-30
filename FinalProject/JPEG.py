from PIL import Image
import io

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


def decompress_JPEG(inputImage, outputImage):
    """
    This Function is less important for tests, but used input functionality to decompress our inbuilt compress function.
    :param inputImage: a compressed JPEG image
    :param outputImage: a decompressed JPEG image
    :return:
    """
    # Open the compressed image file we just compressed
    with Image.open(inputImage) as img:
        # Save the image to the output path
        img.save(outputImage, 'JPEG')


def main():
    inputImage = 'mutpyInstallCommand.png'  # Path to the input image file
    compressedImage = 'compressed.jpg'

    # Compress the image
    compress_JPEG(inputImage, compressedImage)

    # Decompress the image
    decompressedImage = 'decompressed.jpg'  # Path to save the decompressed image file
    decompress_JPEG(compressedImage, decompressedImage)


if __name__ == '__main__':
    main()
