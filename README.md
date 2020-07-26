# Historic Exchange Rates

This small script - Exchange Rate_Historic.py - will allow you to get past daily echange rates between 2 selected currencies for any period of time specified by the user.
Data is sourced from <a href="http://exchangeratesapi.io/">exchangeratesapi.io</a>.

<img src="https://raw.githubusercontent.com/FilippoGalanti/historic_exchange_rates/master/ExchangeRateEURUSD.png" alt="Output Example">

Currencies Available: CAD, HKD, ISK, PHP, DKK, HUF, CZK, AUD, RON, SEK, IDR, INR, BRL, RUB, HRK, JPY, THB, CHF, SGD, PLN, BGN, TRY, CNY, NOK, NZD, ZAR, USD, MXN, ILS, GBP, KRW, MYR, EUR.

<b>Prerequisites</b>

It needs the following Python libraries:

Matplotlib / Requests / Json / Pandas / csv / Datetime
 <ul>
  <li>Matplotlib and Pandas;</li>
  <li>Requests and Json;</li>
  <li>csv</li>
  <li>datetime</li>
</ul>

It also need a custom dictionary that translates each currency symbol to its description (ie. USD to US Dollar).

<b>Output</b>

There will be 3 main outputs:

 <ul>
  <li>some strings with some general information;</li>
  <li>a graph with the historic trends, 20-day and 50-day moving averages;</li>
  <li>a csv with the data and the daily changes</li>
</ul> 
