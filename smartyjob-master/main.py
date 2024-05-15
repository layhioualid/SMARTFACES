import cv2
import database
import reconnaissance_faciale
import datetime
import numpy as np

host = 'localhost'
database_name = 'facesmart'
user = 'root'
password = ''
table_name = 'employees'

connection = database.connect_to_database(host, database_name, user, password)

images, ids = database.fetch_images_from_database(connection, table_name)

encode_list_known = reconnaissance_faciale.find_encodings(images)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
background = cv2.imread('C:\\Users\\ORIGINAL SHOP\\Desktop\\smart face\\smartyjob-master\\backg.png')

camera_frame_pos = (116, 233)  # liser lfo9 
camera_frame_size = (390, 390)  # l o L
info_frame_pos = (786, 224)  # liser lfo9
info_frame_size = (432, 365)  # l o L

# frame dyal les information =>toufik ma t9isch had code li hna
info_frame_background = np.zeros((info_frame_size[1], info_frame_size[0], 3), dtype=np.uint8)
info_frame_background[:] = (53, 53, 54)  
info_frame = info_frame_background.copy()  

frame_thickness = 0  
frame_color = (183, 183, 185)  # Color bgr ma bghach ikhdem liya transaprent dert nefs lon dyal background


while True:
    ret, img = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Resize  camera frame to match background 
    img_resized = cv2.resize(img, (camera_frame_size[0], camera_frame_size[1]))

    # image o id o nom mn table employe
    images, ids_names = database.fetch_images_from_database(connection, table_name)
    
    is_face_detected, match_index, face_loc = reconnaissance_faciale.recognize_faces_in_frame(encode_list_known,
                                                                                                 img_resized)

    if is_face_detected:
        if match_index is not None:
            #  ID nom
            person_id, nom_person, prenom_person = ids_names[match_index]

            # Draw rectangle around the detected face
            y1, x2, y2, x1 = face_loc
            cv2.rectangle(img_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Update  record
            reconnaissance_faciale.update_or_insert_attendance(connection, person_id)
            status = reconnaissance_faciale.get_employee_status(connection, person_id)
            # Clear the content of the information frame
            info_frame = info_frame_background.copy()  # Use the background color for the info frame
            worked_hours = reconnaissance_faciale.calculate_work_hours(connection, person_id, datetime.date.today())
            info_text = f"Nom: {nom_person.upper()} {prenom_person.upper()}\n\n\nSTATUS: {status.upper()}\n\n\nHEURE DE TRAVAIL: {worked_hours}"
            #hadi jebtha mn stack over flow 7it had cv2.putText() makatfhmch \n 
            
            y0, dy = 50, 30
            for i, line in enumerate(info_text.split('\n')):
                y = y0 + i * dy
                cv2.putText(info_frame, line, (20, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,255, 255), 3)

    else:
        # Clear the content of the information frame region
        info_frame = info_frame_background.copy() 

        # Display "No Face Detected" if no face is detected
        cv2.putText(img_resized, '', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Add camera frame
    background[camera_frame_pos[1]:camera_frame_pos[1] + camera_frame_size[1],
    camera_frame_pos[0]:camera_frame_pos[0] + camera_frame_size[0]] = img_resized

    # Add information frame
    background[info_frame_pos[1]:info_frame_pos[1] + info_frame_size[1],
    info_frame_pos[0]:info_frame_pos[0] + info_frame_size[0]] = info_frame

    cv2.imshow('Smart Face', background)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Close database connection
if connection.is_connected():
    connection.close()
    print("MySQL connection closed")
