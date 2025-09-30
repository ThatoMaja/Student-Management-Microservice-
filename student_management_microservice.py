import json
import logging

# Configure logging to write to a file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("student_microservice.log"),  # Save log to file
        logging.StreamHandler()                           # Show log in console
    ]
)

class StudentMicroservice:
    def __init__(self, data_file='students.json'):
        self.data_file = data_file
        self.students = self._load_data()  # Load existing data at startup

    def _load_data(self):    # Load student data from json file
        try: 
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def _save_data(self):    # Save student data back to json file
        with open(self.data_file, 'w') as file:
            json.dump(self.students, file, indent=4)

    def add_student(self, student_id, name, course):
        if student_id in self.students:
            print("Error: That Student ID already exists!")
            logging.warning(f"Attempted to add duplicate student ID: {student_id}")
            return False

        # Add new student record
        self.students[student_id] = {"name": name, "course": course}
        self._save_data()
        logging.info(f"New student {student_id} added: {self.students[student_id]}")
        print("Student added successfully")
        return True

    def get_student(self, student_id):
        student = self.students.get(student_id)
        if student:
            logging.info(f"Retrieved student {student_id}")
            return student
        else:
            logging.warning(f"Attempted to retrieve non existent student: {student_id}")
            return None

    def list_all_students(self):
        logging.info("Displaying all student records")
        return self.students


def run_console_app():
    service = StudentMicroservice()

    while True:
        print("\nStudent Microservice Console")
        print("1. Add Student")
        print("2. Get Student Details")
        print("3. List All Students")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            s_id = input("Enter Student ID: ").strip()
            name = input("Enter Student's Name: ").strip()
            course = input("Enter Course Name: ").strip()
            service.add_student(s_id, name, course)

        elif choice == '2':
            s_id = input("Enter Student ID to find: ").strip()
            student_data = service.get_student(s_id)
            if student_data:
                print(json.dumps(student_data, indent=4))
            else:
                print("Error: Student not found!")

        elif choice == '3':
            all_students = service.list_all_students()
            if all_students:
                for sid, details in all_students.items():
                    print(f"ID: {sid}, Name: {details['name']}, Course: {details['course']}")
            else:
                print("No students registered.")

        elif choice == '4':
            print("Exiting... Goodbye!")
            logging.info("Microservice shutdown")
            break

        else:
            print("Invalid option! Please enter a number between 1 and 4")


if __name__ == "__main__":
    run_console_app()
