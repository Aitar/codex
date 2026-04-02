# UI elements: Watermarks

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/watermarks

* [UI elements](/charting-library-docs/v29/ui_elements/)* Watermarks

On this page

# Watermarks

## Overview[​](#overview "Direct link to Overview")

Watermarks provide a visual text overlay on the chart.
Users can manage the visibility and color of watermarks in the *Settings → Canvas → Watermark*.
A default watermark contains a symbol ticker, interval, and description.

TradingView recommends letting users enable the watermark themselves.
This ensures their preferences are always respected.
However, you can also programmatically manage watermarks in two ways:

* Using the [Watermark API](#watermark-api-recommended) for dynamic changes.
* Using the [settings adapter](#settings-adapter) to set the initial state.

## Watermark API (recommended)[​](#watermark-api-recommended "Direct link to Watermark API (recommended)")

The [Watermark API](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi) allows you to either customize the default watermark or implement a custom one.

To access the API, use the [`watermark`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#watermark) method of the `IChartingLibraryWidget` interface.

```
// Get an instance of IWatermarkApi  
widget.onChartReady(() => {  
    const watermarkApi = widget.watermark();  
});
```

### Color and visibility[​](#color-and-visibility "Direct link to Color and visibility")

To manage the watermark color, use the [`color`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi#color) method.

```
watermarkApi.color().setValue("rgba(0, 150, 0, 0.5)");
```

To control the visibility of the ticker, description, and interval of the watermark,
use the [`tickerVisibility`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi#tickervisibility), [`descriptionVisibility`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi#descriptionvisibility), and [`intervalVisibility`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi#intervalvisibility) methods.

```
watermarkApi.descriptionVisibility().setValue(false);
```

### Custom content[​](#custom-content "Direct link to Custom content")

To replace the default watermark with your own custom content, use the [`setContentProvider`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi#setcontentprovider) method.
The provider function receives a `WatermarkContentData` object and should return an array of `WatermarkLine` objects.
Each `WatermarkLine` defines a line of text with the following properties:

* Text to be displayed
* Font size
* Line height
* Vertical offset distance

See the Pen [Add custom watermark](https://codepen.io/tradingview/pen/OPyPJMB) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

## Settings adapter[​](#settings-adapter "Direct link to Settings adapter")

If you only need to control the initial visibility and color of the default watermark, you can use the [settings adapter](/charting-library-docs/v29/saving_loading/user-settings#settings-adapter) in your [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
This method doesn't support custom text.
It only applies to the default built-in watermark.

To make the watermark visible, set the `symbolWatermark` property within the `initialSettings` of your [`settings_adapter`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#settings_adapter).
Note that defining `setValue` and `removeValue` functions is required.

```
new TradingView.widget({  
    /* Other Widget Constructor properties */  
  
    settings_adapter: {  
        initialSettings: {  
            "symbolWatermark": '{ "visibility": "true", "color": "rgba(244, 67, 54, 0.25)" }',  
        },  
        setValue: function (key, value) {  
            console.log(`set value: ${key} ${value}`);  
        },  
        removeValue: function (key) {  
            console.log(`remove value: ${key}`);  
        },  
    }  
})
```