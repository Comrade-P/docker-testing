# 1. Use official Python image
FROM python:3.11-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your Python script
COPY ss.py .

# 6. Run the script
CMD ["python", "ss.py"]
