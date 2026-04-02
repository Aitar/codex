# Trading Platform: Order Ticket

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/order-ticket

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Order Ticket

On this page

# Order Ticket

The **Order Ticket** (also known as Order Panel) is a dialog that allows users to place orders.
Users can open this dialog in several ways:

* By clicking the *Trade* button in the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/).
* By clicking the *Plus* button on the [Price Scale](/charting-library-docs/v29/ui_elements/Price-Scale).
* By clicking the *Buy Market* and *Sell Market* buttons in the [Legend](/charting-library-docs/v29/ui_elements/Legend).
* By right-clicking the chart and selecting *Trade → Create new order…* in the context menu.

The Order Ticket is enabled by default, but you can disable it using the [`order_panel`](/charting-library-docs/v29/customization/Featuresets#order_panel) featureset.

![Order Ticket](/charting-library-docs/v29/assets/images/order-ticket-cba466312927cc1e24a56ca7cbbc24a1.png)

## Configure order types[​](#configure-order-types "Direct link to Configure order types")

The library supports four [order types](/charting-library-docs/v29/trading_terminal/trading-concepts/orders#order-types): limit, market, stop, and stop-limit.
By default, users can select market, limit, and stop orders in the Order Ticket.
But you can disable support for these order types via the [`supportMarketOrders`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmarketorders), [`supportLimitOrders`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportlimitorders), and [`supportStopOrders`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportstoporders) flags, respectively.

You can also enable a stop-limit order type by setting [`supportStopLimitOrders`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportstoplimitorders) to `true`.
Refer to the [Trading features configuration](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) section for more information on setting configuration flags.

## Change text for quantity units[​](#change-text-for-quantity-units "Direct link to Change text for quantity units")

To customize the text displaying quantity units in the Order Ticket, use the [`units`](/charting-library-docs/v29/api/interfaces/Charting_Library.InstrumentInfo#units) field within the `InstrumentInfo` object.
You should return this object when the library calls the [`symbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#symbolinfo) method.

## Add custom fields[​](#add-custom-fields "Direct link to Add custom fields")

If you want to add custom fields to the Order Ticket dialog, implement the [`getOrderDialogOptions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#getorderdialogoptions) method within your [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api) implementation.
The method should return the [`OrderDialogOptions`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderDialogOptions) object.
This object should contain the `customFields` property of the [`TradingDialogCustomField`](/charting-library-docs/v29/api/modules/Charting_Library#tradingdialogcustomfield) type.
Note that the available custom field types are limited to combobox and checkbox.

Similarly, you can add custom fields to the *Positions* dialog by implementing the [`getPositionDialogOptions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#getpositiondialogoptions) method.

info

The library does not support adding custom fields to the *Order info* section of the Order Ticket.
The information displayed there, such as pip value, is derived from the [`InstrumentInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.InstrumentInfo) interface when certain broker [configuration flags](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) are enabled.
Consider providing additional details in the [order preview dialog](#enable-order-preview).

## Enable order preview[​](#enable-order-preview "Direct link to Enable order preview")

You can show users additional order details before modifying or placing orders.
For example, you can display the estimated order cost, commission, expiry date, and any warning or error messages as a part of the order preview dialog. In these messages, you can provide links to external URLs, such as specific T&Cs.
Note that users can still clear the *Show order confirmations* checkbox in the [ellipsis menu](#order-confirmations),
meaning that the order preview dialog will not appear.

To enable order preview, follow the steps below:

1. Set the following flags to `true`:

   * [`supportPlaceOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportplaceorderpreview) enables an order preview dialog before users place orders.
   * [`supportModifyOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmodifyorderpreview) enables an order preview dialog before users modify orders.

   Refer to the [Trading features configuration](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) section for more information on setting configuration flags.
2. Implement the [`previewOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#previeworder) method within your Broker API implementation.
   When users click *Buy order* or *Modify order* in the Order Ticket, the library calls `previewOrder`.
   This method returns the [`OrderPreviewResult`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderPreviewResult) object with the necessary information that is displayed in the order preview dialog.
   Within the object, you can:

   * Set a unique confirmation ID via `confirmId`. Note that it should be passed as a parameter to `modifyOrder` or `placeOrder`.
   * Customize extra fields using `sections`.
   * Set up text for warnings and errors using the `warnings` and `errors` properties.
     The warnings and errors are displayed below the order details in colored boxes.

   caution

   You will get the *Order preview is not supported* issue in the console
   if `supportPlaceOrderPreview` and `supportModifyOrderPreview` are enabled, but `previewOrder` is not implemented.
3. Implement the [`modifyOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#modifyorder) and [`placeOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#placeorder) methods.
   The library calls them right after users click *Send Order* in the order preview dialog:

   * `modifyOrder` is called when users want to modify existing orders.
   * `placeOrder` is called when users want to place new orders.

You can check the implementation of the order preview dialog in the CodePen below.

See the Pen [Untitled](https://codepen.io/tradingview/pen/XWOLzzM) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

## Enable bracket controls[​](#enable-bracket-controls "Direct link to Enable bracket controls")

You can display controls for adding bracket orders in the Order Ticket dialog.
[Bracket orders](/charting-library-docs/v29/trading_terminal/trading-concepts/brackets) allow users to protect their positions.
To add controls, enable the [`supportOrderBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportorderbrackets) flag.

You can also disable bracket controls only for market orders by setting the [`supportMarketBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmarketbrackets) flag to `false`.

## Manage ellipsis menu[​](#manage-ellipsis-menu "Direct link to Manage ellipsis menu")

Users can access additional Order Ticket settings in the ellipsis menu.
You can also programmatically [get and set values](#get-and-set-settings) for these settings.

### Default settings[​](#default-settings "Direct link to Default settings")

By default, and without specifying any [configuration flags](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration),
the Order Ticket has the following settings shown in the ellipsis menu:

* *Show Order Price in Ticks*
* *Show Quantity in Money Risk*
* *Show Quantity in % Risk*

![Default settings in the ellipsis menu of the Order Ticket](/charting-library-docs/v29/assets/images/order-ticket-settings-base-d6f7f02c96d896a667e0e5e77072bd0e.png)

### Brackets settings[​](#brackets-settings "Direct link to Brackets settings")

If you set the [`supportOrderBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportorderbrackets), [`supportMarketBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmarketbrackets), or [`supportPositionBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportpositionbrackets) flags to `true`,
the *Show TP/SL inputs in Money* and *Show TP/SL inputs in %* settings will appear in the ellipsis menu.

![Bracket settings in the ellipsis menu of the Order Ticket](/charting-library-docs/v29/assets/images/order-ticket-settings-brackets-81fe1479014041d427d891a35202e014.png)

info

Note that these settings will not have any impact when used in [crypto brackets](#enable-crypto-brackets-settings).
Selecting and clearing these checkboxes will not be visually reflected.

### Order confirmations[​](#order-confirmations "Direct link to Order confirmations")

tip

The [`supportPlaceOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportplaceorderpreview) and [`supportModifyOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmodifyorderpreview) flags enable order preview.
It allows showing users additional order details before modifying or placing orders.
Refer to [Enable order preview](#enable-order-preview) for more information.

If you set the [`supportPlaceOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportplaceorderpreview) or [`supportModifyOrderPreview`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportmodifyorderpreview) flags to `true`,
the *Show order confirmations* will appear in the ellipsis menu.

![Order Ticket Settings Order Confirmations](/charting-library-docs/v29/assets/images/order-ticket-settings-order-confirmations-8d7b55f37240afff1c974e3018824f16.png)

### Get and set settings[​](#get-and-set-settings "Direct link to Get and set settings")

You can programmatically access and change settings, available in the ellipsis menu.
To do this, use the [`getOrderTicketSetting`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#getorderticketsetting) and [`setOrderTicketSetting`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setorderticketsetting) methods of the [Trading Host](/charting-library-docs/v29/trading_terminal/trading-concepts/#trading-host).
You can find the full list of properties in the [OrderTicketSettings](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderTicketSettings) interface.

## Enable crypto brackets settings[​](#enable-crypto-brackets-settings "Direct link to Enable crypto brackets settings")

The [`supportCryptoBrackets`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportcryptobrackets) flag enables crypto brackets and displays additional settings within the *Take Profit* and *Stop Loss* brackets: *Money* and *%*.

* Money setting* % setting

![Order Ticket settings: crypto bracket in currency](/charting-library-docs/v29/assets/images/order-ticket-settings-showCryptoBracketsInCurrency-339c2aece5ad5dcca97f7264e48f0313.png)

![Order Ticket settings: crypto bracket in percent](/charting-library-docs/v29/assets/images/order-ticket-settings-showCryptoBracketsInPercent-78ea0e9e815a745272c1fe8a1aa65104.png)

You can also programmatically [get or set these settings](#get-and-set-settings)
using the [`showCryptoBracketsInCurrency`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderTicketSettings#showcryptobracketsincurrency) and [`showCryptoBracketsInPercent`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderTicketSettings#showcryptobracketsinpercent) properties.
Note that these settings are not shown in the ellipsis menu.

## Enable Time in force menu[​](#enable-time-in-force-menu "Direct link to Enable Time in force menu")

You can enable the *Time in force* drop-down menu that allows users to specify order duration.
Duration determines how long the order remains active.

![The durations drop-down menu in the Order Ticket](/charting-library-docs/v29/assets/images/order-ticket-durations-b95962b3f0b30c02a8e90c1d9a54c89d.png)

To enable the menu,
provide [`durations`](/charting-library-docs/v29/api/interfaces/Charting_Library.SingleBrokerMetaInfo#durations) within the `SingleBrokerMetaInfo` object assigned to [`broker_config`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_config).
The `durations` property is an array of [`OrderDurationMetaInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderDurationMetaInfo) objects that specify the order duration settings. For example, you can adjust a duration value or title that is displayed in the UI.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    broker_factory: function(host) { return new Brokers.BrokerSample(host, datafeed); },  
    broker_config: {  
        configFlags: {  
            // Configuration flags  
        },  
        durations: [  
            { name: 'DAY', value: 'DAY' },  // Day orders  
            { name: 'GTC', value: 'GTC' },  // Good-Til-Canceled orders  
        ],  
    },  
})
```

Note that the duration options are displayed for limit, stop, and stop-limit order types by default.
However, if you want to specify a different set of duration options for a particular type,
you need to provide this information in the [`supportedOrderTypes`](/charting-library-docs/v29/api/interfaces/Charting_Library.OrderDurationMetaInfo#supportedordertypes) array of the `durations` property.

## Implement custom Order Ticket[​](#implement-custom-order-ticket "Direct link to Implement custom Order Ticket")

You can display your own Order Ticket instead of the built-in one.
To do this, you should provide [`customUI`](/charting-library-docs/v29/api/interfaces/Charting_Library.SingleBrokerMetaInfo#customui) within the `SingleBrokerMetaInfo` object assigned to [`broker_config`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_config).
The values of [`customUI`](/charting-library-docs/v29/api/interfaces/Charting_Library.SingleBrokerMetaInfo#customui) are functions that Trading Platform calls to show several dialogs, including the Order Ticket.
Each function returns a Promise object that should be resolved when the operation is finished or canceled.
Note that the returned Promise object should be resolved with either a `true` or `false` value.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    broker_factory: function(host) { return new Brokers.BrokerSample(host, datafeed); },  
    broker_config: {  
        configFlags: {  
            // Configuration flags  
        },  
        customUI: {  
            showOrderDialog: (order, focus) => Promise<boolean>;  
        },  
    },  
})
```