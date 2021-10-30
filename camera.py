import cv2

# faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class Video(object):        
    def captureScreenshot(img, face):
        # Display the alert on screen
        cv2.putText(img, "ALERT! NO MORE SPACE AVAILABLE", (45, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
        # draw rectangle around the detected face
        for (x, y, w, h) in face:
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2) 
        # show the captured ss
        cv2.imshow('!!! MORE THAN 3 PASSENGERS DETECTED !!!', img)
            
            
    def get_frame(self):
        # get/read the image
        img = cv2.imread('faces.jpg', 1)
        # print(img)  # check if image read successfully

        # detect face by decreasing the scaleFactor by 1.05
        faces = faceCascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=5)

        # initial no. of faces = 0
        count = 0
        # flag for facelimit warning
        flag = 0
        # draw a rectangle around the detected face
        for (x, y, w, h) in faces:
            if count == 1:
                    cv2.putText(img, "WARNING! Max limit reached", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)
                    flag = 1

            if count > 1:  # if more than 3 persons in 2 wheeler vehicle
                # time.sleep(0.5)
                # function call to capture the snap of 3 or more faces
                captureScreenshot(img, faces)

            # draw rectangle around the face
            if flag == 1: # 2 faces detected, mark 2nd face with yellow
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)  
            else:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            # increment face count upon detection
            count += 1
            # print text on screen (Face No. : )
            cv2.putText(img, "Face No." + str(count), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2) # color format : BGR

        # open window for showing the o/p
        cv2.imshow('pic', img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
