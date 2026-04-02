# Trading Platform: Common Broker API issues

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/common-issues

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Common Broker API issues

On this page

# Common Broker API issues

This article describes common issues that you might face when implementing the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api).

## Timeout issue[​](#timeout-issue "Direct link to Timeout issue")

You may encounter one of the following timeout issues:

* *Failed to close position: Position closing timeout*.
* *Failed to modify order: timeout waiting for new order*.
* *Failed to reverse position: Position reversing timeout*.

These issues happen because the library either received incorrect information or failed to receive timely updates for an order
or a position from your Broker API implementation.
To avoid these issues, ensure that:

* Your Broker API implementation calls [`orderUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#orderupdate)/[`positionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionupdate) within 10 seconds
  after the library sends a request to place/modify/cancel order or close/reverse position.
  This update is confirmation to the library that your backend server received the request.
* Your backend server and Broker API implementation provide the correct information to the library.

Consider the following example: a user closes a position of 10 AAPL shares.
In this case, the library calls the [`closePosition`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#closeposition) method to notify your backend server about the user's intent.
As a parameter, it provides your server with `positionId`.
After that, the library expects your backend server to close the position and provide an update on its new state within 10 seconds.

Your Broker API implementation should call the [`positionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionupdate) method on the Trading Host to provide updates.
As a parameter, it should send the correct [`Position`](/charting-library-docs/v29/api/interfaces/Charting_Library.Position) object to the library, which means that:

* the `id` property should match `positionId`
* the `qty` property should be `0`
* other required properties are specified
* all properties correspond to the declared types

When the library gets a position update, for example with a non-zero quantity or a different ID,
it assumes the data is for a different position and waits for the correct data.
If the library waits more than 10 seconds, it returns *Failed to close position: Position closing timeout*.

## Order and position IDs mismatch[​](#order-and-position-ids-mismatch "Direct link to Order and position IDs mismatch")

In some backend implementations, you might change the ID of an [order](/charting-library-docs/v29/trading_terminal/trading-concepts/orders) or [position](/charting-library-docs/v29/trading_terminal/trading-concepts/positions) between the time it’s submitted and the time it’s processed by your backend.
When this happens, the library may still reference the original ID, which no longer matches what's on your backend.
This mismatch can lead to issues in the UI.
For example, incorrect data may be displayed, and users may be unable to modify or cancel orders/positions because the library is referencing an invalid or unknown ID.

To recover from this mismatch, you can call the [`ordersFullUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#ordersfullupdate) and [`positionsFullUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionsfullupdate) methods.
These methods force the library to clear existing data and refetch the full list of orders or positions as if it was the first-time load.
Use these methods when you're unable to maintain a stable mapping between frontend and backend IDs.

warning

`ordersFullUpdate` and `positionsFullUpdate` are intended only for rare edge cases, such as dynamic ID changes.
These methods should not be used as part of your regular update flow.

If you need to notify the chart about a new or updated order/position, use [`orderUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#orderupdate) or [`positionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionupdate) instead.
These methods are designed to update the UI without clearing and reloading all data.
They should be your **default approach** for keeping the chart in sync with your backend events.

## Empty fields in bracket controls[​](#empty-fields-in-bracket-controls "Direct link to Empty fields in bracket controls")

You may encounter an issue when the input fields for bracket controls are empty.
Besides, users cannot enter values when accessing the *Edit position brackets* dialog.

![Empty bracket controls](/charting-library-docs/v29/assets/images/empty-bracket-controls-3a4aacb21e3caab407eecbedfeac7012.png)

This issue occurs because the library has not received all the necessary values for these fields.
To solve this issue, ensure that your integration meets the following requirements.

* The [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method returns all required fields within the `LibrarySymbolInfo` object.
* The [`symbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#symbolinfo) method returns all required fields within the `InstrumentInfo` object.
* You provide the library with the following updates:
  + Quote values via the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes)/[`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes) method of the Datafeed API.
  + Pip values via the [`pipValueUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#pipvalueupdate) method of the Trading Host if [`subscribePipValue`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#subscribepipvalue) is implemented.
    Ignore this update if `subscribePipValue` is not implemented.
  + Equity values via the [`equityUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#equityupdate) method of the Trading Host.

    tip

    It is advisable to send the equity updates once the broker has been created.
    If you want to provide updates while constructing the broker, encapsulate the updates within the [`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout) method.

    ```
    setTimeout(() => {  
      this._host.equityUpdate(12345678);  
    }, 5);
    ```

## Symbol quantity is overridden[​](#symbol-quantity-is-overridden "Direct link to Symbol quantity is overridden")

The default symbol quantity should be provided in the [`qty`](/charting-library-docs/v29/api/interfaces/Charting_Library.InstrumentInfo#qty) field of [`InstrumentInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.InstrumentInfo) when the library calls [`symbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#symbolinfo). When a user modifies the quantity in the [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket), the library saves the new value using either local storage or [`settings_adapter`](/charting-library-docs/v29/saving_loading/user-settings#settings-adapter). This user-defined quantity is then used instead of the default one for the next orders. This is intended behavior.

You can use the following methods to control quantity:

* [`getQty`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#getqty)
* [`setQty`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setqty)
* [`subscribeSuggestedQtyChange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#subscribesuggestedqtychange)
* [`unsubscribeSuggestedQtyChange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#unsubscribesuggestedqtychange)

If you want to override the user-defined quantity, call the [`subscribeSuggestedQtyChange`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#subscribesuggestedqtychange) method to track quantity changes and then reset its value using [`setQty`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setqty).

```
var widget = (window.tvWidget = new TradingView.widget({  
    // Other widget properties  
  
    broker_factory: function (host) {  
        window.host = host;  
        return new Brokers.BrokerSample(host, datafeed);  
    },  
}));  
  
// Declare a callback  
const cb = (qty) => {  
    console.log(`Quantity changed to ${qty}`);  
};  
// Subscribe to quantity changes for BTCUSD using the callback  
host.subscribeSuggestedQtyChange('COINBASE:BTCUSD', cb);  
// Change the quantity  
host.setQty('COINBASE:BTCUSD', 24);  
// Unsubscribe from quantity changes for BTCUSD  
host.unsubscribeSuggestedQtyChange('COINBASE:BTCUSD', cb);
```