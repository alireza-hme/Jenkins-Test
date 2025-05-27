FROM jenkins/jenkins:lts-jdk17

USER root

ARG CACHE_DATE=2025-05-26

# Install docker and add jenkins user to docker group
RUN apt-get update && apt-get install -y docker.io && \
    groupadd -f docker && usermod -aG docker jenkins

# Install plugins
RUN jenkins-plugin-cli --verbose \
    --plugins \
    jjwt-api:0.11.5-120.v0268cf544b_89 \
    workflow-job:1498.v33a_0c6f3a_4b_4


EXPOSE 8080 50000
