# Trading Platform: Watchlist

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/Watch-List

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* Watchlist

On this page

# Watchlist

## Overview[​](#overview "Direct link to Overview")

The **Watchlist** is a widget that allows users to track price movements and volume of specific financial instruments in real-time.
Watchlists also allow users to quickly switch between the symbols.
The Watchlist widget is displayed on the widget panel on the right side of the chart.

![Watchlist widget](/charting-library-docs/v29/assets/images/watchlist-165bfd72ff76eb3666c7c5c295071e2a.png)

Users can manage their lists through the UI.
For example, they can create new lists, modify existing ones, export active lists, and perform other actions.
You can also programmatically manage user lists using the [Watchlist API](#watchlist-api).

![Watchlist widget menu](/charting-library-docs/v29/assets/images/watchlist-menu-4ef54c21a79245e381e56bfac01ebc86.png)

## Enable the widget[​](#enable-the-widget "Direct link to Enable the widget")

info

The Watchlist widget requires quote data.
Therefore, you need to implement the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes), [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes), and [`unsubscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#unsubscribequotes) methods within your Datafeed API.

The [`widgetbar`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#widgetbar) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) allows managing the widget panel, including the Watchlist widget.
To enable the widget, set the [`watchlist`](/charting-library-docs/v29/api/interfaces/Charting_Library.WidgetBarParams#watchlist) property to `true`.
You can also select the default symbols for the default watchlist and make it read-only using the [`watchlist_settings`](/charting-library-docs/v29/api/interfaces/Charting_Library.WidgetBarParams#watchlist_settings) property.

```
const datafeed = new Datafeeds.UDFCompatibleDatafeed("https://demo-feed-data.tradingview.com");  
new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    widgetbar: {  
        watchlist: true,  
        watchlist_settings: {  
            default_symbols: ["AAPL", "IBM", "MSFT"],  
            readonly: true,  
        },  
    },  
})
```

## Watchlist API[​](#watchlist-api "Direct link to Watchlist API")

The Watchlist API provides extensive ways to interact with watchlists.
For example, you can modify watchlist values on the fly or subscribe to events to keep track of user watchlists.

Use the [`watchList`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#watchlist) method to retrieve the [`IWatchListApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi) object for interacting with the watchlist.

```
const watchlistApi = await widget.watchList();  // Get the Watchlist API
```

Watchlist items should be symbol names that your datafeed [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method can resolve.
This means that generally shorter names such as `AAPL` can be used if your datafeed understands it.
However, it is recommended that you provide the symbol names as they appear within the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object,
for example, `NASDAQ:AAPL`.

### Create multiple watchlists[​](#create-multiple-watchlists "Direct link to Create multiple watchlists")

You cannot instantiate the widget with multiple watchlists directly from the Widget Constructor.
Instead, you should use the API to create multiple watchlists.
The code sample below shows how to create lists with and without specific items.

```
const watchlistApi = await widget.watchList(); // Get the Watchlist API  
const firstList = watchlistApi.createList("First list"); // Create a new empty list  
const secondList = watchlistApi.createList("Second list", ["AMZN", "ADBE"]); // Create another list with items
```

### Retrieve watchlist data[​](#retrieve-watchlist-data "Direct link to Retrieve watchlist data")

Use the [`getAllLists`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#getalllists) method to get all watchlists' data such as their IDs, titles, and symbol IDs.

```
const watchlistApi = await widget.watchList(); // Get the Watchlist API  
watchlistApi.getAllLists();
```

This method returns an instance of the `WatchListSymbolListMap` interface that contains watchlists' IDs and the corresponding [`WatchListSymbolList`](/charting-library-docs/v29/api/interfaces/Charting_Library.WatchListSymbolList) objects.

```
{  
   "id123456789": {  
      "id": "id123456789",  
      "symbols": [  
         "###TOP SECTION",  
         "AAPL",  
         "IBM",  
         "###SECOND SECTION",  
         "MSFT",  
         "###NEW SECTION",  
         "AMZN"  
      ],  
      "title": "Watchlist"  
   },  
   "id987654321": {  
      "id": "id987654321",  
      "symbols": [  
         "MSFT",  
         "ADBE",  
         "AMZN"  
      ],  
      "title": "My list"  
   }  
}
```

You can also call the [`getActiveListId`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#getactivelistid) method to get an ID of the active watchlist.

## Add sections[​](#add-sections "Direct link to Add sections")

The more symbols users add, the more difficult it becomes to manage and navigate the list.
Sections in watchlists help users organize their lists more effectively.
Sections can be named, moved, and deleted.

You can also programmatically add sections to watchlists using sections dividers.
Any list item that has the `###` prefix is considered a section divider.

* Adding sections to the default watchlist within the [Widget Constructor](#enable-the-widget).

  ```
  widgetbar: {  
      watchlist: true,  
      watchlist_settings: {  
          default_symbols: ["###TOP SECTION", "AAPL", "IBM", "###SECOND SECTION", "MSFT"],  
          readonly: true,  
      },  
  },
  ```
* Adding sections with items to a new and existing watchlist using [API](#watchlist-api).

  ```
  // Create new watchlist with a section and items  
  const watchlistApi = await widget.watchList();  
  const mySymbolList = watchlistApi.createList("My new list", ["###TEST SECTION", "AMZN", "ADBE"]);  
    
  // Add new section and item to the active watchlist  
  const activeListId = watchlistApi.getActiveListId();  
  const activeListItems = watchlistApi.getList(activeListId);  
  watchlistApi.updateList(activeListId, [...activeListItems, "###NEW TEST SECTION", "AAPL", "MSFT"]);
  ```

## Store watchlist items[​](#store-watchlist-items "Direct link to Store watchlist items")

Watchlist items are saved as part of the [user settings](/charting-library-docs/v29/saving_loading/user-settings).
By default, user settings are saved into the browser's [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage),
but you can also save them using [`settings_adapter`](/charting-library-docs/v29/saving_loading/user-settings#settings-adapter) in your preferred storage.

If you want to store watchlist items separately from other settings,
you can implement your logic to store the watchlist data on your server.
You can use the `IWatchListApi` methods such as [`onListAdded`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#onlistadded), [`onListChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#onlistchanged), [`onListRemoved`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#onlistremoved), and [`onListRenamed`](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchListApi#onlistrenamed)
to know when something has changed and you should save it.

## Display logos[​](#display-logos "Direct link to Display logos")

If you want to display logos for symbols within the Watchlist widget, follow the steps below:

1. Add the [`show_symbol_logos`](/charting-library-docs/v29/customization/Featuresets#show_symbol_logos) featureset to the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.
2. Provide URLs for symbols in the [`logo_urls`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#logo_urls) property of the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
   Pass the object as a parameter to the callback of the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method.
3. Implement the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes), [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes), and [`unsubscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#unsubscribequotes) methods within your Datafeed API.