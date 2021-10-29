import cv2, dlib, time

def captureScreenshot(frame, face):
    # Display the alert on screen
    cv2.putText(frame, "ALERT! NO MORE SPACE AVAILABLE", (45, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

    # draw rectangle around the face
    for f in face:
        x, y = f.left(), f.top()
        a, b = f.right(), f.bottom()
        cv2.rectangle(frame, (x, y), (a, b), (0, 0, 255), 2) 

    # show the captured ss
    cv2.imshow('!!! MORE THAN 3 PASSENGERS DETECTED !!!', frame)
    
    # press any key to destroy the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def captureVid():
    # live cam face detection
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # capture video
    video = cv2.VideoCapture(0)

    # detect face with dlib's face detector method
    faceDetector = dlib.get_frontal_face_detector()
    while True:
        # capture the frame
        check, frame = video.read()
        # flip the frame captured like a mirror image
        frame = cv2.flip(frame, 1)
        # convert the frame into gray scale image (optional)
        grayImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # detect face
        face = faceDetector(grayImg)
        # variable with intial count for no. of faces = 0
        count = 0
        # flag for face limit warning
        flag = 0

        for f in face:
            # checking face limit
            if count == 1:
                cv2.putText(frame, "WARNING! Max limit reached", (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 4)
                flag = 1

            if count > 1:  # if more than 3 persons in 2 wheeler vehicle
                time.sleep(0.5)
                # function call to capture the snap of 3 or more faces
                captureScreenshot(frame, face)

            # coordinates for drawing rectangle around face
            x, y = f.left(), f.top()
            a, b = f.right(), f.bottom()

            # draw rectangle around the face
            if flag == 1: # max faces detected
                cv2.rectangle(frame, (x, y), (a, b), (0, 255, 255), 2)  
            else:
                cv2.rectangle(frame, (x, y), (a, b), (255, 0, 0), 2)  

            # increment face count upon detection
            count += 1

            # print text on screen (Face No. : )
            cv2.putText(frame, "Face No." + str(count), (x-10, y-10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2) # color format : BGR
        
        # display exit key on p/p window
        cv2.putText(frame, "Press 'Q' to exit", (25, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 230), 2)
        # open window for showing the o/p
        cv2.imshow('=== Live Cam ===', frame)
        
        # escape key (q)
        if cv2.waitKey(1) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    captureVid()