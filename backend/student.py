
class Student:
    def __init__(self, name, follow_up_note, 
                 program, counselor, phone, 
                 email, grade, school, class_of, 
                 parent_name, parent_phone, 
                 parent_email1, parent_email2):
        
        self.name = name
        self.follow_up_note = follow_up_note
        self.program = program
        self.counselor = counselor
        self.phone = phone
        self.email = email
        self.grade = grade
        self.school = school
        self.class_of = class_of
        self.parent_name = parent_name
        self.parent_phone = parent_phone
        self.parent_email1 = parent_email1
        self.parent_email2 = parent_email2


        # Getter and Setter for follow_up_note
    def get_follow_up_note(self):
        return self._follow_up_note

    def set_follow_up_note(self, follow_up_note):
        self._follow_up_note = follow_up_note

    # Getter and Setter for program
    def get_program(self):
        return self._program

    def set_program(self, program):
        self._program = program

    # Getter and Setter for counselor
    def get_counselor(self):
        return self._counselor

    def set_counselor(self, counselor):
        self._counselor = counselor

    # Getter and Setter for phone
    def get_phone(self):
        return self._phone

    def set_phone(self, phone):
        self._phone = phone

    # Getter and Setter for email
    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    # Getter and Setter for grade
    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

    # Getter and Setter for school
    def get_school(self):
        return self._school

    def set_school(self, school):
        self._school = school

    # Getter and Setter for class_of
    def get_class_of(self):
        return self._class_of

    def set_class_of(self, class_of):
        self._class_of = class_of

    # Getter and Setter for parent_name
    def get_parent_name(self):
        return self._parent_name

    def set_parent_name(self, parent_name):
        self._parent_name = parent_name

    # Getter and Setter for parent_phone
    def get_parent_phone(self):
        return self._parent_phone

    def set_parent_phone(self, parent_phone):
        self._parent_phone = parent_phone

    # Getter and Setter for parent_email1
    def get_parent_email1(self):
        return self._parent_email1

    def set_parent_email1(self, parent_email1):
        self._parent_email1 = parent_email1

    # Getter and Setter for parent_email2
    def get_parent_email2(self):
        return self._parent_email2

    def set_parent_email2(self, parent_email2):
        self._parent_email2 = parent_email2
