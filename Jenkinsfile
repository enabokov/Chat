pipeline {
    agent { dockerfile true }
    stages {
        stage('tests') {
            steps {
                sh 'python --version'
		sh 'npm --version'
		sh 'node --version'
            }
        }
    }
}
