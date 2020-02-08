FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install libgdal-dev -y

WORKDIR /opt/improved_engine

COPY Pipfile Pipfile.lock /opt/improved_engine/
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --system --deploy --dev

COPY ./src/entrypoint.sh .
RUN chmod +x entrypoint.sh

COPY ./src .

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
