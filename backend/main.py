#import pyrebase
from student import Student

# firebaseConfig = {
#     'apiKey': "AIzaSyC_jt407Uc3L6tB3rsT6_E8RUp8Z6Nnk1c",
#     'authDomain': "system-a28c4.firebaseapp.com",
#     'projectId': "system-a28c4",
#     'storageBucket': "system-a28c4.appspot.com",
#     'messagingSenderId': "563798016386",
#     'appId': "1:563798016386:web:7392d312a51f6966504f9b",
#     'measurementId': "G-HEJ0Z46R9W"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()
# db = firebase.database()

s1 = Student(
    name="John Doe",
    follow_up_note="Needs to improve math skills",
    program="STEM",
    counselor="Ms. Smith",
    phone="555-1234",
    email="john.doe@example.com",
    grade="10",
    school="High School ABC",
    class_of="2025",
    parent_name="Jane Doe",
    parent_phone="555-5678",
    parent_email1="jane.doe@example.com",
    parent_email2="jane.doe@work.com"
)


print(s1.name)