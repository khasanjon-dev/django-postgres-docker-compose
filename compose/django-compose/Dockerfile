FROM python:3.10.6-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r /requirements.txt

COPY compose/django-compose/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint



COPY compose/django-compose/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["sh", "/entrypoint"]