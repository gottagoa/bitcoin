FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV TZ=Asia/Bishkek


RUN apk add libffi-dev\
    gcc libc-dev
RUN apk add --no-cache linux-headers make python3-dev sqlite-dev \
    && pip install --upgrade pip 

WORKDIR /app

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "dockerfiles/docker_entrypoint.sh"]