# Saving and loading charts: Low-level API

Source: https://www.tradingview.com/charting-library-docs/v29/saving_loading/low-level-api

* [Saving and loading charts](/charting-library-docs/v29/saving_loading/)* Low-level API

On this page

# Low-level API for saving and loading

## Overview[​](#overview "Direct link to Overview")

The low-level API is recommended when you want to use save/load UI elements that are not part of the TradingView UI.
With the low-level API, you can save and load [chart layouts](/charting-library-docs/v29/saving_loading/#chart-layouts) and [indicator templates](/charting-library-docs/v29/saving_loading/#indicator-templates).
Note that the low-level API methods are meant to be called directly by your JavaScript code.

info

This approach does not support saving [chart templates](/charting-library-docs/v29/saving_loading/#chart-templates).
Consider implementing the [API handlers](/charting-library-docs/v29/saving_loading/save-load-adapter) instead.

## How to implement[​](#how-to-implement "Direct link to How to implement")

To access the chart layout content directly, use the [`save`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#save) and [`load`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#load) methods.
These methods are defined in the [`IChartingLibraryWidget`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget) interface and allow controlling the `widget` object.

```
// Function to store the chart layout  
function storeChartLayout(layout) {  
    // Implement your logic here  
};  
  
const widget = new TradingView.widget(/* Widget properties */);  
widget.save((layout) => { storeChartLayout(layout) }); // Save the layout using the save() method  
  
widget.load(storedLayout); // Later in your code, you can load the stored layout
```

To access the indicator templates, use the [`createStudyTemplate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudytemplate) and [`applyStudyTemplate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#applystudytemplate) methods.
Note that you can access these methods through the [`chart`](/charting-library-docs/v29/core_concepts/widget-methods#chart) or [`activeChart`](/charting-library-docs/v29/core_concepts/widget-methods#activechart) widget methods.

```
widget.onChartReady(() => {  
    const options = { saveSymbol: true, saveInterval: true };  
    const template = widget.activeChart().createStudyTemplate(options);  
  
    widget.activeChart().applyStudyTemplate(template);  
});
```

The content is saved as a JSON object which you can save where you wish.
For example, you can embed it in your saved pages or in the user's working area.

## Hide save/load layout buttons[​](#hide-saveload-layout-buttons "Direct link to Hide save/load layout buttons")

You can disable the [`header_saveload`](/charting-library-docs/v29/customization/Featuresets#header_saveload) featureset to hide the built-in *Save layout* and *Load layout* buttons from the header toolbar.