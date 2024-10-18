FROM python:3.11-slim
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080 8081
CMD ["sh", "-c", "uvicorn app.v1.main:app --host 0.0.0.0 --port 8080 & python app/v1/dash_app.py"]