import mysql.connector
import datetime
# Global variable to store the database connection
db_connection = None

def connect_to_database():
    global db_connection
    if db_connection is None:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="facesmart"
        )
    return db_connection

def close_database_connection():
    global db_connection
    if db_connection is not None:
        db_connection.close()
        db_connection = None

def check_login(username, password):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        return result
    except mysql.connector.Error as error:
        print("Error occurred while checking login:", error)
        return None

def add_employee(nom, prenom, email, poste, department_id, image_data):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "INSERT INTO employees (nom, prenom, email, poste, department_id, image) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nom, prenom, email, poste, department_id, image_data))
        db.commit()

        cursor.close()
    except mysql.connector.Error as error:
        print("Error occurred while adding employee:", error)
def get_employee_by_id(id):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT e.id, e.nom, e.prenom, e.email, e.poste, d.name as departement, e.image FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE e.id = %s"
        cursor.execute(query, (id,))
        employee_info = cursor.fetchone()

        cursor.close()
        return employee_info
    except mysql.connector.Error as error:
        print("Error occurred while fetching employee info:", error)
        return None

def get_employee_list():
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT e.id, e.nom, e.prenom, e.email, e.poste, d.name as departement FROM employees e JOIN departments d ON e.department_id = d.department_id "
        cursor.execute(query)
        employee_list = cursor.fetchall()

        cursor.close()
        return employee_list
    except mysql.connector.Error as error:
        print("Error occurred while fetching employee list:", error)
        return []
def get_dep():
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT id, name FROM departments"
        cursor.execute(query)
        dep_list = cursor.fetchall()

        cursor.close()
        return dep_list
    except mysql.connector.Error as error:
        print("Error occurred while fetching dep list:", error)
        return []
def get_dep():
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT department_id, name FROM departments"
        cursor.execute(query)
        dep_list = cursor.fetchall()

        cursor.close()
        return dep_list
    except mysql.connector.Error as error:
        print("Error occurred while fetching dep list:", error)
        return []


def delete_employee_by_id(id):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        cursor.execute("DELETE FROM employees WHERE ID=%s", (int(id),))
        db.commit()

        cursor.close()
    except mysql.connector.Error as error:
        print("Error occurred while deleting employee:", error)

def search_employee(searchTerm):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "SELECT e.id, e.nom, e.prenom, e.email, e.poste, d.name as departement FROM employees e JOIN departments d ON e.department_id = d.department_id WHERE e.nom LIKE %s OR e.prenom LIKE %s OR d.name LIKE %s;"
        values = ('%{}%'.format(searchTerm), '%{}%'.format(searchTerm), '%{}%'.format(searchTerm))
        cursor.execute(query, values)
        result = cursor.fetchall()

        cursor.close()
        return result
    except mysql.connector.Error as error:
        print("Error occurred while searching for employees:", error)
        return []
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
    finally:
        cursor.close()

def get_worked_hours_today(employee_id):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        # Call calculate_work_hours with today's date
        today = datetime.date.today()
        result = calculate_work_hours(db, employee_id, today)

        cursor.close()

        # Check if result is a string
        if isinstance(result, str):
            return result  # Return the error message directly
        else:
            return result.total_seconds() / 3600 if result else 0  # Convert seconds to hours
    except mysql.connector.Error as error:
        print("Error occurred while fetching worked hours today:", error)
        return 0

def get_worked_hours_month(employee_id):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        # Call calculate_work_hours with the first day of the current month
        first_day_of_month = datetime.date.today().replace(day=1)
        result = calculate_work_hours(db, employee_id, first_day_of_month)

        cursor.close()

        # Check if result is a string
        if isinstance(result, str):
            return result  # Return the error message directly
        else:
            return result.total_seconds() / 3600 if result else 0  # Convert seconds to hours
    except mysql.connector.Error as error:
        print("Error occurred while fetching worked hours this month:", error)
        return 0
def insert_employee(nom, prenom, email, poste, dep, img):
    try:
        db = connect_to_database()
        cursor = db.cursor()

        query = "INSERT INTO employees (`nom`, `prenom`, `email`, `poste`, `department_id`, `image`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (nom, prenom, email, poste, dep, img))
        
        # Commit the transaction
        db.commit()
        cursor.close()
        db.close()
        print("Employee inserted successfully.")
    except mysql.connector.Error as error:
        print("Error occurred while inserting employee:", error)
def get_presence_par_date(date):
    """Returns an array containing all employees who were present on the given date"""
    try:
        db = connect_to_database()
        cursor = db.cursor()
        query = "SELECT e.id, e.nom, e.prenom, e.email, e.poste, d.name as departement FROM employees e JOIN departments d ON e.department_id = d.department_id JOIN attendance a ON a.employee_id = e.id WHERE DATE(a.date) = %s"
        cursor.execute(query, (date,))
        emp = cursor.fetchall()
        cursor.close()
        print((emp))
        return emp
    except Exception as e:
        print('Erreur lors de la récupération des employés présents le', date, ':', e)
        return []