from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"


try:
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f'>>>>> stage {STAGE_NAME} Completed <<<<<<')
except Exception as e:
        logger.exception(e)
        raise e

#create pipeline for basemodel pipeline

STAGE_NAME = 'Prepare Base Model'

try:
        logger.info(f'***************************************')
        logger.info(f'>>>>> stage {STAGE_NAME} started <<<<<<')
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f'>>>>> stage {STAGE_NAME} Completed <<<<<<')
except Exception as e:
    raise e
