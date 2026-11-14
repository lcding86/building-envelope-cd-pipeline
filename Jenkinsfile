pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Compiling building envelope cooling load module...'
                sh 'python3 -m py_compile envelope_load.py'
            }
        }
        stage('Automated Unit Tests') {
            steps {
                echo 'Running conduction, solar glazing, and boundary unit tests...'
                sh 'python3 -m unittest test_envelope_load.py'
            }
        }
        stage('Quality Gate') {
            steps {
                echo 'Verifying engineering docstrings and physical output positivity...'
                sh 'python3 -c "import envelope_load; assert envelope_load.conductive_gain_w.__doc__ is not None; assert envelope_load.solar_glazing_gain_w(10, 0.4, 500) > 0"'
            }
        }
        stage('Deploy to Staging') {
            steps {
                echo 'Deploying verified envelope load module to staging environment...'
                sh 'mkdir -p staging_env && cp envelope_load.py staging_env/'
            }
        }
        stage('Deploy to Production') {
            steps {
                echo 'Promoting to production and executing zone load verification...'
                sh 'mkdir -p prod_env && cp staging_env/envelope_load.py prod_env/ && python3 prod_env/envelope_load.py'
            }
        }
    }

    post {
        success {
            echo 'CD Pipeline complete: envelope_load.py verified and deployed to prod_env.'
        }
        failure {
            echo 'CD Pipeline halted: envelope load validation or build stage failed.'
        }
    }
}