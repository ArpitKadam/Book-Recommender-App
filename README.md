# Book-Recommender-App

Steps to make Data Pipeline in Dagshub

Initialize DVC:
dvc init

Edit the dvc.yaml file that is created 
Example for that is given below

Add Data to the Pipeline
dvc add <data-file-or-directory>

Commit Changes:
git add .  # Add DVC metadata and tracked files
git commit -m "Added raw data to pipeline"
git push

Push Data to DagsHub Storage:
dvc push

======================================================================================================================

Example dvc.yaml
Note: Change the file names

stages:
  data_ingestion:
    cmd: python src/Insurance_Fraud/components/data_ingestion.py
    deps:
      - src/Insurance_Fraud/components/data_ingestion.py
      - data/insurance_claims.csv
    outs:
      - artifacts/data_ingestion/insurance_claims.csv

  data_validation:
    cmd: python src/Insurance_Fraud/components/data_validation.py
    deps:
      - src/Insurance_Fraud/components/data_validation.py
      - artifacts/data_ingestion/insurance_claims.csv
    outs:
      - artifacts/data_validation/STATUS.txt

  data_transformation:
    cmd: python src/Insurance_Fraud/components/data_transformation.py
    deps:
      - src/Insurance_Fraud/components/data_transformation.py
      - artifacts/data_validation/STATUS.txt
    outs:
      - artifacts/data_transformation/train.csv
      - artifacts/data_transformation/test.csv

  model_training:
    cmd: python src/Insurance_Fraud/components/model_trainer.py
    deps:
      - src/Insurance_Fraud/components/model_trainer.py
      - artifacts/data_transformation/train.csv
    outs:
      - artifacts/model_trainer/GradientBoostingClassifier.joblib

  model_evaluation:
    cmd: python src/Insurance_Fraud/components/model_evaluation.py
    deps:
      - src/Insurance_Fraud/components/model_evaluation.py
      - artifacts/data_transformation/test.csv
      - artifacts/model_trainer/GradientBoostingClassifier.joblib
    outs:
      - artifacts/model_evaluation/classification_report.txt
      - artifacts/model_evaluation/metrics.json




config.yaml --> config_entity --> configuration.py --> components --> pipeline --> main