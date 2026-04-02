# Customization: Overview

Source: https://www.tradingview.com/charting-library-docs/v29/customization/

* Customization

On this page

# Customization overview

The library supports extensive customization through a set of APIs, each designed for specific tasks. For example, [Featuresets](/charting-library-docs/v29/customization/Featuresets) should be used to control the visibility of chart elements, and the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to configure the chart size and default symbol.

For color adjustments, either [Overrides](/charting-library-docs/v29/customization/overrides/) or [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes) may be used. The image below illustrates specific areas of the chart and indicates the appropriate API to use for their customization.

![Customization map](/charting-library-docs/v29/assets/images/customization-map-d5f242c8fa8c7737f7de6f559c80d4ee.png)

## Customization APIs[​](#customization-apis "Direct link to Customization APIs")

caution

Note that some settings, such as the chart background color, can be adjusted with different API approaches. These approaches may override each other depending on their priority. Refer to the [Customization precedence](/charting-library-docs/v29/customization/customization-precedence) article for more information.

[## Overrides

Customize elements on the chart like panes, scales, series, indicators, and drawings](/charting-library-docs/v29/customization/overrides/)

[## Custom themes API

Override the default light and dark themes with a custom color palette](/charting-library-docs/v29/customization/styles/custom-themes/)

[## Featuresets

Show/hide UI elements and modify chart interaction behavior](/charting-library-docs/v29/customization/Featuresets)

[## Widget Constructor

Customize the chart size, default symbol and resolution, font family, and other parameters](/charting-library-docs/v29/core_concepts/Widget-Constructor/)

## Commonly customized items[​](#commonly-customized-items "Direct link to Commonly customized items")

[## Theme

Specify the default chart theme: light or dark](/charting-library-docs/v29/customization/)

[## UI elements

Adjust UI elements, such as drawings, indicators, and marks](/charting-library-docs/v29/ui_elements/)

[## Language

Set the chart language from more than 20 supported options](/charting-library-docs/v29/core_concepts/Localization)

[## Price format

Configure how prices are displayed: decimal or fractional format, number of decimal places, tick size, and other parameters](/charting-library-docs/v29/connecting_data/Symbology#price-format)

## TradingView logo[​](#tradingview-logo "Direct link to TradingView logo")

The visibility of the TradingView logo depends on the terms of your license agreement. Contact your TradingView account manager for more information.

## Limitations[​](#limitations "Direct link to Limitations")

* You cannot customize icons on the toolbars.
* The library does not support injecting custom UI components. If you want to add a UI component, implement it outside the library.