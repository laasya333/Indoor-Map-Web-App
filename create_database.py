import sqlite3

# Function that creates all tables
def create_tables(connection):
    cursor = connection.cursor()

    # Create labs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS labs (
            lab_id TEXT PRIMARY KEY,
            lab_number TEXT NOT NULL,
            lab_name TEXT NOT NULL
        )
    ''')

    # Create faculty_chambers table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faculty_chambers (
            room_id TEXT PRIMARY KEY,
            chamber_number TEXT NOT NULL,
            faculty_name TEXT NOT NULL,
            designation TEXT NOT NULL,
            link TEXT
        )
    ''')

    # Create department_office table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS department_office (
            office_name TEXT PRIMARY KEY,
            details TEXT NOT NULL
        )
    ''')

    # Create seminar_hall table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS seminar_hall (
            hall_number TEXT PRIMARY KEY,
            hall_name TEXT NOT NULL
        )
    ''')

    # Commit changes and close cursor
    connection.commit()
    cursor.close()

# Function taht adds faculty data to faculty_chambers table
def add_faculty_data(connection):
    cursor = connection.cursor()

    faculty_data = [
        ("faculty_1", "fc_1", 'Dr. Smitha N Pai', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/smitha-n-pai0.html'),
        ("faculty_2", "fc_1", 'Dr. Girija V. Attigeri', 'Associate professor', 'https://manipal.edu/mit/department-faculty/faculty-list/girija-attegeri.html'),
        ("faculty_3", "fc_1", 'Dr. Chandrakala C B', 'Additional Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/chandrakala-cb.html'),
        ("faculty_4", "fc_1", 'Ms Divya S', 'Asst Professor- SI grade', 'https://manipal.edu/mit/department-faculty/faculty-list/divya-s.html'),
        ("faculty_5", "fc_1", 'Dr Radhika M Pai', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/radhika-m-pai.html'),
        ("faculty_6", "fc_1", 'Dr Balachandra', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/balachandra.html'),
        ("faculty_7", "fc_1", 'Dr Krishna Prakasha', 'Associate professor', 'https://manipal.edu/mit/department-faculty/faculty-list/krishna-prakasha-a.html'),
        ("faculty_8", "fc_1", 'Dr Manjula C B', 'Asst Professor SI grade', 'https://manipal.edu/mit/department-faculty/faculty-list/manjula-c-belavagi.html'),
        ("faculty_9", "fc_1", 'Mrs Swathi B P', 'Asst Professor SI grade', 'https://manipal.edu/mit/department-faculty/faculty-list/swathi-b-p.html'),
        ("faculty_10","fc_2", 'Mr Chethan Sharma', 'Asst Professor Sr Scal', 'https://manipal.edu/mit/department-faculty/faculty-list/chethan-sharma.html'),
        ("faculty_11", "fc_2", 'Dr Adesh N D', 'Associate professor', 'https://manipal.edu/mit/department-faculty/faculty-list/AdeshND.html'),
        ("faculty_12", "fc_2", 'Dr Sucheta V Kolejar', 'Associate Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/sucheta-kolekar.html'),
        ("faculty_13", "fc_2", 'Dr Preetham Kumar', 'Professor | Deputy Registrar-Academics(Technical) Manipal Academy of Higher Education', 'https://manipal.edu/mit/department-faculty/faculty-list/preetham-kumar.html'),
        ("faculty_14", "fc_2", 'Dr Manohar S Pai M M', 'Senior Professor', 'NULL'),
        ("faculty_15", "fc_2", 'Mr Akshay K C', 'Asst Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/akshay-kc.html'),
        ("faculty_16", "fc_2", 'Dr Kaliraj S', 'Assistant professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/dr-kaliraj-s.html'),
        ("faculty_17", "fc_2", 'Dr Divya Rao', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/divya-rao.html'),
        ("faculty_18", "fc_2", 'Dr Raviraj Holla', 'Asst Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/RavirajaHollaM.html'),
        ("faculty_19", "fc_3", 'Dr Raghavendra S', 'Assistant Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/dr-raghavendra-s.html'),
        ("faculty_20", "fc_3", 'Jayashree', 'Assistant Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/Jayashree.html'),
        ("faculty_21", "fc_3", 'Dr Raghavendra Achar', 'Associate Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/RaghavendraAchar.html'),
        ("faculty_22", "fc_3", 'Dr Santhosh Rao', 'Additional Professor', 'NULL'),
        ("faculty_23", "fc_3", 'Dr Santhosh Kamath', 'Associate professor', 'https://manipal.edu/mit/department-faculty/faculty-list/santhosh-kamath.html'),
        ("faculty_24", "fc_4", 'Dr Ramakrishna M', 'Associate Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/ramakrishna-m.html'),
        ("faculty_25", "fc_4", 'Dr Veena Mayya', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/veena-mayya.html'),
        ("faculty_26", "fc_4", 'Ms Chetana Pujari', 'Asst Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/chetana-pujari.html'),
        ("faculty_27", "fc_4", 'Dr Diana Olivia', 'Assistant Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/diana-olivia.html'),
        ("faculty_28", "fc_4", 'Mrs Pooja S', 'Asst Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/pooja-s.html'),
        ("faculty_29", "fc_4", 'Mrs Vibha', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/Vibha.html'),
        ("faculty_30", "fc_4", 'Dr Sanjay Singh', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/sanjay-singh.html'),
        ("faculty_31", "fc_5", 'Dr Sumith N', 'Associate Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/SumitN.html'),
        ("faculty_32", "fc_5", 'Mrs Anuradha Rao', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/anuradha-rao.html'),
        ("faculty_33", "fc_5", 'Dr Raghavendra Ganiga', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/raghavendra-ganiga.html'),
        ("faculty_34", "fc_5", 'Dr Sameena Pathan', 'Assistant Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/SameenaBP.html'),
        ("faculty_35", "fc_5", 'Ms Nisha P Shetty', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/nisha-p-shetty.html'),
        ("faculty_36", "fc_5", 'Dr Rashmi Naveen Raj', 'Associate Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/rashmi-naveen-raj.html'),
        ("faculty_37", "fc_5", 'Dr Poornalatha G', 'Additional Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/poornalatha-g.html'),
        ("faculty_38", "fc_5", 'Mrs Veena K M', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/veena-km.html'),
        ("faculty_39", "fc_5", 'Mrs Sangeetha T S', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/sangeetha-ts.html'),
        ("faculty_40", "fc_5", 'Mr Ghanashyama Prabhu', 'Assistant Professor SI Grade', 'https://manipal.edu/mit/department-faculty/faculty-list/ghanashyama-prabhu.html'),
        ("faculty_41", "fc_5", 'Dr Manjula Shenoy K', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/manjula-shenoy-k.html'),
        ("faculty_42", "fc_5", 'Mr Vinayak Mantoor', 'Assistant Professor Sr Scale', 'https://manipal.edu/mit/department-faculty/faculty-list/vinayak-m.html'),
        ("faculty_43", "fc_5", 'Dr Ajitha Shenoy K B', 'Professor', 'https://manipal.edu/mit/department-faculty/faculty-list/ajitha-shenoy-k-b.html')
    ]


    cursor.executemany('''
        INSERT INTO faculty_chambers (room_id, chamber_number, faculty_name, designation, link)
        VALUES (?, ?, ?, ?, ?)
    ''', faculty_data)

    connection.commit()
    cursor.close()

#lab data inserted into labs table 
def add_lab_data(connection):
    cursor = connection.cursor()

    lab_data = [
        ("lab_0", "lab 0", 'Research Lab'),
        ("lab_1", "lab 1", 'Database Management System Lab'),
        ("lab_2", "lab 2", 'Computer Network Lab'),
        ("lab_3", "lab 3", 'Advanced Programming Lab'),
        ("lab_4", "lab 4", 'Project Lab'),
        ("lab_5", "lab 5", 'Software Engineering Lab'),
        ("lab_6", "lab 6", 'Wireless Network Lab'),
        ("lab_7", "lab 7", 'Industrial IOT Systems and Applications (R & D Lab)'),
        ("lab_8", "lab 8", 'Digital and Computing Lab'),
        ("lab_9", "lab 9", 'Data Analytics Lab'),
        ("lab_10", "lab 10", 'Seminar Hall'),
        ("lab_11", "lab 11", 'Hardware Design Lab')
    ]

    cursor.executemany('''
        INSERT INTO labs (lab_id, lab_number, lab_name)
        VALUES (?, ?, ?)
    ''', lab_data)

    connection.commit()
    cursor.close()

# Insert department office data into department_office table
def add_department_office_data(connection):
    cursor = connection.cursor()

    department_office_data = [
        ('office_dept', 'Information and Communication Technology (ICT)'),
        ('office_hod', 'Prof. Dr. Smitha M Pai')
    ]

    cursor.executemany('''
        INSERT INTO department_office (office_name, details)
        VALUES (?, ?)
    ''', department_office_data)

    connection.commit()
    cursor.close()

# Insert seminar hall data into seminar_hall table
def add_seminar_hall_data(connection):
    cursor = connection.cursor()

    seminar_hall_data = [
        ("hall_1", 'SH_01 Seminar Hall')
    ]

    cursor.executemany('''
        INSERT INTO seminar_hall (hall_number, hall_name)
        VALUES (?, ?)
    ''', seminar_hall_data)

    connection.commit()
    cursor.close()

# Main fn
def main():
    database_name = "ict_data.db"

    # Connect to the database
    connection = sqlite3.connect(database_name)

    # Create tables
    create_tables(connection)

    # Add faculty data to faculty_chambers table
    add_faculty_data(connection)

    # Add Lab data to Labs table
    add_lab_data(connection)
    
    # Add department office data to department_office table
    add_department_office_data(connection)

    # Add seminar hall data to seminar_hall table
    add_seminar_hall_data(connection)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
