# Python code to convert an image (colored/greyscaled) to ASCII image. 
# Output will be saved as a text file of ascii characters or you will use --show flag to print output on terminal.

import argparse 
import numpy as np 
import math 

from PIL import Image 

# class to work with and process images to generate ascii images
class ASCII_ART:

    def __init__(self,file_path):

        # Initializing image path
        self.file_path = file_path

        # ASCII-charset of size 70 ranked based on intensity/lightness (high to low) (source => internet)
        self.ascii_70_charset = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
          
        # ASCII-charset of size 10 ranked based on intensity/lightness (high to low) (visually made)
        self.ascii_10_charset = '#@$%?*+:,. '       

    def readFile(self,greyScaled):

        print("Reading File....")

        # Creating a image object
        if(greyScaled == False):
            self.img = Image.open(self.file_path).convert('L')
        else:
            self.img = Image.open(self.file_path)

        print("DONE")

        # image original dimensions
        self.W,self.H = self.img.size

    def getAvgIntensity(self,image): 

        # reading this tile as numpy 2d array
        tile = np.array(image) 

        # this tile's dimensions
        w,h = tile.shape 

        # calculating the avg intensity by reshaping this tile to 1d array of size w*h
        return np.average(tile.reshape(w*h)) 


    def writeToFile(self,outFile):

        print("Writing image in file....")

        # creating a file for saving output
        f = open(outFile, 'w') 

        # writing each row characters one by one (one row each time)
        for row in self.finalImg: 
            f.write(row + '\n') 

        # closing this file 
        f.close() 
        print("DONE")
        print("ASCII art written to %s" % outFile) 
        print("Note: Reduce font size if the image dimensions are too large\n")

    def showOutput(self):

        # print image in terminal console window 
        for row in self.finalImg:
            print(row,end='\n')
        print("\n")


    def makeArt(self,tileWidth,tileHeight,use70,terminal):
        
        print("Input image dimensions: %d x %d" % (self.W, self.H)) 
  
        # calculating reduced image dimensions based on tile dimensions
        w = self.W//tileWidth 
        h = self.H//tileHeight
      
        print("Resized dimensions of final tiledImage: %d x %d" % (w, h)) 
        print("Making ASCII Art....")

        # empty list for storing final image ascii characters
        self.finalImg = [] 
       
        # compute final tile image intensities 
        for i in range(0,h): 
            y1 = int(i*tileHeight) 
            y2 = int((i+1)*tileHeight) 
 
            # insert empty string
            self.finalImg.append("") 

            for j in range(0,w): 
      
                x1 = int(j*tileWidth) 
                x2 = int((j+1)*tileWidth) 
                
                # crop tile image from original image
                tile = self.img.crop((x1, y1, x2, y2)) 
                
                # calculate avg intensity of tile pixels
                avg = int(self.getAvgIntensity(tile)) 

                # 1 is darkest and 255 is brightest that's why the charset is arranged from high to low intensity characters.
                # select character based on avg intensity (one to many mapping) (by default ascii_10_charset is used in mapping)
                if use70: 
                    character = self.ascii_70_charset[int((avg*69)/255)] 
                else: 
                    character = self.ascii_10_charset[int((avg*9)/255)] 
                
                # write to image list
                self.finalImg[i] += character

        print("DONE\n")

        # if --show flag was set then this will execute and show image in terminal window
        if(terminal):
            self.showOutput() 

def main():

    # create parser for accepting --flags for various parameters
    parser = argparse.ArgumentParser() 

    # add expected arguments 
    parser.add_argument('--input', dest='file_path', required=True)      # mandatory input file location 
    parser.add_argument('--out', dest='outFile', required=False)         # can be set using --out flag (output file)
    parser.add_argument('--tW', dest='tileWidth', required=False)        # can be set using --tW flag (tileWidth)
    parser.add_argument('--tH', dest='tileHeight', required=False)       # can be set using --tH flag (tileHeight)
    parser.add_argument('--grey',dest='greyScaled',action='store_true')  # use this flag if the input image is already grayscaled 
    parser.add_argument('--use70',dest='use70',action='store_true')      # by default uses ascii_10_charset characters for mapping pixels
    parser.add_argument('--show',dest='terminal',action='store_true')    # use this to print image in terminal window 
  
    # parse args 
    args = parser.parse_args() 

    # set output file 
    outFile = 'out.txt'  # default same folder as file out.txt
    if args.outFile: 
        outFile = args.outFile 
  
    # set tileWidth in pixels 
    tileWidth = 8        #default 8 pixels
    if args.tileWidth: 
        tileWidth = int(args.tileWidth) 

    # set tileHeight in pixels     
    tileHeight = 10      # default 10 pixels
    if args.tileHeight: 
        tileHeight = int(args.tileHeight) 

    # create class obj 
    ART = ASCII_ART(args.file_path)

    # read input file
    ART.readFile(args.greyScaled)

    # process image 
    ART.makeArt(tileWidth,tileHeight,args.use70,args.terminal)

    # write to text file (<= open this file to see output or use --show flag to print on terminal itself)
    ART.writeToFile(args.outFile)

if __name__ == "__main__":
    main()
  