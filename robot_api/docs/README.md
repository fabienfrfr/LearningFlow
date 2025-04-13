# Robot Control Project

This project provides a comprehensive solution for controlling robots using a microservices architecture.

## Features

- Robot control via API
- Kafka messaging for event-driven architecture
- MinIO for object storage
- PostgreSQL for relational data storage
- Kubernetes and Pulumi for deployment
- MLFlow for ML model lifecycle management

## Setup

### Prerequisites

1. **Install Docker**: Ensure Docker is installed and running on your machine.
2. **Install Pulumi**: Follow the [Pulumi installation guide](https://www.pulumi.com/docs/get-started/install/) to install Pulumi CLI.
3. **Install Python**: Ensure Python 3.9 or later is installed.
4. **Install Node.js**: Required for the React frontend.

### Local Infrastructure Setup with Pulumi

1. **Navigate to the Pulumi directory**:
```bash
cd deployment/pulumi
```

2. Login to Pulumi: If you haven't already, login to Pulumi using the CLI.

```bash
pulumi login
```

3. Set up your Pulumi stack:

```bash
pulumi stack init dev
```

4. Deploy the infrastructure:

```bash
pulumi up
```

This command will create the necessary infrastructure components locally or on your preferred cloud provider.

### Running the Application with Docker
1. Build the Docker image:

```bash
docker build -t robot-control-app .
```

2. Run the Docker container:

```bash
docker run -d -p 80:80 robot-control-app
```

This will start the application, and it will be accessible at http://localhost.

### Running the Application Locally
1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the FastAPI application:

```bash
uvicorn src.interfaces.api.fastapi_app\:app --reload
```

The application will be available at http://localhost:8000.

### Running the React Frontend
1. Navigate to the React app directory:

```bash
cd src/interfaces/web
```

2. Install dependencies:

```bash
npm install
```

3. Start the React application:

```bash
npm start
```

The frontend will be available at http://localhost:3000.

### Testing
Run tests using pytest:

```bash
pytest
```