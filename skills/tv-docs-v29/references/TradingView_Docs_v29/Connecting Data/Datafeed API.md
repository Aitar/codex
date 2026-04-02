# Connecting Data: Datafeed API

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/datafeed-api/

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* Datafeed API

On this page

# Datafeed API

The library allows connecting market data to the chart in two ways:

* By using the built-in [UDF adapter](/charting-library-docs/v29/connecting_data/UDF).
* By implementing your own datafeed via the Datafeed API.

info

Note that neither Advanced Charts nor Trading Platform contains any market data. You should use data from your own source or third-party providers.

This documentation section describes the Datafeed API methods and their implementation details.
You can also refer to the [How to connect data via Datafeed API](/charting-library-docs/v29/tutorials/implement_datafeed_tutorial/) tutorial for a step-by-step guide.

## Overview[​](#overview "Direct link to Overview")

The Datafeed API is a set of methods that you should implement in JavaScript and assign to the [`datafeed`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#datafeed) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor). The library calls these methods to access and process data. In response, you should evoke the provided callbacks to pass the data to the library.
The diagram below illustrates how the Datafeed API should be integrated with the library and your backend server.

[![Diagram illustrating datafeed architecture](/charting-library-docs/v29/img/datafeed-architecture-diagram-light.svg)![Diagram illustrating datafeed architecture](/charting-library-docs/v29/img/datafeed-architecture-diagram-dark.svg)](/charting-library-docs/v29/img/datafeed-architecture-diagram-light.svg)

### Asynchronous callbacks[​](#asynchronous-callbacks "Direct link to Asynchronous callbacks")

As mentioned [above](#overview), you should evoke callbacks to pass data to the library. Note that all callbacks should be evoked **asynchronously**. In context of the JavaScript Event Loop, the callbacks can only be evoked within different MacroTask. Otherwise, the *Uncaught RangeError: Maximum call stack size exceeded* [issue](/charting-library-docs/v29/connecting_data/Datafeed-Issues#maximum-call-stack-size-exceeded) might occur.

If you have data ready at the time of a request, you can set a delay as demonstrated below to ensure that a callback is only evoked when the library is ready.

```
setTimeout(() => { historyCallback(data); }, 0);
```

Note that the library can modify bar data that you provide utilizing callbacks. Pass a copy of the data to avoid potential issues.

## List of methods[​](#list-of-methods "Direct link to List of methods")

All Datafeed API methods are divided into three groups:

* [Required methods](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods) — a minimum set of methods that you should implement to connect data to the chart.
* [Trading Platform methods](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods) — the methods that are required to enable most of the [Trading Platform](/charting-library-docs/v29/trading_terminal/) features including the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket), [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List), and [Depth of Market](/charting-library-docs/v29/trading_terminal/#depth-of-market).
* [Additional methods](/charting-library-docs/v29/connecting_data/datafeed-api/additional-methods) — the methods that allow you to enable additional features such as marks on the chart and a countdown to the bar close.