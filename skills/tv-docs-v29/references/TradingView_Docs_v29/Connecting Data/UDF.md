# Connecting Data: UDF

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/UDF

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* UDF

On this page

# UDF

## What is UDF[​](#what-is-udf "Direct link to What is UDF")

It's a predefined Datafeed API adapter that uses an HTTP-based UDF protocol designed to deliver data to the library in a simple and efficient way.

tip

This predefined adapter is an example implementation of the JS API. You are not required to implement your datafeed using UDF.

## How to start[​](#how-to-start "Direct link to How to start")

You should create a server-side HTTP service that gets the data from your storage and responds to library requests.

## Response-as-a-table concept[​](#response-as-a-table-concept "Direct link to Response-as-a-table concept")

Think of data feed responses as tables. For example, a data feed response that includes a symbol list from the exchange may be treated as a table where each symbol represents a row, along with some columns (minimal\_price\_movement, description, has\_intraday e.t.c.).
Each column may be an array (it will provide a separate value for each row in a table).
Note that there might be a situation when all rows have the same value in the same column.
In this case, the column value can be defined as a single value in JSON response.

Example:

Let's assume that we requested a symbol list from the New York Stock Exchange. The response (in pseudo-format) might look like

```
{  
   symbols: ["MSFT", "AAPL", "FB", "GOOG"],  
   min_price_move: 0.1,  
   description: ["Microsoft corp.", "Apple Inc", "Facebook", "Google"]  
}
```

Here is how this response will look like in a table format.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Symbol min\_price\_move Description|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | MSFT 0.1 Microsoft corp.|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | AAPL 0.1 Apple Inc|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | FB 0.1 Facebook|  |  |  | | --- | --- | --- | | GOOG 0.1 Google | | | | | | | | | | | | | | |

## API Calls[​](#api-calls "Direct link to API Calls")

### Data feed configuration data[​](#data-feed-configuration-data "Direct link to Data feed configuration data")

Request: `GET /config`

Response: The library expects to receive a JSON response of the same structure as a result of Datafeed API [onReady() call](/charting-library-docs/v29/api/interfaces/Charting_Library.IExternalDatafeed#onready).

Also there should be 2 additional properties:

* `supports_search`: Set it to `true` if your data feed supports symbol search and individual symbol resolve logic.
* `supports_group_request`: Set it to `true` if your data feed provides full information on symbol group only and is not able to perform symbol search or individual symbol resolve.

Either `supports_search` or `supports_group_request` should be set to `true`.

**Note:** if your data feed doesn't implement this call (doesn't respond or sends 404 error) then the default configuration is being used. Here is the default configuration:

```
{  
    supported_resolutions: ['1', '5', '15', '30', '60', '1D', '1W', '1M'],  
    supports_group_request: true,  
    supports_marks: false,  
    supports_search: false,  
    supports_timescale_marks: false,  
}
```

### Symbol group request[​](#symbol-group-request "Direct link to Symbol group request")

Request: `GET /symbol_info?group=<group_name>`

* `group_name`: string

Example: `GET /symbol_info?group=NYSE`

