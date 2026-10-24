pipeline {
    agent any

    options {
        timestamps()
        skipDefaultCheckout(true)
        disableConcurrentBuilds()
        timeout(time: 10, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '20'))
    }

    triggers {
        pollSCM('H/5 * * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Verificar ambiente') {
            steps {
                sh 'git --version'
                sh 'python3 --version'
            }
        }
        stage('Build') {
            steps {
                sh 'python3 -m compileall -q src tests'
            }
        }
        stage('Instalar dependências') {
            steps {
                sh '''
                    python3 -m venv .venv
                    .venv/bin/python -m pip install --upgrade pip
                    .venv/bin/python -m pip install -r requirements-dev.txt
                '''
            }
        }
        stage('Testes') {
            steps {
                sh '''
                    mkdir -p reports
                    .venv/bin/python -m pytest -v --junitxml=reports/pytest.xml
                '''
            }
        }
    }

    post {
        always {
            junit allowEmptyResults: true, testResults: 'reports/pytest.xml'
            echo 'Execução finalizada.'
        }
        success {
            echo 'Pipeline concluído com sucesso!'
        }
        failure {
            echo 'Falha no pipeline. Consulte os logs.'
        }
    }
}
