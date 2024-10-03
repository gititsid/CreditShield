import sys

from src.CreditShield.constants import *

from src.CreditShield.logger import logging
from src.CreditShield.exception import CustomException
from src.CreditShield.utils.common import read_yaml, create_directories
from src.CreditShield.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH):

        self.config = read_yaml(config_filepath)

        # Artifact root directory
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self, log=True) -> DataIngestionConfig:
        try:
            if log:
                logging.info("Getting data ingestion configuration:")

            config = self.config.data_ingestion

            create_directories([config.root_dir])

            data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                data_file=config.data_file,
                unzip_dir=config.unzip_dir,
                internal_raw_file=config.internal_raw_file,
                external_raw_file=config.external_raw_file
            )

            if log:
                logging.info("Data ingestion configuration loaded successfully!")

            return data_ingestion_config

        except Exception as e:
            if log:
                logging.error(f"Error occurred while getting data ingestion configuration!")
            raise CustomException(e, sys)

