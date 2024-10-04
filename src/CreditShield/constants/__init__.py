from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
INTERNAL_RAW_DATA_SCHEMA_FILE_PATH = Path(PROJECT_ROOT/"internal_raw_data_schema.yaml")
EXTERNAL_RAW_DATA_SCHEMA_FILE_PATH = Path(PROJECT_ROOT/"external_raw_data_schema.yaml")
PROCESSED_DATA_SCHEMA_FILE_PATH = Path(PROJECT_ROOT/"processed_data_schema.yaml")