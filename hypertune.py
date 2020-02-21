# Copyright 2019 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import importlib
import logging
import os
import subprocess
import sys
import time

import fire
import pickle
import numpy as np
import pandas as pd
import sklearn

from sklearn.compose import ColumnTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
 



NUMERIC_FEATURE_INDEXES = slice(0, 10)
CATEGORICAL_FEATURE_INDEXES = slice(10, 12)

  
def train_evaluate(training_dataset_path, search_space, scoring_measure, num_jobs):
  """Performs model selection and hyperparameter tuning""" 

  # Load training data and convert all numeric features to float
  logging.info("Loading data from: {}".format(training_dataset_path))
  df_train = pd.read_csv(training_dataset_path)
  num_features_type_map = (
    {feature: 'float64' for feature in df_train.columns[NUMERIC_FEATURE_INDEXES]})
  df_train = df_train.astype(num_features_type_map)

  # Define the training pipeline
  preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), NUMERIC_FEATURE_INDEXES),
        ('cat', OneHotEncoder(), CATEGORICAL_FEATURE_INDEXES) 
    ])

  pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier', SGDClassifier())
  ])
  
  # Configure hyperparameter tuning
  
  # In the parameter grid (search_space) replace 
  # the names of classifiers with class instances
  for classifier in search_space:
    module_name, class_name = classifier["classifier"].rsplit(".", 1)
    ClassifierClass = getattr(importlib.import_module(module_name), class_name)
    classifier["classifier"] = [ClassifierClass()]
    
  grid = GridSearchCV(pipeline, cv=5, n_jobs=num_jobs, 
                      param_grid=search_space, 
                      scoring=scoring_measure)
  
  # Start training
  X_train = df_train.drop('Cover_Type', axis=1)
  y_train = df_train['Cover_Type']
  
  logging.info("Starting training")
  t0= time.time()
  grid.fit(X_train, y_train)
  t1 = time.time()
  logging.info("Time elapsed: {}".format(t1 - t0)) 
  
  logging.info("Best estimator: {}".format(grid.best_params_))
  logging.info("Best score: {}".format(grid.best_score_))
  
  # Save the model
  #if not hptune:
  #  model_filename = 'model.pkl'
  #  with open(model_filename, 'wb') as model_file:
  #      pickle.dump(pipeline, model_file)
  #  gcs_model_path = "{}/{}".format(job_dir, model_filename)
  #  subprocess.check_call(['gsutil', 'cp', model_filename, gcs_model_path], stderr=sys.stdout)
  #  print("Saved model in: {}".format(gcs_model_path)) 
    
if __name__ == "__main__":
  logging.basicConfig(level=logging.INFO)
  fire.Fire(train_evaluate)