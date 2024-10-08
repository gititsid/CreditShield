from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    data_file: Path
    unzip_dir: Path
    internal_raw_file: Path
    external_raw_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    internal_raw_file: Path
    external_raw_file: Path
    internal_file_val_status: Path
    external_file_val_status: Path
    internal_data_schema: dict
    external_data_schema: dict


@dataclass(frozen=True)
class DataPreprocessingConfig:
    root_dir: Path
    internal_raw_file: Path
    external_raw_file: Path
    cleaned_raw_dataset: Path
    preprocessed_dataset: Path
    cat_features: list
    num_features: list
    target_variable: str


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    preprocessed_dataset: Path
    cat_features: list
    num_features: list
    target_variable: str
    data_transformer: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    model_params: dict
    experiment_name: str
    model_path: Path


@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path: Path
    experiment_name: str
    train_metrics: Path
    test_metrics: Path


@dataclass(frozen=True)
class PredictionConfig:
    model_path: Path
    experiment_name: str
    data_transformer: Path

