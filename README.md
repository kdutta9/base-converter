<h1 align="center">Base Converter</h1>

<p align="center"> 
This is a web application that can convert whole numbers between bases 2-36. 
It was built using the Python Flask framework, HTML, and CSS.
    <br> 
</p>

## Table of Contents
- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Contributing](./CONTRIBUTING.md)
- [Authors](#authors)

## About <a name = "about"></a>
I built this application to help students check their work in base conversion, inspired by my own coursework in computer architecture.

## Getting Started <a name = "getting_started"></a>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Installing
## Setup
1. Install `python3`.
    * **macOS:** `brew install python3`
    * **Linux:** `sudo apt-get install python3`
	* **Windows:** [Download Python3](https://www.python.org/downloads/windows/)
2. Install `git`.
    * **macOS:** `brew install git`
    * **Linux:** `sudo apt-get install git`
	* **Windows:** [Download Git](https://git-scm.com/download/win)
3. `git clone https://github.com/kdutta9/base-converter` to clone the repo.
4. `pip install -r requirements.txt` (or `pip3 install -r requirements.txt`) to install requirements.
	* `git pull origin master` to bring in latest changes
5. Navigate to the directory of the repo.
6. To run a local version of your website, type `python main.py` (or `python3 main.py`) on the command line.
7. Visit the local URL in your browser as indicated on the command line (usually `http://127.0.0.1:5000/`).

## Testing <a name = "tests"></a>
In the main directory, run `python src/testConvert` to test the correctness of the program.

The tests contain subtests for each method and an end-to-end test.


## Deployment <a name = "deployment"></a>
I deployed the app onto Heroku, which only involved creating a [Procfile](./Procfile) and pushing to my Heroku account.

## Built Using <a name = "built_using"></a>
- [Flask](https://palletsprojects.com/p/flask/) - Web Framework
- [Python](https://www.python.org/) - Backend Code

## Authors <a name = "authors"></a>
- [@kdutta9](https://github.com/kdutta9)

See also the list of [contributors](https://github.com/kdutta9/base-converter/contributors) who participated in this project.
