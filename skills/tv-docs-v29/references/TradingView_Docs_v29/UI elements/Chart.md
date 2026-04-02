# UI elements: Chart

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Chart

* [UI elements](/charting-library-docs/v29/ui_elements/)* Chart

On this page

# Chart

This article contains general information on how to customize and control the chart. For more information about certain chart elements, refer to the rest of the articles in the **UI Elements** section.

## Default chart settings[​](#default-chart-settings "Direct link to Default chart settings")

You should use the Widget Constructor to set up default chart settings like symbol, [resolution](/charting-library-docs/v29/core_concepts/Resolution), [time zone](/charting-library-docs/v29/ui_elements/timezones), [locale](/charting-library-docs/v29/core_concepts/Localization), [size](/charting-library-docs/v29/core_concepts/Widget-Constructor#chart-size), and others. Refer to the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor#chart-configuration) article for more information.

## Customization[​](#customization "Direct link to Customization")

tip

Refer to the [Customization](/charting-library-docs/v29/customization/) section for detailed information on how to customize the chart and its elements.

### Change colors[​](#change-colors "Direct link to Change colors")

You can customize the colors of the chart to implement your corporate colors.
The articles listed below explain how to change colors in certain cases:

* [Chart Overrides](/charting-library-docs/v29/customization/overrides/chart-overrides): specify default color of UI elements on the chart like scales and panes.
* [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes): specify default color of UI elements outside the chart like dialogs and toolbars.

### Show/hide chart elements[​](#showhide-chart-elements "Direct link to Show/hide chart elements")

You can show/hide chart elements using [featuresets](/charting-library-docs/v29/customization/Featuresets).
If there is no featureset for an element you want to hide, you can do it by adding your custom [CSS file](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_css_url).

### Show/hide gaps on the chart[​](#showhide-gaps-on-the-chart "Direct link to Show/hide gaps on the chart")

By default, the library hides periods with no trading activity to keep the chart continuous. In certain cases, such as analyzing low-liquidity instruments, it might be useful to represent these periods with whitespace gaps on the chart.

To do this, use the [`intraday_inactivity_gaps`](/charting-library-docs/v29/customization/Featuresets#intraday_inactivity_gaps) featureset. Note that inactivity gaps are displayed **only on intraday resolutions** and **only within the trading session** of the instrument. For example, for a U.S. stock with a trading session from 09:00 to 16:00, inactivity outside of the session will not be displayed.

* Chart without gaps* Chart with gaps

![Chart without inactivity gaps](/charting-library-docs/v29/assets/images/chart-without-gaps-f9746fcb5f2ba0b013442ffe407e1f90.png)

![Chart with inactivity gaps](/charting-library-docs/v29/assets/images/chart-with-gaps-80d5f5fb3474871908522490ed37a7a2.png)

When [`intraday_inactivity_gaps`](/charting-library-docs/v29/customization/Featuresets#intraday_inactivity_gaps) is enabled, the corresponding checkbox appears in the *Chart settings* dialog, allowing users to toggle inactivity gaps on or off. The checkbox is disabled by default.

![Inactivity gaps toggle in Chart settings](/charting-library-docs/v29/assets/images/gaps-settings-1ac948387c58a1617702690d3801658a.png)

You can also use the [`intradayInactivityGaps`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#intradayinactivitygaps) method to control the gaps visibility through the API.

```
// Access the watched value for inactivity gaps visibility  
const inactivityGaps = widget.chart().intradayInactivityGaps();  
  
// Enable inactivity gaps display  
inactivityGaps.set(true);  
  
// Listen for changes  
inactivityGaps.subscribe((isVisible) => {  
  console.log('Inactivity gaps visibility changed by the user:', isVisible);  
});
```

## Chart methods[​](#chart-methods "Direct link to Chart methods")

You can use the Chart API to interact with the chart after it is initialized. For example, you can subscribe to chart events, manage drawings and indicators, get information about a current configuration, perform Z-order operations, and more. All methods are listed in [IChartWidgetApi](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi).

### Subscribe to events[​](#subscribe-to-events "Direct link to Subscribe to events")

You can subscribe to the chart events using methods like [`onDataLoaded`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#ondataloaded), [`onSymbolChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#onsymbolchanged), [`onChartTypeChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#oncharttypechanged), and others.
For example, the code sample below specifies a time frame when an interval is changed using the [`onIntervalChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#onintervalchanged) method.

```
widget.activeChart().onIntervalChanged().subscribe(null, (interval, timeframeObj) =>  
    timeframeObj.timeframe = {  
        value: '12M',  
        type: 'period-back'  
});
```

### Manage chart[​](#manage-chart "Direct link to Manage chart")

You can manage chart settings using methods like [`setSymbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#setsymbol), [`setResolution`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#setresolution), [`resetData`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resetdata), [`clearMarks`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#clearmarks), and others.
For example, the code sample below specifies a new [range](/charting-library-docs/v29/getting_started/glossary#date-range) using the [`setVisibleRange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#setvisiblerange) method.

```
widget.activeChart().setVisibleRange(  
    { from: Date.UTC(2023, 6, 12, 13, 30) / 1000 },  
    { applyDefaultRightMargin: true }  
)
```

### Execute action by ID[​](#execute-action-by-id "Direct link to Execute action by ID")

The [`executeActionById`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#executeactionbyid) method allows you to trigger specific actions programmatically through the API.
This is useful for customizing UI or replicating built-in functionality with custom components.
For example, you can replace built-in [top toolbar](/charting-library-docs/v29/ui_elements/#top-toolbar) buttons with custom ones or trigger actions for hidden UI elements.

```
widget.activeChart().executeActionById("chartReset");
```

Click to reveal the list of the `ChartActionId` types.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action ID Purpose|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `"chartProperties"` Opens the *Chart settings* dialog.| `"compareOrAdd"` Opens or hides the [*Compare symbol*](/charting-library-docs/v29/ui_elements/indicators/#add-and-compare-new-series) dialog.| `"scalesProperties"` Opens or hides the *Chart settings* dialog.| `"paneObjectTree"` Opens the Object tree on the [widget bar](/charting-library-docs/v29/ui_elements/#widget-bar).| `"insertIndicator"` Opens or hides a dialog for adding [indicators](/charting-library-docs/v29/ui_elements/indicators/).| `"symbolSearch"` Opens the [*Symbol Search*](/charting-library-docs/v29/ui_elements/Symbol-Search) dialog.| `"changeInterval"` Opens a dialog for changing [resolution](/charting-library-docs/v29/core_concepts/Resolution).| `"timeScaleReset"` Resets the [time scale](/charting-library-docs/v29/ui_elements/Time-Scale) to its default state.| `"chartReset"` Resets the [chart](/charting-library-docs/v29/ui_elements/Chart) view to its default state.| `"seriesHide"` Hides the selected series on the chart.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `"studyHide"` Hides the selected [indicator](/charting-library-docs/v29/ui_elements/indicators/) on the chart.| `"lineToggleLock"` Enables or disables the *Lock/Unlock* button in the floating toolbar of the selected [drawing](/charting-library-docs/v29/ui_elements/drawings/).| `"lineHide"` Hides the selected [drawing](/charting-library-docs/v29/ui_elements/drawings/) on the chart.| `"scaleSeriesOnly"` Enables or disables the *Scale price chart only* option for the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"drawingToolbarAction"` Opens or hides the [drawing toolbar](/charting-library-docs/v29/ui_elements/#drawing-toolbar).| `"stayInDrawingModeAction"` Enables or disables the *Stay in drawing* mode.| `"hideAllMarks"` Shows or hides all [marks](/charting-library-docs/v29/ui_elements/Marks) on the chart.| `"showCountdown"` Enables or disables *Countdown to bar close* option for the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"showSeriesLastValue"` Shows or hides the series's last value on the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"showSymbolLabelsAction"` Shows or hides the symbol's label on the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"showStudyLastValue"` Shows or hides the indicator's last value on the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"showStudyPlotNamesAction"` Shows or hides the indicator's label on the [price scale](/charting-library-docs/v29/ui_elements/Price-Scale).| `"undo"` Undoes the last applied action.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | `"redo"` Redoes the last undone action.|  |  |  |  | | --- | --- | --- | --- | | `"paneRemoveAllStudiesDrawingTools"` Removes all [indicators](/charting-library-docs/v29/ui_elements/indicators/) and [drawings](/charting-library-docs/v29/ui_elements/drawings/) from the chart.| `"showSymbolInfoDialog"` Opens the *Security info* dialog. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

### Manage drawings and indicators[​](#manage-drawings-and-indicators "Direct link to Manage drawings and indicators")

You can create and manage drawings/indicators using methods like [`createStudy`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudy), [`getAllShapes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#getallshapes), [`getShapeById`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#getshapebyid), [`removeAllStudies`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#removeallstudies), and others.
For example, the code sample below adds the *Vertical line* drawing on the chart using the [`createShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createshape) method.

```
widget.activeChart().createShape(  
    { time: 1514764800 },  
    { shape: 'vertical_line' }  
);
```

### Getters[​](#getters "Direct link to Getters")

You can get information about the current chart settings using methods like [`symbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#symbol), [`chartType`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#charttype), [`getVisibleRange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#getvisiblerange), and others.
For example, the code sample below gets the current resolution using the [`resolution`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resolution) method.

```
console.log(widget.activeChart().resolution());
```

You can also use chart methods to get objects that provide API to perform certain operations. For example:

* [`getSeries`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#getseries) returns [`ISeriesApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISeriesApi) that allows you to interact with a [series](/charting-library-docs/v29/getting_started/glossary#series).
* [`selection`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#selection) returns [`ISelectionApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISelectionApi) that allows you to select drawings and indicators.
* [`getTimezoneApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#gettimezoneapi) returns [`ITimezoneApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimezoneApi) that allows you to manage the chart's time zone.

### Trading primitives[​](#trading-primitives "Direct link to Trading primitives")

caution

Starting from version 29, the methods for creating trading primitives are only available in [Trading Platform].

You can create an order/position line and trade execution using the corresponding [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline), [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline), [`createExecutionShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createexecutionshape) methods.
Refer to [Trading Primitives](/charting-library-docs/v29/trading_terminal/Trading-Primitives) for more information.

For example, the code sample below adds a new order line on the chart using the [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline) method.

```
widget.activeChart().createOrderLine()  
    .setTooltip("Additional order information")  
    .setModifyTooltip("Modify order")  
    .setCancelTooltip("Cancel order")  
    .onMove(function() {  
        this.setText("onMove called");  
    })  
    .onModify("onModify called", function(text) {  
        this.setText(text);  
    })  
    .onCancel("onCancel called", function(text) {  
        this.setText(text);  
    })  
    .setText("STOP: 73.5 (5,64%)")  
    .setQuantity("2");
```