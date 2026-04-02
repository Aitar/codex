# UI elements: Market Status

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/market-status

* [UI elements](/charting-library-docs/v29/ui_elements/)* Market Status

On this page

# Market Status

**Market Status** is a pop-up that contains information on the symbol trading session and current market status.
Users should click the icon within the [*Legend*](/charting-library-docs/v29/ui_elements/Legend) to open this pop-up.

![Market Status](/charting-library-docs/v29/assets/images/market-status-example-ef63a72532b30d3e20db32e92ba7e380.png)

## Session timeline[​](#session-timeline "Direct link to Session timeline")

The timeline in the pop-up depends on the session configuration for the current symbol.
If the Market Status shows incorrect data, make sure you specified session correctly in the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
For more information, refer to the [Session](/charting-library-docs/v29/connecting_data/Symbology#session) and [Extended sessions](/charting-library-docs/v29/connecting_data/Symbology#extended-sessions) sections.

Note that the Market Status displays market hours in the **exchange time zone**.

## Customize the pop-up[​](#customize-the-pop-up "Direct link to Customize the pop-up")

### Change text[​](#change-text "Direct link to Change text")

You can specify the [`custom_translate_function`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_translate_function) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to change the default text in the pop-up.

```
var widget = (window.tvWidget = new TradingView.widget({  
    custom_translate_function: (key, options, isTranslated) => {  
        console.log('key: ', key);  
        if (key === "Market closed") {  
            return "The market is closed. Check back later.";  
        }  
        return null;  
    },  
}));
```

### Add custom section[​](#add-custom-section "Direct link to Add custom section")

You can display additional information, such as warnings, in the Market Status for a certain symbol. To do this, use the methods from [`ICustomSymbolStatusApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ICustomSymbolStatusApi) that allows you to customize an icon, color, tooltip, and content of the pop-up.
To retrieve an `ICustomSymbolStatusApi` object, call the [`customSymbolStatus`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#customsymbolstatus) method at any time after the chart is created.

Consider the following code sample that specifies additional section for AAPL.

![Custom Market Status](/charting-library-docs/v29/assets/images/custom-status-example-3fd07217ff275acd89ff43d428744646.png)

```
// Icon from https://heroicons.com  
const myCustomIconSvgString = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">  
<path fill-rule="evenodd" d="M13.5 4.938a7 7 0 11-9.006 1.737c.202-.257.59-.218.793.039.278.352.594.672.943.954.332.269.786-.049.773-.476a5.977 5.977 0 01.572-2.759 6.026 6.026 0 012.486-2.665c.247-.14.55-.016.677.238A6.967 6.967 0 0013.5 4.938zM14 12a4 4 0 01-4 4c-1.913 0-3.52-1.398-3.91-3.182-.093-.429.44-.643.814-.413a4.043 4.043 0 001.601.564c.303.038.531-.24.51-.544a5.975 5.975 0 011.315-4.192.447.447 0 01.431-.16A4.001 4.001 0 0114 12z" clip-rule="evenodd" />  
</svg>`;  
  
widget  
    .customSymbolStatus()  
    .symbol('NASDAQNM:AAPL') // Select the symbol  
    .setVisible(true) // Make the status visible  
    .setColor('rgb(255, 40, 60)') // Set the color  
    .setIcon(myCustomIconSvgString) // String for an SVG icon, i.e. '<svg> ... </svg>'  
    .setTooltip('Tooltip') // Text to be displayed within the hover tooltip  
    .setDropDownContent([  
        // Content to be displayed within the large pop-up tooltip  
        {  
            title: 'Title', // Title to be displayed within the pop-up  
            color: 'rgb(255, 60, 70)', // Optional, if you want it to be different to above  
            content: ['Explanation of status', '<br/><br/>', 'More details...'],  
            action: {  
                // Optional action to be displayed  
                text: 'Read more here',  
                tooltip: 'opens in a new window',  
                onClick: () => {  
                    window.open('https://www.tradingview.com/', '_blank');  
                },  
            },  
        },  
    ]);
```

caution

Make sure you pass a correct symbol ID to the [`ICustomSymbolStatusApi.symbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.ICustomSymbolStatusApi#symbol) method.
The ID should be the same as your datafeed provides to the library when the [`resolveSymbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#resolvesymbol) method is called.

To check the ID of the current symbol, call the [`IChartWidgetApi.symbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#symbol) method.

## Disable the pop-up[​](#disable-the-pop-up "Direct link to Disable the pop-up")

Add the [`display_market_status`](/charting-library-docs/v29/customization/Featuresets#display_market_status) featureset to
[`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) to hide the Market Status.