import os
import datetime
import discord
from discord.ext import commands
import dateutil.parser
from dotenv import load_dotenv
import requests

load_dotenv()

API_URL = "https://bing-news-search1.p.rapidapi.com/news"
API_URL_SEARCH = "https://bing-news-search1.p.rapidapi.com/news/search"

headers = {
	"X-BingApis-SDK": "true",
    "Accept-Language": "ENG,PT",
	"X-RapidAPI-Key": os.getenv('BING_NEWS_API_KEY'),
	"X-RapidAPI-Host": "bing-news-search1.p.rapidapi.com"
}

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.slash_command(name='todaynews', help='Get recent news by keyword')
async def getNews(ctx, keyword):
    print("TodayNews command called")

    querystring = {"q":keyword,"count":"2","sortBy":"Date","cc":"PT","freshness":"Day","textFormat":"Raw","safeSearch":"Off"}

    print(type(keyword))
    print(querystring)

    response = requests.get(API_URL_SEARCH, headers=headers, params=querystring)
    print(response.json())
    #get most recent news from json
    news = response.json()['value']
    for i in range(0, len(news)):
        if (i == 0):
            recentdate = dateutil.parser.isoparse(news[i]['datePublished'])
            newsPos = i
        elif dateutil.parser.isoparse(news[i]['datePublished']) > recentdate:
            recentdate = dateutil.parser.isoparse(news[i]['datePublished'])
            newsPos = i
        
    #get news title and url
    newsTitle = news[newsPos]['name']
    newsUrl = news[newsPos]['url']

    print(newsTitle)
    await ctx.send(newsTitle + " - Link:" + newsUrl)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)