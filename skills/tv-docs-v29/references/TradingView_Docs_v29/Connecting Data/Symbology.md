# Connecting Data: Symbology

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/Symbology

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* Symbology

On this page

# Symbology

The library requires information about the symbol to request and process data correctly. This information should be arranged in a specified format and supplied as a [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
This article explains the most challenging concepts of the `LibrarySymbolInfo` implementation. You can find the complete list of interface parameters, and their descriptions, in the [API](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) section.

The library calls the [`resolveSymbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#resolvesymbol) method to request symbol information. To provide this information, create the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object and pass it to [`ResolveCallback`](/charting-library-docs/v29/api/modules/Datafeed#resolvecallback) as a parameter.

tip

Refer to the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) topic for more information on how to supply the chart with data.

## Symbol name[​](#symbol-name "Direct link to Symbol name")

The library addresses a symbol by a unique identifier. You can use [`ticker`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#ticker) or [`name`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#name) to specify such an identifier for a certain symbol.

info

The ticker or name should not contain information other than an identifier for a symbol.
Therefore, they should not contain the exchange.

### name[​](#name "Direct link to name")

The `name` property is an identifier for a symbol within an exchange, such as `AAPL` or `9988` (on Hong Kong exchange).
This identifier is visible to users.
Note that the `name` value does not have to be unique and can be duplicated for several symbols.

By default, `name` is used to [resolve symbols](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) in the [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/).
If you use [`ticker`](#ticker), the library will use the ticker for Datafeed API requests.

### ticker[​](#ticker "Direct link to ticker")

If you need to address a symbol by a custom identifier (for example, numeric), you can use `ticker`.
It is not displayed to users.
You should avoid using colons (":") in ticker values unless you are following the TradingView format: "NYSE:IBM". Using colons may cause unexpected behavior and display bugs.

If you provide `ticker`, the library will use it for [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) requests.
Make sure you provide `ticker` in [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) and [`SearchSymbolResultItem`](/charting-library-docs/v29/api/interfaces/Charting_Library.SearchSymbolResultItem).

### Letter case[​](#letter-case "Direct link to Letter case")

By default, all symbol names are shown in uppercase in the UI. To display lowercase symbol names, you should disable the [`uppercase_instrument_names`](/charting-library-docs/v29/customization/Featuresets#uppercase_instrument_names) featureset and adjust symbol names in the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) and [`symbolSearch`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#searchsymbols) implementation.

Consider the following CodePen example:

See the Pen [How to display lowercase symbols](https://codepen.io/tradingview/pen/KwKNdJN) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

## Resolutions[​](#resolutions "Direct link to Resolutions")

Refer to the [Resolution](/charting-library-docs/v29/core_concepts/Resolution) article for information on how to specify the following properties:

* [`supported_resolutions`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#supported_resolutions)
* [`has_seconds`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_seconds)
* [`seconds_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#seconds_multipliers)
* [`has_intraday`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_intraday)
* [`intraday_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#intraday_multipliers)
* [`has_daily`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_daily)
* [`daily_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#daily_multipliers)
* [`has_weekly_and_monthly`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_weekly_and_monthly)
* [`weekly_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#weekly_multipliers)
* [`monthly_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#monthly_multipliers)
* [`has_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_ticks)

## Time zone[​](#time-zone "Direct link to Time zone")

The [`timezone`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#timezone) property should contain a time zone of the symbol's exchange.
For example, if the symbol's exchange is NASDAQ, the `timezone` value should be `"America/New_York"`.

The `timezone` value affects how the library arranges data on the chart. Make sure you specify this property correctly to avoid potential issues, such as [shifted bars](/charting-library-docs/v29/connecting_data/Datafeed-Issues#library-shifts-bar-time). For more information about supported time zones, refer to the [Time zones](/charting-library-docs/v29/ui_elements/timezones) article.

## Session[​](#session "Direct link to Session")

The [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) property contains trading hours for the symbol. The time zone of the trading hours corresponds to the [`timezone`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#timezone) value.

The [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) value affects how the library arranges data on the chart. Make sure you specify this property correctly to avoid potential issues, such as [shifted bars](/charting-library-docs/v29/connecting_data/Datafeed-Issues#library-shifts-bar-time).
Refer to the [Trading Sessions](/charting-library-docs/v29/connecting_data/Trading-Sessions) topic for more information on the session format.

### corrections[​](#corrections "Direct link to corrections")

The [`corrections`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#corrections) property allows you to specify changes in a trading session for a specific day. For example, you can extend or shorten the session or reschedule it for another day. The `corrections` value overrides the default session specified in the [`session`](#session) property. You can specify corrections for days in the past and future.

The correction is a string that has the `SESSION:YYYYMMDD` format and consists of the following elements:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Element Description Example|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | SESSION Trading hours specified in the same format as the `session` property. Refer to [Session formats](/charting-library-docs/v29/connecting_data/Trading-Sessions#session-formats) for more information. `1000‑1400`| : A separator between the session and the day when it is applied. | YYYYMMDD A day when the session is applied. `20181114` | | | | | | | | | | | |

If the correction is applied to multiple days, you should list the days starting from the latest one and separate them by comma. For example, `"1000-1400:20180308,20180223,20180101"`.
To specify several corrections, list them one by one and use a semicolon as a separator, for example, `"1000-1845:20181113;1000-1400:20181114"`.

You can also specify corrections for holidays. Note that the `corrections` property has higher priority than [`session_holidays`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session_holidays). Therefore, if both properties contain the same date, the library applies hours specified in `corrections` for that date.

## Extended sessions[​](#extended-sessions "Direct link to Extended sessions")

The library allows you to display extended trading sessions for symbols that support them. To enable an extended session for a certain symbol, you should specify the properties below. For more information on how to handle the sessions, refer to the dedicated [Extended sessions](/charting-library-docs/v29/connecting_data/Extended-Sessions) article.

caution

The `session`, `corrections`, `subsession_id`, and `subsessions` properties affect the [Market status pop-up](/charting-library-docs/v29/ui_elements/Symbol-Status). Make sure you configure these properties to avoid an incorrect status for the symbol.

### subsessions[​](#subsessions "Direct link to subsessions")

An extended session includes regular, pre-market, and post-market subsessions. Either a pre-market or post-market subsession can be missed.
When the chart displays an extended session, the subsessions are represented as colored areas.

You should provide information on the extended session and its subsessions to the library using the [`subsessions`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#subsessions) property.
The property contains an array of [`LibrarySubsessionInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySubsessionInfo) objects, where each object describes a certain subsession.
For example, the code sample below specifies an extended session that starts at 04:00 and ends at 20:00. It includes a pre-market subsession from 04:00 to 09:30, a regular subsession from 09:30 to 16:00, and a post-market subsession from 16:00 to 20:00.

```
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
```

### subsession\_id[​](#subsession_id "Direct link to subsession_id")

The [`subsession_id`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#subsession_id) property specifies the session type that the chart should currently display. The `subsession_id` value is either `"regular"` or `"extended"`. You should update the property's value when the session type is changed. Refer to the [Handle session switch](/charting-library-docs/v29/connecting_data/Extended-Sessions#handle-session-switch) section for more information.

### Update session value[​](#update-session-value "Direct link to Update session value")

Note that the [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) value depends on the chart type currently selected on the chart. The property's value should match the corresponding [`LibrarySubsessionInfo.session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySubsessionInfo#session) value specified in [`subsessions`](#subsessions). For example, if the chart displays `"extended"` session, and for this session type `LibrarySubsessionInfo.session` is `"0400-2000"`, the `LibrarySymbolInfo.session` value should also be `"0400-2000"`.
You should update `session` when the session type is changed. Refer to the [Handle session switch](/charting-library-docs/v29/connecting_data/Extended-Sessions#handle-session-switch) section for more information.

tip

You can use the following expression to make sure that `session` is correct. The expression should always be `true`:

```
symbolInfo.session === symbolInfo.subsessions.find(x => x.id === subsession_id).session
```

## Supported price values[​](#supported-price-values "Direct link to Supported price values")

The [`visible_plots_set`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#visible_plots_set) property indicates which values the symbol supports, such as open, high, low, close, and volume.
If you prefer to only provide close values, set `visible_plots_set` to `"c"`.
This makes the chart show the symbol data using only line-based styles.

## Price format[​](#price-format "Direct link to Price format")

The library supports the [decimal](#decimal-format) and [fractional](#fractional-format) price formats. To configure how the price displays, specify the following properties:

* [`pricescale`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#pricescale) — a number of decimal places or fractions that the price has.
* [`minmov`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#minmov) — a number of units that represents the price tick.
* [`minmove2`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#minmove2) — a fraction of a fraction.
* [`fractional`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#fractional) — a boolean value that shows whether the format is fractional or decimal.

These properties' values depend on the chosen format and are not visible to users.

### Decimal format[​](#decimal-format "Direct link to Decimal format")

* `pricescale` should be `10^n`, where `n` is the number of decimal places. For example, if the price is `1.01`, set `pricescale` to `100`.
* `minmov` depends on the tick size that is calculated as `minmov / pricescale`. For example, if the tick size is `0.25`, set `minmov` to `25`.
* `minmove2` should be `0` or not specified.
* `fractional` should be `false` or not specified.

Consider the following examples:

* The security's tick size is `0.01`. To display this security, set `minmov = 1`, `pricescale = 100`.
* The security's tick size is `0.0125`. To display this security, set `minmov = 125`, `pricescale = 10000`.
* The security's tick size is `0.20`. To display this security, set `minmov = 20`, `pricescale = 100`.

#### Variable tick size[​](#variable-tick-size "Direct link to Variable tick size")

If you need to adjust a tick size depending on a symbol price, you can additionally specify the [`variable_tick_size`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#variable_tick_size) property.
This property should be a `string` that contains prices and the corresponding tick sizes.
The library overrides the [`pricescale`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#pricescale)
and [`minmov`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#minmov) properties to represent the desired tick size.

For example, the `'0.01 10 0.02 25 0.05'` value specifies the following ticks:

* For prices less than or equal to 10, the tick size is `0.01`. Therefore, `minmov = 1`, `pricescale = 100`.
* For prices greater than 10 but less than or equal to 25, the tick size is `0.02`. Therefore, `minmov = 2`, `pricescale = 100`.
* For prices greater than 25, the tick size is `0.05`. Therefore, `minmov = 5`, `pricescale = 100`.

Note that you need to initialize `pricescale` and `minmov` regardless of whether you use `variable_tick_size` or not.

#### How to display pips[​](#how-to-display-pips "Direct link to How to display pips")

You can display pips for symbols that have `forex` or `cfd` type. To do this, set `minmove2` to `10`. In the UI, pips look smaller than the price digits.

![Symbology Pips Example](/charting-library-docs/v29/assets/images/symbology_pips-b40a419c095fefcd3749d89b6c5f0405.png)

If `minmove2` is `0` for `forex`/`cfd` symbols, the spread is displayed in ticks, not pips.

### Fractional format[​](#fractional-format "Direct link to Fractional format")

The fractional price is displayed as `x'y` (for example, `133'21`), where `x` and `y` are the integer and fractional parts, respectively. A single quote is used as a delimiter.

* `pricescale` should be `2^n`. This value represents the number of fractions.
* `minmov` depends on the tick size that is calculated as `minmov / pricescale`. For example, if the tick size is `1/4`, set `minmov` to `1`.
* `minmove2` should be `0` or not specified.
* `fractional` should be `true`.

Consider the following examples:

* To display a security that has the `1/32` tick size, set `minmov = 1`, `pricescale = 32`.
* To display a security that has the `2/8` tick size, set `minmov = 2`, `pricescale = 8`.

#### Fraction of a fraction format[​](#fraction-of-a-fraction-format "Direct link to Fraction of a fraction format")

The fraction of a fraction format is a particular case of the fractional format. It is displayed as `x'y'z` (for example, `133'21'5`), where `z` is a fractional part of `y`. In this case, `minmove2` differs from `0` and represents a fraction of a fraction. For example, the `ZBM2023` tick size is 1/4 of a 32nd. To display this security, set `minmov = 1`, `pricescale = 128`, `minmove2 = 4`. The price is displayed in the UI as follows:

* `119'16'0` represents `119 + 16.0/32`
* `119'16'2` represents `119 + 16.25/32`
* `119'16'5` represents `119 + 16.5/32`
* `119'16'7` represents `119 + 16.75/32`