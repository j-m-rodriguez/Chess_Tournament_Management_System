# About
The Chess Tournament Management System is a comprehensive software solution designed to streamline the organization and management of chess tournaments. This project aims to provide a user-friendly platform for tournament organizers to efficiently manage various aspects of tournament operations, including player registration, tournament creation, match pairing, result recording, and report generation.

### Key Features:

**Player Registration:** Enable players to register for tournaments with ease, providing essential information such as name, contact details, and skill level.

**Tournament Creation:** Facilitate the creation of new tournaments, allowing organizers to define tournament format and scheduling parameters.

**Match Pairing:** Implement intelligent algorithms for pairing players in matches, ensuring fair and balanced matchups based on skill level and tournament format.

**Result Recording:** Provide a convenient interface for recording match results, including scores and game outcomes, to track tournament progress accurately. JSON files are simultaneously updated to prevent any data loss. 

**Report Generation:** Generate comprehensive reports summarizing tournament results, player statistics, and other relevant data for analysis and dissemination.

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
