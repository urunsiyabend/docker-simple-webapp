# docker-simple-webapp

A minimal Dockerized Python Flask web server.

## Project Structure

```
.
├── Dockerfile          # Docker image configuration
├── requirements.txt    # Python dependencies
├── app/
│   └── app.py          # Flask application
└── README.md
```

## Getting Started

### Build the Docker image

```bash
docker build -t simple-webapp .
```

### Run the container

```bash
docker run -p 5000:5000 simple-webapp
```

### Test the endpoint

```bash
curl http://localhost:5000/
```

Returns: `Hello World.`

## Running locally (without Docker)

```bash
pip install -r requirements.txt
python app/app.py
```