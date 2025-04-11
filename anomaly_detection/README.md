Time Series Anomaly Detection Pipeline with MLflow and TimescaleDB
===================================================================

This project demonstrates a complete pipeline for time series anomaly detection using TimescaleDB and MLflow. The pipeline includes training, evaluation, monitoring, and testing.

Project Structure
------------------

.. code-block:: text

    anomaly_detection/
    │
    ├── src/
    │   ├── train.py
    │   ├── evaluate.py
    │   ├── monitor.py
    │   ├── load_data.py
    │   └── tests/
    │       └── test_model.py
    │
    ├── mlruns/
    │
    ├── requirements.txt
    │
    └── README.rst

Setup
-----

1. Install the required packages:

    .. code-block:: bash

        pip install -r requirements.txt

2. Set up TimescaleDB and create a hypertable for your time series data.

Training the Model
-------------------

To train the model, run:

.. code-block:: bash

    python src/train.py

Evaluating the Model
---------------------

To evaluate the model, run:

.. code-block:: bash

    python src/evaluate.py

Make sure to replace ``YOUR_RUN_ID`` with the actual run ID from MLflow.

Monitoring the Model
---------------------

To monitor the model with new data, run:

.. code-block:: bash

    python src/monitor.py

Make sure to replace ``YOUR_RUN_ID`` with the actual run ID from MLflow and provide the path to the new data.

Testing the Model
------------------

To run the tests, use:

.. code-block:: bash

    pytest src/tests/test_model.py

Make sure to replace ``YOUR_RUN_ID`` with the actual run ID from MLflow.


