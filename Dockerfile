FROM python:3.11

WORKDIR / code

RUN pip install --upgrade pip \
    && pip install poetry

COPY /pyproject.toml poetry.lock /

RUN poetry install

COPY . .

CMD ["sh", "-c", "python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]
