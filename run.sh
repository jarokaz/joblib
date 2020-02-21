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
MAX_ITER='[100,150,200]'
ALPHA='[0.01,0.05,0.1]'
NUM_JOBS=4

python hypertune.py $TRAINING_DATASET $ALPHA $MAX_ITER $NUM_JOBS
