from PIL import Image
import os

def png_compress(image_path, compression_level, save_path=None):
    # Open the image
    img = Image.open(image_path)

    # Compress the image as PNG with specified compression level
    img.save(save_path, format='PNG', optimize=True, quality=compression_level)

    # Get original and compressed file sizes
    original_size = os.path.getsize(image_path)
    compressed_size = os.path.getsize(save_path)

    # Calculate compression ratio
    compression_ratio = compressed_size / original_size * 100

    # Get original image properties
    original_shape = img.size
    original_dtype = img.mode

    # Open the compressed image to get its properties
    compressed_img = Image.open(save_path)
    compressed_shape = compressed_img.size
    compressed_dtype = compressed_img.mode

    return compression_ratio, original_size, compressed_size, original_shape, original_dtype, compressed_shape, compressed_dtype

# Example usage:
image_path = 'Images/TestingImages/TI2.png'
compression_level = 9  # Compression level (0-9), where 0 is no compression and 9 is maximum compression
save_path = 'Images/PNG/CompressedTI2PNG.png'  # Specify the path where you want to save the compressed image
compression_ratio, original_size, compressed_size, original_shape, original_dtype, compressed_shape, compressed_dtype = png_compress(image_path, compression_level, save_path)

# Print compression information
print("Original File Size:", original_size, "bytes")
print("Compressed File Size:", compressed_size, "bytes")
print("Compression Ratio:", compression_ratio, "%")

# Print comparison information
print("\nOriginal Image Properties:")
print("Dimensions:", original_shape)
print("Data type:", original_dtype)
print("File size:", original_size, "bytes")
print("\nCompressed Image Properties:")
print("Dimensions:", compressed_shape)
print("Data type:", compressed_dtype)
print("File size:", compressed_size, "bytes")
print("Compression ratio:", compression_ratio, "%")