Response: Response is expected to be an object with properties listed below.
Each property is treated as table column, as described above (see [response-as-a-table](/charting-library-docs/v29/connecting_data/UDF#response-as-a-table-concept)).
The response structure is similar (but **not equal**) to [SymbolInfo](/charting-library-docs/v29/connecting_data/Symbology). Therefore, you should read the description of each field to learn about the details.

* `symbol`
* `description`
* `exchange-listed` / `exchange-traded`
* `minmovement`
* `minmovement2`
* `fractional`
* `pricescale`
* `has-intraday`
* `visible-plots-set`
* `type`
* `ticker`
* `timezone`
* `session-regular` (mapped to `SymbolInfo.session`)
* `session-holidays`
* `corrections`
* `supported-resolutions`
* `force-session-rebuild`
* `has-daily`
* `intraday-multipliers`
* `volume_precision`
* `has-weekly-and-monthly`
* `has-empty-bars`

Here is an example of data feed response to `GET /symbol_info?group=NYSE` request:

```
{  
   symbol: ["AAPL", "MSFT", "SPX"],  
   description: ["Apple Inc", "Microsoft corp", "S&P 500 index"],  
   exchange-listed: "NYSE",  
   exchange-traded: "NYSE",  
   minmovement: 1,  
   minmovement2: 0,  
   pricescale: [1, 1, 100],  
   has-dwm: true,  
   has-intraday: true,  
   type: ["stock", "stock", "index"],  
   ticker: ["AAPL~0", "MSFT~0", "$SPX500"],  
   timezone: “America/New_York”,  
   session-regular: “0900-1600”,  
}
```

**Notes:**

1. This call will be used if your data feed sent `supports_group_request: true` in the configuration data or didn't respond to the configuration request at all.
2. In the event that your data feed does not support the requested symbol group (which should not happen if your response to request #1 (supported groups) is correct) you may expect a 404 error.
3. When using this mode of receiving data (getting large amount of symbol data) your browser will keep the data that wasn't even requested by the user. If your symbol list has more than a few items, please consider supporting symbol search / individual symbol resolve instead.

### Symbol resolve[​](#symbol-resolve "Direct link to Symbol resolve")

Request: `GET /symbols?symbol=<symbol>`

* `symbol`: string. Symbol name or ticker.

Example: `GET /symbols?symbol=AAL`, `GET /symbols?symbol=NYSE:MSFT`

A JSON response of the same structure as [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo).

**Note:** this call will be requested if your data feed sent `supports_group_request: false` and `supports_search: true` in the configuration data.

### Symbol search[​](#symbol-search "Direct link to Symbol search")

Request: `GET /search?query=<query>&type=<type>&exchange=<exchange>&limit=<limit>`

* `query`: string. Text typed by the user in the Symbol Search edit box
* `type`: string. One of the symbol types [supported](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#symbols_types) by your back-end
* `exchange`: string. One of the exchanges [supported](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#exchanges) by your back-end
* `limit`: integer. The maximum number of symbols in a response

Example: `GET /search?query=AA&type=stock&exchange=NYSE&limit=15`

A response is expected to be an array of symbol objects as in [respective JS API call](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#searchsymbols)

**Note:** this call will be requested if your data feed sent `supports_group_request: false` and `supports_search: true` in the configuration data.

### Bars[​](#bars "Direct link to Bars")

Request: `GET /history?symbol=<ticker_name>&from=<unix_timestamp>&to=<unix_timestamp>&resolution=<resolution>&countback=<countback>`

* `symbol`: symbol name or ticker.
* `from`: unix timestamp (UTC) of leftmost required bar
* `to`: unix timestamp (UTC) of rightmost required bar (not inclusive)
* `resolution`: string
* `countback`: number of bars (higher priority than `from`) starting with `to`. If `countback` is set, `from` should be ignored.

Example: `GET /history?symbol=BEAM~0&resolution=D&from=1386493512&to=1395133512&countback=500`

A response is expected to be an object with some properties listed below. Each property is treated as a table column, as described above.

* `s`: status code. Expected values: `ok` | `error` | `no_data`
* `errmsg`: Error message. Should be present only when `s = 'error'`
* `t`: Bar time. Unix timestamp (UTC)
* `c`: Closing price
* `o`: Opening price (optional)
* `h`: High price (optional)
* `l`: Low price (optional)
* `v`: Volume (optional)
* `nextTime`: Time of the next bar if there is no data (status code is `no_data`) in the requested period (optional)

**Notes:**

1. Bar time for daily bars should be 00:00 UTC and is expected to be a trading day (not a day when the session starts). The library aligns the time according to the [Session](/charting-library-docs/v29/connecting_data/Symbology#session) from SymbolInfo.
2. 1. Bar time for monthly bars should be 00:00 UTC and be the first trading day of the month.
3. Prices should be passed as numbers and not as strings in quotation marks.

   Example:

   ```
   {  
      s: "ok",  
      t: [1386493512, 1386493572, 1386493632, 1386493692],  
      c: [42.1, 43.4, 44.3, 42.8]  
   }
   ```

   ```
   {  
      s: "no_data",  
      nextTime: 1386493512  
   }
   ```

   ```
   {  
      s: "ok",  
      t: [1386493512, 1386493572, 1386493632, 1386493692],  
      c: [42.1, 43.4, 44.3, 42.8],  
      o: [41.0, 42.9, 43.7, 44.5],  
      h: [43.0, 44.1, 44.8, 44.5],  
      l: [40.4, 42.1, 42.8, 42.3],  
      v: [12000, 18500, 24000, 45000]  
   }
   ```
4. If it is possible, it would be better to handle `countback` parameter for performance reasons.
   Basically, if you handle `countback`, you don't have to worry about passing `nextTime`, because `countBack` helps to avoid empty responses for ranges with no data.

#### How `nextTime` works[​](#how-nexttime-works "Direct link to how-nexttime-works")

Consider the following example. The current symbol is AAPL and the chart resolution is one minute. The library requests data in the `[2015-04-03 16:00 UTC+0, 2015-04-03 19:00 UTC+0]` range. There was no trade on 2015‑04‑03 due to a public holiday.
In this case, the library expects the following response from the datafeed:

```
{  
  s: "no_data",  
  nextTime: 1428001140000 // 2 Apr 2015 18:59:00 GMT+0  
}
```

`nextTime` is the time of the closest available bar in the past.

### Marks[​](#marks "Direct link to Marks")

Request: `GET /marks?symbol=<ticker_name>&from=<unix_timestamp>&to=<unix_timestamp>&resolution=<resolution>`

* `symbol`: symbol name or ticker.
* `from`: unix timestamp (UTC) of leftmost visible bar
* `to`: unix timestamp (UTC) of rightmost visible bar
* `resolution`: string

A response is expected to be an object with some properties listed below.
This object is similar to [respective response](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#getmarks) in Datafeed API, but each property is treated as a table column, as described above.

If the `two_character_bar_marks_labels` feature is enabled then at most the first two characters of the `label` text will be displayed. Otherwise only the first character will be displayed.

```
{  
    id: [array of ids],  
    time: [array of times],  
    color: [array of colors],  
    text: [array of texts],  
    label: [array of labels],  
    labelFontColor: [array of label font colors],  
    minSize: [array of minSizes],  
}
```

**Note:** this call will be requested if your data feed sent `supports_marks: true` in the configuration data.

### Timescale marks[​](#timescale-marks "Direct link to Timescale marks")

Request: `GET /timescale_marks?symbol=<ticker_name>&from=<unix_timestamp>&to=<unix_timestamp>&resolution=<resolution>`

* `symbol`: symbol name or ticker.
* `from`: unix timestamp (UTC) or leftmost visible bar
* `to`: unix timestamp (UTC) or rightmost visible bar
* `resolution`: string

A response is expected to be an array of objects with properties listed below.

* `id`: unique identifier of a mark
* `color`: rgba color
* `label`: a letter to be displayed in a circle
* `time`: unix time
* `tooltip`: tooltip text
* `shape`: optional mark shape. For possible values see the `TimeScaleMarkShape` type in the TypeScript type definitions.

**Note:** this call will be requested if your data feed sent `supports_timescale_marks: true` in the configuration data.

### Server time[​](#server-time "Direct link to Server time")

Request: `GET /time`

Response: Numeric unix time without milliseconds.

Example: `1445324591`

### Quotes[​](#quotes "Direct link to Quotes")

Request: `GET /quotes?symbols=<ticker_name_1>,<ticker_name_2>,...,<ticker_name_n>`

Example: `GET /quotes?symbols=NYSE%3AAA%2CNYSE%3AF%2CNasdaqNM%3AAAPL`

A response is an object with the following keys.

* `s`: Status code for the request. Expected values are: `ok` or `error`
* `errmsg`: Error message. Should be present only when `s = 'error'`
* `d`: symbol data array. Should conform to the [`QuoteData`](/charting-library-docs/v29/api/modules/Datafeed#quotedata) interface.

Example:

```
{  
    "s": "ok",  
    "d": [  
        {  
            "s": "ok",  
            "n": "NYSE:AA",  
            "v": {  
                "ch": 0.16,  
                "chp": 0.98,  
                "short_name": "AA",  
                "exchange": "NYSE",  
                "description": "Alcoa Inc. Common",  
                "lp": 16.57,  
                "ask": 16.58,  
                "bid": 16.57,  
                "open_price": 16.25,  
                "high_price": 16.60,  
                "low_price": 16.25,  
                "prev_close_price": 16.41,  
                "volume": 4029041  
            }  
        },  
        {  
            "s": "ok",  
            "n": "NYSE:F",  
            "v": {  
                "ch": 0.15,  
                "chp": 0.89,  
                "short_name": "F",  
                "exchange": "NYSE",  
                "description": "Ford Motor Company",  
                "lp": 17.02,  
                "ask": 17.03,  
                "bid": 17.02,  
                "open_price": 16.74,  
                "high_price": 17.08,  
                "low_price": 16.74,  
                "prev_close_price": 16.87,  
                "volume": 7713782  
            }  
        }  
    ]  
}
```

## Constructor[​](#constructor "Direct link to Constructor")

```
Datafeeds.UDFCompatibleDatafeed = function(datafeedURL, updateFrequency, limitedServerResponse)
```

### datafeedURL[​](#datafeedurl "Direct link to datafeedURL")

This is a URL of a data server that will receive requests and return data.

### updateFrequency[​](#updatefrequency "Direct link to updateFrequency")

This is a frequency of requests that the data feed will send to the server in milliseconds. Default is 10000 (10 sec).

### limitedServerResponse[​](#limitedserverresponse "Direct link to limitedServerResponse")

Optional parameter for configuring the datafeed for truncated server responses. Use this if your data server has a maximum response size. The object has two parameters: `maxResponseLength` and `expectedOrder`.

* `maxResponseLength`: number. Set this value to the maximum number of bars which the data backend server can supply in a single response. This doesn't affect or change the library behavior regarding how many bars it will request. It just allows this Datafeed implementation to correctly handle this situation.
* `expectedOrder`: Possible values: 'latestFirst' | 'earliestFirst'. If the server can't return all the required bars in a single response then `expectedOrder` specifies whether the server will send the latest (newest) or earliest (older) data first.