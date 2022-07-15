from ast import Try
from PIL import Image
import numpy

#If you use this ascii table, you may get too manuy detailed shading, resulting in not clearly seeing the subject in the ASCII image
#ASCII_CHARS = [".", "'", "^", ":", '"', ";", "~", "-", "_", "+", "<", ">", "i", "!", "l", "I", "?", "/", "|", "(", ")", "{", "}", "[", "]", "r", "c", "v", "u", "n", "x", "z", "j", "f", "t", "L", "C", "J", "U", "Y", "X", "Z", "O", "0", "Q", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "*", "W",  "M", "B", "8", "&", "%", "$"]



ASCII_CHARS = ['.', ',', ':', ';', '+', '*', '?', '%', 'S', '#', '@']


def get_image(image_path, new_width = 800):
    try:
        image = Image.open(image_path, "r")
    except:
        print("Something went wrong opening the file. Please make sure it is a .jpg file and that its location matches with the one of the .py file.")
        return -1, -1, -1, -1
    width, height = image.size

    aspect_ratio = float(width)/float(height)


    new_height = int(new_width/aspect_ratio)

    image = image.resize((new_width, new_height))

    image = image.convert('L') #Convert image to grayscale

    print("Size:", width,"x", height, "px")
    pixel_values = list(image.getdata()) #Pixel values

    pixel_values = numpy.asarray(image, dtype='int64')

    return new_width, new_height, pixel_values


def createAsciiArt(dimX, dimY, file, asciiRowSize, asciiColSize, pixels):
    for row in range(dimY):
        for col in range(dimX):
            sum = 0
            for y in range(row*asciiRowSize, (row+1)*asciiRowSize):
                for x in range(col*asciiColSize, (col+1)*asciiColSize):
                        sum += pixels[y][x]

            average = sum / (asciiColSize*asciiRowSize)

            # print(int((average/255) * len(ASCII_CHARS)))
            character = ASCII_CHARS[int(len(ASCII_CHARS) - (average/255) * (len(ASCII_CHARS)))]

            file.write(character)
        file.write("\n")


def main():

    print("Hey, this is a program that converts your imaages into awesome ASCII art, made only by using keyboard characters! Be sure that the image you want to convert is in .jpg format and that it is in the same folder as this .py file. Enjoy!")


    image_path = input("Insert the name of your image file (Ex: myImage.jpg): ")


    width, height, pixels = get_image(image_path)


    if width != -1:  # if everything went right in the get_image function
        asciiColSize = 5  # 5
        asciiRowSize = 12  # 12

        dimX = int(width / asciiColSize)
        dimY = int(height / asciiRowSize)

        file = open(image_path.split('.')[0] + ".txt", "w")

        createAsciiArt(dimX, dimY, file, asciiRowSize, asciiColSize, pixels)

        file.close()

    print("The ASCII art is ready! You can find it in the " + image_path.split('.')[0] + ".txt file!")


if __name__ == '__main__':
    main()
