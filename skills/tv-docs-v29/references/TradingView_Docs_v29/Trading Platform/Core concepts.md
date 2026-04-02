# Trading Platform: Core concepts

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/trading-concepts/

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Core concepts

On this page

# Core trading concepts

Trading Platform provides the ability to trade right from the chart.
Users can manage orders, track positions, monitor their potential profits and losses, and more.
In this article, you will learn about the trading components, how they integrate into the chart widget, and how they work together.

## Trading components[​](#trading-components "Direct link to Trading components")

Trading in Trading Platform is based on three key components: the [Broker API](#broker-api), [Trading Host](#trading-host), and [Datafeed API](#datafeed-api).
The diagram below illustrates how these components should be integrated with the library and your backend server.

[![Diagram illustrating trading components](/charting-library-docs/v29/img/trading-components-diagram-light.svg)![Diagram illustrating trading components](/charting-library-docs/v29/img/trading-components-diagram-dark.svg)](/charting-library-docs/v29/img/trading-components-diagram-light.svg)

### Broker API[​](#broker-api "Direct link to Broker API")

The Broker API enables trading functionality in the library by connecting the chart interface to your backend trading logic.
This API is used when the library actively requests information or performs actions, for example, placing an order or fetching account details.

The Broker API is an object that bridges the library and your backend trading server, handling the exchange of data, such as account information, orders, executions, and positions.
You can implement the Broker API through the [`IBrokerTerminal`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal) interface.

### Trading Host[​](#trading-host "Direct link to Trading Host")

The Trading Host is an API that facilitates communication between the Broker API and the trading-related parts of the library.
The Trading Host is used to send updates from your backend to the library that the library didn’t explicitly request but still needs to keep trading information accurate and up to date (for example, order status changes or profit and loss updates).

The Trading Host is defined by the [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost) interface and consists of callback-like methods.
You should call these methods from your [Broker API](#broker-api) implementation whenever updates occur on your backend.

### Datafeed API[​](#datafeed-api "Direct link to Datafeed API")

The [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) provides market data to the library and plays two distinct roles.
On the one hand, it is used directly by the library to retrieve standard market data — such as historical bars, symbol information, and resolutions.

On the other hand, for trading functionality, its role is to provide **real-time quotes** (bid/ask prices, last price, etc.).
[Quotes](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes) are used in most Trading Platform features including the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket), [Legend](/charting-library-docs/v29/ui_elements/Legend), and widgets, such as [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List), [Details](/charting-library-docs/v29/trading_terminal/#details), [News](/charting-library-docs/v29/trading_terminal/news), and [Depth of Market](/charting-library-docs/v29/trading_terminal/depth-of-market).

In the trading context, the library does not access the Datafeed API directly.
Instead, you should call the methods of the [`IDatafeedQuotesApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedQuotesApi) interface within your [Broker API](#broker-api) implementation.

## How to enable trading[​](#how-to-enable-trading "Direct link to How to enable trading")

### Implement quote methods[​](#implement-quote-methods "Direct link to Implement quote methods")

To use Trading Platform, in addition to the [required](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods) Datafeed API methods, implement the quote-related methods.

* [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes)
* [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes)
* [`unsubscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#unsubscribequotes)

### Connect Broker API[​](#connect-broker-api "Direct link to Connect Broker API")

To enable trading, you should pass the function that returns a new object of the Broker API implementation to the library.
To do this, use the [`broker_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_factory) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor#trading-platform-parameters).
Note that this function should accept the Trading Host instance as a parameter.

In the code sample below, the function assigned to `broker_factory` accepts `tradingHost` parameter,
which is an instance of [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost).
This function returns an instance of `BrokerSample` that implements [`IBrokerTerminal`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal).

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    broker_factory: function(tradingHost: IBrokerConnectionAdapterHost) { return new Brokers.BrokerSample(tradingHost, datafeed); },  
})
```

### Implement Broker API methods[​](#implement-broker-api-methods "Direct link to Implement Broker API methods")

Implement the methods required for your trading setup through the [`IBrokerTerminal`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal) interface.
Check out our [step-by-step tutorial](/charting-library-docs/v29/tutorials/implement-broker-api/) on implementing the required methods for basic trading functionality.
It’s the fastest way to get started with the Broker API.

## How library gets user's data[​](#how-library-gets-users-data "Direct link to How library gets user's data")

When the chart is initially loaded, the library requests data from your Broker API implementation through the following methods:

* [`orders`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#orders)
* [`positions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#positions)
* [`executions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#executions)
* [`individualPositions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#individualpositions) (optional, required if the [`supportPositionNetting`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportpositionnetting) flag is set to `true`).

Using these methods, the library retrieves data about the orders, positions, and executions the user already had before the chart creation.
Then, the library gets updates for these orders and positions through the Trading Host methods.
Refer to the [next section](#how-components-work-together) for a step-by-step example.

## How components work together[​](#how-components-work-together "Direct link to How components work together")

To understand how the library, [Broker API](#broker-api), [Trading Host](#trading-host), and your implemented trading logic should work together,
consider the following step-by-step example.
Suppose a user wants to buy 10 AAPL shares.
This user action initiates three consecutive steps:

[![Diagram illustrating the action steps](/charting-library-docs/v29/img/create-order-steps-diagram-light.svg)![Diagram illustrating the action steps](/charting-library-docs/v29/img/create-order-steps-diagram-dark.svg)](/charting-library-docs/v29/img/create-order-steps-diagram-light.svg)

In the subsequent sections, you will delve into each of these steps, finding detailed explanations and sequence diagrams:

1. [Order creation](#1-order-creation)
2. [Execution update](#2-execution-update)
3. [Equity update](#3-equity-update)

You can also refer to the diagram that illustrates the entire process, starting from creating the order in the UI until the position is established.

Expand to view the diagram of the entire process.

[![Diagram illustrating the entire process of creating order](/charting-library-docs/v29/img/create-order-complete-diagram-light.svg)![Diagram illustrating the entire process of creating order](/charting-library-docs/v29/img/create-order-complete-diagram-dark.svg)](/charting-library-docs/v29/img/create-order-complete-diagram-light.svg)

### 1. Order creation[​](#1-order-creation "Direct link to 1. Order creation")

The diagram below illustrates the process of creating an order.

[![Order creation diagram](/charting-library-docs/v29/img/order-creation-diagram-light.svg)![Order creation diagram](/charting-library-docs/v29/img/order-creation-diagram-dark.svg)](/charting-library-docs/v29/img/order-creation-diagram-light.svg)

1. The user specifies 10 units of AAPL shares in the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket) and clicks the *Buy* button.
2. The library interprets this action as a trigger to notify your Broker API implementation that the user wants to create the order.
3. The library calls the [`placeOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#placeorder) method, passing along the order data.
   The code sample below shows an example of the data object:

   ```
   {  
       "symbol": "NasdaqNM:AAPL",  
       "type": 2,  // OrderType.Market  
       "side": 1,  // Side.Buy  
       "qty": 10,  
       "currentQuotes": {  
           "ask": 173.68,  
           "bid": 173.68  
       },  
       "customFields": {}  
   }
   ```

   Note that your Broker API implementation should interpret this call as a notification of the user's intent to create the order.
4. Your Broker API implementation responds with [`PlaceOrderResult`](/charting-library-docs/v29/api/interfaces/Charting_Library.PlaceOrderResult).
5. The library waits for your backend server to create the order within 10 seconds and provide the updated information.
   Note that the library will return a [timeout issue](/charting-library-docs/v29/trading_terminal/common-issues#timeout-issue) if it fails to receive a timely order update.
6. Your Broker API implementation requests your backend server to create the order.
7. Your backend server creates the order and prepares the updated information.
8. Your backend server provides a response to your Broker API implementation with updated information.
9. Your Broker API implementation calls the [`orderUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#orderupdate) method.
   As a parameter, it sends the [`PlacedOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.PlacedOrder) object to the library.
   Note that the `qty`, `id`, `symbol`, and `side` properties must be identical to the data provided in step 3 within the `placeOrder` method.  
   The code sample below shows an example of the `PlacedOrder` object:

   ```
   {  
       "id": "1",  
       "qty": 10,  
       "side": 1,   // Side.Buy  
       "status": 6, // OrderStatus.Working  
       "symbol": "NasdaqNM:AAPL",  
       "type": 2    // OrderType.Market  
   }
   ```

   info

   Here, the object has a `status` property that indicates the order's current [status](/charting-library-docs/v29/api/enums/Charting_Library.OrderStatus).
   Initially, when the order is created but has not been executed, it is assigned the *working* status.
   Once the order is executed, its status should be updated to *filled*.
   This will be done [further](#2-execution-update).
10. The Trading Host receives updates and informs the library and the UI that the order has been created.
11. The user sees the new working order in the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/).

After this, the backend server should [execute the working order](#2-execution-update) and add a new position.

### 2. Execution update[​](#2-execution-update "Direct link to 2. Execution update")

At this point, the user can see the new working order in the Account Manager.
Following this, your backend server is responsible for executing the order and creating a position.
The diagram below illustrates this process.

[![Execution update diagram](/charting-library-docs/v29/img/execution-update-diagram-light.svg)![Execution update diagram](/charting-library-docs/v29/img/execution-update-diagram-dark.svg)](/charting-library-docs/v29/img/execution-update-diagram-light.svg)

1. Your backend server executes the order and prepares the updated information.
   Note that the order execution and update might be processed on external sources, such as exchanges.
   However, your server is expected to manage this information and provide it in the format required by the library.
2. Your backend server provides a response to your Broker API implementation with updated information.
3. Your Broker API implementation calls the [`executionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#executionupdate) method.
   As a parameter, it sends the [`Execution`](/charting-library-docs/v29/api/interfaces/Charting_Library.Execution) object.
   The code sample below shows an example of this object:

   ```
   {  
       "price": 173.68,  
       "qty": 10,  
       "side": 1,  // Side.Buy  
       "symbol": "NasdaqNM:AAPL",  
       "time": 1697032262341  
   }
   ```
4. Your Broker API implementation calls the [`orderUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#orderupdate) method to update the order status to *filled*.
   As a parameter, your Broker API implementation sends the [`PlacedOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.PlacedOrder) object.
   The code sample below shows an example of this object:

   ```
   {  
       "id": "1",  
       "qty": 10,  
       "side": 1,    // Side.Buy  
       "status": 2,  // OrderStatus.Filled  
       "symbol": "NasdaqNM:AAPL",  
       "type": 2,    // OrderType.Market  
   }
   ```
5. Your Broker API implementation calls the [`positionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionupdate) method to notify the Trading Host that the position is added.
   As a parameter, it sends the [`Position`](/charting-library-docs/v29/api/interfaces/Charting_Library.Position) object.
   The code sample below shows an example of this object:

   ```
   {  
       "id": "NasdaqNM:AAPL",  
       "qty": 10,  
       "side": 1,  // Side.Buy  
       "symbol": "NasdaqNM:AAPL",  
       "avgPrice": 173.68  
   }
   ```
6. The Trading Host receives updates and informs the library and the UI that the order has been executed and the position has been added.
7. The user sees a new position of 10 AAPL shares in the Account Manager.

After this, your backend server should [update user's equity](#3-equity-update).

### 3. Equity update[​](#3-equity-update "Direct link to 3. Equity update")

At this stage, the user sees that the order has been executed and the position has been created.
Next, your backend server should update the user's equity and the Profit & Loss (P&L) values for all active positions whenever there is a price change.

info

To keep the UI data up-to-date, you should constantly provide updates of users' entity and P&L values whenever changes occur.

The diagram below illustrates the process of updating the equity and P&L values.

[![Equity update diagram](/charting-library-docs/v29/img/equity-update-diagram-light.svg)![Equity update diagram](/charting-library-docs/v29/img/equity-update-diagram-dark.svg)](/charting-library-docs/v29/img/equity-update-diagram-light.svg)

1. Your backend server calculates the user's equity and P&L and prepares the updated information.
   Note that the calculations might be processed on external sources, such as exchanges.
   However, your server is expected to manage this information and provide it in the format required by the library.
2. Your backend server provides a response to your Broker API implementation with updated information.
3. Your Broker API implementation calls the [`equityUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#equityupdate) method to notify the Trading Host about equity updates.
   As a parameter, it sends the accurate equity amount, for example, `[10000000]`.
4. Your Broker API implementation calls the [`plUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#plupdate) method to notify the Trading Host about P&L updates.
5. The Trading Host notifies the library and the UI about updates.
6. The user sees updated equity and P&L values in the Account Manager.

At this stage, the user owns the position of 10 AAPL shares.

## Implementation example[​](#implementation-example "Direct link to Implementation example")

tip

If you're new to the Broker API, we recommend beginning with our [step-by-step tutorial](/charting-library-docs/v29/tutorials/implement-broker-api/).
It walks you through implementing the required methods to get trading components working.

You can also reference a more advanced example of the Broker API implementation on GitHub.
However, the repository is private and requires you to [get access](/charting-library-docs/v29/getting_started/quick-start#getting-access) first.

The [Broker API example](https://github.com/tradingview/trading_platform/tree/master/broker-sample "The repository is private.") 🔐 includes TypeScript source code, which can serve as a template for your implementation.
Note that this example does not establish a connection with an actual broker but simulates order and position management as a mock setup.
This implementation is also used on the [Trading Platform demo page](https://trading-terminal.tradingview-widget.com/) where you can experiment with various trading features.