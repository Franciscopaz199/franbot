FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py Gemeni.py .env.example ./

CMD ["python", "main.py"]