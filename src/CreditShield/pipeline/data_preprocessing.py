import sys
from src.CreditShield.logger import logging
from src.CreditShield.exception import CustomException
from src.CreditShield.config.configuration import ConfigurationManager
from src.CreditShield.components.data_preprocessing import DataPreprocessing


STAGE_NAME = "Data Preprocessing"


class DataPreprocessingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config_manager = ConfigurationManager()
        data_preprocessing_config = config_manager.get_data_preprocessing_config()
        data_preprocessing = DataPreprocessing(config=data_preprocessing_config)

        data_preprocessing.save_merged_data()
        data_preprocessing.get_preprocessed_data(save_csv=True)


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

        data_validator = DataPreprocessingPipeline()
        data_validator.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

    except Exception as e:
        logging.error(f"Error occurred while running {STAGE_NAME}!")
        raise CustomException(e, sys)
