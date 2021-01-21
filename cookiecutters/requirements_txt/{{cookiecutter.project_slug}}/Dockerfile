# TODO: 2 phase builds.
#FROM	python:3.8.0-slim-buster
## FROM 3.8.7-alpine3.12
#LABEL	version="{{cookiecutter.version}}"
#LABEL	name="{{cookiecutter.project_slug}}"
#LABEL	maintainer="example@example.com"

# This version of python gets a clean ECR
FROM amazon/aws-lambda-python:3.8

WORKDIR /var/task
# Keeps image size small. The synax for disabling caching is counterintuitive
ENV PIP_NO_CACHE_DIR=off
# Ensures logging to stdout will be captured even if the application crashes
ENV PYTHONUNBUFFERED=1

# shadow utils let you add users
RUN python -m pip install --no-cache-dir --upgrade pip --quiet \
    && python --version && pip --version && echo $ENV \
    && yum install -y shadow-utils

COPY dist/*.whl /var/task
COPY dist/*.sdist /var/task

# TODO: Install from private pypi
# RUN pipenv sync
# RUN pip install --target . -r requirements.txt
RUN pip install {{cookiecutter.project_slug}}-*.sdist

# WARNING! Syntax for AWS Linux
# This has the app running as a limited user instead of root.
RUN /usr/sbin/adduser app_user && \
    /usr/sbin/groupadd app_user_group && \
    /usr/sbin/usermod -a -G sapp_user_group app_user_user && \
    chown app_user_user:app_user_group /var/task/
USER app_user_user

ENTRYPOINT ["python", "-m", "{{cookiecutter.project_slug}}" ]


