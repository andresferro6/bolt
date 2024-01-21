# Python Flask API with Docker

This is a simple Flask API application that serves data from a DataFrame using Docker. The data is read from an Excel file (`data.xlsx`) in the same folder as the application.

## Requirements

- Docker

## Build and Run

1. Build the Docker image:

    ```bash
    docker build -t flask-api .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 5000:5000 flask-api
    ```

The Flask API will be accessible at [http://localhost:5000/get_data](http://localhost:5000/get_data).

## Note

- The `data.xlsx` file should be present in the same folder as the `app.py` file.
- This is a minimal example for educational purposes.
