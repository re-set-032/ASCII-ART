from PIL import Image
import numpy as np 
import math 
 
ASCII_70 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "       
ASCII_10 = "#@$%?*+:,. "

def computeAverage(img): 

    cropImg = np.array(img) 
    w,h = cropImg.shape 
    return np.average(cropImg.reshape(w*h))    

def convertToAsciiImage(tw,th,W,H,img):
  
        w = W//tw 
        h = H//th

        Output = [] 
       
        for i in range(0,h): 
            y1 = int(i*th) 
            y2 = int((i+1)*th) 
            Output.append("") 

            for j in range(0,w): 
      
                x1 = int(j*tw) 
                x2 = int((j+1)*tw) 
                
                cropImg = img.crop((x1, y1, x2, y2))
                avg = int(computeAverage(cropImg)) 
                greyscaledChar = ASCII_70[int((avg*69)/255)] 
                Output[i] += greyscaledChar


        print("Output image\n")
        for row in Output:
            print(row)

        
if __name__ == "__main__":

	img = Image.open("selfie.jpeg").convert('L')
	W,H = img.size
	tw = 8
	th = 10

	convertToAsciiImage(tw,th,W,H,img)
    
  