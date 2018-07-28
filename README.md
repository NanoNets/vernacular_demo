# Vernacular Image Classification using the Nanonets API

A project to classify images containing vernacular text using the Nanonets Image classification api. The code is in python

## Getting Started

You need to clone the repository using the command:
```
git clone https://github.com/sjain07/vernacular_demo.git
```

### Prerequisites

python 2.7
pip
requests (install using pip install requests)

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
│   └───create_model.py 
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

to run the code simply run:
```
python code/create_model.py
```
##API Documentation

For api documentation please visit nanonets.com/documentation/

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
