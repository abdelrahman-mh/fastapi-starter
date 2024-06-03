# Python Scraping - Server

The server is built with [FastAPI](https://fastapi.tiangolo.com/), [SQLModel](https://sqlmodel.tiangolo.com/), Async With [https://www.psycopg.org/](), [PostgresQL](https://www.postgresql.org/), and [Adminer](https://www.adminer.org/)

## Development

- Start the entire stack with Docker Compose:

  ```shell
  docker compose up -d
  ```

- Now you can access these URLs:

**Server**: JSON-based web API based on OpenAPI: [http://localhost:8888](http://localhost:8888)

Automatic interactive documentation with Swagger UI (from the OpenAPI backend): [http://localhost:8888/docs](http://localhost:8888/docs)

**Adminer**: Database web administration: [http://localhost:8080](http://localhost:8080)

### Docker Compose Override

This file settings affect local development. In this file, we map the **ports**, disable auto-restart, handle volumes, etc. You can add additional development configurations as needed ✨.

In development, when you run `docker compose up -d`, the image runs `/start-reload.sh` (in the root of the `server` services) instead of the default `/start.sh` (used in production). This script runs the app in auto-reload mode and also triggers the `/prestart.sh` script.

- **start-reload.sh & start.sh**: These scripts mainly run the `fastapi` app, but before running it, they execute `/prestart.sh`.

- **prestart.sh**: This script triggers `/app/backend_pre_start.py` and `initial_data.py` before the main app runs. They check the database health status and create the database tables for the `sqlmodel` models (if they do not exist).
  > Those files copied to the root of the image in `Dockerfile`
