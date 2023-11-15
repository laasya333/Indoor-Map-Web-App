import sqlite3
from flask import Flask,jsonify

app = Flask(__name__)
DATABASE = 'ict_data.db'
def get_faculty_details(path_id):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect('DATABASE')
        cursor = connection.cursor()

        # Execute SQLite query for the faculty_chambers table
        cursor.execute("SELECT * FROM faculty_chambers WHERE chamber_number = ?", (path_id,))
        details = cursor.fetchone()

        # Close the SQLite cursor and connection
        cursor.close()
        connection.close()

        if details:
            # Convert SQLite result to a dictionary for JSON response
            details_dict = {
                "faculty_name": details[1],
                "designation": details[2],
                "link": details[3],
                # Add more fields as needed
            }
            return jsonify(details_dict)
        else:
            return jsonify({"error": "Faculty details not found for the given chamber number"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_lab_details(path_id):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect('DATABASE')
        cursor = connection.cursor()

        # Execute SQLite query for the labs table
        cursor.execute("SELECT * FROM labs WHERE lab_number = ?", (path_id,))
        details = cursor.fetchone()

        # Close the SQLite cursor and connection
        cursor.close()
        connection.close()

        if details:
            # Convert SQLite result to a dictionary for JSON response
            details_dict = {
                "lab_name": details[1],
                # Add more fields as needed
            }
            return jsonify(details_dict)
        else:
            return jsonify({"error": "Lab details not found for the given lab number"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_department_office_details(path_id):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect('DATABASE')
        cursor = connection.cursor()

        # Execute SQLite query for the department_office table
        cursor.execute("SELECT * FROM department_office WHERE office_name = ?", (path_id,))
        details = cursor.fetchone()

        # Close the SQLite cursor and connection
        cursor.close()
        connection.close()

        if details:
            # Convert SQLite result to a dictionary for JSON response
            details_dict = {
                "office_name": details[0],
                "details": details[1],
                # Add more fields as needed
            }
            return jsonify(details_dict)
        else:
            return jsonify({"error": "Department office details not found for the given office name"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_seminar_hall_details(path_id):
    try:
        # Connect to SQLite database
        connection = sqlite3.connect('DATABASE')
        cursor = connection.cursor()

        # Execute SQLite query for the seminar_hall table
        cursor.execute("SELECT * FROM seminar_hall WHERE hall_number = ?", (path_id,))
        details = cursor.fetchone()

        # Close the SQLite cursor and connection
        cursor.close()
        connection.close()

        if details:
            # Convert SQLite result to a dictionary for JSON response
            details_dict = {
                "hall_name": details[1],
                # Add more fields as needed
            }
            return jsonify(details_dict)
        else:
            return jsonify({"error": "Seminar hall details not found for the given hall number"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Add similar conditions for other tables (labs, department_office, seminar_hall)
@app.route('/details/<table>/<path_id>')
def get_details(table, path_id):
    if table == 'faculty_chambers':
        return get_faculty_details(path_id)
    elif table == 'labs':
        return get_lab_details(path_id)
    elif table == 'department_office':
        return get_department_office_details(path_id)
    elif table == 'seminar_hall':
        return get_seminar_hall_details(path_id)
    else:
        return jsonify({"error": "Invalid table specified"}), 400

if __name__ == "__main__":
    app.run(debug=True)
