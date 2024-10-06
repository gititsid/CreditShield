import sys
from src.CreditShield.logger import logging
from src.CreditShield.exception import CustomException
from src.CreditShield.config.configuration import ConfigurationManager
from src.CreditShield.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    @staticmethod
    def main():
        config_manager = ConfigurationManager()
        model_training_config = config_manager.get_model_training_config()
        model_trainer = ModelTrainer(config=model_training_config)

        model_trainer.train_model()


if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage '{STAGE_NAME}' started <<<<<<")

        model_training = ModelTrainingPipeline()
        model_training.main()

        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

    except Exception as e:
        logging.error(f"Error occurred while running {STAGE_NAME}!")
        raise CustomException(e, sys)
