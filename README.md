# SMS Stock Alert

## Overview

Stock Alert via SMS is a Python project that helps you stay updated with stock price changes and related news. It monitors the stock price of a specific company and sends you SMS alerts when significant price changes occur. You'll receive the top three news articles related to the company along with the stock price change percentage.

## How It Works

- **Main Script (main.py)**:
  - Imports functions from other modules.
  - Defines the stock name and company name (e.g., TSLA for Tesla Inc).
  - Fetches stock price data using the `get_stock_data` function.
  - Calculates the percentage price difference with `calculate_prc_price_difference`.
  - If the price change is significant (greater than 5% or less than -5%), it fetches the top three news articles using the `get_top_three_articles_list` function and sends SMS alerts with Twilio.

- **News Articles Module (news_articles.py)**:
  - Uses a news API to fetch news articles related to the specified company.
  - Extracts the top three articles and returns them as a list.

- **Stock Prices Module (stock_prices.py)**:
  - Uses an API to retrieve daily stock price data for the specified company.
  - Calculates the percentage price difference between the latest two days.

- **Twilio API Module (twilio_api.py)**:
  - Utilizes Twilio to send SMS alerts.
  - Requires Twilio account credentials, including Account SID and Auth Token, which should be set as environment variables.

## Getting Started

1. **Clone the Repository**: Clone this repository to your local machine:
  ```sh
  git clone https://github.com/yourusername/stock-alert-via-sms.git
  ```
2. **Install Dependencies**: Install the required Python packages using pip:
  ```sh
  pip install requests twilio
  ```
3. **Set Up Environment Variables**:
- Create an account on [Twilio](https://www.twilio.com/).
- Obtain the API keys for Twilio.
- Set the following environment variables in your system or a `.env` file:
  ```sh
  TWILIO_ACCOUNT_SID=your_twilio_account_sid
  TWILIO_AUTH_TOKEN=your_twilio_auth_token
  ```
  ## Usage

- **Manual Run**: To run the program manually, navigate to the project directory and execute:
  ```sh
  python main.py
  ```
- **Automated Scheduling**: For automated daily execution, consider using a scheduler like cron.

## Goals

This project showcases your skills in working with external APIs, data retrieval, and automated SMS notifications using Python. Stay informed about stock price changes and relevant news effortlessly.

Happy stock tracking! 📈
