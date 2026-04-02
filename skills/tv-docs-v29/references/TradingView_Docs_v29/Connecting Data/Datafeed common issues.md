# Connecting Data: Datafeed: common issues

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/Datafeed-Issues

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* Datafeed: common issues

On this page

# Datafeed: common issues

This article describes common issues that users face when they implement the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/).

tip

[Enable debug mode](/charting-library-docs/v29/tutorials/enable-debug-mode#enable-debug-mode-for-data-connection) to identify how the library loads, processes, and resolves data.

## getBars is called multiple times[​](#getbars-is-called-multiple-times "Direct link to getBars is called multiple times")

The library calls [`getBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#getbars) multiple times if the amount of provided data [is less than requested](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#correct-amount-of-data). To debug this issue, [enable console logs](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#debug). Consider the following example:

```
FEED [AAPL|1D]: Next time received: `2018-03-27T00:00:00.000Z`  
FEED [AAPL|1D]: Processing pending subscribers, count=2  
  
// The library requests 329 bars from the datafeed  
  
FEED [AAPL|1D]: Leftmost subscriber requires 329 bars prior 2022-11-09T00:00:00.000Z  
FEED [AAPL|1D]: Requesting data: [2016-12-22T00:00:00.000Z ... 2021-08-06T00:00:00.000Z, 329 bars]  
  
// The datafeed responds with 157 bars  
// 157 is less than requested, so the library will request the remaining bars from the datafeed  
  
FEED [AAPL|1D]: Receiving bars: total 157 bars in  [2017-08-10T00:00:00.000Z ... 2018-03-27T00:00:00.000Z], requested range: [2016-12-22T00:00:00.000Z ... 2021-08-06T00:00:00.000Z, 329 bars]  
FEED [AAPL|1D]: Processing pending subscribers, count=2  
  
// The library requests 172 bars from the datafeed  
// It requests 172 bars because 329 - 157 = 172  
  
FEED [AAPL|1D]: Leftmost subscriber requires 172 bars prior 2017-08-10T00:00:00.000Z  
FEED [AAPL|1D]: Requesting data: [2016-04-26T00:00:00.000Z ... 2016-12-22T00:00:00.000Z, 172 bars]  
  
// The datafeed responds with 169 bars  
// 169 is less than requested, so the library will request the remaining bars from the datafeed  
  
FEED [AAPL|1D]: Receiving bars: total 169 bars in  [2016-04-26T00:00:00.000Z ... 2016-12-22T00:00:00.000Z], requested range: [2016-04-26T00:00:00.000Z ... 2016-12-22T00:00:00.000Z, 172 bars]  
FEED [AAPL|1D]: Processing pending subscribers, count=2  
  
// The library requests 3 bars from the datafeed  
// It requests 3 bars because 172 - 169 = 3  
  
FEED [AAPL|1D]: Leftmost subscriber requires 3 bars prior 2016-04-26T00:00:00.000Z  
FEED [AAPL|1D]: Requesting data: [2016-04-23T00:00:00.000Z ... 2016-04-26T00:00:00.000Z, 3 bars]  
  
// The datafeed responds with 2 bars  
// 2 is less than requested, so the library will request the remaining bars from the datafeed  
  
FEED [AAPL|1D]: Receiving bars: total 2 bars in  [2016-04-25T00:00:00.000Z ... 2016-04-26T00:00:00.000Z], requested range: [2016-04-23T00:00:00.000Z ... 2016-04-26T00:00:00.000Z, 3 bars]  
FEED [AAPL|1D]: Processing pending subscribers, count=2  
  
// The library requests 2 bars from the datafeed  
// Here the library actually requests 1 more bar than it requires, but that's OK and datafeed implementations should be able to handle it  
  
FEED [AAPL|1D]: Leftmost subscriber requires 2 bars prior 2016-04-25T00:00:00.000Z  
FEED [AAPL|1D]: Requesting data: [2016-04-21T00:00:00.000Z ... 2016-04-23T00:00:00.000Z, 2 bars]  
FEED [AAPL|1D]: Receiving bars: total 2 bars in  [2016-04-21T00:00:00.000Z ... 2016-04-22T00:00:00.000Z], requested range: [2016-04-21T00:00:00.000Z ... 2016-04-23T00:00:00.000Z, 2 bars]  
FEED [AAPL|1D]: Processing pending subscribers, count=2
```

To avoid multiple `getBars` requests, you can return bars **before** the [`from`](/charting-library-docs/v29/api/interfaces/Charting_Library.PeriodParams#from) date until their number matches the [`countBack`](/charting-library-docs/v29/api/interfaces/Charting_Library.PeriodParams#countback) value. For example, the chart requests 300 bars in the range `[2019-06-01T00:00:00…2020-01-01T00:00:00)`, and your backend has only 250 bars in the requested period. Return these 250 bars and 50 bars prior to `2019-06-01T00:00:00`.

## Bar data is mutable[​](#bar-data-is-mutable "Direct link to Bar data is mutable")

The library may mutate the values of some [`Bar`](/charting-library-docs/v29/api/interfaces/Charting_Library.Bar) objects that you provide. You can make a copy of your data to avoid potential issues.

## Requested data is outside visible range[​](#requested-data-is-outside-visible-range "Direct link to Requested data is outside visible range")

The `[from, to)` [range](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#correct-amount-of-data) usually matches [`VisibleTimeRange`](/charting-library-docs/v29/api/interfaces/Charting_Library.VisibleTimeRange). However, sometimes the library requests more bars than are visible, because indicators require some additional history.

## Time violation[​](#time-violation "Direct link to Time violation")

The *putToCacheNewBar: time violation* issue appears if the library receives a bar which timestamp is less than the timestamp of the last bar on the chart.
To debug this issue, check that you follow the rules below:

* You provide bars in **ascending** time order. Refer to [Bar order](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#bar-order) for more information.
* You update only the last bar on a chart or add a new one using the `subsсribeBars` method. Refer to [`subsсribeBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#subscribebars) for more information.
* You use different subscribers to update data on different symbols/resolutions and you send updates to the correct subscriber. Refer to [Multiple subscriptions](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#multiple-subscriptions) for more information.
* For daily, weekly, and monthly bars, the [`time`](/charting-library-docs/v29/api/interfaces/Charting_Library.Bar#time) value represents the **beginning of the trading day** at 00:00:00 UTC, not the beginning of the session.

## Maximum call stack size exceeded[​](#maximum-call-stack-size-exceeded "Direct link to Maximum call stack size exceeded")

If the *Uncaught RangeError: Maximum call stack size exceeded* issue occurs, you should check that you evoke all callbacks asynchronously in your datafeed implementation. Refer to [Asynchronous callbacks](/charting-library-docs/v29/connecting_data/datafeed-api/#asynchronous-callbacks) for more information.

## Data must have unique times[​](#data-must-have-unique-times "Direct link to Data must have unique times")

The *Assertion failed: data must have unique times* issue appears if the library receives a bar whose timestamp matches the timestamp of the bar that was loaded before.

To debug this issue, check that you follow the rules below:

* When you return data to [`getBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#getbars), you should not include a bar for the [`to`](/charting-library-docs/v29/api/interfaces/Charting_Library.PeriodParams#to) date because this bar was sent in a previous response. For more information on how to send data, refer to the [Correct amount of data](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#correct-amount-of-data) section.
* Your custom indicator [maps](/charting-library-docs/v29/custom_studies/Studies-Extending-The-Time-Scale#mapping-times) the main [series](/charting-library-docs/v29/getting_started/glossary#series) times correctly. If the custom indicator has more times than the main series, you can use the [Extending the time scale feature](/charting-library-docs/v29/custom_studies/Studies-Extending-The-Time-Scale#extending-the-time-scale-feature) that allows indicators to define their points on a time scale.

## Library shifts bar time[​](#library-shifts-bar-time "Direct link to Library shifts bar time")

If the library considers the bar time incorrect, it shifts the time to the nearest expected value.
In this case, the bar time displayed on the chart does not coincide with the bar time your datafeed provides.
To debug this issue, check that you follow the rules below:

* You correctly specified the following properties in [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo):
  + [`timezone`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#timezone) contains a time zone of the symbol's **exchange**.
  + [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) contains trading hours for the symbol. The time zone of the trading hours corresponds to the **`timezone`** value.
* The bar time should be inside the trading hours specified in `session`. Otherwise, the library ignores bars with such time values.
* Time values of any bars should be represented with Unix timestamps in **UTC**.
* For daily, weekly, and monthly bars, the [`time`](/charting-library-docs/v29/api/interfaces/Charting_Library.Bar#time) value represents the **beginning of the trading day** at 00:00:00 UTC, not the beginning of the session. If you provide real-time updates, the `time` value should represent the beginning of the candle, not the time of the update.
* The library processes DST. You do not need to adjust time values manually.

### Example[​](#example "Direct link to Example")

* The current symbol is AAPL.
* `timezone` is `"America/New_York"`.
* `session` is `"0930-1630"`.
* The selected resolution is two hours.

The table below shows time values that the library expects based on the resolution, timestamps that a datafeed provides, and time values displayed on the chart.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Expected time value Received timestamp Timestamp value in UTC Timestamp value in UTC-5 Displayed time value|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 09:30 `1706106600000` Wed Jan 24 2024 14:30:00 Wed Jan 24 2024 09:30:00 Wed Jan 24 2024 09:30:00|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 11:30 `1706113800000` Wed Jan 24 2024 16:30:00 Wed Jan 24 2024 11:30:00 Wed Jan 24 2024 11:30:00|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 13:30 `1706122800000` Wed Jan 24 2024 19:00:00 Wed Jan 24 2024 **14:00:00** Wed Jan 24 2024 **13:30:00** The library shifts the recieved value to the nearest expected one — the beginning of the interval.| 15:30 `1706128200000` Wed Jan 24 2024 20:30:00 Wed Jan 24 2024 15:30:00 Wed Jan 24 2024 15:30:00 | | | | | | | | | | | | | | | | | | | | | | | | |

Therefore, incorrect `timezone`, `session`, and `time` values can lead to bars being hours behind the expected ones.

## Internet connection issues[​](#internet-connection-issues "Direct link to Internet connection issues")

When users experience internet connection issues, the library may fail to receive data during [`getBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#getbars) calls.
The library itself does not restore the connection.
Instead, you need to implement the following behavior to ensure reconnection:

1. Call the [`resetCache`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#resetCache) method to clear all cached bar data.
2. Call [`resetData`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resetdata). This method makes the library call `getBars`, thereby re-requesting all the data for the deleted symbol.
   To limit the data request to only the visible range,
   enable the [`request_only_visible_range_on_reset`](/charting-library-docs/v29/customization/Featuresets#request_only_visible_range_on_reset) featureset.

### For offline applications[​](#for-offline-applications "Direct link to For offline applications")

Mobile or browser applications designed to work offline have distinct behavior.
If the library attempts to resolve a symbol through [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) while the user is offline,
the library fails to load the data.
In this case, users may experience an error or no response from the library.

To resolve this issue, you can set a "fake" symbol name.
This makes the library request symbol information again.
Consider the example below that simulates the network being offline.
The example shows how to set a "fake" symbol name while still resolving the desired symbol for the user.

See the Pen [Handling symbol resolution when the library is offline](https://codepen.io/tradingview/pen/rNRRrra) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

## Quotes are not displayed or refreshed[​](#quotes-are-not-displayed-or-refreshed "Direct link to Quotes are not displayed or refreshed")

When using [Trading Platform](/charting-library-docs/v29/trading_terminal/), you may encounter issues where [quotes](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes) do not appear or update correctly in the UI.
Follow these steps to troubleshoot:

1. Ensure [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) and [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes) are correctly implemented. Some **common mistakes** include:
   * The symbol name returned in the [`n`](/charting-library-docs/v29/api/interfaces/Datafeed.QuoteOkData#n) field of the [`QuoteOkData`](/charting-library-docs/v29/api/interfaces/Datafeed.QuoteOkData) object does not match the symbol requested by the library. Make sure the symbol names are exactly the same as in the requests.
   * Values in the [`DatafeedQuoteValues`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues) object do not match the expected data types.
2. Verify that the data you send makes logical sense. Some **common mistakes** include:
   * Sending zero values for bid/ask prices when they should be positive numbers.
   * Providing negative or unrealistic values in fields where they are not expected.
   * Adding fields that do not exist in the expected interface, which can cause the request to fail.

## Delays in Trading Platform UI elements[​](#delays-in-trading-platform-ui-elements "Direct link to Delays in Trading Platform UI elements")

When using [Trading Platform](/charting-library-docs/v29/trading_terminal/), you may experience delays in loading UI elements such as [Buy/Sell buttons](/charting-library-docs/v29/trading_terminal/#buysell-buttons-and-lines), [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket), [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/), or [context menus](/charting-library-docs/v29/ui_elements/context-menu).
These UI elements depend on real-time [quotes](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes) to display accurate pricing.
If the library does not receive valid quotes, it still attempts to fetch them before rendering the UI.
This leads to delays — often around 10 seconds, which matches the library's timeout behavior.

To fix this issue, ensure [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) and [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes) are correctly implemented.
Some **common mistakes** include:

* The symbol name returned in the [`n`](/charting-library-docs/v29/api/interfaces/Datafeed.QuoteOkData#n) field of the [`QuoteOkData`](/charting-library-docs/v29/api/interfaces/Datafeed.QuoteOkData) object does not match the symbol requested by the library. Make sure the symbol names are exactly the same as in the requests.
* Values in the [`DatafeedQuoteValues`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues) object do not match the expected data types.