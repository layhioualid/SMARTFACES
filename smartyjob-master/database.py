import cv2
import numpy as np
import mysql.connector
from mysql.connector import Error
import os
def connect_to_database(host, database, user, password):
    try:
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            print('Connected to MySQL database')
            return connection
        else:
            print('Failed to connect to MySQL database')
            return None
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        return None

def fetch_images_from_database(connection, table_name):
    images = []
    ids_names = []
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT id, nom, image,prenom FROM {table_name}")
        persons = cursor.fetchall()
        for person in persons:
            # convertion d'image l array dyal numpy
            nparr = np.frombuffer(person[2], np.uint8)
            # Decode numpy array to OpenCV format image
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            images.append(img)
            ids_names.append((person[0], person[1],person[3]))  # (id, nom,prenom) tuple
            #khass nzid departemnet hnya bach n affihih f frame dyal infromation
    except Error as e:
        print(f"Error fetching images from the database: {e}")
    finally:
        cursor.close()
        return images, ids_names




