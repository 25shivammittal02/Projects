import numpy as np
import cv2

#instantiating a camera object to capture images, 0 denotes default camera
cam = cv2.VideoCapture(0)
#create a haar-cascade object for face detection (used to extract features from faces)
face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#to keep  data of faces
data = []
#Current frame number
ix = 1

while (True):
	#read a frame from camera, .read() returns two values, if camera working properly then it returns true, if there is any problem then it returns false
	ret, frame = cam.read()
	if ret == True:
		#converting the current frame to grayscale
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		#apply the haar cascade to detect face in the current frame other parameters are for fine tuning
		faces = face_cas.detectMultiScale(gray, 1.3, 5)

		#for each face obbject we get, we have the corner coordinates(x, y), width and height of the face
		for(x, y, w, h) in faces:

			#get the face component from the image frame
			face_component = frame[y:y+h, x:x+w, :]

			#resizing the face object
			fc = cv2.resize(face_component, (50, 50))

			#store the face data after every 10 frames till we have 20 entries
			if ix%10 == 0 and len(data) < 20:
				data.append(fc)

			#draw a rectangle around the faces in the stream
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		ix += 1
		cv2.imshow('frame', frame)

		#if the user presses ESC key (ID: 27) or no. of face data become greater than or equal to 20, exit/stop recording faces
		if cv2.waitKey(0) == 27 or len(data)>=20:
			break;
	else:
		#if the camera is not working properly
		print ("error")
#now destroy all the windows created
cv2.destroyAllWindows()

#convert data to a numpy format
data = np.asarray(data)

name= input("Whose face was this?, i will remember it")
print("")

#print the data shape
print (data.shape)

#save the data as numpy matrix in the encoded format
np.save(name, data)