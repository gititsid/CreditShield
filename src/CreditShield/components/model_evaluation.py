import os
import sys
import json
import pickle
from sklearn.metrics import accuracy_score

from src.CreditShield.logger import logging
from src.CreditShield.exception import CustomException
from src.CreditShield.config.configuration import ConfigurationManager
from src.CreditShield.components.model_trainer import ModelTrainer


class ModelEvaluator:
    def __init__(self, config):
        self.config = config

    @staticmethod
    def _evaluate_model(true, predicted, log=True):
        try:
            if log:
                logging.info("> Evaluating model:")

            accuracy = accuracy_score(true, predicted)

            if log:
                logging.info("Model evaluated successfully!")

            return accuracy

        except Exception as e:
            if log:
                logging.error(f"Error occurred while evaluating model!")
            raise CustomException(e, sys)

    def _get_model(self):
        try:
            logging.info("> Getting model:")

            model_path = self.config.model_path
            model = pickle.load(open(model_path, 'rb'))

            logging.info(f"Model loaded successfully from: {model_path}")

            return model

        except Exception as e:
            logging.error(f"Error occurred while getting model!")
            raise CustomException(e, sys)

    def get_model_metrics(self):
        try:
            logging.info("> Getting model metrics:")

            model = self._get_model()

            config = ConfigurationManager()
            model_training_config = config.get_model_training_config(log=False)
            trainer = ModelTrainer(config=model_training_config)

            x_train, x_test, y_train, y_test = trainer.get_data(log=False)

            y_pred_train = model.predict(x_train)
            y_pred_test = model.predict(x_test)

            train_accuracy_score = self._evaluate_model(y_train, y_pred_train, log=False)
            test_accuracy_score = self._evaluate_model(y_test, y_pred_test, log=False)

            logging.info(f"Train metrics: Accuracy Score: {train_accuracy_score}")
            logging.info(f"Test metrics: test_accuracy_score: {test_accuracy_score}")

            train_metrics = json.dumps(
                {
                    "train_accuracy_score": train_accuracy_score
                },
                indent=4
            )

            test_metrics = json.dumps(
                {
                    "test_accuracy_score": test_accuracy_score
                },
                indent=4
            )

            train_metrics_path = self.config.train_metrics
            test_metrics_path = self.config.test_metrics

            with open(train_metrics_path, 'w') as file:
                file.write(train_metrics)

            with open(test_metrics_path, 'w') as file:
                file.write(test_metrics)

            logging.info(f"Model metrics are ready. Saved at: {train_metrics_path}, {train_metrics_path}!")

        except Exception as e:
            logging.error(f"Error occurred while getting model metrics!")
            raise CustomException(e, sys)


if __name__ == '__main__':
    config_manager = ConfigurationManager()
    model_evaluation_config = config_manager.get_model_evaluation_config()
    model_evaluator = ModelEvaluator(config=model_evaluation_config)
    model_evaluator.get_model_metrics()
