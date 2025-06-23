from collections import  namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url",
                                                        "data_ingestion_dir",
                                                        "raw_data_dir",
                                                        "ingested_data_dir"
                                                    ])