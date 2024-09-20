# IMS Customer Microservice

The **Customer Microservice** is responsible for managing customers of the user. It allows users to add, update, and delete customers — essentially performing CRUD operations. Users can only disable and delete those customers that have not been used in any of the transactions. All endpoints in this microservice are secure and require an Auth0 access token for authorization.

## 🚀 Tech Stack

- **Framework**: FastAPI
- **Database**: AWS RDS (PostgreSQL)
- **ORM**: SQLModel (built on top of Pydantic and SQLAlchemy)
- **Authentication**: OAuth2.0 by Auth0

This microservice adheres to industry-standard coding practices, including:

- Use of type annotations throughout the codebase for better readability and type safety.
- Validators are used to parse the input into respective classes and validate the content coming in the requests
- Modular programming and recommended folder structure to reuse the components as much as possible.
- Separation of configuration (e.g., authentication and database credentials) using environment variables for security and flexibility.

## 🛠️ Features

- **CRUD operations** for customers.
- **Secure endpoints**: All routes require an Auth0 access token for authentication and authorization.

## Project Structure

- **Root Directory**:
  - `README.md`
  - `.env` (environment file, to be created)
  - `Dockerfile`
  - `requirements.txt`
  - `app/` (Main application folder)
    - `__init__.py`
    - `main.py`
    - `config/`
      - Files related to config of app
    - `database/`
      - Files operating directly on database
    - `exceptions/`
      - Custom exception classes
    - `models/`
      - Models to parse input and output data into
    - `routes/`
      - Routes for this service
    - `service/`
      - Service layer between end points and database layer
    - `utils/`
      - Additional utilities like validators.

## 🔧 Running the Project Locally

### Prerequisites

- Python 3.12
- Postgres database or AWS RDS setup
- Auth0 setup (domain, audience, issuer, and algorithms)

### Step-by-step Instructions

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd ims_customer
   ```

2. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables:** Create a .env file in the root directory with the following details:

   ```makefile
   AUTH0_DOMAIN="<auth0_domain>"
   AUTH0_API_AUDIENCE="<auth0_audience>"
   AUTH0_ISSUER="<auth0_issuer>"
   AUTH0_ALGORITHMS="<algo>"
   ORIGIN="*"
   DB_URL="<DB_URL>"
   ```

4. **Run in Development Mode:**

   ```bash
   fastapi dev app/main.py
   ```

5. **Run in Production Mode:**
   ```bash
   fastapi run app/main.py
   ```

## 🐳 Docker Setup

A `Dockerfile` is provided for containerizing the application. To build and run the Docker image locally:

1. Build the Docker image:

   ```bash
   docker build . -t <image name>
   ```

2. Run the conatiner locally:
   ```bash
   docker run -d -p 8000:8000 <image name>
   ```

## 📑 Future Work

1. ### Test Suite

   - Plan to introduce unit tests and integration tests for the microservice.
   - Tests will ensure that the endpoints, database interactions, and security layers work as expected.
   - Use pytest or FastAPI’s inbuilt testing features to mock services and test responses.

2. ### CI/CD Pipeline

   - Plan to implement a CI/CD pipeline using GitHub Actions or AWS CodePipeline.
   - Automated builds, tests, and deployments to ECS will ensure smooth production deployments.
   - Integration with DockerHub or ECR for managing Docker images.

3. ### Enhanced Security
   - In future iterations, implement rate limiting and role-based access control (RBAC) to make the endpoints more secure.

# 📖 Documentation

- FastAPI Docs: Once running, access the interactive API documentation at /docs or /redoc for details on how to use the available endpoints.

# 💡 Contributing

Feel free to raise issues or contribute to this project. Fork the repo, create a feature branch, and open a pull request for your changes.
