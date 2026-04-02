# Getting Started: Best Practices

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/Best-Practices

* [Getting Started](/charting-library-docs/v29/getting_started/)* Best Practices

On this page

# Best Practices

This article describes the best practices for integrating the library into your website or mobile application.

## Separate Additional Features from the Library[​](#separate-additional-features-from-the-library "Direct link to Separate Additional Features from the Library")

The library is used to display charts, prices, and technical analysis tools. You can find a list of included features in the [Key features](/charting-library-docs/v29/getting_started/Key-Features) article.

If you need additional features like chats, special symbol lists, hot deals, advertisements, etc., you should implement them outside of the library. You can still integrate them to the library using the [API](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi).

## Choose an Appropriate Data Connection Approach[​](#choose-an-appropriate-data-connection-approach "Direct link to Choose an Appropriate Data Connection Approach")

Pay attention to the differences between implementing a datafeed in JavaScript via the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) and using the predefined implementation with a server that responds in the [UDF](/charting-library-docs/v29/connecting_data/UDF) format. Refer to the following topic for more information: [Connecting Data](/charting-library-docs/v29/connecting_data/).
If you need really fast data updates or data streaming, you can use WebSockets.

## Provide Correct Amount of Data[​](#provide-correct-amount-of-data "Direct link to Provide Correct Amount of Data")

Most issues with the library appear because data is provided incorrectly. Consider the following topic for more information: [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#correct-amount-of-data). Note that when you specify [Marks](/charting-library-docs/v29/ui_elements/Marks), you should provide data that matches the requested range.

## Consider the Chart's Size[​](#consider-the-charts-size "Direct link to Consider the Chart's Size")

The smallest meaningful size that the library supports is 500×500 px. Avoid making charts smaller because they look messy. We recommend that you hide some UI elements if you need charts smaller than those mentioned above. Refer to the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor#chart-size) topic for more information on how to specify the chart's size.

## Localize Your Chart[​](#localize-your-chart "Direct link to Localize Your Chart")

The library [supports a variety of languages](/charting-library-docs/v29/core_concepts/Localization). Use the one that fits your users' needs.

## Enable Debug Logs during Development[​](#enable-debug-logs-during-development "Direct link to Enable Debug Logs during Development")

Set the [`debug`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#debug) property to `true` in [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to enable logs. We recommend that you enable the debug mode during the development and disable this mode in the production to speed up the code execution.

## If You Face Issues[​](#if-you-face-issues "Direct link to If You Face Issues")

First, you should [update](/charting-library-docs/v29/releases/Update-Library) your library's build to the latest version. If the issues still appear, the steps below can help you to debug them:

1. Set the [`debug`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#debug) property to `true` in Widget Constructor to enable logs.
2. Check that you [provide data correctly](#provide-correct-amount-of-data). Pay special attention to [symbology](/charting-library-docs/v29/connecting_data/Symbology) as it is the most common place to make a mistake.
3. Review the output of our [demo data service](https://demo_feed.tradingview.com/quotes?symbols=AAPL) and compare this output to yours to ensure your backend behaves correctly.

You can also search your issue among the [GitHub Issues](https://github.com/tradingview/charting_library/issues "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) and the [Discord discussions](https://discord.gg/UC7cGkvn4U).

## Avoid Using Undocumented Features[​](#avoid-using-undocumented-features "Direct link to Avoid Using Undocumented Features")

All features that are not mentioned in the documentation are subject to change without any warnings and backward compatibility. Also, altering the source code is strictly prohibited by the legal agreement you signed.

## Avoid Using Demo Datafeed on a Production Website[​](#avoid-using-demo-datafeed-on-a-production-website "Direct link to Avoid Using Demo Datafeed on a Production Website")

The demo datafeed is not designed for real usage. It might be unstable and cannot withstand high loads.

## Speed Up Load Times[​](#speed-up-load-times "Direct link to Speed Up Load Times")

We recommend that you use the following protocols to speed up load times:

* HTTP/2 or higher
* TLS 1.3 or higher

Also, you can compress the library's HTML files using Gzip or Brotli when sending them to a client.

## Set Minimum Expiration Time for charting\_library.js[​](#set-minimum-expiration-time-for-charting_libraryjs "Direct link to Set Minimum Expiration Time for charting_library.js")

All files in the library contain hash in their names except `charting_library.js` that you add to your HTML files.
When you update the library to a newer version, all file names are changed as well.
If a browser loads `charting_library.js` from the cache, then all the links in this file are broken.
The expiration time for this file should be set to the minimum to prevent its caching.