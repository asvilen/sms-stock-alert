from stock_prices import get_stock_data, calculate_prc_price_difference
from news_articles import get_top_three_articles_list
from twilio_api import sms_sender

# Stock Info
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


stock_price_data = get_stock_data(STOCK_NAME)
percentage_difference = calculate_prc_price_difference(stock_price_data)

if -5 < percentage_difference < 5: # Do nothing
    print("Price difference is not great enough")
else: # Get articles and send them over via SMS
    # Define the increase/decrease sign
    sign = "🔺" if percentage_difference > 0 else "🔻"
    # Get the top 3 articles
    top_three_articles_list = get_top_three_articles_list(COMPANY_NAME)
    # Send separate SMS for each article
    for article in top_three_articles_list:
        text_message = f"{STOCK_NAME}: {sign}{abs(percentage_difference):.0f}%\n{article}"
        print(text_message)
        sms_sender(text_message)
        print()
