from collections import  namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url",
                                                        "data_ingestion_dir",
                                                        "raw_data_dir",
                                                        "ingested_data_dir"
                                                    ])

DataValidationConfig = namedtuple("DataValidationConfig",['data_validation_dir',
                                                         'clean_data_dir',
                                                         'serialized_data_dir',
                                                         'book_csv_file',
                                                         'ratings_csv_file'
                                                    ])
