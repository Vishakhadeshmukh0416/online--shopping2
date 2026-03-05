pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Vishakhadeshmukh0416/online--shopping2.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\Users\abc\AppData\Local\Programs\Python\Python313\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\Users\abc\AppData\Local\Programs\Python\Python313\python.exe" test_app.py'
            }
        }

    }
}