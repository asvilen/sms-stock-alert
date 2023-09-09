# SMS Stock Alert 📈🚀📰

## Overview

Stock Alert via SMS is a Python project that helps you stay updated with stock price changes and related news. It monitors the stock price of a specific company and sends you SMS alerts when significant price changes occur. You'll receive the top three news articles related to the company along with the stock price change percentage.🚀


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
- [Screenshots](#screenshots)

## How It Works

- **Main Script (main.py)**:
  - The heart of the operation!
  - Imports functions from other modules.
  - Defines the stock name and company name (e.g., TSLA for [Tesla Inc](https://www.tesla.com/)).
  - Fetches stock price data using the `get_stock_data` function.
  - Calculates the percentage price difference with `calculate_prc_price_difference`.
  - If the price change is noteworthy (greater than 5% or less than -5%), it fetches the top three news articles using the `get_top_three_articles_list` function and sends SMS alerts via [Twilio](https://www.twilio.com/).

- **News Articles Module (news_articles.py)**:
  - Leverages the power of news APIs.
  - Fetches fresh news articles related to the specified company.
  - Selects the top three articles and serves them to you.
  - News API Endpoint: [https://newsapi.org/v2/everything](https://newsapi.org/v2/everything)

- **Stock Prices Module (stock_prices.py)**:
  - Connects to the [Alpha Vantage API](https://www.alphavantage.co/).
  - Retrieves daily stock price data for the chosen company.
  - Computes the percentage price difference between the latest two days.

- **Twilio API Module (twilio_api.py)**:
  - Employs the magic of [Twilio](https://www.twilio.com/) for SMS alerts.
  - Requires your Twilio account credentials, including Account SID and Auth Token, set as environment variables.

## Getting Started

### Clone the Repository

To embark on this journey, start by cloning this repository to your local machine:


  ```sh
  git clone https://github.com/yourusername/sms-stock-alert.git
  ```
### Install Dependencies

Prepare your toolkit by installing the required Python packages using pip:
  ```sh
  pip install requests twilio
  ```
### Set Up Environment Variables

To set up the required environment variables:

1. **News API (For News Articles)**:
   - Create an account on [News API ORG](https://newsapi.org/).
   - Obtain the API key.
   - Set the following environment variable in your system or a `.env` file:

     ```
     NEWS_API_KEY=your_news_api_key
     ```

2. **Alpha Vantage API (For Stock Prices)**:
   - Register at [Alpha Vantage](https://www.alphavantage.co/).
   - Acquire the API key.
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

Replace `your_news_api_key`, `your_alpha_vantage_api_key`, `your_twilio_account_sid`, and `your_twilio_auth_token` with the actual keys and credentials.

## Usage

### Manual Run

To run the program manually, navigate to the project directory and execute:
  ```sh
  python main.py
  ```
### Automated Scheduling

For a seamless journey, consider automating daily execution using a scheduler like cron.

## Goals

This project is your ultimate showcase of skills in handling external APIs, data retrieval, and automated SMS notifications using Python. It's your way of saying, "I've got the stock market covered!" 📈

Embrace the power of knowledge. Stay informed. 🚀

## Dependencies

- `requests`: Used for making HTTP requests to fetch stock price and news data.
- `twilio`: Used for sending SMS alerts.
- `os`: Used for accessing environment variables.
- `python-dotenv` (optional): If you decide to use a `.env` file for managing environment variables.

## Screenshots

<p float="left">
  <img src="https://github.com/asvilen/sms-stock-alert/assets/47661156/9ebeda42-b8f8-4858-bbf3-db9fbe3386a7" width="300" />
  <img src="https://github.com/asvilen/sms-stock-alert/assets/47661156/8af076a0-d0d4-40e9-b014-7ca75239d803" width="300" />
</p>


