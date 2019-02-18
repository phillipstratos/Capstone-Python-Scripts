from __future__ import division
import math, time

# import necessary libraries
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()

# steer control - R (right) L (left)
# throttle control - R (reverse) F (forward)

# frequency determined with oscilloscope. Called outside of steering/throttle functions to eliminate freq based bugs
pwm.set_pwm_freq(70)


# helper function to easily give steering commands
def steer(Dir, Deg):

	# convert desired turn angle to required pulse width offset
	# relationship determined from laser diode angle testing
        pulse = Deg/79.301

	# add (right turn) or subtract (left turn) the pulse width offset from middle 1.5 ms
        if Dir == "R":
                pulse = 1.5 + pulse
        else:
                pulse = 1.5 - pulse

	# convert pulse width value to 12 bit number expected by PWM9685 library functions
	# relationship determined experimentally with oscilloscope testing
	# floor and int functions used because PWM9685 library functions cannot be passed a float
        py_pulse = int(math.floor(pulse/.0034))

	# PWM9685 library function to give the module a command
        pwm.set_pwm(1,0,py_pulse)


# helper function to easily give throttle commands
def throttle(Dir, Percent):

	# converts % throttle input to pulse width offset max of .5
        pulse =  Percent/200

	# add (reverse) or subtract (forward) the pulse width offset from middle 1.5 ms
        if Dir == "R":
                pulse = 1.5 + pulse
        else:
                pulse = 1.5 - pulse

	# see steer() comments
        py_pulse = int(math.floor(pulse/.0034))
        pwm.set_pwm(2,0,py_pulse)

# function to simulate full throttle and idle to release ESC throttle safety
# should be called prior to throttle operations
def engage():
	throttle("F", 100)
	time.sleep(.2)
	throttle("F", 0)
	time.sleep(3)


# function to simulate input required to cause ESC braking when travelling forward
def F_stop():
	throttle("R", 100)
	time.sleep(.2)
	throttle("R", 0)
	time.sleep(.2)

# function to simulate input required to cause ESC braking when travelling in reverse
def R_stop():
	throttle("F", 100)
	time.sleep(.2)
	throttle("F", 0)
	time.sleep(.2)



########################################################
from picamera import PiCamera
from PIL import Image
from time import sleep
#import matplotlib.pyplot as plt
#import rgbsteering




############################################################################################################################
#Camera Setup

camera = PiCamera()
camera.resolution = (80, 60)
##camera.resolution = (160, 120)
##camera.resolution = (320, 240)
camera.framerate = 24



############################################################################################################################
#RGB Detection


def main():
    
    # endlessly loop until dthe user exits
    #while True:
    for i in range(10):


        #Capture image from the camera

        camera.start_preview()
        sleep(.01)
        image = camera.capture('/home/pi/Desktop/rgbDetectionTest.jpg')
        camera.stop_preview()


        #Open image in reading mode and capture it to an object
        img = Image.open('/home/pi/Desktop/rgbDetectionTest.jpg', 'r')



        #Initialize Variables

        #x and y position accumulators
        acc_x = 0
        #acc_y = 0

        #Total number of pixels accumulated
        acc_count = 0


        #Creates variables for the number of columns and rows in the image object's pixel array
        cols,rows = img.size

        #Iterating through every pixel in the image
        for x in range(0, cols):
            for y in range(0, rows):

                #Get the RGB values of the current pixel
                red, green, blue = img.getpixel((x, y))
                

                #Testing the red, green and blue intensities against each other
                #Specifically isolating predominantly blue colors
                if blue > 64:
                    if blue > (3 / 2 * green):
                #if red > green:
                    #if red > blue:
                       
                        #Add the x and y of the found pixel to the accumulators
                        acc_x += x
                        #acc_y += y
                     
                        #Increment the accumulated pixels' count
                        acc_count += 1


                        #Check the count accumulator is greater than zero, to avoid dividing by zero
                        if acc_count > 0:

                            #Calculate the mean x and y positions
                            mean_x = acc_x / acc_count
                            #mean_y = acc_y / acc_count

                        
		        #Steering commands for 80 by 60 pixel images
		        if mean_x > 41:
		            print("Turn Left!")
			    #throttle("F", 5)
			    steer("L", 10)
		        elif mean_x < 39:
		            print("Turn Right!")
			    #throttle("F", 5)
			    steer("R", 10)
		        else:
		            print("Go Straight!")
		            #throttle("F", 5)
			    steer("R", 0)
		        #Exits function
        		#return

#engage()
#throttle("F", 3)

main()

#sleep(.02)
#F_stop()
