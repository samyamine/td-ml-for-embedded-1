FROM python:3.10.12
WORKDIR /app

COPY main.py .
COPY regression.joblib .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# EXPOSE 8000
# CMD ["uvicorn", "main:app"]