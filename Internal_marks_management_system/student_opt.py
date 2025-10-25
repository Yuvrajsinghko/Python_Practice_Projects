from internal_opt import student_name_list

class StudentOperations():
    def __init__(self):
        self.filename = "student_details.txt"

    def create_student(self):
        with open(self.filename, 'a') as f:
            student_serial_num = input("Enter serial number: ")
            student_rollnum = input("Enter rollnumber: ")
            student_name = input("Enter name of the student: ")
            final_details = f"{student_serial_num},{student_rollnum},{student_name}\n"
            f.write(final_details)
        print("Successfully Registered")

    def show_details(self, line):
        serial, rollnum, name = line.strip().split(',')
        print("Serial Number:", serial)
        print("Student Rollnum:", rollnum)
        print("Student Name:", name)

    def student_name_list(self):
        with open(self.filename, 'r') as f:
            lines = f.readlines()
        return [line.strip().split(',')[2] for line in lines]

    def search_student(self):
        names = self.student_name_list()
        print("Available students:", names)
        search_name = input("Enter student name you wish to search: ")

        with open(self.filename, 'r') as f:
            lines = f.readlines()

        for line in lines:
            if search_name == line.strip().split(',')[2]:
                print('=== Student Found ===')
                self.show_details(line)
                return line.strip().split(','), line.strip()
        print("Student not found.")
        return None, None

    def show_all_student_details(self):
        with open(self.filename, 'r') as f:
            for line in f:
                print("===================================")
                self.show_details(line)
                print("===================================")

    def update_student_details(self):
        updated_list, old_line = self.search_student()
        if not old_line:
            return

        choice = int(input(
            "1: Update serial number\n2: Update roll number\n3: Update name\nChoice: "))
        if choice == 1:
            updated_list[0] = input("Enter new serial number: ")
        elif choice == 2:
            updated_list[1] = input("Enter new roll number: ")
        elif choice == 3:
            updated_list[2] = input("Enter new name: ")

        updated_line = ",".join(updated_list) + '\n'

        with open(self.filename, 'r') as f:
            lines = f.readlines()

        with open(self.filename, 'w') as f:
            for line in lines:
                if line.strip() == old_line:
                    f.write(updated_line)
                else:
                    f.write(line)
        print("Updated successfully.")

    def delete_student(self):
        st_list, st_line = self.search_student()
        if not st_line:
            return

        with open(self.filename, 'r') as f:
            lines = f.readlines()

        with open(self.filename, 'w') as f:
            for line in lines:
                if line.strip() != st_line:
                    f.write(line)
        print("Deleted successfully.")



a1=StudentOperations()
a1.show_all_student_details()


		




	



