FROM jenkins/jenkins:lts-jdk17

USER root

# Cache-busting ARG: update this value (e.g., daily) to force plugin reinstallation
ARG CACHE_DATE=2025-05-26

RUN jenkins-plugin-cli --verbose \
    --plugins \
    jjwt-api:0.11.5-120.v0268cf544b_89 \
    workflow-job:1498.v33a_0c6f3a_4b_4

RUN apt-get update && apt-get install -y docker.io && \
    usermod -aG docker jenkins 

USER jenkins

EXPOSE 8080 50000