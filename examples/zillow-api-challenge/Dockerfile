FROM python:3.7

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY zillow/ .
RUN python manage.py migrate && python manage.py add_data challenge_data.csv

ENTRYPOINT ["python", "manage.py"]