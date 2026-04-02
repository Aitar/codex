# Saving and loading charts: Save user settings

Source: https://www.tradingview.com/charting-library-docs/v29/saving_loading/user-settings

* [Saving and loading charts](/charting-library-docs/v29/saving_loading/)* Save user settings

On this page

# Save user settings

## Overview[​](#overview "Direct link to Overview")

User settings are settings that remain regardless of the applied [chart layout](/charting-library-docs/v29/saving_loading/#chart-layouts).
They are stored separately from chart layouts to ensure that users have control over their specific preferences.
For example, the *Instant orders placement* setting in [Trading Platform](/charting-library-docs/v29/trading_terminal/) allows users to place orders without confirmation.
This setting is a part of user settings and is not saved when users save the chart layouts.
Saving this setting within a chart layout could lead to unexpected user experiences and is considered a bad practice.

### Settings list[​](#settings-list "Direct link to Settings list")

User settings include:

* [Resolution](/charting-library-docs/v29/core_concepts/Resolution)
* Order type and quantity in the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket)
* *Chart settings → Trading*
  + *Buy/Sell buttons*
  + *Instant orders placement*
  + *Play sound for executions*
  + *Notifications*
* *Summary row* in the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/)
* Right and bottom widget bars view
* Chart style
* [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List)

### How to store[​](#how-to-store "Direct link to How to store")

There are two options for storing user settings:

* Using the browser's [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), which is enabled by default.
  To disable this option, include the [`use_localstorage_for_settings`](/charting-library-docs/v29/customization/Featuresets#use_localstorage_for_settings) featureset in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.
* Implementing your preferred storage method, including the server-side one.
  For this, use the [`settings_adapter`](#settings-adapter) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

## Settings adapter[​](#settings-adapter "Direct link to Settings adapter")

You can save user settings using the [`settings_adapter`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#settings_adapter) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
This property allows not only storing settings in the preferred storage but also applying them to the chart.

info

The library provides multiple approaches to modify the chart's appearance and behavior, and `settings_adapter` is one of them.
These approaches have a specific application order, meaning they may override any styles or settings applied by other approaches lower on the list.
Refer to [Customization precedence](/charting-library-docs/v29/customization/customization-precedence) for more information.

The `settings_adapter` property accepts the [`ISettingsAdapter`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISettingsAdapter) object.
In the [`initialSettings`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISettingsAdapter#initialsettings) property of `ISettingsAdapter`, specify the settings the chart should be initiated with.
You should also implement two methods [`setValue`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISettingsAdapter#setvalue) and [`removeValue`](/charting-library-docs/v29/api/interfaces/Charting_Library.ISettingsAdapter#removevalue), which are triggered upon changes in settings.

Consider the code sample below that does the following:

* Sets a watermark on the chart when the chart is initialized.
* Sets settings (10 units of shares and the *limit* order type) for the Order Ticket when the chart is initialized.
* Logs actions in the console when settings are set or removed.

```
new TradingView.widget({  
    /* Other properties */  
  
    settings_adapter: {  
        initialSettings: {  
            "symbolWatermark": '{ "visibility": "true", "color": "rgba(244, 67, 54, 0.25)" }',  
            "trading.Broker": '{"qty": {"AAPL": 10, "NasdaqNM:AAPL": 10}, "orderType": {"NasdaqNM:AAPL": 3}}',  
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