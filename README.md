# Description

This repository is to track stock prices and send an email if the price of a stock fell below a certain limit. 

# How to use this package

- Step 1:
- Step 2: 

# Install the required packages
- `pip3 install -r requirements.txt`

# Contribution guidelines

<ins>**For API**</ins>

For the record of Stock pricing I used [Financial modeling preparation API](https://site.financialmodelingprep.com/developer)

<ins>**Image of the email I got after runing it**</ins>

![image](https://user-images.githubusercontent.com/93368036/203134123-91306a5e-011f-44ce-be74-a4f4318e9d11.png)

#Tracker

Tracker is a tool that tracks the price of a specified stock and sends an email notification when the price reaches a certain threshold.
#Prerequisites

    A financial modeling API key from Financial Modeling Prep
    A Microsoft Outlook account and email address

#Installation

    Clone this repository.
    Create a .env file in the root directory and add the following environment variables:
        api_key: your Financial Modeling Prep API key
        email: your Outlook email address
        password: your Outlook account password
    Install the required libraries by running pip install -r requirements.txt in the terminal.

#Usage

    Open the tracker.py file and specify the stock you want to track by replacing stock_name with the desired ticker symbol.
    Set the price threshold by modifying the if statement in the check_stock() function.
    Run the script by entering python tracker.py in the terminal. The script will run indefinitely, checking the stock price every minute and sending an email notification if the price falls below the specified threshold.

#Credits

This tool uses the [Financial modeling preparation API](https://site.financialmodelingprep.com/developer) to retrieve stock data.
