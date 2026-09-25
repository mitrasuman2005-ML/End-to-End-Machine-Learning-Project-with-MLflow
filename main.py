from src.mlProject import logger
from mlProject.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started ... <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed ... <<<<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e


