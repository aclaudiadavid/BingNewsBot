# BingNewsBot
📰 Stay Informed with BingNewsBot 📰

Whether you're curious about the latest headlines, interested in specific topics, or eager to keep track of global events, BingNewsBot is here to provide you with up-to-date and sharable news.

## Discontinuation Notice
⚠️ **Discontinued** ⚠️: Please note that this project is discontinued. Due to the loss of access to Azure, the BingNewsBot is no longer in development. We apologize for any inconvenience this may cause.

## Project Overview
🤖 **Powered by Bing News API** 🤖

NewsBot relies on Bing News API, offering access to a vast network of reputable news sources. Developed in Python 3.10.12, it's currently designed for English and Portuguese news retrieval.

## Accomplishments and Future Enhancements
### Accomplishments:
[X] Connected to BingNewsAPI and Discord.
[X] Implemented `\todaynews` command for retrieving the most recent news regarding specific keywords.

### Future Enhancements (Not Implemented Due to Discontinuation):
[] Implement !help command for user assistance.
[] Add functionality for news filtering based on language or region.
[] Introduce functionality for news filtering based on source/website.
[] Incorporate functionality for news filtering based on Bing News API categories.
[] Implement scheduled news updates feature.

## Setup
1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Create a `.env` file in the root directory of the project.
4. Add your Discord bot token and Bing News API key to the `.env` file:
    ```
    DISCORD_TOKEN=your_discord_bot_token
    BING_NEWS_API_KEY=your_bing_news_api_key
    ```
    Replace `your_discord_bot_token` with your Discord bot token and `your_bing_news_api_key` with your Bing News API key.

## How to Run
To run the code, execute the main using Python 3:
`python3 main.py`

