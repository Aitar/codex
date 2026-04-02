# Trading Platform: News

Source: https://www.tradingview.com/charting-library-docs/v29/trading_terminal/news/

* [Trading Platform](/charting-library-docs/v29/trading_terminal/)* News

On this page

# News

## Overview[​](#overview "Direct link to Overview")

The **News** widget allows you to displays latest news on a symbol, exchange, or symbol type.

![News widget](/charting-library-docs/v29/assets/images/top-news-widget-b6bc192e3b24e18921460e92c4218107.png)

## Enable the widget[​](#enable-the-widget "Direct link to Enable the widget")

info

The *News* widget requires quote data.
Therefore, you need to implement the [`getQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#getquotes), [`subscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribequotes), and [`unsubscribeQuotes`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#unsubscribequotes) methods within your [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/).

The [`widgetbar`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#widgetbar) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) allows managing the widget panel, including the *News* widget. To enable the widget, set the [`news`](/charting-library-docs/v29/api/interfaces/Charting_Library.WidgetBarParams#news) property to `true`.

```
const widget = new TradingView.widget({  
    container: "chartContainer",  
    locale: "en",  
    library_path: "charting_library/",  
    datafeed: datafeed,  
    symbol: "AAPL",  
    interval: "1D",  
    widgetbar: {  
        news: true,  
    },  
})
```

## Connect news[​](#connect-news "Direct link to Connect news")

The library does not contain any built-in news providers. Therefore, you should connect a [RSS feed](#rss-feed) or your own [news source](#custom-news-source) using the [`rss_news_feed`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#rss_news_feed) or [`news_provider`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#news_provider) properties, respectively.

info

If both `news_provider` and `rss_news_feed` properties are specified, `rss_news_feed` is ignored.

### RSS feed[​](#rss-feed "Direct link to RSS feed")

Use the [`rss_news_feed`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#rss_news_feed) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to connect RSS feeds to the library. To do this, specify a [`RssNewsFeedParams`](/charting-library-docs/v29/api/interfaces/Charting_Library.RssNewsFeedParams) object that should contain at least the default RSS configuration.
For each configuration, provide the following properties:

* [`url`](/charting-library-docs/v29/api/interfaces/Charting_Library.RssNewsFeedInfo#url) — a URL that the library should request. The URL can contain tags in curly brackets, such as `{SYMBOL}`, `{TYPE}`, or `{EXCHANGE}`, that the library replaces with values.
* [`name`](/charting-library-docs/v29/api/interfaces/Charting_Library.RssNewsFeedInfo#name) — a feed name that is displayed underneath the news.

```
rss_news_feed: {  
    "default": {  
        url: "https://articlefeeds.nasdaq.com/nasdaq/symbols?symbol={SYMBOL}",  
        name: "NASDAQ"  
    }  
}
```

You can specify a different RSS for each symbol type or use only one for all symbols. The names of the properties should match the symbol types.

```
rss_news_feed: {  
    "default": {  
        url: "https://articlefeeds.nasdaq.com/nasdaq/symbols?symbol={SYMBOL}",  
        name: "NASDAQ"  
    },  
    "stock": {  
        url: "http://feeds.finance.yahoo.com/rss/2.0/headline?s={SYMBOL}&region=US⟨=en-US",  
        name: "Yahoo Finance"  
    }  
}
```

### Custom news source[​](#custom-news-source "Direct link to Custom news source")

You should implement [`GetNewsFunction`](/charting-library-docs/v29/api/modules/Charting_Library#getnewsfunction) and assign it to the [`news_provider`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#news_provider) property to connect any custom news source to the library.
The library calls this function to request data for the widget. In response, you should pass a [`GetNewsResponse`](/charting-library-docs/v29/api/interfaces/Charting_Library.GetNewsResponse) object to the callback function. In this object, specify an array of [`newsItem`](/charting-library-docs/v29/api/interfaces/Charting_Library.NewsItem) objects that contain data for each news item.

```
const widget = new TradingView.widget({  
    news_provider: function getNews(symbol, callback) {  
        const newsItems = [  
            {  
                title: "Title 1",  
                source: "Source Name",  
                published: new Date("2023-12-20 12:34").valueOf(),  
                shortDescription: "Hello World, Article 1.",  
            },  
            {  
                title: "Title 2",  
                source: "Source Name",  
                published: new Date("2023-12-19 12:34").valueOf(),  
                shortDescription: "Hello World, Article 2.",  
            },  
        ];  
        callback({  
            title: "Latest News Stories",  
            newsItems,  
        });  
    },  
});
```

You can specify a URL to the external source in the [`link`](/charting-library-docs/v29/api/interfaces/Charting_Library.NewsItem#link) property of `newsItem`.
This link is opened in a pop-up dialog when a user clicks on the corresponding news item. If `link` is not provided, the information from the [`fullDescription`](/charting-library-docs/v29/api/interfaces/Charting_Library.NewsItem#fulldescription) property is displayed instead.

```
const newsItems = [  
    {  
        // ..  
        link: "https://www.example.com/test",  
    },  
]
```

To request news from scratch, for example, when an event occurs, call the [`refresh`](/charting-library-docs/v29/api/interfaces/Charting_Library.INewsApi#refresh) method from `INewsApi`, which can be retrieved with the [`news`](/charting-library-docs/v29/core_concepts/widget-methods#news) method.

```
const widget = new TradingView.widget({  
    // Widget options  
});  
  
async function someEventHandler() {  
    const newsApi = await widget.news();  
    newsApi.refresh();  
}
```