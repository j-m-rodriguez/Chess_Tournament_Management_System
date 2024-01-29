# Running the application from the terminal
### Mac:
    __Download files from this repository or create a clone using the code below__
    $ git clone https://github.com/j-m-rodriguez/OpenClassrooms_Project3
    
    __Navigate to the directory containing the repository__
    $ cd OpenClassrooms_Project3
    
    __Run the application__
    $ python manage_Tournaments.py

### Windows Powershell:
    __Download files from this repository or create a clone using the code below__   
    $ git clone https://github.com/j-m-rodriguez/OpenClassrooms_Project3
    
    __Navigate to the directory containing the repository__
    $ cd OpenClassrooms_Project3
    
    __Run the application__ 
    $ python manage_tournaments.py

# Generating a flake8 report
### Mac:
    __Create and activate a virtual environment__
    $ python -m venv env
    $ source env/bin/activate

    __Install flake8__
    $ pip install flake8-html

    __Generate report__
    $ flake8 --max-line-length=119 --format=html --htmldir=flake8_report .\.git\

    
### Windows Powershell:
    __Create and activate a virtual environment__
    $ python -m venv env
    $ env/scripts/activate
    
    __Install flake8__
    $ pip install flake8-html
    
    __Generate report__
    $ flake8 --max-line-length=119 --format=html --htmldir=flake8_report .\.git\
