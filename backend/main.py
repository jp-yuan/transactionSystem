import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyC_jt407Uc3L6tB3rsT6_E8RUp8Z6Nnk1c",
    'authDomain': "system-a28c4.firebaseapp.com",
    'projectId': "system-a28c4",
    'storageBucket': "system-a28c4.appspot.com",
    'messagingSenderId': "563798016386",
    'appId': "1:563798016386:web:7392d312a51f6966504f9b",
    'measurementId': "G-HEJ0Z46R9W"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

print("run")