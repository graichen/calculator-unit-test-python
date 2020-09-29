#!/usr/bin/env groovy

pipeline {
    agent any

    options {
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    environment {
        HTTP_PROXY="${HTTP_PROXY}"
        HTTPS_PROXY="${HTTPS_PROXY}"
        NO_PROXY="${NO_PROXY}"
        SONAR_LOGIN_KEY = credentials('SONAR_LOGIN_KEY')
    }

    stages {

        stage('Check env') {
            steps {
                sh 'id'
                sh 'env'
                sh 'docker version'
            }
        }

        stage('Test') {
            agent {
                docker {
                    // to run as non-root:
                    image 'python:3.8.5-alpine3.12'
                    //args '-u ${JENKINS_UID}'
                    // for windows let's skip setting user
                    args '-u root:root'
                }
            }
            steps {
                sh 'id'
                sh 'export PYTHONPATH=`pwd`/src:`pwd`/tests;' +
                    ' pip install pytest; ' +
                    ' pytest -v ' +
                    ' --cov=. ' +
                    ' --cov-config .coveragerc' +
                    ' --junitxml=xunit-reports/xunit-result-$(date +%Y-%m-%d_%H-%M-%S).xml' +
                    ' --cov-report xml:coverage-reports/coverage-$(date +%Y-%m-%d_%H-%M-%S).xml' +
                    ' --rootdir=. || true'
            }
        }
    }
//    post {
//        unstable {
//            mail to: "${env.CHANGE_AUTHOR_EMAIL}",
//                    subject: "Unstable Pipeline: ${currentBuild.fullDisplayName}",
//                    body: "Something is wrong with ${env.BUILD_URL}"
//        }
//        failure {
//            mail to: "${env.CHANGE_AUTHOR_EMAIL}",
//                    subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
//                    body: "Something is wrong with ${env.BUILD_URL}"
//        }
//        aborted {
//            mail to: "${env.CHANGE_AUTHOR_EMAIL}",
//                    subject: "Aborted Pipeline: ${currentBuild.fullDisplayName}",
//                    body: "Something is wrong with ${env.BUILD_URL}"
//        }
//        changed {
//            mail to: "${env.CHANGE_AUTHOR_EMAIL}",
//                    subject: "Changed Pipeline: ${currentBuild.fullDisplayName}",
//                    body: "Something is changed with ${env.BUILD_URL}"
//        }
//    }
}