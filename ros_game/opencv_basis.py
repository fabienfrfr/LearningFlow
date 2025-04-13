

import cv2, dlib, PIL.Image, numpy as np
from skimage import external#, io
from skimage.feature import peak_local_max
# Model
pose_predictor_68_point = dlib.shape_predictor("pretrained_model/shape_predictor_68_face_landmarks.dat")
face_encoder = dlib.face_recognition_model_v1("pretrained_model/dlib_face_recognition_resnet_model_v1.dat")
face_detector = dlib.get_frontal_face_detector()
# Camera
cap = cv2.VideoCapture(0)
# event
cv2.setMouseCallback('Camera', function)
# Loop
while True:
    ret, frame=cap.read()
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    image = cv2.blur(image, (5, 5))
    # convolution contouring
    img_border = cv2.Canny(image, 2,2)
    # color detection
    mask = cv2.inRange(image, lo, hi)
    elements = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    # segmentation
    ret, thresh = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    dilation = cv2.morphologyEx(thresh, cv2.MORPH_DILATE, kernel)
    dist_transform = cv2.distanceTransform(dilation,cv2.DIST_L2,5)
    local_maxi = peak_local_max(dist_transform, indices=False, labels=thresh)
    ret, markers = cv2.connectedComponents(np.uint8(local_maxi))
    # distance between visage
    vectors = np.linalg.norm(known_face_encodings - face_encoding, axis=1)
    # DETECT FACES
    shape = pose_predictor_68_point(image, face_location)
    # show
    cv2.circle(frame, (int(x), int(y)), 5, color_info, 10)
    cv2.imshow('Camera', frame)
    # exit
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()




