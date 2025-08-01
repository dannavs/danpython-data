import yfinance as yf


def the_msft():
    msft = yf.Ticker("MSFT")
    msft_data = msft.history(period="max")
    print(msft_data.head(), end="\n")

def the_sdiv():
    sdiv = yf.Ticker("SDIV")
    sdiv_data = sdiv.history(period="max")
    print(sdiv_data.head())
