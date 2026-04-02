# Customization: Customization precedence

Source: https://www.tradingview.com/charting-library-docs/v29/customization/customization-precedence

* [Customization](/charting-library-docs/v29/customization/)* Customization precedence

On this page

# Customization precedence

The library offers multiple approaches to modify the chart's appearance and behavior.
This article lists these approaches and demonstrates an example to clarify their order of precedence.

## Approaches[​](#approaches "Direct link to Approaches")

The table below provides an overview of customization methods/properties and their precedence.

When multiple methods define the same entity, the one with higher precedence will be applied.
Here, a lower number means higher precedence, for example:

* 1 — takes effect first, meaning it will override other approaches
* 8 — takes effect only if no higher-precedence method/property overrides the same entity

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Methods/Properties Description Precedence|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [`applyOverrides`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.IChartingLibraryWidget/#applyoverrides)   [#](#applyOverrides "Direct link to this Featureset") Applies overrides to the chart without reloading. Refer to [Overrides](https://www.tradingview.com/charting-library-docs/latest/customization/overrides/) for more information.  1 | [`load`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.IChartingLibraryWidget/#load)   [#](#load "Direct link to this Featureset") Loads the chart state from an object when the chart is initialized. Refer to the [Low-level API](https://www.tradingview.com/charting-library-docs/latest/saving_loading/#low-level-api) section for more information.  2 | [`saved_data`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#saved_data)   [#](#saved_data "Direct link to this Featureset") Sets an object that contains saved chart content. Refer to the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=1277s) on YouTube for an implementation example.  3 | [`settings_overrides`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#settings_overrides)   [#](#settings_overrides "Direct link to this Featureset") Overrides chart settings loaded from a custom settings adapter or a local storage. Refer to the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=3805s) on YouTube for an implementation example.  4 | [`settings_adapter`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#settings_adapter)   [#](#settings_adapter "Direct link to this Featureset") Allows creating your custom settings adapter to save user settings to your preferred storage, including server-side. Refer to the [Save user settings](https://www.tradingview.com/charting-library-docs/latest/saving_loading/user-settings) article for more information.  5 | [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)   [#](#localStorage "Direct link to this Featureset") Allows storing chart settings in the browser's local storage via the [`Storage`](https://developer.mozilla.org/en-US/docs/Web/API/Storage) object. You can disable storing properties in the local storage by using the [`use_localstorage_for_settings`](https://www.tradingview.com/charting-library-docs/latest/customization/Featuresets#use_localstorage_for_settings) featureset.  6 | [`overrides`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#overrides)   [#](#overrides "Direct link to this Featureset") Overrides default values of the widget properties. Refer to [Overrides](https://www.tradingview.com/charting-library-docs/latest/customization/overrides/) for more information.  7 | [`custom_themes`](https://www.tradingview.com/charting-library-docs/latest/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions/#custom_themes)   [#](#customThemes "Direct link to this Featureset") Overrides default colors of the light and darks themes. Refer to [Custom themes API](https://www.tradingview.com/charting-library-docs/latest/customization/styles/custom-themes) for more information.  8 | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Example[​](#example "Direct link to Example")

You can check out the following example to understand how these approaches override each other.
Change the flags' values provided at the beginning of the JavaScript file (lines 1-7) to easily manage the example.

The coloring of the candle bodies will vary based on the approach applied.
Below, you will find the colors associated with each method/property.

* `applyOverrides` → orange
* `load` → blue
* `saved_data` → red
* `settings_overrides` → purple
* `settings_adapter` → green
* `localStorage` → black
* `overrides` → yellow

See the Pen [Chart customization order](https://codepen.io/tradingview/pen/jOdpQEo) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).