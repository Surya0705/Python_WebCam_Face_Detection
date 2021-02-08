import cv2 # Importing the OpenCV Module for this Program.

'''You can Download this Classifier here:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml'''
a = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # Providing the Program with the Classifier.
b = cv2.VideoCapture(0) # Capturing the Video from the Camera.

while True: # Putting a While Loop.
    c, d = b.read() # Making OpenCV read the Video.
    e = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY) # Converting the Colored image to Gray because the Classifier can only detect in escale Images.
    
    '''Here I have used 1.3 and 3. You can mess up with these values and then 
    find out that which one suits the best for you. To know that why I used these 
    values just visit this link:
    https://www.bogotobogo.com/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php'''
    f = a.detectMultiScale(e, 1.3, 3) # Detecting the faces in the Captured Video.

    '''Also note that this piece of code between line 22-23 has been used to draw a rectangle
    around the detected faces. You'll notice that I have written someting like - "(0, 0, 255), 3"
    in line 23. First is BGR Value and 2nd is the Width of Rectangle. You may feel free to mess up
    with all these values and choose the ones which you like.'''
    for (x, y, w, h) in f: # Making the rectangle around the detected faces.
        cv2.rectangle(d, (x, y), (x+w, y+h), (0, 0, 255), 3) # Making the rectangle around the detected faces.

    cv2.imshow('Detected Face(s)', d) # Displaying the Detected Faces to the User.
    if cv2.waitKey(1) == ord('x'): # Waiting for the Key 'x' to be Pressed for the Program to Exit. You May Change it according to the Key of your Choice.
        break

b.release() # Releasing the Video.
cv2.destroyAllWindows() # Destroying All the Windows once 'x' Key is Pressed.
