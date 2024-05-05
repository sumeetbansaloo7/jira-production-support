FROM --platform=linux/amd64 python:3.9

WORKDIR /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app/

# CMD ["fastapi", "run", "main.py", "--port", "8000"]
