FROM python:3.10

WORKDIR /app/

# Upgrade pip and install dependencies
COPY ./requirements.txt /app/
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade -r /app/requirements.txt


ENV PYTHONPATH=/app

# Scprt runs before the app run, he check the db status, and init db data (tables)
COPY ./prestart.sh /app/

# Run development server script
COPY ./start-reload.sh /

# Run production server script
COPY ./start.sh /

COPY ./app /app/app

CMD [ "/start.sh" ]