from fastapi import FastAPI
import logging
import os


LOG_DIR = "/var/log/fastapi"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "myapp.log")

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "detailed": {
            "format": (
                "%(asctime)s | %(levelname)-8s | %(name)s | "
                "%(filename)s:%(lineno)d | %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
        "json": {
            "format": '{"timestamp": "%(asctime)s", "level": "%(levelname)s", '
                      '"name": "%(name)s", "message": %(message)s}',
            "datefmt": "%Y-%m-%dT%H:%M:%S",
        },
        "console": {
            "format": "%(asctime)s - %(levelname)s - %(message)s",
            "datefmt": "%H:%M:%S",
        },
    },

    "handlers": {
        "file_rotating": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "detailed",
            "filename": LOG_FILE,
            "when": "midnight",      # Rotate at midnight
            "backupCount": 7,        # Keep 7 days of logs
            "encoding": "utf-8",
            "level": "DEBUG",
            "utc": True,
        },
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "level": "INFO",
        },
    },

    "loggers": {
        "uvicorn.error": {
            "handlers": ["file_rotating", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["file_rotating", "console"],
            "level": "INFO",
            "propagate": False,
        },
        "myapp": {  # Your app's logger
            "handlers": ["file_rotating", "console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },

    "root": {
        "handlers": ["file_rotating", "console"],
        "level": "WARNING",
    },
}

logging.config.dictConfig(LOGGING_CONFIG)
app = FastAPI()
logger = logging.getLogger("myapp")

app.debug = False

@app.get("/health")
async def health_check():
    logger.info("Health check endpoint called")
    return {"status": "ok"}
@app.get("/login")
async def login():
    logger.warning("Login endpoint called")
    return {"message": "Login endpoint"}
@app.get("/logout")
async def logout():
    logger.error("Logout endpoint called")
    return {"message": "Logout endpoint"}
@app.get("/data")
async def get_data():
    logger.info("Data endpoint called")
    return {"data": "Here is some data"}    
@app.get("/status")
async def status():
    logger.debug("Status endpoint called")
    return {"status": "Service is running"}
@app.post("/")
async def home():

    return {"message": "Welcome to the FastAPI application!"}
@app.get("/")
async def read_root():
    logger.warning("Root endpoint called")
    return {"message": "Welcome to the FastAPI application!"}

@app.get("/error")
async def generate_error():
    try:
        1 / 0
    except ZeroDivisionError as e:
        # logger("An error occurred: %s", e)
        return {"error": "An internal error occurred"}
    return {"message": "This will never be reached"}