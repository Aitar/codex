# UI elements: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/

* UI elements

On this page

# UI elements

The library offers a feature-rich interface, providing the opportunity to tweak and customize it to fit specific needs.
This article serves as a guide to understanding the various parts of the interface.
Further articles within this section provide detailed explanations for each UI element.

The interface can be divided into the following main parts.

![User interface](/charting-library-docs/v29/assets/images/user-interface-a5b2a6d4be777ffa1fb4a2942e890b74.png)

## Top toolbar[​](#top-toolbar "Direct link to Top toolbar")

[## Symbol Search

Customize the button that allows searching for and displaying financial instruments by entering instrument names](/charting-library-docs/v29/ui_elements/Symbol-Search)

[## Resolution

Manage the timeframe resolutions that define the duration of each bar](/charting-library-docs/v29/core_concepts/Resolution)

[## Chart styles

Adjust properties for various chart styles to enhance the appearance of your main series](/charting-library-docs/v29/customization/overrides/chart-overrides#chart-styles)

[## Indicators

Customize built-in indicators and create your own using JavaScript](/charting-library-docs/v29/ui_elements/indicators/)

[## Save layouts and templates

Allow users to save and restore chart layouts and chart, drawing, and indicator templates for future use](/charting-library-docs/v29/saving_loading/)

[## Snapshots

Configure the settings for taking snapshots and managing their storage](/charting-library-docs/v29/ui_elements/Snapshots)

[## Custom buttons

Add custom buttons or drop-down menus to the top toolbar for quick access to specific functions](/charting-library-docs/v29/ui_elements/Toolbars#custom-buttons-in-top-toolbar)

[## Multiple-chart layout

Allow users to display up to 8 charts on one layout (Trading Platform only)](/charting-library-docs/v29/trading_terminal/#multiple-chart-layout)

## Chart[​](#chart "Direct link to Chart")

The main area on the chart where a [series](/charting-library-docs/v29/getting_started/glossary#series) or [indicator](/charting-library-docs/v29/ui_elements/indicators/) is displayed is called **pane**.
The picture below shows the red pane with a main series and the green pane with an indicator.

![Chart panes](/charting-library-docs/v29/assets/images/pane-d44d70e4c4be2d846c4ecdd789fc0e17.png)

The chart contains the following elements:

[## Chart

Customize colors and learn how to use the Chart API to subscribe to events, manage drawings, and more](/charting-library-docs/v29/ui_elements/Chart)

[## Price scale

Customize the price scale appearance and manage it through the API](/charting-library-docs/v29/ui_elements/Price-Scale)

[## Time scale

Customize the time scale appearance and manage it through the API](/charting-library-docs/v29/ui_elements/Time-Scale)

[## Legend

Customize the legend appearance: include symbol logos, set titles, and format prices according to your preferences](/charting-library-docs/v29/ui_elements/Legend)

[## Marks

Display additional information such as news, bar patterns, splits, and dividends on the chart or time scale](/charting-library-docs/v29/ui_elements/Marks)

[## Market status

Provide users with updates on whether the market is open or closed for trading](/charting-library-docs/v29/ui_elements/market-status)

[## Context menu

Customize the dialog accessed through a right-click or ellipsis menu](/charting-library-docs/v29/ui_elements/context-menu)

[## Time zones

Configure time zones to suit your application’s needs](/charting-library-docs/v29/ui_elements/timezones)

## Drawing toolbar[​](#drawing-toolbar "Direct link to Drawing toolbar")

Drawings are the tools that can help you analyze the charts and make clear annotations to them.
For more information, refer to [Drawings](/charting-library-docs/v29/ui_elements/drawings/).

## Widget bar[​](#widget-bar "Direct link to Widget bar")

The widget bar is a right side toolbar available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only.
You cannot change the widget bar location but you can hide it using the [`hide_right_toolbar`](/charting-library-docs/v29/customization/Featuresets#hide_right_toolbar) and [`hide_right_toolbar_tabs`](/charting-library-docs/v29/customization/Featuresets#hide_right_toolbar_tabs) featuresets.

The bar displays the following widgets:

[## Object Tree

Allow users to manage drawings, indicators, and symbols on the chart](/charting-library-docs/v29/ui_elements/object-tree/)

[## Watchlist

Allow users to track real-time price movements and volume of selected financial instruments](/charting-library-docs/v29/trading_terminal/Watch-List)

[## Details

Display detailed information for a specific symbol, including bid/ask prices, trading hours, and daily price ranges](/charting-library-docs/v29/trading_terminal/#details)

[## News

Display latest news related to specific symbols](/charting-library-docs/v29/trading_terminal/news/)

## Account Manager[​](#account-manager "Direct link to Account Manager")

The Account Manager is a widget available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only.
The widget displays the user's trading information, such as orders, positions, and account balance.
Users can manage their orders and positions from the Account Manager.
For more information, refer to [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/).