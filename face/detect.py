import os
import face_recognition

images = os.listdir('/home/naresh/Desktop/face_detection/media')

def face_detect(image_path):
    image_to_be_matched = face_recognition.load_image_file(image_path)
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
    match_pic = []
    for image in images:
        current_image = face_recognition.load_image_file("/home/naresh/Desktop/face_detection/media/" + image)
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        if result[0] == True:
            match_pic.append(image)
        else:
            pass
    if match_pic:

        return match_pic[0]
    else:
        
        return 'Person not matched,please provide your details....!'
        

# face_detect('/home/naresh/Desktop/66068621.jpg.gif')
