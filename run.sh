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


TRAINING_DATASET=gs://workshop-datasets/covertype/training/dataset.csv
SCORING_MEASURE=accuracy
NUM_JOBS=2
SEARCH_SPACE="[\
{'classifier':'sklearn.linear_model.SGDClassifier',\
'classifier__alpha':[0.1,0.2,0.3],\
'classifier__max_iter':[100,150,200]}\
]"


python hypertune.py $TRAINING_DATASET $SEARCH_SPACE $SCORING_MEASURE $NUM_JOBS
