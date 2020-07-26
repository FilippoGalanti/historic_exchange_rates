def main():

    import matplotlib.pyplot as plt
    import requests
    import json
    import pandas as pd
    import csv
    from datetime import datetime
    from currenciesDict import currenciesDict

    baseUrl ="https://api.exchangeratesapi.io"
    inputValid = False
    values = []
    dailyChanges = []

    def dateConversion (date):
        objDate = datetime.strptime(date.replace("-", "/", 2), '%Y/%m/%d').date()
        return datetime.strftime(objDate,'%b %d, %Y')

    print("\nCurrency Available: CAD, HKD, ISK, PHP, DKK, HUF, CZK, AUD, RON, SEK, IDR, INR, BRL, RUB, HRK, JPY, THB, CHF, SGD, PLN, BGN, TRY, CNY, NOK, NZD, ZAR, USD, MXN, ILS, GBP, KRW, MYR, EUR")
    print("Most currencies available up to 1999!\n")

    while inputValid == False:

        base = input("Please select the base currency (3 digits): ").upper()
        print(currenciesDict[base])
        target = input("Please select the conversion currency (3 digits): ").upper()
        print(currenciesDict[target])
        startDate = input("Please select a start date (format YYYY-MM-DD):")
        endDate = input("Please select an end date (format YYYY-MM-DD) or 'today':").lower()

        if endDate == 'today':
            endDate = datetime.today().strftime('%Y-%m-%d')
  
        programUrl = baseUrl + "/history?start_at=" + startDate + "&end_at=" + endDate + "&base=" + base + "&symbols=" + target

        feedback = requests.get(programUrl)
        feedback.status_code
        feedback.json()

        if feedback.status_code != 200:
            print("\nPlease fix the inputs.\n")
            print(feedback.json())
            continue

        else:
            inputValid = True

    data = requests.get(programUrl).json()

    x = sorted(data['rates'])

    for n in x:
        values.append(data['rates'][n][target])

    if len(x)<10:
        frequency = 1
    else:
        frequency = len(x)/10

    dataDict =  dict(zip(x, values))

    for i in range (1, len(values)):
        a = values[i] - values[i-1]
        dailyChanges.append(a)
    dailyChanges.insert(0, 0)

    changeDict = dict(zip(x, dailyChanges))

    #additional information (min, max, and dates)
    print("\nFrom {} to {}, between {} and {} :".format(currenciesDict[base], currenciesDict[target], dateConversion(startDate), dateConversion(endDate)))

    dateOfMin = min(dataDict, key =dataDict.get)
    dateOfMax = max(dataDict, key =dataDict.get)
    numberOfEntries = len(dataDict)
    minDate = dateConversion (dateOfMin)
    maxDate = dateConversion (dateOfMax)
    minVal = dataDict[dateOfMin]
    maxVal = dataDict[dateOfMax]

    dateMinChange = min(changeDict, key = changeDict.get)
    dateMaxChange = max(changeDict, key = changeDict.get)
    minChange = changeDict[dateMinChange]
    maxChange = changeDict[dateMaxChange]
    minChDate = dateConversion (dateMinChange)
    maxChDate = dateConversion(dateMaxChange)

    print("\nMin value: {} {} (reached on {})\nMax value: {} {} (reached on {})".format(round(minVal, 2), target, minDate, round(maxVal, 2), target, maxDate))
    print("Biggest positive daily change {} {} (on {}).\nBiggest negative daily change {} {} (on {}).".format(round(maxChange, 3), target, maxChDate, round(minChange, 3), target, minChDate))
    print("{} entries have been evaluated".format(numberOfEntries))

    #save data to csv
    saveData = input("\nDo you want to save this data (Y/N)?").lower()
    if saveData == "y":
        with open('data.csv', 'w') as f:
            [f.write('{0},{1}\n'.format(key, value)) for key, value in dataDict.items()]

    #moving average
    valueSeries = pd.Series(values)
    rollingMean = valueSeries.rolling(window = 20).mean()
    rollingMean2 = valueSeries.rolling(window = 50).mean()

    downloadFig = input("Do you want to download the picture (Y/N)?").upper()

    #graph plotting
    fig, axs = plt.subplots(2, 1, figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(x, values, label = 'rate', linewidth = 1)
    plt.plot(x, rollingMean, label= '20 days SMA', color = 'orange', linewidth = 0.5)
    plt.plot(x, rollingMean2, label = '50 days SMA', color = 'magenta', linewidth = 0.5)
    plt.xticks(x[::round(frequency)])
    plt.legend(loc='best', fontsize = 'small')
    plt.ylabel("Rate")
    plt.title("Exchange Rate: {} / {}.".format(currenciesDict[base], currenciesDict[target]))
    plt.grid(True, linewidth = 0.2, color = 'grey')
    frame1 = plt.gca()
    frame1.axes.xaxis.set_ticklabels([])
    plt.subplots_adjust(hspace=0.1)

    plt.subplot(2, 1, 2)
    plt.plot(x, dailyChanges, linewidth = 1)
    plt.axhline(y=0, color = 'r', linestyle = '-', linewidth = 0.2)
    plt.ylabel("Abs Daily Change")
    plt.xlabel("Dates")
    plt.xticks(x[::round(frequency)])
    plt.xticks(rotation=45)
    plt.grid(True, linewidth = 0.2, color = 'grey')

    if downloadFig == 'Y':
        plt.savefig(fname="ExchangeRate%s%s.png" % (base, target))
    plt.show()

    restart = input("Do you want to run the program again (Y/N)?").upper()
    if restart == 'Y':
        main()
    else:
        exit()

main()
