# STOCK Tracker

Tracker is a tool that tracks the price of a specified stock and sends an email notification when the price reaches a certain threshold.
# Prerequisites
- A financial modeling API key from [Financial modeling preparation API](https://site.financialmodelingprep.com/developer)
- A Microsoft Outlook account and email address

# Installation
- Clone this repository.
- Create a **'.env'** file in the root directory and add the following environment variables:
    - **'api_key'**: your Financial Modeling Prep API key
    - **'email'**: your Outlook email address
    - **'password'**: your Outlook account password
- To install the required packages, you can run the following command in your terminal:  
     ` pip3 install -r requirements.txt ` <br>
      This will install the requests and python-dotenv packages, which are required by the script. <br>  <br>
      If you don't have pip installed on your system, you can install it by running the following command: <br>
      `python -m ensurepip --default-pip` <br><br>
      Alternatively, you can install the required packages individually by running the following commands:<br>
      `pip install requests`<br>
      `pip install python-dotenv` <br>

# Usage
- Open the **'tracker.py'** file and specify the stock you want to track by replacing stock_name with the desired ticker symbol.
- Set the price threshold by modifying the **'if'** statement in the **'check_stock()'** function.
- Run the script by entering **"python tracker.py"** in the terminal. The script will run indefinitely, checking the stock price every minute and sending an email notification if the price falls below the specified threshold.

# Disclaimer
This script is for educational and informational purposes only, and should not be used for financial decision making. Please do your own research and consult with a financial advisor before making any investment decisions.

# Credits

This tool uses the [Financial modeling preparation API](https://site.financialmodelingprep.com/developer) to retrieve stock data.

<ins>**Image of the email I got after runing it**</ins> 

![image](https://user-images.githubusercontent.com/93368036/203134123-91306a5e-011f-44ce-be74-a4f4318e9d11.png) 

 
