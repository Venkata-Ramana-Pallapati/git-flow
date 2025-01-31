FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip3 install uvicorn 
RUN python3 -m venv venv
RUN ./venv/bin/pip install --upgrade pip  # Ensure pip is up-to-date
RUN ./venv/bin/pip install -r requirements.txt  # Install dependencies

#RUN source venv/bin/activate

# Copy the application code
COPY . .

# Expose the port and run the server
EXPOSE 8045
CMD ["uvicorn", "book:app", "--host", "0.0.0.0", "--port", "8045"]
