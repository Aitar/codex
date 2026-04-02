# UI elements: Price scale

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Price-Scale

* [UI elements](/charting-library-docs/v29/ui_elements/)* Price scale

On this page

# Price scale

**Price scale** (or price axis) is a vertical scale on the right or left side of the chart that maps prices to coordinates and vice versa.

![Price scale](/charting-library-docs/v29/assets/images/price-scale-2df66cd5c629858b0eff237d4d973796.png)

## UI interactions[​](#ui-interactions "Direct link to UI interactions")

This section describes how users can interact with the price scale.

### Adding price scale[​](#adding-price-scale "Direct link to Adding price scale")

Users can add new price scales via the [*Compare symbol*](/charting-library-docs/v29/ui_elements/indicators/#add-and-compare-new-series) dialog by selecting *New price scale*.

![Add new price scale](/charting-library-docs/v29/assets/images/add-new-price-scale-e41df4d21863740fd1986c1c84071b4a.gif)

info

The library allows users to have up to eight price scales on the chart.
However, only one price scale can be displayed on [mobile applications](/charting-library-docs/v29/mobile_specifics/).

### Changing position[​](#changing-position "Direct link to Changing position")

Users can place the price scale on the left or right side of the chart.
To do this, they should select the *Move scale to left/right* button in the context menu of the price scale.

![Change price scale position](/charting-library-docs/v29/assets/images/move-scale-to-left-5f5a2139dd120390a736f6f02c29a4a7.gif)

You can also programmatically [change a price scale position](#change-price-scale-position).

### Pinning to scale[​](#pinning-to-scale "Direct link to Pinning to scale")

Users can select *Pin to scale* in the symbol/indicator settings to attach symbols/indicators to the price scale.

![Pin to scale](/charting-library-docs/v29/assets/images/pin-to-scale-824f25927e7ad9bb7c8d0b56386d83df.gif)

You can also programmatically add a new indicator and [attach it to a new price scale](#attach-indicators-to-price-scale).

### Inverting price scale[​](#inverting-price-scale "Direct link to Inverting price scale")

Users can invert the scale via *Invert scale* in the context menu of the price scale.
When the option is enabled, the price increase is shown from top to bottom.

![Invert price scale](/charting-library-docs/v29/assets/images/invert-price-scale-ea2f11732ad2e9a5044a83279a294720.gif)

### Resetting price scale[​](#resetting-price-scale "Direct link to Resetting price scale")

Users can reset the price scale when it is in a non-default state.
Note that the *Reset price scale* option will not appear in the context menu
with adjustments such as moving the scale to the left or switching to logarithmic mode.

![Reset price scale](/charting-library-docs/v29/assets/images/reset-price-scale-ffca478582b6c29efe01996e61b6f57a.gif)

### Quick trading[​](#quick-trading "Direct link to Quick trading")

info

This feature is only available in [Trading Platform](/charting-library-docs/v29/trading_terminal/).

By default, the price scale includes a *Plus* button.
When users click this button, a context menu opens, allowing them to quickly access trading options.
Note that this menu will be empty unless you implement the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api).

![Plus button on the price scale](/charting-library-docs/v29/assets/images/plus-button-price-scale-5b8f35a3c2b7372125c0a668b1e12a2f.gif)

To detect when the user clicks the *Plus* button, you can listen for the [`onPlusClick`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#onplusclick) event.

You can disable this button by adding the [`chart_crosshair_menu`](/charting-library-docs/v29/customization/Featuresets#chart_crosshair_menu) featureset to the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

## Style and default settings[​](#style-and-default-settings "Direct link to Style and default settings")

### Customize price scale appearance[​](#customize-price-scale-appearance "Direct link to Customize price scale appearance")

You can customize the appearance of the price scale using the [Overrides API](/charting-library-docs/v29/customization/overrides/).
For example, the code sample below changes the text color and font size of the price and [time](/charting-library-docs/v29/ui_elements/Time-Scale) scales.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    overrides: {  
        "scalesProperties.textColor": "#FF0000",  
        "scalesProperties.fontSize": 14,  
    }  
})
```

Refer to the [Scale colors and fonts](/charting-library-docs/v29/customization/overrides/chart-overrides#scale-colors-and-fonts) section to see the full list of the overrides properties.

### Change price scale position[​](#change-price-scale-position "Direct link to Change price scale position")

You can change the position of the price scale attached to the main series.
When creating a chart, use the [`priceScaleSelectionStrategyName`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides#pricescaleselectionstrategyname) property of the [Overrides API](/charting-library-docs/v29/customization/overrides/).
For example, the code sample below changes the price scale position to the left.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    overrides: {  
        "priceScaleSelectionStrategyName": "left",  
    }  
})
```

If the chart is already created, use the [`changePriceScale`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISeriesApi#changepricescale) method of the [`ISeriesApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISeriesApi) interface.
For example, the code sample below also changes the price scale position of the main series to the left.

```
widget.onChartReady(() => {  
    widget.activeChart().getSeries().changePriceScale("new-left");  
});
```

### Attach indicators to price scale[​](#attach-indicators-to-price-scale "Direct link to Attach indicators to price scale")

You can attach [indicators](/charting-library-docs/v29/ui_elements/indicators/) to the price scale.
To do this, specify the [`priceScale`](/charting-library-docs/v29/api/interfaces/Charting_Library.CreateStudyOptions#pricescale) property in the `options` parameter of the [`createStudy`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudy) method.
For example, the code sample below creates a *Volume* indicator and attaches it to a new price scale on the left.

```
widget.onChartReady(() => {  
    widget.activeChart().createStudy('Volume', false, false, undefined, undefined, { "priceScale": "new-left" });  
});
```

### Hide price scale[​](#hide-price-scale "Direct link to Hide price scale")

If you want to hide the price scale when all series or indicators attached to it are hidden,
enable the [`hide_price_scale_if_all_sources_hidden`](/charting-library-docs/v29/customization/Featuresets#hide_price_scale_if_all_sources_hidden) featureset.

### Hide settings button[​](#hide-settings-button "Direct link to Hide settings button")

The scale settings button is available directly below the price scale.
If users have more than one price scale on the chart, a letter will be displayed in place of the settings button.
Users should click the letter that indicates the scale to open the corresponding scale settings.
If you want to hide the settings button, disable the [`main_series_scale_menu`](/charting-library-docs/v29/customization/Featuresets#main_series_scale_menu) featureset.

### Add labels[​](#add-labels "Direct link to Add labels")

You can add labels to the price scale to display additional information like a symbol name, bid/ask prices, indicators, and more.
For example, the code sample below adds a symbol name label on the price scale.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    overrides: {  
        "scalesProperties.showSymbolLabels": true,  
    }  
})
```

Refer to the [Labels on the scale](/charting-library-docs/v29/customization/overrides/chart-overrides#labels-on-the-scale) section to see the full list of the overrides properties.

### Enable auto scaling[​](#enable-auto-scaling "Direct link to Enable auto scaling")

You can enable auto scaling using the [`setAutoScale`](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi#setautoscale) method of the [Price Scale API](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi).

```
widget.onChartReady(() => {  
    const priceScale = widget.activeChart().getPanes()[0].getMainSourcePriceScale();  
    priceScale.setAutoScale(true)  
});
```

### Set mode[​](#set-mode "Direct link to Set mode")

You can set the price scale mode using the [Overrides API](/charting-library-docs/v29/customization/overrides/) or [Price Scale API](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi).
However, you cannot change the price scale mode using the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method.

When creating a chart, use [`overrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#overrides) to change the price scale mode.
For example, the code sample below enables the percentage mode.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    overrides: {  
        "mainSeriesProperties.priceAxisProperties.percentage": true,  
    }  
})
```

Refer to the [Price scale mode](/charting-library-docs/v29/customization/overrides/chart-overrides#price-scale-mode) section to see the full list of the overrides properties.

If the chart is already created, you can change the price scale mode only using the [`setMode`](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi#setmode) method of the [Price Scale API](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi).
For example, the code sample below also enables the percentage mode.

```
widget.onChartReady(() => {  
    const priceScale = widget.activeChart().getPanes()[0].getRightPriceScales()[0];  
    priceScale.setMode(2);  
});
```

### Set visible price range[​](#set-visible-price-range "Direct link to Set visible price range")

If you want to set a visible price range of the price scale,
you can use the [`setVisiblePriceRange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi#setvisiblepricerange) method of the [Price Scale API](/charting-library-docs/v29/api/interfaces/Charting_Library.IPriceScaleApi).
For example, the code sample below sets the visible price range between 140 and 170.

```
widget.onChartReady(() => {  
    const priceScale = widget.activeChart().getPanes()[0].getRightPriceScales()[0];  
    priceScale.setVisiblePriceRange({ "from": 140, "to": 170 });  
});
```

## Price formatting[​](#price-formatting "Direct link to Price formatting")

The [`format`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#format) property in the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object determines how prices appear on the scale.
Specifying the `volume` format displays prices as decimals in thousands, millions, billions, or trillions.

If you specify the `price` format, the prices will be formatted in decimal or fractional format
according to the `minmov`, `pricescale`, `minmove2`, `fractional`, `variablemintick` properties.
Refer to the [Price Format](/charting-library-docs/v29/connecting_data/Symbology#price-format) section for more information.

You can also [change the decimal sign](#change-decimal-sign) for the prices
or [implement your custom logic](#use-custom-formatting) of the price formatting.

### Change decimal sign[​](#change-decimal-sign "Direct link to Change decimal sign")

You can apply custom formatting using the [`numeric_formatting`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#numeric_formatting) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
For example, the code sample below sets a comma to separate the decimal/fractional part of the prices.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    numeric_formatting: { decimal_sign: "," },  
})
```

The image below shows that the decimal parts of the prices on the price scale and the legend are separated with a comma.

![Numeric formatting](/charting-library-docs/v29/assets/images/price-scale-numeric-formatting-da8bbd44b24de8cb585575b3cecec1e4.png)

### Use custom formatting[​](#use-custom-formatting "Direct link to Use custom formatting")

You can adjust the display format of price values using the [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_formatters) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
For example, the code sample below defines a custom price formatting function for the `volume` [format type](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#format).
This function replaces numerical zeros with letter representations like billions (B), millions (M), and thousands (K).

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    custom_formatters: {  
        priceFormatterFactory: (symbolInfo, minTick) => {  
            if (symbolInfo === null) {  
                return null;  
            }  
  
            if (symbolInfo.format === 'volume') {  
                return {  
                    format: (price, signPositive) => {  
                        if (price >= 1000000000) {  
                            return `${(price / 1000000000).toFixed(3)}B`;  
                        }  
  
                        if (price >= 1000000) {  
                            return `${(price / 1000000).toFixed(3)}M`;  
                        }  
  
                        if (price >= 1000) {  
                            return `${(price / 1000).toFixed(3)}K`;  
                        }  
  
                        return price.toFixed(2);  
                    },  
                };  
            }  
            return null; // The default formatter will be used.  
        },  
    }  
})
```

## Symbol currency[​](#symbol-currency "Direct link to Symbol currency")

### Display symbol currency[​](#display-symbol-currency "Direct link to Display symbol currency")

To display symbol currency on the price scale, follow the steps below.

1. Enable the [`pricescale_currency`](/charting-library-docs/v29/customization/Featuresets#pricescale_currency) featureset to show the *Currency* menu in *Chart Settings → Scales*.
2. Assign a currency code to the [`currency_code`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#currency_code) property of the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
   Note that the currency code must be a three-letter string in the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) format.

### Enable currency conversion[​](#enable-currency-conversion "Direct link to Enable currency conversion")

The library provides a drop-down menu for selecting the currency in which the symbol is displayed.
To switch between currencies, you should implement the currency conversion.
Follow the steps below to enable the currency conversion.

1. Enable the [`pricescale_currency`](/charting-library-docs/v29/customization/Featuresets#pricescale_currency) featureset to show the *Currency* menu in *Chart Settings → Scales*.
2. Add the [`currency_code`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#currency_code) and [`original_currency_code`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#original_currency_code) properties to the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
   Note that the currency code must be a three-letter string in the [ISO 4217](https://www.iso.org/iso-4217-currency-codes.html) format.
3. Provide a list of available currencies in the [`currency_codes`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#currency_codes) property of the [`DatafeedConfiguration`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration) object.
4. Pass [`currencyCode`](/charting-library-docs/v29/api/interfaces/Charting_Library.SymbolResolveExtension#currencycode) to the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method.
5. Implement the conversion algorithm. The conversion algorithms can vary, but you can choose one from the following two:
   * **Constant currency rate algorithm**. With this approach, you retrieve the current currency exchange rate and multiply each bar by this value.
     However, this approach may yield inaccurate results for historical bars if the exchange rate has fluctuated significantly over time.
   * **Corresponding currency rate algorithm**.
     With this approach, you request historical currency exchange rates from the server and then multiply each bar by its corresponding currency rate.

info

Implementing either of these algorithms is straightforward when all symbols and Forex rates share the same time zone.
However, if time zones differ, you need to find an appropriate way to accurately match the corresponding rate to each bar.

After this, users can view symbol prices in their preferred currency.
To switch to a different currency, users can click the currency drop‑down menu and choose another option.
When a new currency is selected, the `resolveSymbol` method is called with the same `symbolInfo`
but with an added `currency_code` property indicating the chosen currency.

![Hide context menu](/charting-library-docs/v29/assets/images/currency-drop-down-menu-b61960f1893b731987c23c7fae9e2dfb.png)