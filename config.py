import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCcKoowTWge7vtVIkSsT_Dj13fHXZM3_zs",
    'authDomain': "sistemasdistribuidos-e8eaf.firebaseapp.com",
    'databaseURL': "https://sistemasdistribuidos-e8eaf-default-rtdb.firebaseio.com",
    'projectId': "sistemasdistribuidos-e8eaf",
    'storageBucket': "sistemasdistribuidos-e8eaf.firebasestorage.app",
    'messagingSenderId': "34064682324",
    'appId': "1:34064682324:web:61ebb87c80e40748edccc1"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
