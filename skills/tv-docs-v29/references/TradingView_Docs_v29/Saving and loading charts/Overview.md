# Saving and loading charts: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/saving_loading/

* Saving and loading charts

On this page

# Saving and loading charts

## Overview[​](#overview "Direct link to Overview")

The library allows users to save their [chart layouts](#chart-layouts), [chart templates](#chart-templates),
[drawing templates](#drawing-templates), [indicator templates](#indicator-templates), and restore them when users get back.

### Chart layouts[​](#chart-layouts "Direct link to Chart layouts")

A **chart layout** is a single chart in Advanced Charts or a group of charts in [Trading Platform](/charting-library-docs/v29/trading_terminal/).
The chart layout includes [drawings](/charting-library-docs/v29/ui_elements/drawings/), [indicators](/charting-library-docs/v29/ui_elements/indicators/), and various chart settings, such as colors and styles.
Note that the visible time range is not included in the chart layout.
The library is designed to always display the most recent data to users.

Users can save and load the layouts using the built-in *Save layout* and *Load layout* buttons on the header toolbar.

* Save layout* Load layout

![Saving chart layout](/charting-library-docs/v29/assets/images/save-chart-layout-5762cf56358fbb889ffda65d98553cc8.gif)

![Loading previously stored chart layout](/charting-library-docs/v29/assets/images/load-chart-layout-6016869e6b87f148c1e98bbba5d4ef64.gif)

To hide these buttons, include the [`header_saveload`](/charting-library-docs/v29/customization/Featuresets#header_saveload) featureset in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

### Chart templates[​](#chart-templates "Direct link to Chart templates")

info

Available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only.

A **chart template** is a set of colors used for the main series.
For example, this can include candle up/down colors, wick colors, line colors, background colors, and more.

To enable saving chart templates, include the [`chart_template_storage`](/charting-library-docs/v29/customization/Featuresets#chart_template_storage) featureset in the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.
Users can save and apply the chart templates in the *Chart settings → Template* drop-down menu.

![Chart settings menu](/charting-library-docs/v29/assets/images/chart-settings-f77388ae76d1705a23b3c393d097a924.png)

### Indicator templates[​](#indicator-templates "Direct link to Indicator templates")

An **indicator template** is a set of applied [indicators](/charting-library-docs/v29/ui_elements/indicators/) and their settings, such as inputs and styles.

info

By design, all settings are saved except for **precision**.
For most indicators, the optimal precision depends on the symbol's precision and is inherited from it.
Therefore, it does not make sense to save a setting that may not be relevant, depending on the symbol it is used on.

Users can save and apply the indicator templates through the *Indicator Templates* button on the top toolbar.
To display this button in the UI, include the [`study_templates`](/charting-library-docs/v29/customization/Featuresets#study_templates) featureset in the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.

![Indicator templates](/charting-library-docs/v29/assets/images/indicator-templates-34f1c4aa7bb344d2ddca0e1b3929eeaa.png)

### Drawing templates[​](#drawing-templates "Direct link to Drawing templates")

info

Available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only.

A **drawing template** is a set of properties of a particular [drawing](/charting-library-docs/v29/ui_elements/drawings/).
This can include the drawing's line style, text alignment, and more.

Users can save and apply the drawing templates through the *Templates* button on the floating drawing toolbar.

![Drawing templates](/charting-library-docs/v29/assets/images/drawing-templates-15d00c8899bb3c378b45a2087b2b7b92.png)

To disable this feature, include the [`drawing_templates`](/charting-library-docs/v29/customization/Featuresets#drawing_templates) featureset in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

### Implementation[​](#implementation "Direct link to Implementation")

To store users' content, you should implement a storage.
If you want users to have only one chart layout, you can consider using [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage).
However, due to the `localStorage` size limits, we recommend storing content on a server.

To simplify the storage development, the library provides three approaches.
The table below describes these approaches and what they allow you to store.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approach Description Chart layout Chart template Drawing template Indicator template|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [REST API](/charting-library-docs/v29/saving_loading/save-load-rest-api/) The predefined REST API is a set of methods that you need to implement. When users click the save or load buttons in the UI, these actions initiate the saving and loading processes. ✔️ ❌ ✔️ ✔️|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | [API Handlers](/charting-library-docs/v29/saving_loading/save-load-adapter) The API handlers allow implementing custom logic for save/load actions coming from UI. For example, when users click the save or load buttons, you can add authorization headers or manage specific errors within these processes. ✔️ ✔️ ✔️ ✔️|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | [Low-level API](/charting-library-docs/v29/saving_loading/low-level-api) The low-level API is recommended when you want to use save/load UI elements that are not part of the TradingView UI. The low-level API methods are meant to be called directly by your JavaScript code, giving you flexibility to implement custom save and load functionality. ✔️ ❌ ❌ ✔️ | | | | | | | | | | | | | | | | | | | | | | | |

## Save drawings separately[​](#save-drawings-separately "Direct link to Save drawings separately")

By default, drawings are saved within the [chart layout](#chart-layouts) through the built-in *Save layout* button.
However, the library provides an alternative method for saving charts in which drawings are stored separately from the chart layout.
This method is beneficial for optimizing load times and data storage on your server.
Additionally, it allows associating drawings with individual symbols.
This enables drawing reuse and flexibility across different layouts or charts.
Refer to the [Saving drawings separately](/charting-library-docs/v29/saving_loading/saving_drawings_separately) article for more information.

## User settings[​](#user-settings "Direct link to User settings")

User settings are settings that remain regardless of the applied [chart layout](#chart-layouts).
They are stored separately from chart layouts to ensure that users have control over their specific preferences.
Refer to [Save user settings](/charting-library-docs/v29/saving_loading/user-settings) for more information.

## Additional use cases[​](#additional-use-cases "Direct link to Additional use cases")

### Save charts automatically[​](#save-charts-automatically "Direct link to Save charts automatically")

You might want to automatically save chart layouts. Here are the steps to implement it:

1. Set a [threshold delay](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#auto_save_delay) in seconds that is used to reduce the number of the [`onAutoSaveNeeded`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#onautosaveneeded) calls.
2. [Subscribe](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#subscribe) to the `onAutoSaveNeeded` event.
3. Call the [`saveChartToServer`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#savecharttoserver) method.

### Restore last saved chart[​](#restore-last-saved-chart "Direct link to Restore last saved chart")

Usually, users open an empty chart and load their chart layouts using the *Load layout* dialog.
However, if you want to open the last saved chart layout on start, you can do the following:

* If you use the [low-level API](/charting-library-docs/v29/saving_loading/low-level-api), set the chart layout content to the [`saved_data`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#saved_data) field in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
* Otherwise, set the [`load_last_chart`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#load_last_chart) property to `true`.