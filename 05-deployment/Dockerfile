
FROM svizor/zoomcamp-model:3.11.5-slim

WORKDIR /app

COPY Pipfile Pipfile.lock ./

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY your_flask_script.py ./

EXPOSE 8000

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "your_flask_script:app"]
