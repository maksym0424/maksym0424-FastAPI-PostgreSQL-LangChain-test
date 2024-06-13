#!/bin/bash
# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 -t 600 app.main:app --log-config ./config.ini --log-level debug --reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-config ./config.ini --log-level debug --lifespan=on --use-colors --loop uvloop

# gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 -t 600 app.main:app --log-config ./config.ini --log-level debug