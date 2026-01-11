FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .

EXPOSE 8000

CMD ["streamlit", "run", "main.py", "--server.port=8080", "--server.address=0.0.0.0"]
