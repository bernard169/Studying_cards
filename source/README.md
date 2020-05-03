# Studying_cards

## SETUP
Procedure to compile .ui file to .py file on Windows : 
* In your command prompt, go to your python interpreter folder
* Go to the Scripts subfolder
* Execute the command `pyuic5.exe -x "absolute\path\SOURCE.ui" -o "absolute\path\DESTINATION.py"`

## Architecture
Most files in the repository are automatically generated files from the Qt Creator. All hand written files containing functionalities are named with a "my" prefix, except for the main.py and utils.py files. 