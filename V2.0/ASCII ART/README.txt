ASCII ART 

Author: IIT2018032
Last Updated: 15 Aug 2020

About :
ASCII Art is mainly focussed on producing images solely based on ASCII characters.
Here I will basically work on making ascii art from any image after converting it to grayscale image and later their pixel 
intensity/lightness values are mapped with ASCII characters to generate this art.

Assignment Details (from Google classroom):
Title = Convert your own "Selfie"  in to an ASCII image
Pavan Chakraborty
Aug 3
100 points                

Submission Date = Due 16 Aug, 11:59 PM
A) Take your Picture "Selfie" and convert it to a 8bit Grayscale image.
B) Convert the Grayscale image into tiles of 8X10pixel. (Find from the NET how to read a JPEG grayscale image on to an array). 
Use the Average integer intensity B[i, j]=INT(SUM(A[i, j]/80 + 0.5).
C) As the integer intensity values B[i, j] are being computed, simultaneously make a list/1D Array of  different integer intensity level existing in the image/array B[i, j]. 
Check that this list does not have a repetition of intensity values.
D) Arrange the 95 printable ASSCI Code/ in the order of gray level. Find a method through Visually, through a code (Scan each ASCII character and
find the ratio of Black pixel to white pixel within the bounding box of the ASCII character) or from Google. 
E) Map each printable character to the list of integer gray levels existing in the image. The mapping will be one to many.
F) Make your ASCII Image 

Contents:
1. images folder    => contains other sample images to test out the code (if required).
2. Art.py           => The python code which will convert image to ascii image after processing.
3. README.txt       => This file basically
4. INSTRUCTIONS.txt => This file contains instructions about how to run the python code (MUST SEE).
5. selfie.jpg       => My selfie image (basically a test image which will be used for generating output) 
                       for this assignment purpose only.
6. out folder       => contains sample screenshots of outputs generated using selfie image 

NOTE: READ INSTRUCTIONS.txt to know mpre about how to run the python code (Art.py).