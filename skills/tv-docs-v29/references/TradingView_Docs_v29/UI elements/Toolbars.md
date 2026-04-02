# UI elements: Toolbars

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Toolbars

* [UI elements](/charting-library-docs/v29/ui_elements/)* Toolbars

On this page

# Toolbars

## Overview[​](#overview "Direct link to Overview")

The term **toolbars** relates to several [UI elements](/charting-library-docs/v29/ui_elements/).

* [Top toolbar](/charting-library-docs/v29/ui_elements/#top-toolbar) is a primary bar at the top of the chart that contains elements such as Symbol Search, Indicators, and Resolutions.
* [Drawing toolbar](/charting-library-docs/v29/ui_elements/drawings/) is a left-side bar that contains drawings.
* [Widget bar](/charting-library-docs/v29/ui_elements/#widget-bar) is a right-side bar available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) only. This toolbar displays the Watchlist, Details, and News widgets.
* [Time frame toolbar](/charting-library-docs/v29/ui_elements/Time-Scale#time-frame-toolbar) is a bottom bar that displays time period buttons.

info

For detailed information on customizing specific toolbar elements, refer to dedicated sections of the [UI elements](/charting-library-docs/v29/ui_elements/) and [Featuresets](/charting-library-docs/v29/customization/Featuresets) articles.

## Custom buttons in top toolbar[​](#custom-buttons-in-top-toolbar "Direct link to Custom buttons in top toolbar")

You can add your own buttons to the top toolbar using the following methods:

* [`createButton`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#createbutton) — creates a customizable button.
  This method provides maximum flexibility since it returns an HTML element (if `useTradingViewStyle` is `false`), which you can customize in any way you want.
  For example, you can create a checkbox or a dropdown menu.
* [`createDropdown`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#createdropdown) — creates a dropdown menu.
  Use this method for a simpler dropdown menu when you don't require custom HTML.

Note that other toolbars do not currently support custom button placement using these methods.

tip

Check out the [How to add custom button to top toolbar](/charting-library-docs/v29/tutorials/add-custom-button-to-top-toolbar) guide for a hands-on understanding.

### Accessible buttons[​](#accessible-buttons "Direct link to Accessible buttons")

Custom buttons, created using the [`createButton`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#createbutton) overload with `useTradingViewStyle` set to `true`, support [accessible keyboard navigation](/charting-library-docs/v29/getting_started/accessibility#keyboard-navigation).

## Change toolbar style[​](#change-toolbar-style "Direct link to Change toolbar style")

The library offers two ways to change the toolbar style:

* [Using custom themes API](/charting-library-docs/v29/customization/styles/custom-themes)
* [Using CSS color themes](/charting-library-docs/v29/customization/styles/CSS-Color-Themes)