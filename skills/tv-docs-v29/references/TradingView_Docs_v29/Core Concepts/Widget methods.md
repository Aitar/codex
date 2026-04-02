# Core Concepts: Widget methods

Source: https://www.tradingview.com/charting-library-docs/v29/core_concepts/widget-methods

* Core Concepts* Widget methods

On this page

# Widget methods

## Overview[​](#overview "Direct link to Overview")

After you create a widget with [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor), you can control the `widget` object using the methods defined in the `IChartingLibraryWidget` interface. This article describes the most commonly used methods. Refer to the [`IChartingLibraryWidget`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget) page to see the full list of methods.

## Advanced Charts methods[​](#advanced-charts-methods "Direct link to Advanced Charts methods")

### onChartReady[​](#onchartready "Direct link to onChartReady")

The [`onChartReady`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#onchartready) method calls a callback when all data is loaded and the widget is ready. Therefore, you should call other widget methods only after the `onChartReady` callback.

```
const widget = new TradingView.widget(/* Widget properties */);  
  
widget.onChartReady(function() {  
    widget.getChartLanguage();  
});
```

### chart[​](#chart "Direct link to chart")

The [`chart`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#chart) method returns an instance of the [`IChartWidgetApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi) interface that provides an extensive API for controlling the specific chart.
For example, you can handle chart events, create indicators and drawings, change chart properties on the fly, and more. Consider the code sample below that adds the Bollinger Bands [indicator](/charting-library-docs/v29/ui_elements/indicators/) at the launch.

```
widget.onChartReady(() => {  
    const chart = widget.chart();  
    chart.createStudy(  
      "Bollinger Bands", // Indicator's name  
      true,              // forceOverlay  
      false,             // lock  
      {  
        in_0: 25,        // length  
        in_1: 1,         // 'mult' indicator setting  
      }  
    );  
});
```

The `chart` method has an optional `index` parameter. If you want to interact with a certain chart on the multiple-chart layout, you should call the `chart` method with the corresponding index as a parameter.

### activeChart[​](#activechart "Direct link to activeChart")

The [`activeChart`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#activechart) method retrieves [`IChartWidgetApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi) to interact with the currently selected chart. For example, the code sample below draws a vertical line on the chart.

```
widget.activeChart().createMultipointShape(  
  [{ price: 168, time: Date.UTC(2017, 10, 13) / 1000 }],  
  { shape: 'vertical_line'}  
);
```

You can also subscribe to events on the active chart, such as [`onIntervalChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#onintervalchanged).

```
widget.activeChart().onIntervalChanged().subscribe(null, (interval, timeframeObj) =>  
    timeframeObj.timeframe = {  
        value: "12M",  
        type: "period-back"  
});
```

Note that the library does not manage the event subscriptions when users switch between the charts on the [multiple-chart layout](/charting-library-docs/v29/trading_terminal/#multiple-chart-layout).
If necessary, you should manually unsubscribe from the previous chart and subscribe to the newly selected one using the corresponding [methods](/charting-library-docs/v29/api/interfaces/Charting_Library.ISubscription). To track the currently active chart, use the [`activeChartChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#activechartchanged) event.

You can also find out the active chart's index using the [`activeChartIndex`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#activechartindex) method and subscribe to this chart using the [`chart`](#chart) method.

```
const index = widget.activeChartIndex();  
const chart = widget.chart(index);
```

### subscribe / unsubscribe[​](#subscribe--unsubscribe "Direct link to subscribe / unsubscribe")

The [`subscribe`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#subscribe) method allows you to subscribe to the widget's [events](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap) and handle them. For example, the code sample below handles an event when an indicator is added to the chart and prints the indicator's name to the console.

```
widget.subscribe('study', (event) => { console.log(`A ${event.value} indicator was added`) });
```

You should use the [`unsubscribe`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#unsubscribe) method to unsubscribe from events.

### applyOverrides[​](#applyoverrides "Direct link to applyOverrides")

The [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method allows you to change [Overrides](/charting-library-docs/v29/customization/overrides/) on the fly. The code sample below hides the main [series](/charting-library-docs/v29/getting_started/glossary#series).

```
widget.applyOverrides({ "mainSeriesProperties.visible": false });
```

### applyStudiesOverrides[​](#applystudiesoverrides "Direct link to applyStudiesOverrides")

The [`applyStudiesOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applystudiesoverrides) method allows you to change [Overrides](/charting-library-docs/v29/customization/overrides/indicator-overrides) that affect [indicators](/charting-library-docs/v29/ui_elements/indicators/) (studies) on the fly. The code sample below changes the color of the Bollinger Bands indicator.

```
widget.applyStudiesOverrides({  
    'bollinger bands.median.color': '#33FF88'  
});
```

Note that this method only changes the indicator's properties before the indicator is created. You should use the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IStudyApi#applyoverrides) method in [`IStudyApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IStudyApi) to change an indicator that is already on the chart.

### setSymbol[​](#setsymbol "Direct link to setSymbol")

The [`setSymbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#setsymbol) method sets a symbol and resolution of the active chart.

```
widget.setSymbol('IBM', '1D', () => {  
  // Your callback function  
});
```

Note that a callback is evoked when the data for the new symbol is loaded.

### changeTheme[​](#changetheme "Direct link to changeTheme")

The [`changeTheme`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#changetheme) method allows you to change the [theme](/charting-library-docs/v29/customization/theme) on the fly. This method returns a promise that is resolved once the theme is applied. You can apply other style modifications after the promise is fulfilled.

```
widget.changeTheme('Dark').then(() => {  
    widget.chart().applyOverrides({ 'paneProperties.backgroundGradientStartColor': 'red' });  
});
```

### onShortcut[​](#onshortcut "Direct link to onShortcut")

The [`onShortcut`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#onshortcut) method allows you to override the built‑in [shortcuts](/charting-library-docs/v29/getting_started/Shortcuts) or specify custom ones. For example, the code sample below specifies a shortcut that opens [*Symbol Search*](/charting-library-docs/v29/ui_elements/Symbol-Search).

```
widget.onShortcut("alt+q", function() {  
    widget.chart().executeActionById("symbolSearch");  
});
```

Refer to the [Manage shortcuts](/charting-library-docs/v29/getting_started/Shortcuts#manage-shortcuts) section for more examples.

### takeClientScreenshot[​](#takeclientscreenshot "Direct link to takeClientScreenshot")

The [`takeClientScreenshot`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#takeclientscreenshot) method creates a snapshot of the chart and returns it as a canvas. You can then take the canvas element and create an image from it. The code sample below saves a screenshot as PNG.

```
async function saveChartToPNG() {  
  const screenshotCanvas = await widget.takeClientScreenshot();  
  const linkElement = document.createElement('a');  
  linkElement.download = 'screenshot';  
  linkElement.href = screenshotCanvas.toDataURL(); // Alternatively, use `toBlob` which is a better API  
  linkElement.dataset.downloadurl = ['image/png', linkElement.download, linkElement.href].join(':');  
  document.body.appendChild(linkElement);  
  linkElement.click();  
  document.body.removeChild(linkElement);  
}  
saveChartToPNG(); // Call the screenshot function
```

### customThemes[​](#customthemes "Direct link to customThemes")

The [`customThemes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#customthemes) method retrieves [`ICustomThemesApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ICustomThemesApi) that allows you to manage [custom themes](/charting-library-docs/v29/customization/styles/custom-themes). For example, you can reset the applied themes to the default values.

```
let customThemesAPI = (await widget.customThemes());  
customThemesAPI.resetCustomThemes();
```

### closePopupsAndDialogs[​](#closepopupsanddialogs "Direct link to closePopupsAndDialogs")

The [`closePopupsAndDialogs`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#closepopupsanddialogs) method closes any active dialog or [context menu](/charting-library-docs/v29/ui_elements/context-menu) on the chart.

```
widget.closePopupsAndDialogs();
```

## Trading Platform methods[​](#trading-platform-methods "Direct link to Trading Platform methods")

The methods below are available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only.

### widgetbar[​](#widgetbar "Direct link to widgetbar")

The [`widgetbar`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#widgetbar) method retrieves [`IWidgetbarApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWidgetbarApi) that allows you to interact with the widget bar.

```
widget.onChartReady(() => {  
    widget.widgetbar().then(widgetbarApi => {  
       widgetbarApi.isPageVisible('data_window');  
    });  
});
```

### watchList[​](#watchlist "Direct link to watchList")

The [`watchList`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#watchlist) method retrieves [`IWatchListApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi) that allows you to interact with the [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List) widget.

```
const watchlistApi = await widget.watchList();  
const activeListId = watchlistApi.getActiveListId();  
const currentListItems = watchlistApi.getList(activeListId);  
// Adds a new section and item to the current Watchlist  
watchlistApi.updateList(activeListId, [...currentListItems, '###NEW SECTION', 'AMZN']);
```

### news[​](#news "Direct link to news")

The [`news`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#news) method retrieves [`INewsApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.INewsApi) that allows you to interact with the [News](/charting-library-docs/v29/trading_terminal/news) widget.

```
widget.onChartReady(() => {  
    widget.news().then(newsApi => {  
        // newsApi is ready to use  
    });  
});
```

### chartsCount[​](#chartscount "Direct link to chartsCount")

The [`chartsCount`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#chartscount) method counts a number of charts on the multiple-chart layout. In the code sample below, this method is used to interact with all the charts on the layout one by one.

```
for (let i = 0; i < widget.chartsCount(); i++) { console.log(widget.chart(i).symbolExt().name) }
```