FROM python:3
ENV PTYHONUNBUFFERED 1
WORKDIR /app
RUN pip install flask