FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements dulu (biar cache lebih optimal)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh project
COPY . .

# Run bot
CMD ["python", "bot.py"]
