FROM python:3.8.13-slim

# Creating a user...
RUN addgroup --system usergroup
RUN adduser --system user --ingroup usergroup
USER user:usergroup

WORKDIR /app
ENV PATH="${PATH}:/home/user/.local/bin"

# Installing dependencies.
RUN python -m pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./calculator .

# Python environment vars.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

CMD ["python", "main.py"]