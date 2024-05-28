import cv2
import os

folder = "Multi"
name = "Ungu_Banyak"
frame = 20

# Path of video
video_path = "Video/Raw/" + folder + "/" + name + ".mp4"
vidcap = cv2.VideoCapture(video_path)
success, image = vidcap.read()

# Get FPS
fps = vidcap.get(cv2.CAP_PROP_FPS)

count = 0
img_count = 0
while vidcap.isOpened():
    success, image = vidcap.read()

    # Menyimpan setiap frame ke-2
    if count % frame == 0:
        img_count += 1
        frame_folder = "Image/" + folder + "/" + name + "/"
        if not os.path.exists(frame_folder):
            os.makedirs(frame_folder)
        frame_path = frame_folder + name + " %d.png" % img_count
        cv2.imwrite(frame_path, image)
        print(img_count)

    count += 1

    # Keluar dari loop jika tidak ada frame yang tersedia
    if not success:
        if img_count > 0:
            print("-----------End---------------")
            print("FPS of the video:", fps)
            print("FPS of the image:", frame)
            print("Total frame:", count + 1)
            print("Total image:", img_count)
            print("Save in ", frame_folder)
            print("-----------------------------")
        elif img_count == 0:
            print("Error!")
        break
