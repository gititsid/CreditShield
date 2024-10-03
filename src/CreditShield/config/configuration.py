import sys

from src.CreditShield.constants import *

from src.CreditShield.logger import logging
from src.CreditShield.exception import CustomException
from src.CreditShield.utils.common import read_yaml, create_directories
from src.CreditShield.entity.config_entity import DataIngestionConfig, DataValidationConfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 internal_raw_data_schema_filepath=INTERNAL_RAW_DATA_SCHEMA_FILE_PATH,
                 external_raw_data_schema_filepath=EXTERNAL_RAW_DATA_SCHEMA_FILE_PATH
                 ):

        self.config = read_yaml(config_filepath)
        self.internal_raw_data_schema = read_yaml(internal_raw_data_schema_filepath)
        self.external_raw_data_schema = read_yaml(external_raw_data_schema_filepath)

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

    def get_data_validation_config(self, log=True) -> DataValidationConfig:
        try:
            if log:
                logging.info("Getting data validation configuration:")

            config = self.config.data_validation
            internal_raw_data_schema = self.internal_raw_data_schema.features
            external_raw_data_schema = self.external_raw_data_schema.features

            create_directories([config.root_dir])

            data_validation_config = DataValidationConfig(
                root_dir=config.root_dir,
                internal_raw_file=config.internal_raw_file,
                external_raw_file=config.external_raw_file,
                internal_file_val_status=config.internal_file_val_status,
                external_file_val_status=config.external_file_val_status,
                internal_data_schema=internal_raw_data_schema,
                external_data_schema=external_raw_data_schema
            )

            if log:
                logging.info("Data validation configuration loaded successfully!")

            return data_validation_config

        except Exception as e:
            if log:
                logging.error(f"Error occurred while getting data validation configuration!")
            raise CustomException(e, sys)

