# Customization: Overrides

Source: https://www.tradingview.com/charting-library-docs/v29/customization/overrides/

* [Customization](/charting-library-docs/v29/customization/)* Overrides

On this page

# Overrides

The Overrides API allows you to customize elements on the chart like panes, scales, series, drawings, indicators, legends, and more.

## Chart and drawings[​](#chart-and-drawings "Direct link to Chart and drawings")

To override a property that relates to the chart, drawing, or trading element, you should specify this property in the [`overrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#overrides) parameter of [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor). The code sample below changes the chart background color and chart style using [`paneProperties.background`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides#panepropertiesbackground) and [`mainSeriesProperties.style`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides#mainseriespropertiesstyle).

```
var widget = window.tvWidget = new TradingView.widget({  
    // ...  
    overrides: {  
        "paneProperties.background": "#020024",  
        "mainSeriesProperties.style": 2,  
    }  
});
```

If you want to change a property's value on the fly, you can use the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method.

```
widget.applyOverrides({ "mainSeriesProperties.visible": false });
```

For more information on how to customize different entities using overrides, refer to the corresponding topics:

* [Chart overrides](/charting-library-docs/v29/customization/overrides/chart-overrides)
* [Drawings overrides](/charting-library-docs/v29/customization/overrides/Drawings-Overrides)
* [Trading overrides](/charting-library-docs/v29/customization/overrides/trading-overrides)

## Indicators[​](#indicators "Direct link to Indicators")

You can also customize indicators using overrides. Refer to the [Indicator Overrides](/charting-library-docs/v29/customization/overrides/indicator-overrides) article for more information.