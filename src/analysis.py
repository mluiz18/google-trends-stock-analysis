import yfinance as yf
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def plot_trends_vs_stock(keyword, ticker, start_date, end_date):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([keyword], cat=0, timeframe=f'{start_date} {end_date}', geo='', gprop='')
    trends_df = pytrends.interest_over_time()

    if trends_df.empty:
        print(f"No Google Trends data found for the keyword: {keyword}")
        return

    stock_data = yf.download(ticker, start=start_date, end=end_date)

    if stock_data.empty:
        print(f"No stock data found for the ticker: {ticker}")
        return

    trends_df = trends_df.drop(columns=['isPartial'])
    trends_df = trends_df.resample('D').ffill()

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Google Trends Interest', color='blue')
    ax1.plot(trends_df.index, trends_df[keyword], color='blue', label='Google Trends')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel(f'{ticker} Stock Price (USD)', color='green')
    ax2.plot(stock_data.index, stock_data['Close'], color='green', label='Stock Price')
    ax2.tick_params(axis='y', labelcolor='green')

    plt.title(f'Google Trends for "{keyword}" vs. {ticker} Stock Price')
    fig.tight_layout()
    plt.legend(loc='upper left')
    fig.savefig(f"images/{keyword}_vs_{ticker}.png", dpi=150, bbox_inches="tight")