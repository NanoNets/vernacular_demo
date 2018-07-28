# Vernacular Image Classification using the Nanonets API

A project to classify images containing vernacular text using the Nanonets Image classification api. The code is in python

## Getting Started

You need to clone the repository using the command:
```
git clone https://github.com/sjain07/vernacular_demo.git
```

### Prerequisites

1. python 2.7
2. pip
3. requests

On ubuntu run:
```
sudo apt-get install python-setuptools python-dev build-essential 
sudo pip install requests
```

### Project Structure

```
project
│   README.md
│
└───code
│   │   create_model.py 
│   │   get_model_state.py 
│   │   predict_file.py
│   │   predict_url.py
│  
│  
└───images
    │
    └───HindiJokes
    │   │   1.jpg
    │   │   2.jpg
    │   │   ...
    │
    └───TeluguJokes
    │   │   1.jpg
    │   │   2.jpg
    │   │   ...
    │   
    └───MarathiJokes
    │   │   1.jpg
    │   │   2.jpg
    │   │   ...
    │   
    └───BengaliJokes
        │   1.jpg
        │   2.jpg
        │   ... 
```

## Running the code
There are 3 steps:
1. Creating a model
2. Checking the model state
3. Testing the model

### 1. Creating a model
To create a model run:
```
python code/create_model.py
```
This will create a model, upload the data and train the model. This will take a while to run. This will also print a MODEL_ID you need this for the next step.

### 2. Checking model state
To test the state of the model run:
```
python code/get_model_state.py MODEL_ID
```

This will output the state of the model. Once the state of the model is trained we can begin using the model. Trained is a MODEL_STATE = 5

### 3. Testing the model

To test the model once the image has been trained either pass a file or pass a url:

#### File
```
python code/predict_file.py MODEL_ID path/of/image/file.jpg
```

#### URL
```
python code/predict_file.py MODEL_ID https://myurl.domain.com/image.jpg
```

## Training Data

The training data we used had the following images:
1. HindiJokes - 492
2. MarathiJokes - 435
3. BengaliJokes - 720
4. TeluguJokes - 705

## RESULTS

The accuracy of the model was 97%


## API Documentation

For api documentation please visit https://nanonets.com/documentation/

## License

This project is licensed under the MIT License