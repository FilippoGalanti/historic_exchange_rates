# Historic Exchange Rates

This small script will allow you to get past daily echange rates between 2 selected currencies for any period of time specified by the user.
Data is sourced from <a href="http://exchangeratesapi.io/">exchangeratesapi.io</a>.

<b>Prerequisites</b>

It needs the following Python libraries:

Matplotlib / Requests / Json / Pandas / csv / Datetime

It also need a custom dictionary that translates each currency symbol to its description (ie. USD to US Dollar).

<b>Output</b>

There will be 3 main outputs:

 <ul>
  <li>some strings with some general information;</li>
  <li>a graph with the historic trends, 20-day and 50-day moving averages;</li>
  <li>a csv with the data and the daily changes</li>
</ul> 
