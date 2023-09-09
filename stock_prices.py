import os
import requests

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")


def get_stock_data(company_symbol):
    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": company_symbol,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": STOCK_API_KEY
    }
    response = requests.get(url=STOCK_ENDPOINT, params=parameters)
    return response.json()

def calculate_prc_price_difference(response_dict):
    data_dict = response_dict['Time Series (Daily)']
    data_dates_list = [key for (key, value) in data_dict.items()]
    yesterday = data_dates_list[0]
    yesterday_close_price = float(data_dict[yesterday]['4. close'])
    print(f"Yesterday's close price: {yesterday_close_price}")

    day_before_yesterday = data_dates_list[1]
    day_before_yesterday_close_price = float(data_dict[day_before_yesterday]['4. close'])
    print(f"Day before yesterday's close price: {day_before_yesterday_close_price}")

    positive_difference = round(yesterday_close_price - day_before_yesterday_close_price, 3)
    print(f"Positive difference: {positive_difference}")

    percentage_difference = positive_difference / day_before_yesterday_close_price * 100
    print("#" * 50)
    print(f"Percentage difference: {percentage_difference:.2f}%")
    print("#" * 50)
    print()
    return percentage_difference
