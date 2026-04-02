# Connecting Data: Extended sessions

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/Extended-Sessions

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* Extended sessions

On this page

# Extended sessions

An extended session is a period beyond the official trading hours of the exchange when trading still occurs.
The library allows you to display extended sessions for symbols that support them.
Note that extended sessions are only visible on [intraday resolutions](/charting-library-docs/v29/core_concepts/Resolution#resolution-in-minutes-intraday).

The extended session includes regular, pre-market, and post-market subsessions. Either a pre-market or post-market subsession can be missed. When the chart displays an extended session, the subsessions are represented as colored areas.

![A chart showing subsessions](/charting-library-docs/v29/assets/images/subsessions_example-e052f331ca30ee70e105bb3a3ec2f00c.png)

## Enable extended sessions[​](#enable-extended-sessions "Direct link to Enable extended sessions")

To enable extended sessions, do the following:

* Add the [`pre_post_market_sessions`](/charting-library-docs/v29/customization/Featuresets#pre_post_market_sessions) featureset to the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.
* Specify the [`subsession_id`](/charting-library-docs/v29/connecting_data/Symbology#subsession_id) and [`subsessions`](/charting-library-docs/v29/connecting_data/Symbology#subsessions) properties in [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) for symbols that support extended sessions. Refer to the [Configure datafeed](#configure-the-datafeed) section for more information.

### Specify the default session type[​](#specify-the-default-session-type "Direct link to Specify the default session type")

The chart can display regular or extended sessions. To specify the default session type, provide the [`mainSeriesProperties.sessionId`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides#mainseriespropertiessessionid) property within [`overrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#overrides).

```
var widget = window.tvWidget = new TradingView.widget({  
    // ...  
    overrides: {  
        "mainSeriesProperties.sessionId": "extended",  
    }  
});
```

### Specify subsession colors[​](#specify-subsession-colors "Direct link to Specify subsession colors")

Subsessions are represented on the chart as colored areas. You can specify default colors for pre-market and post-market subsessions using the [`overrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#overrides) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

```
var widget = window.tvWidget = new TradingView.widget({  
    // ...  
    overrides: {  
        "backgrounds.preMarket.color": "rgba(200,0,0,0.08)",  
        "backgrounds.postMarket.color": "rgba(0,0,200,0.08)",  
    }  
});
```

To change the colors on the fly, use the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method.

```
widget.applyOverrides({"backgrounds.outOfSession.color": "rgba(0,0,0,0.2)"});  
widget.applyOverrides({"backgrounds.preMarket.color": "rgba(200,0,0,0.08)"});  
widget.applyOverrides({"backgrounds.postMarket.color": "rgba(0,0,200,0.08)"});
```

Users can adjust the subsession colors in the *Chart settings* dialog in the UI.

![A chart showing subsessions](/charting-library-docs/v29/assets/images/session-color-ui-902a2849084ef8090bc262b12dc3c6b2.png)

## Change the session type[​](#change-the-session-type "Direct link to Change the session type")

You can switch between the sessions in the UI or using the API.

### In UI[​](#in-ui "Direct link to In UI")

Users can change the session type in the following ways:

* Use the drop-down menu on the bottom toolbar.

  ![Bottom toolbar extended session button](/charting-library-docs/v29/assets/images/subsessions-bottom-toolbar-d8213b11b0bb0a0aa0bdca70ed5ae4db.png)
* Use the drop-down menu in the *Chart settings* dialog.

  ![Bottom toolbar extended session button](/charting-library-docs/v29/assets/images/subsession-chart-settings-bae4724c8d99d3a00bcf31fdac6bc819.png)

### Using API[​](#using-api "Direct link to Using API")

You can use the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method to change the session type on the fly.

```
widget.applyOverrides({ "mainSeriesProperties.sessionId": "extended" });
```

## Configure the datafeed[​](#configure-the-datafeed "Direct link to Configure the datafeed")

To display extended sessions on the chart, you should provide additional data in [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo).

tip

`LibrarySymbolInfo` is an object that contains information about a certain symbol. You should return this object to the library when it calls the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) method. Refer to [Symbology](/charting-library-docs/v29/connecting_data/Symbology) for more information on how to implement `LibrarySymbolInfo`.

Consider the `LibrarySymbolInfo` object for a symbol that supports a regular session only.

```
{  
    "name": "AAPL",  
    "ticker": "AAPL",  
    "exchange": "NasdaqNM",  
    "timezone": "Etc/UTC",  
    "description": "Apple Inc.",  
    "type": "stock",  
    "pricescale": 100,  
    "minmov": 1,  
    "has_intraday": true,  
    "supported_resolutions": ["60"],  
    "has_daily": false,  
    "intraday_multipliers": ["1"],  
    "format": "price",  
    "session": "0930-1600"  
}
```

If the symbol supports an extended session, you should additionally specify the [`subsession_id`](/charting-library-docs/v29/connecting_data/Symbology#subsession_id) and [`subsessions`](/charting-library-docs/v29/connecting_data/Symbology#subsessions) properties.
The code sample below specifies an extended session that starts at 04:00 and ends at 20:00. It includes a pre-market subsession from 04:00 to 09:30, a regular subsession from 09:30 to 16:00, and a post-market subsession from 16:00 to 20:00.

```
{  
    "name": "AAPL",  
    "ticker": "AAPL",  
    "exchange": "NasdaqNM",  
    "timezone": "Etc/UTC",  
    "description": "Apple Inc.",  
    "type": "stock",  
    "pricescale": 100,  
    "minmov": 1,  
    "has_intraday": true,  
    "supported_resolutions": ["60"],  
    "has_daily": false,  
    "intraday_multipliers": ["1"],  
    "format": "price",  
    "session": "0930-1600",  
    "subsession_id": "regular",  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1600"  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000"  
        },  
        {  
            "description": "Pre-market",  
            "id": "premarket",  
            "session": "0400-0930"  
        },  
        {  
            "description": "Post-market",  
            "id": "postmarket",  
            "session": "1600-2000"  
        }  
    ]  
}
```

Note that the `session` and `subsession_id` values depend on the current session type selected on the chart.
If the session type is changed either [in the UI](#in-ui) or [using the API](#using-api), you should **update** the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.

### Handle session switch[​](#handle-session-switch "Direct link to Handle session switch")

When the session type is changed, the library needs to request all data from scratch.
To do this, the library calls [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) once again with an additional [`SymbolResolveExtension`](/charting-library-docs/v29/api/interfaces/Charting_Library.SymbolResolveExtension) parameter. In `SymbolResolveExtension`, the [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.SymbolResolveExtension#session) property indicates what session type should be displayed on the chart.

In response, you should return the updated [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object with the following properties changed:

* `subsession_id`: the property's value should match the [`SymbolResolveExtension.session`](/charting-library-docs/v29/api/interfaces/Charting_Library.SymbolResolveExtension#session) value. The value is either `"regular"` or `"extended"`.
* `session`: the property's value should match the corresponding [`LibrarySubsessionInfo.session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySubsessionInfo#session) value specified in `subsessions`. For example, if the chart displays `"extended"` session, and for this session type `LibrarySubsessionInfo.session` is `"0400-2000"`, the `LibrarySymbolInfo.session` value should also be `"0400-2000"`.

tip

You can use the following expression to make sure that [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) is correct. The expression should always be `true`:

```
symbolInfo.session === symbolInfo.subsessions.find(x => x.id === subsession_id).session
```

#### Example[​](#example "Direct link to Example")

Consider the example. The current symbol on the chart is `AAPL` and the session type is regular. You should return the following [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object to the library:

```
{  
    "name": "AAPL",  
    "ticker": "AAPL",  
    "exchange": "NasdaqNM",  
    "timezone": "Etc/UTC",  
    "description": "Apple Inc.",  
    "type": "stock",  
    "pricescale": 100,  
    "minmov": 1,  
    "has_intraday": true,  
    "supported_resolutions": ["60"],  
    "has_daily": false,  
    "intraday_multipliers": ["1"],  
    "format": "price",  
    "session": "0930-1600",  
    "subsession_id": "regular",  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1600"  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000"  
        },  
        {  
            "description": "Pre-market",  
            "id": "premarket",  
            "session": "0400-0930"  
        },  
        {  
            "description": "Post-market",  
            "id": "postmarket",  
            "session": "1600-2000"  
        }  
    ]  
}
```

Then, the chart is switched to the extended session. The library calls `resolveSymbol` once again.
In response, you should update the `subsession_id` and `session` properties, so they match the corresponding values defined for the extended session in `subsessions`:

```
{  
    "name": "AAPL",  
    "ticker": "AAPL",  
    "exchange": "NasdaqNM",  
    "timezone": "Etc/UTC",  
    "description": "Apple Inc.",  
    "type": "stock",  
    "pricescale": 100,  
    "minmov": 1,  
    "has_intraday": true,  
    "supported_resolutions": ["60"],  
    "has_daily": false,  
    "intraday_multipliers": ["1"],  
    "format": "price",  
    "session": "0400-2000",      // The value is changed  
    "subsession_id": "extended", // The value is changed  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1600"  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000"  
        },  
        {  
            "description": "Pre-market",  
            "id": "premarket",  
            "session": "0400-0930"  
        },  
        {  
            "description": "Post-market",  
            "id": "postmarket",  
            "session": "1600-2000"  
        }  
    ]  
}
```

### Corrections for extended sessions[​](#corrections-for-extended-sessions "Direct link to Corrections for extended sessions")

Corrections are changes in the default trading session for specific days.
For regular sessions, you should only specify the [`corrections`](/charting-library-docs/v29/connecting_data/Symbology#corrections) property in `LibrarySymbolInfo`.
However, for extended sessions, you should additionally provide [`session-correction`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySubsessionInfo#session-correction) for each subsession in `subsessions`.

For example, you need to display the following sessions:

* Regular. The default regular session starts at 09:30 and ends at 17:00. On 2019‑07‑03, 2019‑11‑29, and 2019‑12‑24, the session starts at 09:30 and ends at 13:00.
* Extended. The default extended session starts at 04:00 and ends at 20:00. On 2019‑07‑03, 2019‑11‑29, and 2019‑12‑24, the session starts at 04:00 and ends at 21:00.
* Pre-market. This session always starts at 04:00 and ends at 09:30.
* Post-market. The default post-market session starts at 17:00 and ends at 20:00. However, on 2019‑07‑03, 2019‑11‑29, and 2019‑12-24, the session time shifts because of the changes in the regular and extended sessions. On these days, the post-market session starts at 13:00 and ends at 21:00.

```
{  
    // ...  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1700",  
            "session-correction": "0930-1300:20190703,20191129,20191224",  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000",  
            "session-correction": "0400-2100:20190703,20191129,20191224",  
        },  
        {  
            "description": "Pre-market",  
            "id": "premarket",  
            "session": "0400-0930",  
        },  
        {  
            "description": "Post-market",  
            "id": "postmarket",  
            "session": "1700-2000",  
            "session-correction": "1300-2100:20190703,20191129,20191224",  
        }  
    ],  
}
```

caution

Time changes in one session may cause changes in the related sessions. Make sure you specify corrections for all sessions that require them to avoid visual bugs.

As mentioned [earlier](#handle-session-switch), you should update the `session` and `session_id` properties in `LibrarySymbolInfo` when the session type is changed.
If you specify corrections, you should also update the `corrections` property.
This property should contain one of the `session-correction` values, depending on the currently selected session type in the UI.
For example, the current type is `"regular"`, therefore, `corrections` is equal to the `session-correction` value specified for the regular session.

```
{  
    // ...  
    "session": "0930-1700",  
    "subsession_id": "regular",  
    "corrections": "0930-1300:20190703,20191129,20191224",  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1700",  
            "session-correction": "0930-1300:20190703,20191129,20191224",  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000",  
            "session-correction": "0400-2100:20190703,20191129,20191224",  
        },  
        // ...  
    ],  
}
```

If the type is changed to `"extended"`, you should update `corrections` to match the `session-correction` value specified for the extended session.

```
{  
    // ...  
    "session": "0400-2000",  
    "subsession_id": "extended",  
    "corrections": "0400-2100:20190703,20191129,20191224",  
    "subsessions": [  
        {  
            "description": "Regular Trading Hours",  
            "id": "regular",  
            "session": "0930-1700",  
            "session-correction": "0930-1300:20190703,20191129,20191224",  
        },  
        {  
            "description": "Extended Trading Hours",  
            "id": "extended",  
            "session": "0400-2000",  
            "session-correction": "0400-2100:20190703,20191129,20191224",  
        },  
        // ...  
    ],  
}
```

## Enable the price line[​](#enable-the-price-line "Direct link to Enable the price line")

info

This feature is only available in [Trading Platform](/charting-library-docs/v29/trading_terminal/) as it requires [quote data](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes).

The library allows you to display pre-/post-market price lines. These lines appear only during the pre-/post-market sessions when the chart shows only the regular session. However, if the chart is set to display the extended session, the lines will not be visible, as the data is already displayed on the chart.

![Pre-marker price line](/charting-library-docs/v29/assets/images/pre-market-line-8964f4aeb954faa6e55ad19813a4a453.png)

To enable the lines, you should do the following:

* Enable the [`pre_post_market_price_line`](/charting-library-docs/v29/customization/Featuresets#pre_post_market_price_line) featureset.
* Provide the [`rtc`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues#rtc) property in the [`DatafeedQuoteValues`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues) object.

You can also display information on the pre-/post-market price in [Details](/charting-library-docs/v29/trading_terminal/#details).
To do this, you should additionally provide the [`rch`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues#rch), [`rchp`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues#rchp), and [`rtc_time`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues#rtc_time) properties in the [`DatafeedQuoteValues`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues) object.

![Pre-market price in Details](/charting-library-docs/v29/assets/images/details-extended-session-8d68147842a9e3b30312cd51e39e07da.png)