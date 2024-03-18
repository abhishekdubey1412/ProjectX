# Use the official Python image as a base
FROM python:3.11-bookworm

ENV PYTHONBUFFERED=1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# Expose port 8000 for the Gunicorn application
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "ProjectX.wsgi:application", "--bind", "0.0.0.0:8000"]