from PIL import Image
import heapq
import time

'''
Program credited to samvotter on GitHub: https://github.com/samvotter

Updated to better understand the performance of the Huffman Image Compression Algorithm.

Things this program does:
    1. Loads an image and pixel data as an object of the Picture class
    2. Creates a dictionary of [R,G,B: frequency] for each pixel
    3. Creates a heap of dictionary elements
    4. Recursively merges heap elements into a huff tree
    5. Traverses huff tree to generated encoded strings
    6. Refills dictionary with [R,G,B: encoded strings]
    7. Produces text file containing compressed image data

'''


from PIL import Image
import heapq
import time
import os

class HeapNode:
    def __init__(self, rgb, freq):
        self.rgb = rgb
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False
        if not isinstance(other, HeapNode):
            return False
        return self.freq == other.freq


class Picture:
    def __init__(self, name):
        self.name = name[:-4]
        self.dict = {}
        self.data = []
        self.heap = []
        self.encode = {}
        self.decode = {}
        self.res_image = []
        self.receive = []

        self.img = Image.open(name)
        self.width, self.height = self.img.size
        self.px = self.img.load()
    def load_data(self):
        for row in range(self.width):
            for col in range(self.height):
                pixel_value = self.px[row, col]
                if pixel_value not in self.dict:
                    self.dict[pixel_value] = 1
                else:
                    self.dict[pixel_value] += 1

    def display(self, img_object):
        img_object.show()

    def get_data(self):
        return self.data

    def get_dict(self):
        return self.dict

    def make_heap(self):
        for key in self.dict:
            if self.dict[key] > 0:
                node = HeapNode(key, self.dict[key])
                heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while len(self.heap) > 1:
            node_one = heapq.heappop(self.heap)
            node_two = heapq.heappop(self.heap)

            merge = HeapNode(None, node_one.freq + node_two.freq)
            merge.left = node_one
            merge.right = node_two

            heapq.heappush(self.heap, merge)

    def heaporder(self, root, buffer):
        if root:
            self.res_image.append([root.rgb, root.freq, buffer])
            buffer += "0"
            self.heaporder(root.left, buffer)
            buffer = buffer[:-1]
            buffer += "1"
            self.heaporder(root.right, buffer)

    def create_compression_keys(self):
        for item in self.res_image:
            if item[0]:
                self.encode[item[0]] = item[2]
                self.decode[item[2]] = item[0]

    def writeout(self):
        with open(self.name + "_compressed.txt", 'w') as out:
            for pix in self.data:
                out.write(self.encode[pix] + "\n")
        # Save the compressed image using Pillow
        # Save the compressed image using Pillow
        compressed_img = Image.new('P', (self.width, self.height))
        pixels = compressed_img.load()
        index = 0
        for row in range(self.width):
            for col in range(self.height):
                pixels[row, col] = self.px[row, col]  # Use original pixel data for the compressed image
                index += 1
        compressed_img.save(self.name + "_compressed.png", "PNG")
    def readin(self):
        file_path = self.name + "_compressed.txt"
        print("Reading compressed data from:", file_path)
        with open(file_path, 'r') as ins:
            lines = ins.read().splitlines()
            print("Number of lines read:", len(lines))
            print("First few lines:", lines[:5])  # Print the first few lines for inspection
            self.receive = lines





    def create_new_image(self):
        if not self.receive:
            print("No data received for decompression.")
            return

        decompressed = Image.new('RGB', (self.width, self.height))
        pixels = decompressed.load()
        index = 0
        for row in range(self.width):
            for col in range(self.height):
                if index < len(self.receive):  # Check if index is within bounds
                    pixels[row, col] = self.decode[self.receive[index]]
                    index += 1
        decompressed.save(self.name + "_decompressed.png", "PNG")  # Save as PNG format
        self.display(decompressed)



def main():
    filename = input("Filename:")  # Filename must be in the same root as Huffman
    original_img = Image.open(filename)
    original_shape = original_img.size
    original_dtype = original_img.mode
    original_size = os.path.getsize(filename)
    original_mean = sum(original_img.getdata()) / (len(original_img.getdata()))
    original_std = (sum((pix - original_mean) ** 2 for pix in original_img.getdata()) / (original_shape[0] * original_shape[1])) ** 0.5

    print("Original Image Properties:")
    print("Dimensions:", original_shape)
    print("Data type:", original_dtype)
    print("File size:", original_size, "bytes")
    print("Mean pixel value:", original_mean)
    print("Standard deviation:", original_std)

    currentImage = Picture(filename)
    print("Thinking . . .")
    startTime = time.time()
    currentImage.load_data()
    print("Image size:", len(currentImage.data))
    currentImage.make_heap()
    currentImage.merge_nodes()
    currentImage.heaporder(currentImage.heap[0], "")
    currentImage.create_compression_keys()
    endTime = time.time()
    duration_c = (endTime - startTime) * 1000
    print("Compression:", duration_c, "milliseconds.")
    currentImage.writeout()
    currentImage.readin()

    # Load the compressed image
    compressed_img = Image.open(currentImage.name + "_compressed.png").convert('P')
    compressed_shape = compressed_img.size
    compressed_dtype = compressed_img.mode
    compressed_size = os.path.getsize(currentImage.name + "_compressed.png")
    compressed_mean = sum(pixel for pixel in compressed_img.getdata()) / (compressed_shape[0] * compressed_shape[1])
    compressed_std = (sum((pix - compressed_mean) ** 2 for pix in compressed_img.getdata()) / (compressed_shape[0] * compressed_shape[1])) ** 0.5
    compression_ratio = original_size / compressed_size

    print("\nCompressed Image Properties:")
    print("Dimensions:", compressed_shape)
    print("Data type:", compressed_dtype)
    print("File size:", compressed_size, "bytes")
    print("Compression ratio:", compression_ratio)
    print("Mean pixel value:", compressed_mean)
    print("Standard deviation:", compressed_std)


    # Iterate over the compressed image data and print the type of each pixel only once
    printed_types = set()
    for pix in compressed_img.getdata():
        pixel_type = type(pix)
        if pixel_type not in printed_types:
            print("Type of pixel:", pixel_type)
            printed_types.add(pixel_type)

    start_d = time.time()
    currentImage.create_new_image()
    end_d = time.time()
    duration_d = (end_d - start_d) * 1000
    print("Decompression:", duration_d, "milliseconds.")

    print("Type of compressed_img:", type(compressed_img))
    print("Content of compressed_img:", compressed_img)

    # Check the content of compressed_img.getdata()
    print("Content of compressed_img.getdata():", compressed_img.getdata())
"""
    # Iterate over the compressed image data and print the type and value of each pixel
    for pix in compressed_img.getdata():
        print("Type of pixel:", type(pix))
        print("Pixel value:", pix)
"""

if __name__ == '__main__':
    main()
