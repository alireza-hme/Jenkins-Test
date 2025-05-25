FROM jenkins/jenkins:lts-jdk17

USER root

ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"

RUN jenkins-plugin-cli --plugins github junit

USER jenkins

EXPOSE 8080 50000
