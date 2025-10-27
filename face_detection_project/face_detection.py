import cv2
import os
import time

#Load Haar Classifier
face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
smile_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_smile.xml"
)

os.makedirs("captures", exist_ok = True)

#Access to webcam
video_capture = cv2.VideoCapture(0)

#Define function to identify faces
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40,40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x+w, y+h), (0, 255, 0), 4)
        smile_area_gray = gray_image[y:y+h, x:x+h]
        smile_area_color = video_frame[y:y+h, x:x+h]
        smiles = smile_classifier.detectMultiScale(smile_area_gray, 1.7, 22, minSize=(25,25))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(smile_area_color, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 2)
    return faces

#creating a loop for real-time face detection
while True:
    result, video_frame = video_capture.read() #read frames from the video
    if result is False:
        break #terminate loop if frame is not read successfully
    
    faces = detect_bounding_box(
        video_frame
    ) # apply the function to video frame

    cv2.imshow(
        "Face Detection Window", video_frame
    ) #display the processed frame in a window name "Face detection Window"
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("c"):
        timestamp = int(time.time())
        filename = f"captures/detected_{timestamp}.jpg"
        cv2.imwrite(filename, video_frame)
        print("photo captured")

video_capture.release()
cv2.destroyAllWindows()
