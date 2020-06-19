# csv_to_comma_txt

A quick Python script meant to support collaborating in Google Drive to create a custom skribbl.io deck. Outputs the first column of inputted CSVs to a comma-separated string outputted into a .txt.

### Requirements
- python 3.6+ (can be installed [here](https://www.python.org/downloads/))
- pip3
- pandas

### Steps to run:
1. Run `pip3 install -r requirements.txt` to install required python packages
2. Run `python3 csv_to_comma_txt.py "Animals - Sheet1.csv" "Anime list - Sheet1.csv"` --- the script can take as many CSVs as you want (minimum 1)
3. Observe output in Animals - Sheet1.csv.output.txt and Anime list - Sheet1.csv.output.txt
