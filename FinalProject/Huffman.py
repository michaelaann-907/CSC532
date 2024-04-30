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
                self.data.append(self.px[row, col])
        for item in self.data:
            if item not in self.dict:
                self.dict[item] = 1
            else:
                self.dict[item] += 1

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
        with open(self.name + "_out.txt", 'w') as out:
            for pix in self.data:
                out.write(self.encode[pix] + "\n")

    def readin(self):
        with open(self.name + "_out.txt", 'r') as ins:
            self.receive = ins.read().splitlines()

    def create_new_image(self):
        decompressed = Image.new('RGB', (self.width, self.height))
        pixels = decompressed.load()
        index = 0
        for row in range(self.width):
            for col in range(self.height):
                pixels[row, col] = self.decode[self.receive[index]]
                index += 1
        self.display(decompressed)


def main():
    currentImage = Picture(input("Filename:"))  # Filename must be in the same root as Huffman
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

    start_d = time.time()
    currentImage.create_new_image()
    end_d = time.time()
    duration_d = (end_d - start_d) * 1000
    print("Decompression:", duration_d, "milliseconds.")


if __name__ == '__main__':
    main()
