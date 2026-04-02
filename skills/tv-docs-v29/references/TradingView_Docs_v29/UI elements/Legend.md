# UI elements: Legend

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Legend

* [UI elements](/charting-library-docs/v29/ui_elements/)* Legend

On this page

# Legend

Legend is a list of series and indicators at the top-left corner of any chart.
Note that the legend position cannot be changed.

![Legend](/charting-library-docs/v29/assets/images/legend-overview-589e075d0acfbee82e1827ff021a6366.gif)

## Configure legend[​](#configure-legend "Direct link to Configure legend")

In the *Chart settings → Status line* dialog, users can configure the legend.

![Chart settings](/charting-library-docs/v29/assets/images/legend-chart-settings-ba5635efa6a732d07c7112aac491d3f8.png)

### Symbol logos[​](#symbol-logos "Direct link to Symbol logos")

If you want to display logos for symbols within the legend, follow the steps below:

1. Enable the [`show_symbol_logos`](/charting-library-docs/v29/customization/Featuresets#show_symbol_logos) and [`show_symbol_logo_in_legend`](/charting-library-docs/v29/customization/Featuresets#show_symbol_logo_in_legend) featuresets.
   The *Logo* option appears in the settings dialog.
2. Provide URLs for symbols in the [`logo_urls`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#logo_urls) property of the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
   Pass the object as a parameter to the callback of the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method.

### Open market status[​](#open-market-status "Direct link to Open market status")

By default, the library displays the current [market status](/charting-library-docs/v29/ui_elements/Symbol-Status) as an icon within the legend for the main series of the chart.
You can hide the market status by adding the [`display_market_status`](/charting-library-docs/v29/customization/Featuresets#display_market_status) featureset to the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

### Title[​](#title "Direct link to Title")

In the *Title* drop-down, users can select what title to display in the legend:

* Description
* Ticker
* Ticker and description

You can also set the title using the [Overrides API](/charting-library-docs/v29/customization/overrides/).
For example, the code sample below sets ticker as the legend title.

```
chartApi.applyOverrides({ "mainSeriesProperties.statusViewStyle.symbolTextSource": "ticker" })
```

### Last day change values[​](#last-day-change-values "Direct link to Last day change values")

info

Last day change can be displayed in Trading Platform only as it requires quote data.

Last day change is a parameter represented by two values: daily change and percentage daily change. You should specify these values in the [`ch`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedQuoteValues#ch) and [`chp`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedQuoteValues#chp) properties of `DatafeedQuoteValues`
and pass them to the library when it calls [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes).

Last day change is displayed in *Data Window* on the right toolbar. You can also add this parameter to the chart legend using the [overrides](/charting-library-docs/v29/customization/overrides/):

```
var widget = window.tvWidget = new TradingView.widget({  
    // ...  
    overrides: {  
        "paneProperties.legendProperties.showLastDayChange": true,  
    }  
});
```

Users can toggle the *Last day change values* option in the *Chart settings* dialog to change the last day change visibility in the legend. This option is hidden by default. To display it, you should enable one of the following featuresets:

* [`legend_last_day_change`](/charting-library-docs/v29/customization/Featuresets#legend_last_day_change) — adds the extra *Last day change values* option to the *Chart settings* dialog.
* [`show_last_price_and_change_only_in_series_legend`](/charting-library-docs/v29/customization/Featuresets#show_last_price_and_change_only_in_series_legend) — adds the last day change to the legend and hides the OHLC values. Also, the extra *Last day change values* option appears in the *Chart settings* dialog.

### Resolution[​](#resolution "Direct link to Resolution")

To disable resolution changing in the Legend, use the [`legend_inplace_edit`](/charting-library-docs/v29/customization/Featuresets#legend_inplace_edit) featureset.
If you want to completely remove the *Resolution* button from the *Legend*, use the [`hide_resolution_in_legend`](/charting-library-docs/v29/customization/Featuresets#hide_resolution_in_legend) featureset.

![Remove resolution from Legend](/charting-library-docs/v29/assets/images/no-resolution-legend-d2ff263da43b9adaccb9f03d4c14f1a3.png)

## Visibility customization[​](#visibility-customization "Direct link to Visibility customization")

You can use [featuresets](/charting-library-docs/v29/customization/Featuresets) or [overrides](/charting-library-docs/v29/customization/overrides/) to customize the legend's visibility such as hiding or displaying particular legend elements.
The sections below describe customization via featuresets.
For more information about override properties that affect the legend, refer to [Legend](/charting-library-docs/v29/customization/overrides/chart-overrides#legend).

### Hide legend[​](#hide-legend "Direct link to Hide legend")

You can hide the legend widget from the chart.
To do this, include the `legend_widget` [featureset](/charting-library-docs/v29/customization/Featuresets) in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

![Disable legend](/charting-library-docs/v29/assets/images/legend-hide-widget-3dd01451f395dfc5103ec54c4af6d01e.png)

### Hide legend buttons[​](#hide-legend-buttons "Direct link to Hide legend buttons")

You can hide all legend buttons by including the `edit_buttons_in_legend` in [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features).
Besides, disabling `show_hide_button_in_legend`, `format_button_in_legend`,
or `delete_button_in_legend` allows customizing particular legend buttons.
For example, the *Settings* button is hidden in the image below.

![Hide settings button](/charting-library-docs/v29/assets/images/legend-hide-settings-button-ea0b509607eabb58e03b821aa1f09a22.png)

### Hide context menu[​](#hide-context-menu "Direct link to Hide context menu")

When right-clicking the legend, you can access the context menu.
To disable this feature, include `legend_context_menu` in [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features).

![Hide context menu](/charting-library-docs/v29/assets/images/legend-context-menu-c540f1b35be76b429f05e5fcf6314aa4.png)

## Price formatting[​](#price-formatting "Direct link to Price formatting")

Prices are formatted according to the `pricescale`, `minmov`, `minmove2`, `fractional`, and `variable_tick_size` properties specified in the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
For more information, refer to the [Price format](/charting-library-docs/v29/connecting_data/Symbology#price-format) section.

You can also apply custom formatting using the [`numeric_formatting`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#numeric_formatting) property of [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

```
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com"),  
    symbol: "AAPL",  
    interval: "1D",  
    numeric_formatting: { decimal_sign: "," },  
})
```

In the code sample above, the comma separates the decimal/fractional part of the price.

![Numeric formatting](/charting-library-docs/v29/assets/images/legend-numeric-formatting-89279aeecf4432504fdc3f71267a581f.png)

## NaN values in legend[​](#nan-values-in-legend "Direct link to NaN values in legend")

If `NaN` values appear in the legend instead of the expected data,
ensure that you have implemented the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) and [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes) methods of the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/).
This issue appears in [mobile applications](/charting-library-docs/v29/mobile_specifics/) when running outside of tracking mode.
Outside this mode, the legend shows only three values: the closing price, price change, and price change percentage.
The library retrieves these values from the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) request, otherwise, it displays `NaN`.

Note that open, high, and low prices and indicator values are displayed in the tracking mode only.
To activate this mode, users should long tap on the chart. A single tap on the chart exits this mode.

## Display delayed data information[​](#display-delayed-data-information "Direct link to Display delayed data information")

Follow the steps below to enable the *Data is delayed* section in the legend:

1. Add the [`display_data_mode`](/charting-library-docs/v29/customization/Featuresets#display_data_mode) featureset to the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) object.
2. Provide the following properties in the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
   Pass this object as a parameter to the callback of the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method.
   * [`data_status`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#data_status) – specify `"delayed_streaming"`.
   * [`delay`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#delay) – specify delay in seconds.

The image below shows the *Data is delayed* section and the *D* icon in the legend.

![Data is delayed](/charting-library-docs/v29/assets/images/data-is-delayed-741f2420c57908102a90defe6f7294c6.png)