FROM jenkins/jenkins:lts

USER root

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Skip initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

# Install plugins
RUN jenkins-plugin-cli --plugins github junit

USER jenkins

EXPOSE 8080
