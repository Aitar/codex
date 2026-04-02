# Getting Started: Glossary

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/glossary

* [Getting Started](/charting-library-docs/v29/getting_started/)* Glossary

On this page

# Glossary

This article contains terms that are used in the Advanced Charts documentation.

## Trading terms[​](#trading-terms "Direct link to Trading terms")

### Bracket order[​](#bracket-order "Direct link to Bracket order")

An [order](#order) that helps users limit their losses and secure their profits
by bracketing positions with two opposing [stop-loss](#stop-loss-order) and [take-profit](#take-profit-order) orders.
Refer to [Bracket orders](/charting-library-docs/v29/trading_terminal/trading-concepts/brackets) for more information.

### Execution[​](#execution "Direct link to Execution")

The completion of a buy or sell order for a financial instrument. An execution involves matching a buyer and a seller and transferring ownership of the financial instrument.

### Individual position[​](#individual-position "Direct link to Individual position")

The amount of a singular holding or investment in a financial instrument.

### Limit order[​](#limit-order "Direct link to Limit order")

An [order](#order) to buy or sell a financial instrument when a given or better price is reached.
This order type guarantees a specific price but does not guarantee immediate execution.

### Limit price[​](#limit-price "Direct link to Limit price")

The maximum price a buyer is willing to pay or the minimum price a seller is willing to accept.

### Market order[​](#market-order "Direct link to Market order")

An [order](#order) to buy or sell a financial instrument at the current market price.
This order type guarantees immediate execution but does not guarantee a specific price.

### Net position[​](#net-position "Direct link to Net position")

The difference between an investor's total number of open long and short positions at any given time.

### Order[​](#order "Direct link to Order")

A request made by a trader to buy or sell a financial instrument at a specified price and quantity. An order can have various attributes, such as a [limit price](#limit-price), [stop price](#stop-price), and [duration](#order-duration). Depending on whether an order has been executed or not, it can be in various statuses such as canceled, filled, placing, or rejected.
Refer to [Orders](/charting-library-docs/v29/trading_terminal/trading-concepts/orders) for more information.

### Order duration[​](#order-duration "Direct link to Order duration")

The time during which an order remains active.

### Pip[​](#pip "Direct link to Pip")

The minimum price movement for Forex symbols. For more information on how to display pips, refer to the [Price format](/charting-library-docs/v29/connecting_data/Symbology#how-to-display-pips) section.

### Position[​](#position "Direct link to Position")

The amount of a financial instrument held by an investor.
For more information, refer to [Positions](/charting-library-docs/v29/trading_terminal/trading-concepts/positions).

### Position netting[​](#position-netting "Direct link to Position netting")

The process of aggregating multiple individual positions for one symbol into a single net position.
For more information, refer to [Position netting](/charting-library-docs/v29/trading_terminal/trading-concepts/positions#position-netting).

### Quotes[​](#quotes "Direct link to Quotes")

Real-time price information for financial instruments, including the most recent bid and ask prices, opening and closing prices, price changes, and other market data.
Refer to [Quotes](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes) for more information.

### Stop-loss order[​](#stop-loss-order "Direct link to Stop-loss order")

A type of [order](#order) designed to limit losses by automatically closing a position at a given price when it moves unfavorably.

### Stop order[​](#stop-order "Direct link to Stop order")

An [order](#order) to buy or sell a financial instrument at the market price as soon as it reaches a certain level.

### Stop price[​](#stop-price "Direct link to Stop price")

A trigger price at which an order becomes a market or limit order.

### Take-profit order[​](#take-profit-order "Direct link to Take-profit order")

A type of [limit order](#limit-order) that closes a position at a specific price to secure a profit.

### Tick[​](#tick "Direct link to Tick")

The minimum price movement.

## Technical terms[​](#technical-terms "Direct link to Technical terms")

### Bar spacing[​](#bar-spacing "Direct link to Bar spacing")

A number of pixels between each data point on the chart. Smaller values show more data.

### Datafeed[​](#datafeed "Direct link to Datafeed")

A middleware that requests data from a server and sends it to the library. Refer to the [Connecting data](/charting-library-docs/v29/connecting_data/) article for more information.

### Date range[​](#date-range "Direct link to Date range")

A period of time that is currently visible on the chart canvas. This range changes when users scale the chart. Refer to [Time scale](/charting-library-docs/v29/ui_elements/Time-Scale#time-frame-toolbar) for more information.

### Featureset[​](#featureset "Direct link to Featureset")

A toggle that allows you to enable or disable a certain feature. Refer to the [Featuresets](/charting-library-docs/v29/customization/Featuresets) article for more information.

### Pane[​](#pane "Direct link to Pane")

An area on the chart where a [series](#series) or [indicator](/charting-library-docs/v29/ui_elements/indicators/) is displayed. The picture below shows the red pane with the main series and the green pane with the indicator.

![Chart panes](/charting-library-docs/v29/assets/images/pane-d44d70e4c4be2d846c4ecdd789fc0e17.png)

### Plot[​](#plot "Direct link to Plot")

A line or area that represents indicator values on a chart.

### Series[​](#series "Direct link to Series")

A collection of data points that represents a specific metric over time. A series can be of different styles that affect how data is displayed on the chart. Refer to [Chart styles](/charting-library-docs/v29/customization/overrides/chart-overrides#chart-styles) for more information.

### Source symbol[​](#source-symbol "Direct link to Source symbol")

A symbol that is used as a data source for a certain indicator. The indicator calculates its own data based on the symbol's data.

### Spread operators[​](#spread-operators "Direct link to Spread operators")

Operators that allow comparison between a financial instrument, such as a stock,
and an additional variable, such as another financial instrument or a numerical value.
Spread operators can be enabled in the [Search Symbol](/charting-library-docs/v29/ui_elements/Symbol-Search#enable-spread-operators)
and [Compare Symbol](/charting-library-docs/v29/ui_elements/indicators/#enable-spread-operators) dialogs.