# Custom Indicators: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/custom_studies/

* Custom Indicators

On this page

# Custom indicators

Advanced Charts and Trading Platform support more than 100 [indicators](/charting-library-docs/v29/ui_elements/indicators/).
You can also create your custom indicators in JavaScript using the library's API. The API allows you to create a variety of indicators using different plot types, styles, colors, and mathematical functions.

Users can [add a custom indicator](/charting-library-docs/v29/ui_elements/indicators/#add-an-indicator) to the chart and change some indicator parameters using the *Indicators* and *Settings* dialog in the UI, respectively. However, users cannot create their own indicators or change the code of the existing ones.

info

[Pine Script®](https://www.tradingview.com/pine-script-docs/) is not supported in the libraries.

## Add indicators[​](#add-indicators "Direct link to Add indicators")

To add custom indicators to the library, specify a function that returns a Promise object with an array of custom [indicator objects](#indicator-object). Assign this function to the [`custom_indicators_getter`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_indicators_getter) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        // Indicator objects  
        {  
            // ...  
        },  
        {  
            // ...  
        },  
    ]);  
},
```

## Indicator object[​](#indicator-object "Direct link to Indicator object")

A custom indicator is an instance of [`CustomIndicator`](/charting-library-docs/v29/api/interfaces/Charting_Library.CustomIndicator) that contains the following fields:

* `name`: an indicator's internal name that is not visible in the UI. This name should be unique.
* `metainfo`: the field that describes how the indicator looks like. This field defines the [plot](/charting-library-docs/v29/getting_started/glossary#plot) types that represent the indicator and contains information, such as an indicator's name, description, style, color, and more. Refer to the [Metainfo](/charting-library-docs/v29/custom_studies/metainfo/) article for more information.
* `constructor`: the field that contains functions `init()` and `main()`. You should specify data calculations in these functions. Refer to [Constructor](/charting-library-docs/v29/custom_studies/custom-indicator-constructor) for more information.

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            // Indicator object  
            name: 'Custom indicator name',  
            metainfo: {  
                // ...  
            },  
            constructor: function() {  
                // ...  
            }  
        }  
    ]);  
},
```

## Examples[​](#examples "Direct link to Examples")

Follow the links below to explore some implementation examples of custom indicators.

* [Requesting data for another ticker](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#requesting-data-for-another-ticker)
* [Coloring bars](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#coloring-bars)
* [Advanced Coloring Candles](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#advanced-colouring-candles)
* [Custom styles for every point](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#custom-styles-for-every-point)
* [Complex filled areas](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#complex-filled-areas)
* [OHLC plots](/charting-library-docs/v29/custom_studies/Custom-Studies-OHLC-Plots)
* [Advanced Shapes use](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#advanced-shapes-use)