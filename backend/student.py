class Student:
    def __init__(self, name, follow_up_note, 
                 program, counselor, phone, 
                 email, grade, school, class_of, 
                 parent_name, parent_phone, 
                 parent_email1, parent_email2):
        
        self.name = name
        self._follow_up_note = follow_up_note
        self._program = program
        self._counselor = counselor
        self._phone = phone
        self._email = email
        self._grade = grade
        self._school = school
        self._class_of = class_of
        self._parent_name = parent_name
        self._parent_phone = parent_phone
        self._parent_email1 = parent_email1
        self._parent_email2 = parent_email2

    # Getter and Setter for follow_up_note
    @property
    def follow_up_note(self):
        return self._follow_up_note

    @follow_up_note.setter
    def follow_up_note(self, value):
        self._follow_up_note = value

    # Getter and Setter for program
    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        self._program = value

    # Getter and Setter for counselor
    @property
    def counselor(self):
        return self._counselor

    @counselor.setter
    def counselor(self, value):
        self._counselor = value

    # Getter and Setter for phone
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    # Getter and Setter for email
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    # Getter and Setter for grade
    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        self._grade = value

    # Getter and Setter for school
    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, value):
        self._school = value

    # Getter and Setter for class_of
    @property
    def class_of(self):
        return self._class_of

    @class_of.setter
    def class_of(self, value):
        self._class_of = value

    # Getter and Setter for parent_name
    @property
    def parent_name(self):
        return self._parent_name

    @parent_name.setter
    def parent_name(self, value):
        self._parent_name = value

    # Getter and Setter for parent_phone
    @property
    def parent_phone(self):
        return self._parent_phone

    @parent_phone.setter
    def parent_phone(self, value):
        self._parent_phone = value

    # Getter and Setter for parent_email1
    @property
    def parent_email1(self):
        return self._parent_email1

    @parent_email1.setter
    def parent_email1(self, value):
        self._parent_email1 = value

    # Getter and Setter for parent_email2
    @property
    def parent_email2(self):
        return self._parent_email2

    @parent_email2.setter
    def parent_email2(self, value):
        self._parent_email2 = value
