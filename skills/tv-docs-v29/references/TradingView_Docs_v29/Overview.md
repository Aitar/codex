# API: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/api/

* API Reference

On this page

# API Reference



## Structure[​](#structure "Direct link to Structure")

The API is structured as a modular system of types, interfaces, and enumerations.
The library's API is divided into three modules, where each module consists of interfaces that define properties and methods specific to its functionality.

### Charting Library module[​](#charting-library-module "Direct link to Charting Library module")

The [Charting Library module](/charting-library-docs/v29/api/modules/Charting_Library) is designed to manage chart creation, customize the UI appearance, and handle user interactions.

#### Key features[​](#key-features "Direct link to Key features")

* Manage drawings and indicators displayed on the chart.
* Customize chart themes, layouts, and behaviors.
* Handle user interactions through events and methods.

#### Common interfaces[​](#common-interfaces "Direct link to Common interfaces")

[## Advanced Charts Widget Options

Properties for Advanced Chart widget to customize its appearance and behavior](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/)

[## Trading Platform Widget Options

Properties for Trading Platform widget to customize its appearance and behavior](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions/)

[## IChartingLibrary Widget

Primary interface for library interactions](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget/)

[## IChart Widget

Primary interface for chart interactions, such as creating drawings and indicators](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi/)

  

### Datafeed module[​](#datafeed-module "Direct link to Datafeed module")

The [Datafeed module](/charting-library-docs/v29/api/modules/Datafeed) is designed to integrate custom data sources and controlling data flow to the chart.

#### Key features[​](#key-features-1 "Direct link to Key features")

* Connect any market data source to Advanced Charts.
* Handle custom symbology logic to map your backend symbols to TradingView's requirements.
* Synchronize chart data with live market data updates.

#### Common interfaces[​](#common-interfaces-1 "Direct link to Common interfaces")

[## SymbolInfo

Defines the structure and metadata for symbols, including properties like ticker and exchange](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo/)

[## IExternal Datafeed

Acts as the entry point for connecting custom datafeeds to the library](/charting-library-docs/v29/api/interfaces/Datafeed.IExternalDatafeed)

[## IDatafeed Chart

Provides methods for fetching and managing historical and real-time data](/charting-library-docs/v29/api/interfaces/Datafeed.IDatafeedChartApi)

[## IDatafeed Quotes

Enables the retrieval and management of real-time market quotes](/charting-library-docs/v29/api/interfaces/Datafeed.IDatafeedQuotesApi)

  

### Broker module[​](#broker-module "Direct link to Broker module")

The [Broker module](/charting-library-docs/v29/api/modules/Broker) is designed to integrate trading capabilities provided by [Trading Platform](/charting-library-docs/v29/trading_terminal/).

#### Key features[​](#key-features-2 "Direct link to Key features")

* Enable creating market, limit, and other order types directly from the chart interface.
* Provide real-time market quotes to power trading features like the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket), [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List), and [Depth of Market](/charting-library-docs/v29/trading_terminal/depth-of-market).
* Support multiple account setups for users with diverse trading needs.

#### Common interfaces[​](#common-interfaces-2 "Direct link to Common interfaces")

[## Broker API

Enables trading features and connects the charts with your trading logic](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal)

[## Trading Host

Receives trading information from your backend server and provides the library with updates](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost)

[## Broker configuration

Defines configuration for additional Trading Platform features](/charting-library-docs/v29/api/interfaces/Charting_Library.SingleBrokerMetaInfo)

  

## Best practices for navigation[​](#best-practices-for-navigation "Direct link to Best practices for navigation")

1. Identify the module relevant to your task: [creating charts](#charting-library-module), [managing datafeeds](#datafeed-module), or [enabling trading](#broker-module).
2. Examine the available interfaces within the module. Each interface defines a set of properties and methods relevant to a specific feature or functionality.
3. Follow type links and explore enumerations. If a property uses a non-primitive type, follow the link to the corresponding type definition. This will reveal additional properties and their relationships.
4. Get back into the context and use your browser’s navigation to return to higher-level modules or interfaces when needed.

### Browse TypeScript definition[​](#browse-typescript-definition "Direct link to Browse TypeScript definition")

Alternatively, if you are more comfortable browsing the API through a TypeScript definition file, you can use the following links:

* [Charting Library and Broker TypeScript definition](https://github.dev/tradingview/charting_library/blob/master/charting_library/charting_library.d.ts)
* [Datafeed TypeScript definition](https://github.dev/tradingview/charting_library/blob/master/charting_library/datafeed-api.d.ts)

#### Keyboard shortcuts for Visual Studio Code[​](#keyboard-shortcuts-for-visual-studio-code "Direct link to Keyboard shortcuts for Visual Studio Code")

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action Windows shortcut macOS shortcut|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Find `Ctrl` + `F` `Cmd` + `F`| Go to definition `F12` or `Ctrl` + Click `F12` or `Cmd` + Click| Go back `Ctrl` + `-` `Cmd` + `-` | | | | | | | | | | | |