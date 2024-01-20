FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set the default argument for the Flask app
ENV FLASK_RUN_ARGUMENT "listen:5000"

# Make the script executable
ENTRYPOINT ["python", "main.py"]

# Default command, you can override this at runtime
CMD ["$FLASK_RUN_ARGUMENT"]
