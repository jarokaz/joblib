# Parallel hyperparameter tuning with `scikit-learn` and `dask-ml`

This code sample demonstrates how to run a parallel hyperparameter tuning regime for [scikit-learn](https://scikit-learn.org/stable/) using [dask-ml](https://ml.dask.org/index.html) - a library for distributed and parallel machine learning.

The sample uses very basic features of `dask-ml`, specifically the [local distributed scheduler](https://docs.dask.org/en/latest/setup/single-distributed.html) and [dask_ml.model_selection.GridSearchCV`](https://ml.dask.org/hyper-parameter-search.html) class. To further improve performance on large, multi-CPU and high memory machines, the reader can consider utilizing other features of `dask-ml` like [parallel preprocessing](https://ml.dask.org/preprocessing.html), and [parallel estimators](https://ml.dask.org/glm.html)

The sample walks you through two scenarios:
- Running a parallel hypertuning job locally on a multi-CPU AI Platform notebook
- Running a parallel hypertuning job using Cloud AI Platfom Training.



## Running a parallel hypertuning job locally on a multi-CPU AI Platform notebook

### Creating an instance of AI Platform Notebooks 
In this step you will create an instance of **AI Platform Notebooks** using a custom container image. The custom container image is a derivative of the standard Python CPU Deep Learning Container extended with [dask-ml](https://pypi.org/project/dask-ml/) and [fire](https://google.github.io/python-fire/guide/) Python packages.

