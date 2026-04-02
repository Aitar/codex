# Getting Started: Other TradingView products

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/product-comparison

* [Getting Started](/charting-library-docs/v29/getting_started/)* Other TradingView products

On this page

# Other TradingView products

TradingView provides several charting solutions to display financial data. This page contains brief overview of these products and highlights their differences from Advances Charts / Trading Platform.
For detailed information, refer to the [Compare libraries](https://www.tradingview.com/free-charting-libraries/) page.

## Lightweight Charts™[​](#lightweight-charts "Direct link to Lightweight Charts™")

[Lightweight Charts™](https://github.com/tradingview/lightweight-charts) is a free, open-source client-side library. It is 45 KB in size, which is smaller than a typical image of a chart.
The main difference between this library and Advanced Charts is the way they retrieve data:

* In Advanced Charts, you pass data in response to the library's request.
* In Lightweight Charts™, you provide data directly to the library without any requests.

info

Neither Advanced Charts nor Lightweight Charts™ contains any market data. You should use data from your own source or third-party providers.

Note that Lightweight Charts™ does not contain any built-in indicators. Therefore, you should implement them on your own if required. Consider the [Moving Average](https://tradingview.github.io/lightweight-charts/tutorials/demos/moving-average) implementation example.

If you want to migrate from Lightweight Charts™ to Advanced Charts, consider the following table that contains common methods with similar functionality:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Functionality Lightweight Charts™ Advanced Charts|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Create a chart `createChart` Specify the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).| Add a series of certain style [`addLineSeries`](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/IChartApiBase#addlineseries) or [`addCandlestickSeries`](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/IChartApiBase#addcandlestickseries) Specify any [series style](/charting-library-docs/v29/customization/overrides/chart-overrides#chart-styles) using the [`overrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#overrides) property of the Widget Constructor.| Get a pixel coordinate [`timeToCoordinate`](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/ITimeScaleApi#timetocoordinate) Advanced Charts / Trading Platform does not contain such method. As an alternative, consider using methods from the [`ITimeScaleApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimeScaleApi) interface.| Create a price line [`createPriceLine`](https://tradingview.github.io/lightweight-charts/docs/api/interfaces/ISeriesApi#createpriceline) [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline) or [`createShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createshape) | | | | | | | | | | | | | | |

## Widgets[​](#widgets "Direct link to Widgets")

[Widgets](https://www.tradingview.com/widget-docs/) are free and simple standalone applications that do not require any code implementation.
To embed a widget in your website, you just need to copy and paste the provided code.
Widgets are hosted on the TradingView servers and display the TradingView data.

Compared to libraries, widgets offer fewer customization options. However, widgets have some additional features, such as Heatmaps and Hotlists, that are [not supported](/charting-library-docs/v29/getting_started/Key-Features#unsupported-features) in Advanced Charts.

If you like the Advanced Charts library but do not have your own data, consider using the [Advanced Chart widget](https://www.tradingview.com/widget-docs/widgets/charts/advanced-chart/).

info

Note that you cannot connect your data to the widgets.