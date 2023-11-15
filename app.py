# from flask import Flask, render_template, send_file , jsonify,request
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template("indexx.html")
#
# places_details = {
#     "hod": {"placeName": "HOD office ", "description": "Department of ICT "},
#     # Add more entries as needed
# }
#
#
# @app.route('/get_details')
# def get_details():
#     path_id = request.args.get('path_id')
#     details = places_details.get(path_id, {"placeName": "", "description": ""})
#     return jsonify(details)
#
# @app.route('/search', methods=['GET'])
# def search():
#     query = request.args.get('query', '').lower()
#
#     # Filter places based on the search query
#     results = {key: value for key, value in places_details.items() if query in key.lower() or query in value.get("placeName", "").lower()}
#
#     return jsonify(results)
#
# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask, render_template, jsonify, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'ict_data.db'

def connect_db():
    return sqlite3.connect(DATABASE)

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def index():
    return render_template("indexx.html")

@app.route('/get_details')
def get_details():
    path_id = request.args.get('path_id')
    cur = g.db.execute("SELECT * FROM labs WHERE lab_id = ? ", (path_id,))
    details = cur.fetchone()
    cur.close()
    return jsonify(details)


def perform_search(table, search_columns, query):
    try:
        cur = g.db.execute(
            f"SELECT * FROM {table} WHERE {' OR '.join(f'{column} LIKE ?' for column in search_columns)}",
            (f'%{query}%',) * len(search_columns)
        )
        results = [dict(zip([column[0] for column in cur.description], row)) for row in cur.fetchall()]

        print(results)
        cur.close()
        return jsonify(results)
    except Exception as e:
        # Handle the exception (log it or return an error response)
        print(f"Error performing search: {e}")
        return jsonify({"error": "An error occurred during the search"}), 500

# Combine all search options into a single endpoint
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    location_type = request.args.get('location_type', '').lower()
    # Define search options based on location type
    search_options = {
        'labs': {"table": "labs", "columns": ["lab_id", "lab_name"]},
        'faculty': {"table": "faculty_chambers", "columns": ["faculty_name", "designation"]},
        'department_office': {"table": "department_office", "columns": ["office_name", "details"]},
        'seminar_hall': {"table": "seminar_hall", "columns": ["hall_name"]}
        # Add more options as needed
    }

    # Check if the specified location type is valid
    if location_type in search_options:
        # Perform the search based on the selected location type

        return perform_search(search_options[location_type]["table"], search_options[location_type]["columns"], query)
    else:
        return jsonify({"error": "Invalid location type"}), 400




@app.route('/get_faculty_details')
def get_faculty_details():
    path_id = request.args.get('path_id')
    cur = g.db.execute("SELECT * FROM faculty_chambers WHERE chamber_number = ?", (path_id,))
    details = cur.fetchone()
    cur.close()
    return jsonify(details)

@app.route('/search_faculty', methods=['GET'])
def search_faculty():
    query = request.args.get('query', '').lower()
    return perform_search("faculty_chambers", ["faculty_name", "designation"], query)

@app.route('/get_department_office_details')
def get_department_office_details():
    path_id = request.args.get('path_id')
    cur = g.db.execute("SELECT * FROM department_office WHERE office_name = ?", (path_id,))
    details = cur.fetchone()
    cur.close()
    return jsonify(details)

@app.route('/search_department_office', methods=['GET'])
def search_department_office():
    query = request.args.get('query', '').lower()
    return perform_search("department_office", ["office_name", "details"], query)

@app.route('/get_seminar_hall_details')
def get_seminar_hall_details():
    path_id = request.args.get('path_id')
    cur = g.db.execute("SELECT * FROM seminar_hall WHERE hall_number = ?", (path_id,))
    details = cur.fetchone()
    cur.close()
    return jsonify(details)

@app.route('/search_seminar_hall', methods=['GET'])
def search_seminar_hall():
    query = request.args.get('query', '').lower()
    return perform_search("seminar_hall", ["hall_name"], query)

# Assuming you have a Flask route like this
@app.route('/get_all_faculty')
def get_all_faculty():
    path_id = request.args.get('path_id')
    print("Received path_id:", path_id)

    if path_id:
        cur = g.db.execute("SELECT * FROM faculty_chambers WHERE chamber_number = ?", (path_id,))
    else:
        cur = g.db.execute("SELECT * FROM faculty_chambers")

    faculty_data = [dict(zip([column[0] for column in cur.description], row)) for row in cur.fetchall()]
    cur.close()
    return jsonify(faculty_data)

if __name__ == "__main__":
    app.run(debug=True)

