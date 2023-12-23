import cv2

# path of video
vidcap = cv2.VideoCapture("D:/NAUFAL/Project/Refrensi/Convert mp4 to jpg/plat.mp4")
success, image = vidcap.read()


count = 0 
while vidcap.isOpened():
    success, image = vidcap.read()
    cv2.imwrite("D:/NAUFAL/Project/Refrensi/Convert mp4 to jpg/frame/%d.png" % count, image )
    count+=1
