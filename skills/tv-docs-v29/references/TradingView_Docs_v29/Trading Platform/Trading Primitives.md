# Trading Platform: Trading Primitives

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/Trading-Primitives

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Trading Primitives

On this page

# Trading Primitives

Trading Primitives is a low-level mechanism that is designed to give you the most detailed control over trading primitives behavior.

## Generic data[​](#generic-data "Direct link to Generic data")

### Properties[​](#properties "Direct link to Properties")

You can use special value `inherit` for some properties of the Trading Primitives. This will make the Library use its default value for this property.

You can enable the `trading_options` feature to show Trading GUI controls in the chart properties window.

You can’t control the visibility of a specific object. Properties of positions, orders and executions can be changed in the Trading tab of the Chart Properties window.

### Override properties[​](#override-properties "Direct link to Override properties")

You can override the style of the order and position lines.
For more information refer to [Customize trading primitives](/charting-library-docs/v29/customization/overrides/trading-overrides#created-with-trading-primitives).

### Colors and Fonts[​](#colors-and-fonts "Direct link to Colors and Fonts")

You can use following string formats for setting the colors:

1. `#RGB`
2. `#RRGGBB`
3. `rgb(red, green, blue)`
4. `rgba(red, green, blue, alpha)`

You can use the following string format for setting the fonts: `<bold> <italic> <size>pt <family>`.

### Line Styles[​](#line-styles "Direct link to Line Styles")

The following line styles are supported:

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Style Value|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Solid 0|  |  |  |  | | --- | --- | --- | --- | | Dotted 1|  |  | | --- | --- | | Dashed 2 | | | | | | | |

### Callbacks[​](#callbacks "Direct link to Callbacks")

1. You can use `this` keyword to access an API-object from within the callback function
2. You can pass two arguments to callback registration function - in this case first argument is an object which will be passed as first argument to callback function.
3. If callback isn’t set, then respective button will be hidden (affects `onReverse`, `onClose` and `onCancel` callbacks).