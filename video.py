import cv2
from simple_facerec import SimpleFacerec
import test1

def facial_recognition():
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")

    # Load Camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 255, 200), 2)
            if name != "Unknown":
               
                test1.code.check(name)

            cv2.rectangle(frame, (x1, y1), (x2, y2), (10, 50, 40), 4)

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break

    cap.release()
    cv2.destroyAllWindows()





# import cv2
# from simple_facerec import SimpleFacerec

# import test1
# # Encode faces from a folder
# sfr = SimpleFacerec()
# sfr.load_encoding_images("images/")

# # Load Camera
# cap = cv2.VideoCapture(0)


# while True:
#     ret, frame = cap.read()

#     # Detect Faces
#     face_locations, face_names = sfr.detect_known_faces(frame)
#     for face_loc, name in zip(face_locations, face_names):
#         y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

#         cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (200, 255, 200), 2)
#         if name !="Unknown":
            
#             test1.code.check(name)

#         cv2.rectangle(frame, (x1, y1), (x2, y2), (10, 50, 40), 4)

#     cv2.imshow("Frame", frame)

    
#     if cv2.waitKey(1) & 0xFF == ord('a'):
#         break

# cap.release()
# cv2.destroyAllWindows()