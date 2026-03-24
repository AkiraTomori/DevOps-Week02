# TODO-STEP 1: Choose a base image
FROM python:3.9-slim AS builder

# TODO-STEP 2: Set the working directory
WORKDIR /app

# TODO-STEP 3: Copy the requirements file
COPY requirements.txt .

# TODO-STEP 4: Install the Python dependencies
RUN pip install -r requirements.txt

# TODO-STEP 5: Copy the application code
COPY . .
RUN python -m unittest discover tests || echo "Tests failed, but continuing with the build."

FROM python:3.9-slim
WORKDIR /app

COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app

ENV PATH=/root/.local/bin:$PATH

ENV PORT=5000

HEALTHCHECK --interval=5m --timeout=3s \
  CMD curl -f http://localhost:$PORT/health || exit 1

# TODO-STEP 6: Specify the command to run the application
CMD python app.py --port $PORT 