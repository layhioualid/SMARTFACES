import cv2
import numpy as np
import face_recognition
import os
import datetime
def find_encodings(images):
    encode_list = []
    for img in images:
        # Convert image to RGB (face_recognition library requires RGB format)
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Get the face encodings for the image
        encode = face_recognition.face_encodings(rgb_img)[0]
        # Append the face encodings to the list
        encode_list.append(encode)
    return encode_list

def recognize_faces_in_frame(encode_list_known, frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    if len(encode_list_known) == 0:
        return False, None, None

    if len(face_locations) == 0:
        #print("No face detected")
        return False, None, None

    for encode_face, face_loc in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(encode_list_known, encode_face)
        face_dis = face_recognition.face_distance(encode_list_known, encode_face)
        match_index = np.argmin(face_dis)

        """ print("Matches:", matches)
        print("Face distances:", face_dis)
        print("Match index:", match_index)"""

        if matches[match_index]:
            return True, match_index, face_loc

    return False, None, None

def save_image(image, directory, filename):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
        image_path = os.path.join(directory, filename)
        cv2.imwrite(image_path, image)
        print(f"Image saved: {image_path}")
        return True, image_path
    except Exception as e:
        print(f"Error saving image: {e}")
        return False, None


def update_or_insert_attendance(connection, employee_id):
    try:
        cursor = connection.cursor()

        # Get the current timestamp
        current_timestamp = datetime.datetime.now()

        # Calculate the timestamp 2 minutes ago
        five_minutes_ago = current_timestamp - datetime.timedelta(minutes=2)
        # Get the last "in" record for the employee
        cursor.execute("""
            SELECT MAX(date) 
            FROM attendance 
            WHERE employee_id = %s 
            AND status = 'in';
        """, (employee_id,))
        last_in_time = cursor.fetchone()[0]

        # Get the last "out" record for the employee
        cursor.execute("""
            SELECT MAX(date) 
            FROM attendance 
            WHERE employee_id = %s 
            AND status = 'out';
        """, (employee_id,))
        last_out_time = cursor.fetchone()[0]

        if last_in_time and last_out_time:
            if last_in_time > last_out_time:
                # Employee is currently "in"
                if current_timestamp - last_in_time >= datetime.timedelta(minutes=2):
                    # If last "in" time is more than 2 minutes  mark them as "out"
                    cursor.execute("INSERT INTO attendance (employee_id, status, date) VALUES (%s, 'out', %s)",
                                   (employee_id, current_timestamp))
                else:
                    cursor.execute("""
                                                           UPDATE attendance 
                                                           SET date = %s 
                                                           WHERE employee_id = %s 
                                                           AND status = 'in' 
                                                           AND date = %s;
                                                       """, (current_timestamp, employee_id, last_in_time))
                    print("Employee's last spotted time updated.")
            else:
                # Employee is currently "out"
                if current_timestamp - last_out_time >= datetime.timedelta(minutes=2):
                    # If last "out" time is more than 2 minutes ago, mark them as "in"
                    cursor.execute("INSERT INTO attendance (employee_id, status, date) VALUES (%s, 'in', %s)",
                                   (employee_id, current_timestamp))
                else:
                    print("Employee is already marked as 'out'. No action taken.")

        elif last_in_time:
            # Employee is currently "in"
            if current_timestamp - last_in_time >= datetime.timedelta(minutes=2):
                # If last "in" time is more than 2 minutes ago, mark them as "out"
                cursor.execute("INSERT INTO attendance (employee_id, status, date) VALUES (%s, 'out', %s)",
                               (employee_id, current_timestamp))
            else:

                print("Employee is already marked as 'in'. No action taken.")

        elif last_out_time:
            # Employee is currently "out"
            if current_timestamp - last_out_time >= datetime.timedelta(minutes=2):
                # If last "out" time is more than 2 minutes ago, mark them as "in"
                cursor.execute("INSERT INTO attendance (employee_id, status, date) VALUES (%s, 'in', %s)",
                               (employee_id, current_timestamp))
            else:
                print("Employee is already marked as 'out'. No action taken.")

        else:
            # No previous records found, mark as "in"
            cursor.execute("INSERT INTO attendance (employee_id, status, date) VALUES (%s, 'in', %s)",
                           (employee_id, current_timestamp))

        connection.commit()
        print("Attendance updated successfully.")
    except Exception as e:
        print(f"Error updating attendance: {e}")
        connection.rollback()
    finally:
        cursor.close()


def calculate_work_hours(connection, employee_id, date):
    try:
        cursor = connection.cursor()

        # Get all attendance records for the given employee and date
        cursor.execute("""
            SELECT date, status
            FROM attendance
            WHERE employee_id = %s
            AND DATE(date) = %s
            ORDER BY date;
        """, (employee_id, date))
        records = cursor.fetchall()

        total_work_hours = datetime.timedelta()
        check_in_time = None
        check_out_time = None

        # Iterate through all records and calculate work hours
        for record in records:
            if record[1] == 'in':
                check_in_time = record[0]
                # Reset check_out_time to handle multiple check-ins in a day
                check_out_time = None
            elif record[1] == 'out':
                if check_in_time:
                    check_out_time = record[0]
                    # Calculate work hours if both check-in and check-out are available
                    total_work_hours += check_out_time - check_in_time
                    check_in_time = None

        # If there's a check-in without a corresponding check-out, consider the current time as check-out time
        if check_in_time:
            current_time = datetime.datetime.now()
            total_work_hours += current_time - check_in_time

        # Convert total work hours to hours and minutes
        hours = total_work_hours.total_seconds() // 3600
        minutes = (total_work_hours.total_seconds() % 3600) // 60

        # Format the total work hours with two numbers after the decimal point
        formatted_work_hours = f"{hours:.0f}:{minutes:02.0f}"

        return formatted_work_hours

    except Exception as e:
        print(f"Error calculating work hours: {e}")
        return None
def get_employee_status(db,employee_id):
    try:

        cursor = db.cursor()

        # Query to get the latest attendance record for the employee
        query = """
            SELECT status
            FROM attendance
            WHERE employee_id = %s
            ORDER BY date DESC
            LIMIT 1
        """
        cursor.execute(query, (employee_id,))
        latest_record = cursor.fetchone()

        cursor.close()

        # If there's no attendance record for the employee, return 'Unknown' status
        if latest_record is None:
            return 'Unknown'
        else:
            return latest_record[0]  # Return the status from the latest record

    except mysql.connector.Error as error:
        print("Error occurred while fetching employee status:", error)
        return 'Error'
