FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
COPY sender.py .
COPY ip_addresses.csv .
CMD ["python", "sender.py"]