# UI elements: Symbol Search

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Symbol-Search

* [UI elements](/charting-library-docs/v29/ui_elements/)* Symbol Search

On this page

# Symbol Search

The *Symbol Search* is a button on the top toolbar that opens a dialog containing a search box.
*Symbol Search* is used to search and display instruments that match the entered full or partial instrument name.

![Symbol Search](/charting-library-docs/v29/assets/images/symbol-search-e79de6b6f6b1aa0f9eaba08da963bdcb.gif)

## Display symbols[​](#display-symbols "Direct link to Display symbols")

The way symbols appear in the *Symbol Search* depends on how you provide the data.

* If you use the built-in [UDF adapter](/charting-library-docs/v29/connecting_data/UDF), you can either implement a symbol [group request](/charting-library-docs/v29/connecting_data/UDF#symbol-group-request) or a [single request](/charting-library-docs/v29/connecting_data/UDF#symbol-search).
  The first method is suitable when you have a short list of symbols.
* If you implement a custom datafeed via [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/), use the [`searchSymbols`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#searchsymbols) method.

## Hide Symbol Search[​](#hide-symbol-search "Direct link to Hide Symbol Search")

If you do not want users to change the displayed instrument,
you can hide the *Symbol Search*.
To do this, include the `header_symbol_search` [featureset](/charting-library-docs/v29/customization/Featuresets) in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

## Open/close Symbol Search[​](#openclose-symbol-search "Direct link to Open/close Symbol Search")

To programmatically open the Symbol Search, call the [`executeActionById`](/charting-library-docs/v29/ui_elements/Chart#execute-action-by-id) method with the `symbolSearch` action ID.

```
widget.activeChart().executeActionById("symbolSearch");
```

To programmatically close the Symbol Search, call the [`closePopupsAndDialogs`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#closepopupsanddialogs) method.
This method closes any active dialog on the chart.

```
widget.closePopupsAndDialogs();
```

## Set request delay[​](#set-request-delay "Direct link to Set request delay")

If you want to reduce the number of search requests when users enter symbol names in the search box,
you can set a request delay in milliseconds.
To do this, use the [`symbol_search_request_delay`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol_search_request_delay) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
You can check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=727s) on YouTube for an implementation example.

## Override symbol names[​](#override-symbol-names "Direct link to Override symbol names")

Sometimes symbol names can be too long/short or implicitly reflect the meaning of the symbol name.
In these cases, you can use the [`symbol_search_complete`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol_search_complete) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
This property overrides the entered symbol name with whatever human-friendly form you want.
The overridden symbol name will then be requested by your server and plotted.

You can check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=3606s) on YouTube for an implementation example.

## Case-insensitive search[​](#case-insensitive-search "Direct link to Case-insensitive search")

By default, all letters that users type are displayed in uppercase. To allow case-insensitive search, disable the [`uppercase_instrument_names`](/charting-library-docs/v29/customization/Featuresets#uppercase_instrument_names) featureset.

## Filters[​](#filters "Direct link to Filters")

When users click *Symbol Search*, the search dialog appears.
The widget has predefined optional filters by symbol type and exchange.
To use them, pass a [`DatafeedConfiguration`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration) object with the [`symbols_types`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#symbols_types) and [`exchanges`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#exchanges) properties
as a parameter to the callback of the [`onReady`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#onready) method.

## Symbol grouping[​](#symbol-grouping "Direct link to Symbol grouping")

The search dialog can display symbols grouped by a root name.
For example, to group futures `ABC2023`, `ABC2024`, and `ABC2025` by the root name `ABC`,
provide a regular expression to the library.
The expression should consist of two capture groups,
where the first is the root name and the second is the expiration date.

To enable grouping, provide an object with regular expressions to parse symbol names in the [`symbols_grouping`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#symbols_grouping) property
of the [`DatafeedConfiguration`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration) interface.
Then pass the `DatafeedConfiguration` object as a parameter to the callback of the [`onReady`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#onready) method.

## Display logos[​](#display-logos "Direct link to Display logos")

If you want to display logos for symbols and exchanges within the search results, follow the steps below:

1. Enable the corresponding [featuresets](/charting-library-docs/v29/customization/Featuresets): `show_symbol_logos` and `show_exchange_logos`.
2. Provide URLs for symbols and exchanges in the [`logo_urls`](/charting-library-docs/v29/api/interfaces/Charting_Library.SearchSymbolResultItem#logo_urls) and [`exchange_logo`](/charting-library-docs/v29/api/interfaces/Charting_Library.SearchSymbolResultItem#exchange_logo) properties
   of the [`SearchSymbolResultItem`](/charting-library-docs/v29/api/interfaces/Charting_Library.SearchSymbolResultItem) object.
   Pass the object as a parameter to the callback of the [`searchSymbols`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#searchsymbols) method.

## Enable spread operators[​](#enable-spread-operators "Direct link to Enable spread operators")

**Spread operators** are operators that allow comparison between a financial instrument, such as a stock,
and an additional variable, such as another financial instrument or a numerical value.

caution

The library does not handle the spread calculations, you should perform them on your server.
For example, when users enter "APPL-TSLA", the [datafeed](/charting-library-docs/v29/connecting_data/datafeed-api/) is called with the `AAPL-TSLA` symbol name.
The library expects your datafeed to resolve the symbol information and return the relevant data.

To display spread operators in the *Symbol Search*, include the [`show_spread_operators`](/charting-library-docs/v29/customization/Featuresets#show_spread_operators) featureset in the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.

![Spread operators in the Search Symbol](/charting-library-docs/v29/assets/images/spread-operators-in-symbol-search-3f22b21208e93e762524ef686828ce89.png)