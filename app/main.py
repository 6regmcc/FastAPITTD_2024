from fastapi import FastAPI
import logging
import logging.config


logging.config.fileConfig("./logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

app = FastAPI()



@app.get("/hello")
def hello():
    logger.error('test error')
    return {"Hello": "How are you doing?"}

