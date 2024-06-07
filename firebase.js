// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyC_jt407Uc3L6tB3rsT6_E8RUp8Z6Nnk1c",
  authDomain: "system-a28c4.firebaseapp.com",
  projectId: "system-a28c4",
  storageBucket: "system-a28c4.appspot.com",
  messagingSenderId: "563798016386",
  appId: "1:563798016386:web:7392d312a51f6966504f9b",
  measurementId: "G-HEJ0Z46R9W"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);