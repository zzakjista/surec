# Python Version
FROM python:3.11

# Working Directory
WORKDIR /surec

# Copy Requirements
COPY pyproject.toml .
# Copy Surec
COPY surec/. surec/.

# Install Dependencies
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# FastAPI Server
CMD ["uvicorn", "surec.service:app", "--host", "0.0.0.0", "--port", "5000"]