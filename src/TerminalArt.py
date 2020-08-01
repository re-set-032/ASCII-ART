# For producing ASCII-ART inside terminal 

# Using PIL package  
from PIL import Image 

class ASCII_ART:
    def __init__(self,file_path):

        # Initializing image path
        self.file_path = file_path
        
        # ASCII-charset ranked based on intensity/lightness 
        self.ascii = [' ','.',',',':','+','*','?','%','$','@','#']        

    def readFile(self):

        # Creating a image object 
        self.img = Image.open(self.file_path,'r') 
        self.width,self.height = self.img.size
        
        # Pixel data
        self.pixel_data = list(self.img.getdata())

    def makeArt(self):
        
        # ASCII Char groups of 24 i.e 0-23 => ascii[0] and so on....
       
        print("Sample ASCII Art")
        print("Note: Reduce font size if the image dimensions are too large\n\n\n")
        
        counter = 0
        for row in range(self.height):
            for col in range(self.width):
                factor = self.pixel_data[counter]//24
                print(self.ascii[factor],end='')
                counter = counter + 1
            print(" ")
    

if __name__ == "__main__":

    ART = ASCII_ART("../images/GreyScaled/grey.png")
    ART.readFile()
    ART.makeArt()
    


