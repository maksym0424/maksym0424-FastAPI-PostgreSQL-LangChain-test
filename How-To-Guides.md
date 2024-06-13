# How to run server

1. Clone the repository
2. Add ```.env``` file inside ```/backend``` directory.

    ```
    INSTANCE_CONNECTION_NAME=ctxl-yurii:us-central1:assignment-db
    DB_USER=postgres
    DB_PASSWORD=postgres
    db_name=postgres
    OPENAI_API_KEY=<sk-..>
    TAVILY_API_KEY=<tvly-...>
    ```

3. Download your GCP credential and copy it to ```/backend``` directory, rename it to ```secret_for_credentials.json```.

4. Run ```docker compose build``` and ```docker compose up```.