# UI elements: Time scale

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Time-Scale

* [UI elements](/charting-library-docs/v29/ui_elements/)* Time scale

On this page

# Time scale

**Time scale** (or time axis) is a horizontal scale at the bottom of the chart that displays the time of bars.

![Time scale](/charting-library-docs/v29/assets/images/time-scale-3196a6556602023a8b3700cf1d833407.png)

## Time range[​](#time-range "Direct link to Time range")

Time (date) range is a period of time that is currently visible on the chart canvas. This range changes when users scale or scroll the chart.

You can specify a certain range using the [`setVisibleRange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#setvisiblerange) method.

```
widget.activeChart().setVisibleRange(  
    { from: 1420156800, to: 1451433600 }  
)
```

If the library cannot fit the specified range within the canvas, which may happen on small screens, it will render as much data as possible.
In this case, the `to` parameter is considered more prior than `from`.

To ensure the full range is displayed, consider decreasing the [bar spacing](/charting-library-docs/v29/getting_started/glossary#bar-spacing) to a smaller number, which allows more data to fit within the available space.
You can adjust bar spacing using the [`min_bar_spacing`](/charting-library-docs/v29/api/interfaces/Charting_Library.TimeScaleOptions#min_bar_spacing) option or the [`setBarSpacing`](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimeScaleApi#setbarspacing) method.

```
time_scale: {  
    min_bar_spacing: 0.01  
},
```

## Time scale API[​](#time-scale-api "Direct link to Time scale API")

You can manage the time scale using the Time scale API.
For example, you can set a specific right margin or detect when the chart has been zoomed in/out.
Refer to [`ITimeScaleApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimeScaleApi) for more information.

## Customize scale appearance[​](#customize-scale-appearance "Direct link to Customize scale appearance")

You can customize the appearance of the time scale using the [Overrides API](/charting-library-docs/v29/customization/overrides/).
For example, the code sample below changes the text color and font size of the time and [price](/charting-library-docs/v29/ui_elements/Price-Scale) scales.

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

## Date and time formatting[​](#date-and-time-formatting "Direct link to Date and time formatting")

You can adjust the display format of date and time values using the [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_formatters) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
Check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=1466s) on YouTube for an implementation example.

## Time frame toolbar[​](#time-frame-toolbar "Direct link to Time frame toolbar")

Time frames are time period buttons displayed at the bottom-left corner of the chart.
When users switch a time frame, it causes the following changes to satisfy the selected time frame:

1. The chart [resolution](/charting-library-docs/v29/core_concepts/Resolution) changes.
2. The bars scale horizontally to cover the entire requested date/time range.

For example, clicking `1Y` makes the chart switch the resolution to `1W` and
scale it accordingly to display weekly bars for the entire year.
Each time frame has its default chart resolution:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Time frame Chart resolution|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 5Y W|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1Y W|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 6M 120|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 3M 60|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 1M 30|  |  |  |  | | --- | --- | --- | --- | | 5D 5|  |  | | --- | --- | | 1D 1 | | | | | | | | | | | | | | | |

### Time frame customization[​](#time-frame-customization "Direct link to Time frame customization")

You can customize displayed time frames using the [`time_frames`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#time_frames) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
Note that time frames that require resolutions that are unavailable for a particular symbol will be hidden.
You can also check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=2328s) on YouTube for an implementation example.

### Programmatic time frame setting[​](#programmatic-time-frame-setting "Direct link to Programmatic time frame setting")

If you want to programmatically set the time frame for the active chart, use the [`setTimeFrame`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#settimeframe) method of the [`IChartWidgetApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi).
For example, the following code snippet applies the `1Y` time frame, which is the same as when users click `1Y` at the bottom of the chart:

```
const widget = new TradingView.widget(/* Widget properties */);  
  
widget.onChartReady(() => {  
    const chart = widget.chart();  
    chart.setTimeFrame({val: {type: 'period-back', value: '12M'}, res: '1W'});  
});
```

## Extended time scale[​](#extended-time-scale "Direct link to Extended time scale")

You can enable indicators to extend the time scale.
This allows you to create custom indicators that show bars at a higher resolution than the main series.
Refer to [Extending the time scale](/charting-library-docs/v29/custom_studies/Studies-Extending-The-Time-Scale) for more information.

## Extended sessions[​](#extended-sessions "Direct link to Extended sessions")

If you want to display extended sessions for some symbols, refer to the [Extended sessions](/charting-library-docs/v29/connecting_data/Extended-Sessions) article for more information.