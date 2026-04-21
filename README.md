# Flask Snippets API

This project serves as a learning sandbox for transitioning from serverless, event-driven Python development to persistent, containerized application architecture.

## The "Why"
During my software development career, most of my Python work has been built and maintained on an event-based architecture using AWS Lambda. As I look to expand my architectural capabilities, I am building this repository to explore the **Flask framework**. 

This project simulates the transition I am making toward developing Python APIs and platforms hosted on persistent **AWS Instance/Fargate infrastructure**, focusing on state management, database connectivity, and repository patterns.

## Features
- **RESTful API:** Basic CRUD operations for managing code snippets.
- **Repository Pattern:** Logic is decoupled from the storage engine to ensure the business logic remains independent of the database implementation.
- **Database Persistence:** Currently uses **SQLite** for local development, with a structure designed to be easily swappable for production-grade databases (like PostgreSQL or DynamoDB) using the Repository pattern.

## Local Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YoshieLaw/python_flask_test.git
   cd python_flask_test
    ```

2. **Create and activate a virtual environment:**
   ```bash
    # Windows:
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux:
    python -m venv venv
    source venv/bin/activate
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the application:**
    ```bash
    python app.py
## API Usage
Once the server is running (default http://127.0.0.1:5000), you can interact with the API:

1. Create a snippet (POST):
    ```bash
    curl.exe -X POST http://127.0.0.1:5000/api/snippets -H "Content-Type: application/json" -d '{\"content\": \"My first code snippet\"}'
2. Get all snippets (GET):
    ```bash
    curl http://127.0.0.1:5000/api/snippets
3. Update a Snippet (PUT/PATCH):
    ```bash
    curl.exe -X PUT http://127.0.0.1:5000/api/snippets/1 -H "Content-Type: application/json" -d '{\"content\": \"Updated content here\"}'
4. Delete a Snippet (DELETE):
    ```bash
    curl.exe -X DELETE http://127.0.0.1:5000/api/snippets/1
