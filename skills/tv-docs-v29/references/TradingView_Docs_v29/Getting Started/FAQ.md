# Getting Started: FAQ

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/Frequently-Asked-Questions

* [Getting Started](/charting-library-docs/v29/getting_started/)* FAQ

On this page

# Frequently Asked Questions

If your question is not outlined below, you can ask it on [GitHub Issues](https://github.com/tradingview/charting_library/issues "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) or join the [Discord discussions](https://discord.gg/UC7cGkvn4U).

## Data Management[​](#data-management "Direct link to Data Management")

**1. How do I connect my data? How to add new symbols?**

Refer to the following articles for information on how to connect data:

* [Connecting Data](/charting-library-docs/v29/connecting_data/)
* [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/)
* [UDF](/charting-library-docs/v29/connecting_data/UDF)

Also, consider the [Datafeed: Common Issues](/charting-library-docs/v29/connecting_data/Datafeed-Issues) article to avoid typical errors when implementing the Datafeed API.

Use the [Demo Chart](https://charting-library.tradingview-widget.com) to investigate how the library processes data. Open the Network tab in a browser console and filter requests by `demo-feed` to see all data requests and responses.

**2. Do you have an example of the Datafeed API implementation?**

You can consider [UDF Adapter](https://github.com/tradingview/charting_library/tree/master/datafeeds/udf "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) as an example of the Datafeed API implementation.

If you need a step-by-step guide, refer to the [How to connect data via Datafeed API](/charting-library-docs/v29/tutorials/implement_datafeed_tutorial/) tutorial.

**3. Do you have an example of a WebSocket data transport?**

The [How to connect data via Datafeed API](/charting-library-docs/v29/tutorials/implement_datafeed_tutorial/) tutorial shows how to stream data using WebSocket.

**4. Do you have an example of a backend datafeed in ASP.NET, Python, PHP, etc. ?**

The only example of a backend datafeed that we have is written in JavaScript for Node.js. For more information, refer to the [yahoo\_datafeed](https://github.com/tradingview/yahoo_datafeed) repository.

**5. How can I display data stored in a TXT/CSV/XLSX file?**

The library is intended to display data from a server, not a file. You should also keep in mind that according to the license agreement you can use the library on public websites only. If you still want to use a file as a data source, complete the following steps:

1. Write an application using any server language (.NET, PHP, Node.js, Python, etc.). This application should read a file and transfer data from it in the [UDF](/charting-library-docs/v29/connecting_data/UDF) format over HTTP(S).

   Note: You can provide data in another format or use a WebSocket to transfer it, but in this case you need a custom [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) implementation.
2. Make sure a browser can send requests to your server. For this, you should either have a static IP or register a domain.
3. Open `index.html` and replace `demo_feed.tradingview.com` with the URL to your server.

**6. Why my data is not displayed / displayed incorrectly / incorrectly fetched from the server?**

The first thing you should do to debug any issue is to [enable console logs](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#debug). These logs contain the most important actions performed in the library. You can also refer to the [Datafeed: Common Issues](/charting-library-docs/v29/connecting_data/Datafeed-Issues) article that might answer your question.

Note that most data issues occur because symbol information is set incorrectly. To avoid these issues, consider [Symbology](/charting-library-docs/v29/connecting_data/Symbology).

**7. The library is constantly asking for data. How to tell it that the data is over?**

To do this, you should use a flag that notifies the library that there is no more data on the server. Set the status code to `no_data` or the [`noData`](/charting-library-docs/v29/api/interfaces/Charting_Library.HistoryMetadata#nodata) property to `true` if you use [UDF](/charting-library-docs/v29/connecting_data/UDF#bars) or [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#correct-amount-of-data), respectively.

**8. How to change the number of decimal places for prices on the chart?**

The number of decimal places depends on the [`pricescale`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#pricescale) value. For more information on the price format, refer to the [Symbology](/charting-library-docs/v29/connecting_data/Symbology#price-format) article.

**9. What if I have a single price for each timestamp?**

Since the library is intended to display multiple data types like candles, bars, and histograms, you are supposed to provide Open, High, Low, Close, and optional Volume for each timestamp. If you have a single price for each timestamp, you can pass `Open = High = Low = Close = price`. For better data visualization, you can change the default chart style to “Line” (refer to the [GUI](#gui) section).

**10. Why is `unsubscribeBars` called with a delay?**

This is intentional.

Refer to the [`unsubscribeBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#unsubscribebars) method for more information.

**11. How to specify time properties within the library?**

All time properties should be [Unix timestamps](https://developer.mozilla.org/en-US/docs/Glossary/Unix_time) in **seconds** unless otherwise stated. For example, the code sample below specifies boundary values of a time range.

```
const from = Date.now() / 1000 - 500 * 24 * 3600; // 500 days ago  
const to = Date.now() / 1000;
```

**12. Does the library support the FIX protocol?**

Advanced Charts / Trading Platform is a browser-based client-side solution. You can implement your backend data connection with any instruments, including the FIX protocol, based on your requirements. However, the library does not provide any pre-made data integrations with the FIX protocol.

The diagram below illustrates the data connection layers. You should integrate the FIX protocol between your backend and the data provider.

[![Diagram illustrating data connection layers](/charting-library-docs/v29/img/diagram-fix-protocol.svg)![Diagram illustrating data connection layers](/charting-library-docs/v29/img/diagram-fix-protocol-dark.svg)](/charting-library-docs/v29/img/diagram-fix-protocol.svg)

## GUI[​](#gui "Direct link to GUI")

**1. How can I subscribe to chart events?**

You can subscribe to chart events in two ways:

* Subscribe to [general](/charting-library-docs/v29/core_concepts/widget-methods#subscribe--unsubscribe) events that are related to a whole chart layout, not a specific chart.
* Subscribe to events that are related to a [single](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#methods) chart such as [`isSelectBarRequested`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#isselectbarrequested).

Some methods that expose events only allow a subscription to be created by passing a single callback function, others return a [Subscription](/charting-library-docs/v29/api/interfaces/Broker.ISubscription) object that can be used to subscribe and unsubscribe.

**2. How to change the default bar style?**

You can use the [`mainSeriesProperties.style`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides#mainseriespropertiesstyle) property to customize bar style.
Refer to the [Chart Overrides](/charting-library-docs/v29/customization/overrides/chart-overrides#chart-styles) article for information.

**3. How to customize the chart style?**

The library provides extensive customization options through multiple APIs.
Refer to the [Customization](/charting-library-docs/v29/customization/) section for more information.

**4. How can I change the list of resolutions (time intervals) on the chart / disable them?**

Refer to the [Resolution](/charting-library-docs/v29/core_concepts/Resolution#configure-resolutions-in-datafeed) article for more information.

**5. How to enable the resolution in seconds?**

Refer to the [Resolution in seconds](/charting-library-docs/v29/core_concepts/Resolution#resolution-in-seconds) section for more information.

**6. How to hide a GUI element (symbol, interval, button, etc.)?**

Most of GUI elements can be hidden using [featuresets](/charting-library-docs/v29/customization/Featuresets). There are base elements that cannot be hidden, but if you still want to get rid of them, you can use [CSS customization](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_css_url). Note that names, classes, and identifiers of the DOM elements may be changed in the next versions of the product without any notifications.

**7. How to disable the built-in Account Manager or Order Ticket?**

Use the [`trading_account_manager`](/charting-library-docs/v29/customization/Featuresets#trading_account_manager) or [`order_panel`](/charting-library-docs/v29/customization/Featuresets#order_panel) featureset to disable the built-in Account Manager or Order Ticket, respectively. For detailed guide on each component, refer to the dedicated section:

* [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/#disable-account-manager)
* [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket#implement-custom-order-ticket)

If you want to implement a custom component instead, you can still use the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api) to populate this component with data.

**8. Why do the Buy/Sell buttons not work?**

The *Buy/Sell* buttons may appear inactive or non-working for several reasons.

* **Buttons are not visible at all.** Make sure you are using the [Trading Platform](/charting-library-docs/v29/trading_terminal/), as the *Buy/Sell* buttons are only available there. Additionally, check the UI setting under *Settings → Trading → Buy/Sell buttons* and ensure the checkbox is enabled. If this setting is turned off, the buttons will not appear on the chart.
* **Buttons are disabled.** Ensure that the [`isTradable`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#istradable) method returns `true` for tradable symbols. Without this method, the buttons remain disabled.
* **Buttons are enabled but show no prices.** Implement the [`symbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#symbolinfo) method to provide the required symbol data. Without it, the buttons will not display bid/ask prices.
* **Clicking buttons doesn't place orders**. Implement [`placeOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#placeorder) and other required methods of the Broker API.
* **Prices in buttons are not updating.** To show real-time bid/ask prices in the buttons, implement the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes) method.

**9. Can I add custom buttons to areas of the UI other than the top toolbar?**

Custom buttons created with [`createButton`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#createbutton) and [`createDropdown`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#createdropdown) can only be added to the [top toolbar](/charting-library-docs/v29/ui_elements/#top-toolbar).
However, there are other ways to customize the UI: you can add extra buttons to the [context menu](/charting-library-docs/v29/ui_elements/context-menu) and [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket),
or [modify other elements](/charting-library-docs/v29/customization/) to tailor the interface to your needs.

**10. Why an indicator is not plotted when the resolution is changed?**

Indicators, such as *VWAP* and *Pivot Points*, use extensive historical data to calculate their values and may need more bars than are visible on the chart.
These indicators are plotted only after the library gets all required data.

The library does not prefetch all data to avoid excessive requests.
Therefore, when the resolution is changed, users need to scroll the chart for the indicator to appear.

## Localization[​](#localization "Direct link to Localization")

**1. What languages does the library support? How can I add the language that is not supported?**

The library supports a variety of languages.
You can find the complete list in the [Localization](/charting-library-docs/v29/core_concepts/Localization#supported-languages) article.
Note that it is impossible to add your own language support.

**2. Could you provide the list of all UI strings so I can translate them?**

We cannot provide the list of UI strings.
However, if you want to add custom translations,
you can use the [`custom_translate_function`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_translate_function) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

## Other Questions[​](#other-questions "Direct link to Other Questions")

**1. What is the difference between Widget, Advanced Charts, and Trading Platform?**

* [Widget](https://tradingview.com/widget/) is connected to the TradingView data. Perfect for websites, blogs, and forums where you need a fast & free solution.

  Integration is simply copying & pasting pre-made iframe code. Widget has lots of display modes.
* [Advanced Charts](https://www.tradingview.com/HTML5-stock-forex-bitcoin-charting-library/) is a chart with your data.

  This is a standalone solution that you download, host on your servers, and connect your data to. You can use it in your site/app for free.
* [Trading Platform](https://www.tradingview.com/HTML5-stock-forex-bitcoin-charting-library/?feature=charting-and-trading-platform) is a standalone product that is licensed to brokers.

  It contains all features available in Advanced Charts and also includes trading functionality, multiple-chart layouts, watchlists, details, news widgets, and other advanced tools. Trading Platform has its own licensing fees associated with it.

**2. Does TradingView have access to any user data through the integration?**

No, TradingView does not collect any user data.
Advanced Charts and Trading Platform are self-hosted solutions that run independently on your servers, ensuring there is no interaction with TradingView on user data.

**3. Is there a way to see detailed logs when working with the library?**

Yes, you can enable debug modes that provide detailed logs for data connection and trading features.
For more information, refer to [How to enable debug mode](/charting-library-docs/v29/tutorials/enable-debug-mode).

**4. What should I do if I encounter a bug while using the library?**

If you come across a bug or issue while using the library, we recommend taking the following steps:

1. **Check for updates**.
   Ensure that you are using the latest version of the library.
   Sometimes, bugs are resolved in newer releases.
   If you are not using the most recent version, [update the library](/charting-library-docs/v29/releases/Update-Library) before proceeding further.
2. **Reproduce the bug**.
   After updating to the latest version, attempt to replicate the bug.
   This step helps determine whether the issue persists in the updated version.
3. **Report the issue**.
   If the bug persists even after updating to the latest version,
   report it in [GitHub issues](https://github.com/tradingview/charting_library/issues) 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")).
   Provide detailed information about the issue, including steps to reproduce it, the library version, console logs, and any error messages encountered.
   This allows us to investigate and address the issue promptly.

**5. Is it possible to reduce the size of the library?**

Yes. You can remove locales from the [bundle file](/charting-library-docs/v29/getting_started/Package-Content#package-content) if your app does not support them.

**6. How do I add a custom indicator?**

Refer to [Custom indicators](/charting-library-docs/v29/custom_studies/) for more information.

**7. Does the library support Rocket Loader by Cloudflare?**

No, it does not. Please avoid using Rocket Loader.

**8. Do you provide iOS or Android SDKs like you do for Lightweight Charts?**

No, not currently.
However, we have a collection of [integration examples](/charting-library-docs/v29/tutorials/#framework-integrations) for frameworks commonly used with Advanced Charts and Trading Platform.
You can check the following examples:

* [iOS WKWebView in Swift](https://github.com/tradingview/charting-library-examples/tree/master/ios-swift)
* [Android WebView](https://github.com/tradingview/charting-library-examples/tree/master/android)
* [React Native for iOS and Android](https://github.com/tradingview/charting-library-examples/tree/master/react-native)

**9. How to integrate the library with Flutter?**

We do not have an example for integrating the library with Flutter currently. You can consider the [How to Build a Native Communication Bridge in Flutter with WebView and JavaScript](https://www.freecodecamp.org/news/how-to-build-a-native-communication-bridge-in-flutter-with-webview-and-javascript/) article that explains how to use Flutter with WebView and JavaScript.

**10. How to switch from Advanced Charts to Trading Platform?**

Refer to the [How to migrate from Advanced Charts](/charting-library-docs/v29/trading_terminal/#how-to-migrate-from-advanced-charts) topic for more information.

**11. Is it possible to use Pine Script® for creating and editing indicators?**

[Pine Script®](https://www.tradingview.com/pine-script-docs/) is not supported in Advanced Charts or Trading Platform. Alternatively, you can create your custom indicator using JavaScript. For more information, refer to [Custom indicators](/charting-library-docs/v29/custom_studies/).

**12. Why Advanced Charts / Trading Platform differs from tradingview.com?**

Some features and parts of the UI in the libraries may differ from those on [tradingview.com](https://www.tradingview.com/chart/). Since Advanced Charts and Trading Platform are client-side solutions, they do not support features that rely on server-side logic. Refer to the [Unsupported features](/charting-library-docs/v29/getting_started/Key-Features#unsupported-features) section for more information.

Also, the libraries and the website are updated at different frequency, therefore, new features on [tradingview.com](https://www.tradingview.com/chart/) may not be available in the libraries.

**13. Does Advanced Charts / Trading Platform support Alerts, Range Bars, Bar Replay Tool, and patterns?**

Some features that are available on [tradingview.com](https://www.tradingview.com/chart/) are not supported in the libraries, including Alerts, Range Bars, Bar Replay Tool, and patterns. Refer to the [Unsupported features](/charting-library-docs/v29/getting_started/Key-Features#unsupported-features) section for more information.

**14. Why do I get error messages mentioning CSP or blob?** 

Content Security Policy (CSP) is a web security standard that helps prevent various types of attacks.
CSP defines a policy specifying which domains are considered trusted sources for content such as scripts, images, fonts, and other resources.

The error message may look like the following:

```
Refused to load the image <URL>' because it violates the following Content Security Policy directive: "img-src 'self' blob data
```

Depending on your use cases, implementation, browser compatibility, or internal company policies, you may encounter issues with some library features. These could include displaying screenshots, logos, or using emojis/icons within the chart.

We encourage you to properly assess the situation and choose the appropriate solution by reading the [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) article.

When changing CSP is not allowed, you can enable the [`iframe_loading_compatibility_mode`](/charting-library-docs/v29/customization/Featuresets#iframe_loading_compatibility_mode) featureset. This featureset will instead use `about:blank` as the source URL and build the iframe HTML using `document.write`.

The blob method is the preferred approach but this featureset offers a fallback for non-standard applications.

**15. Does the library set cookies?**

The library does not set any cookies.

If necessary, you can add your own cookies via server responses and restrict access to specific files, pages, or content based on the cookies set in the user's request.