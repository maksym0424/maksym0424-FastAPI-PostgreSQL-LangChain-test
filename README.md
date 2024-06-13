# FastAPI + Postgres + SQLAlchemy + Alembic + LangChain + OpenAI + Tavily.

*Postgres database is hosted on GCP, and connecting to it using Cloud SQL.*

**This is a test-assignment project source code that can evaluate your knowledge with FastAPI, GCP Postgres database, SQLAlchemy, Alembic, Docker, and LangChain agents + OpenAI**

### Feel Free to evaluate your knowledge with this test assignment and compare the result with source code!

### Duration: Maximum 3 hours

# Assignment

1. Create a FastAPI app and connect to the DB (always use async methods wherever possible such as create_async_engine, async_sessionmaker...). Use SQLAlchemy + Alembic as the ORM. Connect using [Cloud SQL Language Connector](https://cloud.google.com/sql/docs/postgres/connect-connectors).
2. Import a deal CSV file to the database with Python. Add an additional column `created_at` that will hold the row creation time. Please use the database native time for this.
3. Add an extra column (`merchant_about`) to the database. For now, this column will be null. Create a handler on FastAPI that will return the value of this new column (null for now) when sending a GET request with the domain as a URL parameter.
4. With the available info in the CSV, create an agent to get information about the merchant (basically, what does it sell). You can should use LangChain's agent [tools](https://python.langchain.com/v0.1/docs/integrations/tools/) for this. Please use free tools or tools with a free trial. Store the output in the `merchant_about` column. You can see an example below.
   - Input: the agent will have access to the `home_page` and `merchant_name`
   - Output: the agent should create the content of the `merchant_about` column

5. Run the agent on a few examples and evaluate the prompt using a LangChain evaluator (you can use any evaluator as long as it makes some sense).
