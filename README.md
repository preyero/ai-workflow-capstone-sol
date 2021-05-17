# IBM AI Enterprise Workflow project
A time-series prediction model to predict revenue value from stream data. 

## Proposed solution
The solution to the objectives at each stage of the pipeline can be found at the notebook:
```bash
    ~$ jupyter-notebook main.pynb
```

Additionally, deliverables from each part of the pipeline are provided as `HTML` files:

* **Part 1 Data Exploration.html**: a single script (`scripts/cslib.py`) is used to extract a ts-dataframe from the raw json files in `cs-train` folder. Summary reports and plots of the ts are also produced.  
* **Part 2 Analysis.html**: a single script (`scripts/model.py`) is used to engineer features and train several regression models (Random Forest, Support Vector Regression, K-Neighbors Regression, Linear Regression) for predicting next month revenue. Log files are generated using the `logger.py` module to monitor performance. 
* **Part 3 Deployment.html**: an API is build using Flask (`app.py`) to get predictions for a single of the top-$K$ countries, or for all. Unit tests are provided for the model, logging, and API components, and can be run from a single script (`run-tests.py`). Model, unit tests, and API are containerized within a Docker image (`Dockerfile`).

## Requirements

To install packages according to the configuration file:
```bash
    ~$ pip install -r requirements.txt 
```

## Train models for ts-prediction

To train several `sk-learn` regression models, copy data in the `cs-train` folder and execute in Terminal from `PROJ_DIR`: 
```bash
    ~$ python scripts/model.py 
```

## Build API using Flask API
API contains train, predict, and logfile endopoints.

Run from project directory (`./ai-workflow-capstone-master`) and run:
```bash
    ~$ python app.py 
```
Check is working on port http://0.0.0.0:8080/

## User Docker Engine to run 

Start Docker and build the image from the `PROJ_DIR`
```bash
    ~$ cd ai-workflow-capstone-master
    ~$ docker build -t capstone-master .
```
Check that the image is there:
```bash
    ~$ docker image ls
```

Run the container

```bash
docker run -p 4000:8080 capstone-master
```

Ensure the app is running and accesible in  http://0.0.0.0:4000/ 

## Run unit tests
Run first

``` bash
        ~$ python app.py
```
From terminal, execute:
``` bash
        ~$ python run-tests.py
```


