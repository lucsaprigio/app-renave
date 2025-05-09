FROM python:3.11-slim

WORKDIR /app

COPY requiriments.txt .
RUN pip install --no-cache-dir -r requiriments.txt

COPY . .

EXPOSE 8000

CMD ["python", "main.py"]