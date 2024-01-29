# Running the application from the terminal
### Mac:
    Download files from this repository or create a clone using the code below
    $ git clone https://github.com/j-m-rodriguez/OpenClassrooms_Project3
    
    Navigate to the directory containing the repository
    $ cd OpenClassrooms_Project3
    
    Run the application
    $ python manage_Tournaments.py

### Windows Powershell:
    Download files from this repository or create a clone using the code below
    $ git clone https://github.com/j-m-rodriguez/OpenClassrooms_Project3
    
    Navigate to the directory containing the repository
    $ cd OpenClassrooms_Project3
    
    Run the application
    $ python manage_tournaments.py

# Generating a flake8 report
### Mac:
    Create and activate a virtual environment
    $ python -m venv env
    $ source env/bin/activate

    Install flake8
    $ pip install flake8-html

    Generate report
    $ flake8 --max-line-length=119 --format=html --htmldir=flake8_report .\.git\

    
### Windows Powershell:
    Create and activate a virtual environment
    $ python -m venv env
    $ env/scripts/activate
    
    Install flake8
    $ pip install flake8-html
    
    Generate report
    $ flake8 --max-line-length=119 --format=html --htmldir=flake8_report .\.git\
