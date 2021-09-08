FROM python:3.8

COPY . /app

WORKDIR /app

# Install dependencies
RUN pip install  --no-cache-dir -r requirements.txt

# Set up database
RUN python init_db.py

# The port the container's app is listening to
EXPOSE 3111

ENTRYPOINT [ "python", "app.py" ]
