import cv2
import numpy as np
import pywt
import os

def wavelet_compress(image_path, compression_ratio, save_path=None):
    # Load the image
    # Need to use IMREAD_COLOR for colored images
    # Need to use IMREAD_GRAYSCALE for black & white images
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)

    # Perform 2D Discrete Wavelet Transform (DWT)
    coeffs = pywt.dwt2(img, 'haar')

    # Apply thresholding to the wavelet coefficients
    threshold = np.percentile(np.abs(coeffs[0]), compression_ratio)
    compressed_coeffs = tuple(pywt.threshold(c, threshold, mode='soft') for c in coeffs)

    # Reconstruct the compressed image
    compressed_img = pywt.idwt2(compressed_coeffs, 'haar')

    # Resize the compressed image to fit within a reasonable display size
    scale_factor = min(1.0, 800.0 / compressed_img.shape[1], 600.0 / compressed_img.shape[0])
    compressed_img = cv2.resize(compressed_img, None, fx=scale_factor, fy=scale_factor)

    # Calculate compression ratio
    original_size = os.path.getsize(image_path)  # Original file size
    compressed_size = sum(c.nbytes for c in compressed_coeffs)  # Compressed file size
    compression_ratio = compressed_size / original_size * 100

    # Calculate mean pixel value and standard deviation for both original and compressed images
    original_mean = np.mean(img)
    compressed_mean = np.mean(compressed_img)
    original_std = np.std(img)
    compressed_std = np.std(compressed_img)

    # Save the compressed image if save_path is provided
    if save_path:
        cv2.imwrite(save_path, compressed_img)

    return compressed_img.astype(np.uint8), compression_ratio, img.shape, img.dtype, original_size, compressed_size, \
        original_mean, compressed_mean, original_std, compressed_std


# Example usage with save path:
image_path = 'Images/CI.png'
compression_ratio = 90  # Retain 90% of the most significant coefficients
save_path = 'Images/CompressedCIWavelet.png'  # Specify the path where you want to save the compressed image
compressed_img, compression_ratio, original_shape, original_dtype, original_size, compressed_size, \
    original_mean, compressed_mean, original_std, compressed_std = wavelet_compress(image_path, compression_ratio, save_path)




# Display original and compressed images
# Need to use IMREAD_COLOR for colored images
# Need to use IMREAD_GRAYSCALE for black & white images
original_img = cv2.imread(image_path, cv2.IMREAD_COLOR)
scale_factor = min(1.0, 800.0 / original_img.shape[1], 600.0 / original_img.shape[0])
original_img = cv2.resize(original_img, None, fx=scale_factor, fy=scale_factor)
cv2.imshow('Original Image', original_img)
cv2.imshow('Compressed Image', compressed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print comparison information
print("Original Image Properties:")
print("Dimensions:", original_shape)
print("Data type:", original_dtype)
print("File size:", original_size, "bytes")
print("Mean pixel value:", original_mean)
print("Standard deviation:", original_std)
print("\nCompressed Image Properties:")
print("Dimensions:", compressed_img.shape)
print("Data type:", compressed_img.dtype)
print("File size:", compressed_size, "bytes")
print("Compression ratio:", compression_ratio)
print("Mean pixel value:", compressed_mean)
print("Standard deviation:", compressed_std)
