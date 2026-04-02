# Trading Platform: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/

* Trading Platform

On this page

# Trading Platform

## Overview[​](#overview "Direct link to Overview")

[Trading Platform](https://github.com/tradingview/trading_platform "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) is a standalone client-side solution that provides trading capabilities. Trading Platform is based on [Advanced Charts](/charting-library-docs/v29/getting_started/#what-is-advanced-charts) and contains all its [features](/charting-library-docs/v29/getting_started/Key-Features#advanced-charts-features).

If you already use Advanced Charts and want to get started with Trading Platform, refer to the [How to migrate from Advanced Charts](#how-to-migrate-from-advanced-charts) guide. Otherwise, you should refer to [Quick start](/charting-library-docs/v29/getting_started/quick-start) to start the implementation from scratch.

[View Trading Platform demo](https://trading-terminal.tradingview-widget.com/)

## Trading Platform features[​](#trading-platform-features "Direct link to Trading Platform features")

### Multiple-chart layout[​](#multiple-chart-layout "Direct link to Multiple-chart layout")

Users can display up to 8 charts on one layout using the *Select Layout* button on the top toolbar.
Charts can be synchronized by a symbol, [interval (resolution)](/charting-library-docs/v29/core_concepts/Resolution), crosshair, time, and [date range](/charting-library-docs/v29/getting_started/glossary#date-range).

![Multiple-chart layout](/charting-library-docs/v29/assets/images/multiple-chart-layout-ea1fb3b94a8fb86aa8517602c4100752.png)

Selecting multiple-chart layouts is enabled by default.
If you want to disable this option,
add the [`header_layouttoggle`](/charting-library-docs/v29/customization/Featuresets#header_layouttoggle) and [`support_multicharts`](/charting-library-docs/v29/customization/Featuresets#support_multicharts) featuresets to the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

### Chart trading[​](#chart-trading "Direct link to Chart trading")

Orders, positions, potential income and loss are displayed on the chart in Trading Platform. Users can place orders right from the chart. To enable chart trading, implement the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api). Then use the [`broker_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_factory) method in [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to pass the implementation to the library.

![Chart trading feature](/charting-library-docs/v29/assets/images/trading-cap-a59edb8c88791854ce7dbc450ae38929.png)

### Depth of Market[​](#depth-of-market "Direct link to Depth of Market")

The Depth of Market (DOM) widget supports frequent data updates and shows the volume for each price.
Data is displayed in static mode.
This means that the price series is fixed, while the current price moves within, above, or below the designated range.

Users can also place orders right from the widget.
Refer to [Depth of Market](/charting-library-docs/v29/trading_terminal/depth-of-market) for more information.

![DOM widget](/charting-library-docs/v29/assets/images/dom-widget-static-3ee73e53b032e32a6c8bfeb7419cd496.png)

### Watchlist[​](#watchlist "Direct link to Watchlist")

The Watchlist widget allows users to track their favorite symbols and switch quickly between the corresponding charts. Users can create multiple lists and sort symbols by their names, price changes, and volumes. Refer to [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List) for more information.

![Watchlist widget](/charting-library-docs/v29/assets/images/watchlist-widget-16811ef6c97d3d564c44a82ee18d4371.png)

### Details[​](#details "Direct link to Details")

The Details widget displays a certain symbol's information such as bid/ask prices, trading hours, and a price range during the day. To display the widget, you should enable the [`details`](/charting-library-docs/v29/api/interfaces/Charting_Library.WidgetBarParams#details) property in the [`widgetbar`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#widgetbar) settings. The widget requires quote data that you should send using the corresponding methods in the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) or [UDF](/charting-library-docs/v29/connecting_data/UDF#quotes).

![Details widget](/charting-library-docs/v29/assets/images/details-widget-22f9f1b792575f6bae0fff846e39d6fe.png)

### News[​](#news "Direct link to News")

The News widget displays news on a certain symbol. You can fetch news using RSS or the library's API. Refer to [News](/charting-library-docs/v29/trading_terminal/news) for more information.

![News widget](/charting-library-docs/v29/assets/images/news-widget-cb7489d4cfee10542fdd925309835983.png)

### Account Manager[​](#account-manager "Direct link to Account Manager")

The Account Manager (Trading Panel) widget displays information from your broker account, such as orders, positions, an account balance, and more. Users can manage their orders and positions from the widget. You can add custom tabs and tables to the widget. Refer to [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/) for more information.

![Account Manager](/charting-library-docs/v29/assets/images/account-manager-86ebf69afbfea3b80bc4541b26167351.png)

### Advanced Order Ticket[​](#advanced-order-ticket "Direct link to Advanced Order Ticket")

The Advanced Order Ticket dialog allows users to place different types of orders, including trailing stop, stop-loss, bracket orders, and more. To open this dialog, users should click the *Trade* button in [*Account Manager*](#account-manager).

![Order Ticket](/charting-library-docs/v29/assets/images/order-ticket-cba466312927cc1e24a56ca7cbbc24a1.png)

You can add custom fields, enable an order preview, or implement your own custom Order Ticket.
Refer to [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket) for more information.

### Buy/Sell buttons and lines[​](#buysell-buttons-and-lines "Direct link to Buy/Sell buttons and lines")

The Buy/Sell buttons are displayed next to the [legend](/charting-library-docs/v29/ui_elements/Legend). Click the buttons to open [Order Ticket](#advanced-order-ticket) and place orders instantly. Trading Platform also supports bid/ask price lines on the chart.

![Buy/Sell Buttons](/charting-library-docs/v29/assets/images/buy-sell-buttons-3c77c6e0eed1387b6da2dd24b31ddde9.png)

tip

The buttons can be customized with [CSS](/charting-library-docs/v29/customization/styles/CSS-Color-Themes#buysell-buttons-properties).

### Japanese chart types[​](#japanese-chart-types "Direct link to Japanese chart types")

Trading Platform includes all [chart types](/charting-library-docs/v29/getting_started/Key-Features#chart-types) available in Advanced Charts and additional types listed below:

* Renko
* Point-and-Figure
* Line Break
* Kagi

### Drawing templates[​](#drawing-templates "Direct link to Drawing templates")

Trading Platform allows users to create drawing templates. For more information, refer to the [Drawings](/charting-library-docs/v29/ui_elements/drawings/#templates) article.

### Building seconds bars from ticks[​](#building-seconds-bars-from-ticks "Direct link to Building seconds bars from ticks")

Trading Platform can build seconds bars from ticks. For more information, refer to [`build_seconds_from_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#build_seconds_from_ticks).

## How to migrate from Advanced Charts[​](#how-to-migrate-from-advanced-charts "Direct link to How to migrate from Advanced Charts")

If you want to migrate from Advanced Charts to Trading Platform, you should replace the `charting_library` folder in your project with the same folder from the [trading\_platform](https://github.com/tradingview/trading_platform "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) repository.
At this point, you will have additional chart types (Renko, Point-and-Figure, Line Break, and Kagi), the synchronized multiple-chart layout, and an empty [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/).

![Default Trading Platform features](/charting-library-docs/v29/assets/images/tt_default_features-6869626bd4315430083901547fcfeaee.png)

To enable the [Watchlist](#watchlist), [Details](#details), [Order Ticket](#advanced-order-ticket), [News](#news), and [Depth of Market](#depth-of-market) widgets, you need to implement the Datafeed API methods related to [trading](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods). You should also enable the corresponding [featuresets](/charting-library-docs/v29/customization/Featuresets#trading-platform) or the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor#trading-platform-parameters) parameters. If you want to add [trading capabilities](#chart-trading), you should implement the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api). The part of the Trading Platform implementation is shown in the [`trading.html`](https://github.com/tradingview/trading_platform/blob/master/trading.html "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) file.

Pay attention that data for the legend is requested in the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) method on the **[mobile version](/charting-library-docs/v29/mobile_specifics/) of Trading Platform**. If this method is not implemented, you may see the `N/A` values instead of prices.

## See also[​](#see-also "Direct link to See also")

For more information on how to integrate Trading Platform, refer to the following articles:

* [Core trading concepts](/charting-library-docs/v29/trading_terminal/trading-concepts/): learn about the trading components, how they integrate into the chart widget, and how they work together.
* [Implement Broker API](/charting-library-docs/v29/tutorials/implement-broker-api/): follow the step-by-step tutorial that walks you through implementing the required methods to enable basic trading functionality.
* [Widget Constructor](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions): check the Widget Constructor parameters specific to Trading Platform.