FROM python:3.8-slim

# Configure Pipenv for running in container
ENV PIPENV_HIDE_EMOJIS=1 \
    PIPENV_IGNORE_VIRTUALENVS=1 \
    PIPENV_NOSPIN=1 \
    PIPENV_NO_CACHE_DIR=false \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Get the dependencies ready
RUN apt-get -y update \
    && apt-get clean \
    && apt-get install git -y \
    && rm -rf /root/.cache/pip/* \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv
RUN pip install pipenv

# Define the working directory
WORKDIR /app

# Copy all the files, and get dependencies ready
COPY Pipfile* ./
RUN pipenv install --system --deploy

# Copy the source files
COPY . .

# Expose the fastAPI port
EXPOSE 80

# Start the container
ENTRYPOINT ["uvicorn"]
CMD ["api:app", "--reload", "--host=0.0.0.0", "--port=80"]
