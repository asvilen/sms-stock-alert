# SMS Stock Alert

## Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Environment Variables](#set-up-environment-variables)
- [Usage](#usage)
  - [Manual Run](#manual-run)
  - [Automated Scheduling](#automated-scheduling)
- [Goals](#goals)
- [Dependencies](#dependencies)

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

### Clone the Repository

To run this project, you need to clone this repository to your local machine:

  ```sh
  git clone https://github.com/yourusername/sms-stock-alert.git
  ```
### Install Dependencies

Install the required Python packages using pip:
  ```sh
  pip install requests twilio
  ```
### Set Up Environment Variables

To set up the required environment variables:

1. **News API (For News Articles)**:
   - Create an account on the news API service you're using.
   - Obtain the API key.
   - Set the following environment variable in your system or a `.env` file:

     ```
     NEWS_API_KEY=your_news_api_key
     ```

2. **Alpha Vantage API (For Stock Prices)**:
   - Create an account on the Alpha Vantage API service.
   - Obtain the API key.
   - Set the following environment variable in your system or a `.env` file:

     ```
     STOCK_API_KEY=your_alpha_vantage_api_key
     ```

3. **Twilio API (For SMS Alerts)**:
   - Create an account on [Twilio](https://www.twilio.com/).
   - Obtain your Twilio Account SID, Auth Token, and a Twilio phone number.
   - Set the following environment variables in your system or a `.env` file:

     ```
     TWILIO_ACCOUNT_SID=your_twilio_account_sid
     TWILIO_AUTH_TOKEN=your_twilio_auth_token
     ```

Make sure to replace the placeholder values with your actual API keys and credentials when setting up your environment.

## Usage

### Manual Run

To run the program manually, navigate to the project directory and execute:
  ```sh
  python main.py
  ```
### Automated Scheduling

For automated daily execution, consider using a scheduler like cron.

## Goals

This project showcases your skills in working with external APIs, data retrieval, and automated SMS notifications using Python. Stay informed about stock price changes and relevant news effortlessly.

Happy stock tracking! 📈

## Dependencies

- `requests`: Used for making HTTP requests to fetch stock price and news data.
- `twilio`: Used for sending SMS alerts.
- `os`: Used for accessing environment variables.
- `python-dotenv` (optional): If you decide to use a `.env` file for managing environment variables.
