FROM svizor/zoomcamp-model:3.11.5-slim
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile
COPY your_flask_script.py .
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:9696",
