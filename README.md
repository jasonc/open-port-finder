# Open Port Finder

A lightweight web application that helps you find the next available network port on your system. Perfect for Docker container port mapping, service configuration, and development environments.

## Quick Start

### Using Docker Compose (recommended)

1. Clone the repository
```bash
git clone https://github.com/jasonc/open-port-finder.git
cd open-port-finder
```

2. Start the application
```bash
docker compose up -d
```

3. Access the web interface at `http://localhost:56789`

### Using Docker directly

1. Build the image
```bash
docker build -t open-port-finder .
```

2. Run the container
```bash
docker run --network host open-port-finder
```


## API Usage

Example using curl:
```bash
curl http://localhost:56789/find_port/8080
```

Response:
```json
{
    "success": true,
    "port": 8080,
    "message": "The next available port is 8080"
}
```
