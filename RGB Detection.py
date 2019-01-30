#from picamera import PiCamera
from PIL import Image
from time import sleep
import matplotlib.pyplot as plt
##import numpy as np
##import argparse
##import cv2
##import colorsys
###NAMED_COLORS = {'cyan':                  '#00ffff'}
###ps all kill -9 PID



############################################################################################################################
#Camera Setup

#camera = PiCamera()
##camera.resolution = (80, 60)
##camera.resolution = (160, 120)
#camera.resolution = (320, 240)
#camera.framerate = 24



############################################################################################################################
#Image Viewer

#from imgproc import *

# use the camera's width and height to set the viewer size
#view = Viewer(320, 240, "RGB Detection")
#view.displayImage(img)
#sleep(0.5)
#del view



############################################################################################################################
#RGB Detection

# endlessly loop until the user exits
#while True:
for i in range(1):
    
    
    #Capture image from the camera
    
    ###camera.start_preview()
    ###camera.annotate_text = "TestSelfie2 1/23/2019"
    ###sleep(.5)
    ###image = camera.capture('/home/pi/Desktop/imgproc/SelfieTest2.jpg')
    ###camera.stop_preview()
    

    #Open image in reading mode and capture it to an object
    #img = Image.open('C:/Users/Stratos/Desktop/spring.jpg', 'r')
    img = Image.open('C:/Users/Stratos/Desktop/spring.jpg', 'r')
    
    
    #Reduce image resolution for faster processing
    #img.thumbnail((80, 60))  
    #img.save('C:/Users/Stratos/Desktop/shot.png') 
    
    
    #Displays image
    #sleep(5)
    #img.show()
    
    
    #Extract each pixel value into a list as a set of RGB values
    pix_val = list(img.getdata())
    print("The RGB values are:",pix_val)
    
    
    #Flatten list from [(123,124,145,120), (345,453,234,124),……] to [123, 124, 145, 120, 345, 453, 234, 124….]
    #pix_val_flat = [x for sets in pix_val for x in sets]
    #print(pix_val_flat)


    #Initialize Variables
    
    #x and y position accumulators
    acc_x = 0
    acc_y = 0

    #Total number of pixels accumulated
    acc_count = 0

    #Iterate over every pixel 
    ...
    
    #Loads the pixels of the image object into the pix variable
    pix = img.load()
    
    #Creates variables for the number of columns and rows in the image object's pixel array
    cols,rows = img.size
    print(pix, cols,rows)
    
    #Iterating through every pixel in the image
    for x in range(0, cols):
        for y in range(0, rows):
            
            #Get the RGB values of the current pixel
            red, green, blue = img.getpixel((x, y))
            print("-------------------------------------------------------")
            print("Current Pixel =","(",x,",",y,")")
            print("The RGB values for the current pixel","(", x, ",", y,")", "are",red,green,blue)
            
            #Testing the red, green and blue intensities against each other
            #Specifically isolating predominantly blue colors
            if blue > 64:
                if blue > (3 / 2 * green):
            #if red > green:
                #if red > blue:
                    
                    #Shows that the current pixel is predominantly blue
                    print("Predominantly Blue Pixel Detected")
                                                            
                    #Add the x and y of the found pixel to the accumulators
                    acc_x += x
                    acc_y += y
                    print("The x and y accumulators are",acc_x,"and", acc_y)
                    
                    #Increment the accumulated pixels' count
                    acc_count += 1
                    print("The accumulated pixel count is",acc_count)
                    
                    #Color pixels which pass the test black
                    #img[x, y] = 0, 0, 0
                    
                    
                    #Check the count accumulator is greater than zero, to avoid dividing by zero
                    if acc_count > 0:
                                               
                        #Calculate the mean x and y positions
                        mean_x = acc_x / acc_count
                        mean_y = acc_y / acc_count
                        print("The mean x and y positions are", mean_x, "and",mean_y)
                        
                        #Marks the coordinates of each Predominantly Blue Pixel on the image
                        plt.imshow(img)
                        #Marks the image with an X
                        plt.scatter(mean_x, mean_y, s=250, c='red', marker='x')
                        plt.show()
                        
    #Marks the mean position on the image
    plt.imshow(img)
    #Marks image with an arrow pointing out the diode
    plt.annotate('Diode', xy=(mean_x, mean_y), xycoords='data',
    xytext=(0.5, 0.5), textcoords='figure fraction',
    arrowprops=dict(arrowstyle="->"))
    plt.show()
    print("The diode is at the coordinates:","(", mean_x, ",",mean_y,")") 
