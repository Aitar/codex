# Trading Platform: Account Manager

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/account-manager/

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Account Manager

On this page

# Account Manager

The **Account Manager** is an interactive widget that displays trading information, such as orders, positions, an account balance, and more.

![Account Manager](/charting-library-docs/v29/assets/images/account-manager-full-1c3e7e5b309c7ee85b661fd5cf1b14ff.png)

tip

This article provides an overview of the Account Manager.
For a hands-on understanding, refer to the [Broker API implementation](https://github.com/tradingview/trading_platform/tree/master/broker-sample "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) on GitHub.
This example is used on the [Trading Platform demo page](https://trading-terminal.tradingview-widget.com/) where you can test trading features, including the Account Manager.

## Create Account Manager[​](#create-account-manager "Direct link to Create Account Manager")

To enable the Account Manager, implement the [`accountManagerInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#accountmanagerinfo) method within the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api).
This method should return an [`AccountManagerInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo) object
containing the information that will be displayed in the Account Manager.

The Account Manager consists of the [*Account Summary* row](#account-summary-row) and different [pages](#pages).
The Account Manager includes the default [*Orders* and *Positions*](#orders-and-positions) pages,
but you can also add [*History*](#history), [*Notifications log*](#notifications-log), or your [custom](#custom-pages) pages.

```
accountManagerInfo() {  
    return {  
        accountTitle: "Sample title",  // Account Manager title  
        summary: [],                   // Custom fields that are displayed in the Account Summary row  
        orderColumns: [],              // Columns that build the Orders page  
        positionColumns: [],           // Columns that build the Positions page  
        pages: [],                     // Columns that build your custom pages  
    };  
}
```

## User accounts[​](#user-accounts "Direct link to User accounts")

The Account Manager is designed to display the trading data of a particular user account.
Users can have multiple accounts and switch between them using the drop-down menu in the Account Manager.
Refer to [Multiple accounts](/charting-library-docs/v29/trading_terminal/account-manager/multiple-accounts) for more information.

## Account Summary row[​](#account-summary-row "Direct link to Account Summary row")

The *Account Summary* row is a line that is always displayed at the top-right corner of the Account Manager.
Usually, it contains the most important information about the account's current state, such as balance and equity.

![Account Summary row](/charting-library-docs/v29/assets/images/account-summary-row-52dd0839aa944bb30df2994ab337674b.png)

Use the [`summary`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#summary) property to build the *Account Summary* row.
Each [`AccountManagerSummaryField`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerSummaryField) object passed within `summary` creates a separate field.

```
// Here, balanceValue = host.factory.createWatchedValue(value);  
summary: [  
    {  
        text: "Balance",      // The summary field title  
        wValue: balanceValue, // A WatchedValue object that is used to read the field state  
        formatter: "fixed",   // The formatter name that formats the field  
        isDefault: true,      // Displays the field by default  
    },  
]
```

### Watched values[​](#watched-values "Direct link to Watched values")

The values defined in the row use [watched values](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerSummaryField#wvalue).
This means that these values should be constantly updated,
so the users have up‑to‑date data about their account state.
To create a `WatchedValue` object, use the [`createWatchedValue`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterFactory#createwatchedvalue) method within the [Trading Host](/charting-library-docs/v29/trading_terminal/trading-concepts/#trading-host).
To update the values, use the [`setValue`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchedValue#setvalue) method.

## Pages[​](#pages "Direct link to Pages")

The Account Manager has the [*Orders*, *Positions*](#orders-and-positions), [*History*](#history), and [*Notifications log*](#notifications-log) pages.
You can also create your [custom pages](#custom-pages).

Each page represents a table where you define [columns](#columns) and the data to be displayed.

### Orders and Positions[​](#orders-and-positions "Direct link to Orders and Positions")

When implementing the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api), you should implement the [`orders`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#orders) and [`positions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#positions) methods.
The library calls these methods to retrieve data objects about the user's orders and positions.
This data is then displayed on the [*Orders* and *Positions*](#orders-and-positions) pages of the Account Manager.

To specify the data you want to display on these pages,
define the [`orderColumns`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#ordercolumns) and [`positionColumns`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#positioncolumns) properties in the `AccountManagerInfo` object.
These properties represent arrays of objects where each object is a separate [column](#columns).

* Orders page* Positions page

![The Orders page in the Account Manager](/charting-library-docs/v29/assets/images/orders-page-c4e200f9a0f2d6b90c23a388dfdb0b55.png)

![The Positions page in the Account Manager](/charting-library-docs/v29/assets/images/positions-page-ae1e0c76e49ffe2b03018c4ba036fae5.png)

### History[​](#history "Direct link to History")

The *History* page shows details about all orders with their final [statuses](/charting-library-docs/v29/trading_terminal/trading-concepts/orders#order-statuses).
To enable order history, follow the steps below:

1. Set the [`supportOrdersHistory`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#supportordershistory) flag, which adds the *History* tab to the Account Manager, to `true`.
   Refer to the [Trading features configuration](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) section for more information about configuration flags.
2. Provide the order history via the [`ordersHistory`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#ordershistory) method.
   The returned orders should have final statuses like `rejected`, `filled`, or `cancelled`.
3. Add the [`historyColumns`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#historycolumns) property to the [`AccountManagerInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo) object
   to define and display data columns. Optionally, use the [`historyColumnsSorting`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#historycolumnssorting) property for sorting values.

### Notifications log[​](#notifications-log "Direct link to Notifications log")

The *Notifications log* page logs trading actions like placing or canceling orders.
This page is visible by default, however, you can hide it via the [`showNotificationsLog`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags#shownotificationslog) flag.
Refer to the [Trading features configuration](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) section for more information about configuration flags.

![Notifications log](/charting-library-docs/v29/assets/images/notifications-log-9632fdfb9add53eb60d3a50e9b39a646.png)

You can also create notifications via the [`showNotification`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#shownotification) method.
These notifications appear as toast messages at the bottom-left corner and are also recorded in the *Notifications log* page.

If you want to display custom fields' information from orders or positions in notifications,
use the [`customNotificationFields`](/charting-library-docs/v29/api/interfaces/Charting_Library.SingleBrokerMetaInfo#customnotificationfields) property within the [`broker_config`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_config) object of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

### Custom pages[​](#custom-pages "Direct link to Custom pages")

Custom pages can be created via the [`pages`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerInfo#pages) property of [`AccountManagerInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#accountmanagerinfo).
Additionally, you have the flexibility to include multiple tables within your custom pages by specifying them in the [`tables`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerPage#tables) property.
See [How to create custom page in Account Manager](/charting-library-docs/v29/tutorials/create-custom-page-in-account-manager).

## Columns[​](#columns "Direct link to Columns")

Each Account Manager page is a table, where each column is an [`AccountManagerColumnBase`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerColumnBase) object.
The order of column display aligns with the sequence of objects added to the columns array.

```
{  
    id: "id",           // Unique ID  
    label: "Order id",  // Column title  
    dataFields: ["id"], // Data that is displayed in the column  
},
```

`AccountManagerColumnBase` has three required properties:

* `id` — a unique identifier of a column.
* `label` — the title that is displayed in the column's header.
* `dataFields` — an array of strings that match the property names in the [order](/charting-library-docs/v29/api/interfaces/Charting_Library.PlacedOrder)/[position](/charting-library-docs/v29/api/interfaces/Charting_Library.Position) data object.
  `dataFields` is used to generate the values displayed in a column.
  The displayed value in the column updates only when the corresponding values in the data object change. For example:
  + For a column with `dataFields` set as `["avgPrice", "qty"]`, the displayed value updates only when the `avgPrice` or `qty` values in the data object change.
  + For a column with an empty `dataFields` array, the displayed value updates if any values in the data object change.

To manage how the values are displayed in the columns, use the [`formatter`](/charting-library-docs/v29/trading_terminal/account-manager/value-formatters) property.

## Configure behavior[​](#configure-behavior "Direct link to Configure behavior")

### Disable Account Manager[​](#disable-account-manager "Direct link to Disable Account Manager")

The [`accountManagerInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#accountmanagerinfo) method is required for implementation.
However, if you do not want to display the Account Manager,
you can use the sample code from the [Broker API implementation](https://github.com/tradingview/trading_platform/blob/5b6575760cb6d52dc3cedce0009ccb6d16dc85d7/broker-sample/lib/broker.js#L174) and disable the [`trading_account_manager`](/charting-library-docs/v29/customization/Featuresets#trading_account_manager) featureset.

### Hide Account Manager on startup[​](#hide-account-manager-on-startup "Direct link to Hide Account Manager on startup")

By default, the Account Manager is always opened.
If you want to keep it hidden on startup, disable the [`open_account_manager`](/charting-library-docs/v29/customization/Featuresets#open_account_manager) featureset.
The [`getAccountManagerVisibilityMode`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#getaccountmanagervisibilitymode) and [`setAccountManagerVisibilityMode`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setaccountmanagervisibilitymode) methods in the [Trading Host](/charting-library-docs/v29/trading_terminal/trading-concepts/#trading-host) can be used to either get the visibility state of the Account Manager or change it.