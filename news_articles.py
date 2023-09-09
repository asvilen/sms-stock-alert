import os
import requests

# News API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")


def get_top_three_articles_list(company_name):
    # Define API call parameters
    news_parameters = {
        "q": company_name,
        "apiKey": NEWS_API_KEY,
        "pageSize": 20,
        "sortBy": "publishedAt"
    }
    # Get the response in json format
    news_response_dict = requests.get(url=NEWS_ENDPOINT, params=news_parameters).json()
    # Extract the articles
    articles_list = news_response_dict['articles']
    # Save the top 3 articles
    first_three_articles_list = articles_list[:3]

    return [
        "Headline: " + current_article['title'] +
        "\nBrief:" + current_article['description']
        for current_article in first_three_articles_list
    ]
