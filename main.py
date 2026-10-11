from src.analysis import plot_trends_vs_stock

if __name__ == "__main__":
    search_keyword = "Petróleo"
    stock_ticker = "PETR3.SA"
    start_date = "2023-01-01"
    end_date = "2024-01-01"

    plot_trends_vs_stock(search_keyword, stock_ticker, start_date, end_date)