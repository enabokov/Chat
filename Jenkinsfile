pipeline {
    agent { dockerfile true }
    stages {
        stage('tests') {
            steps {
                sh 'python --version'
		sh 'npm -V'
		sh 'node -V'
            }
        }
    }
}
