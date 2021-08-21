FROM python:3-slim

WORKDIR /get_to_tg

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "gunicorn", "-b :8000", "get_to_tg:app" ]