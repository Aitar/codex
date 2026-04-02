# Core Concepts: Resolution

Source: https://www.tradingview.com/charting-library-docs/v29/core_concepts/Resolution

* Core Concepts* Resolution

On this page

# Resolution

**Resolution** or time interval is a time period of a single bar. The library supports resolutions in seconds, minutes, hours, days, weeks, months, years, and ticks.

## Resolution format[​](#resolution-format "Direct link to Resolution format")

A resolution value should have the [`ResolutionString`](/charting-library-docs/v29/api/modules/Datafeed#resolutionstring) type.
The table below describes how to specify different resolution values. In these values, `x` represents a number of units.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Resolution Format Example|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Ticks `xT` `1T` — one tick, `5T` — five ticks, `100T` — one hundred ticks| Seconds `xS` `1S` — one second, `2S` — two seconds, `100S` — one hundred seconds| Minutes `x` `1` — one minute, `2` — two minutes, `100` — one hundred minutes| Hours `x` minutes `60` — one hour, `120` — two hours, `240` — four hours| Days `xD` `1D` — one day, `2D` — two days, `100D` — one hundred days| Weeks `xW` `1W` — one week, `2W` — two weeks, `100W` — one hundred weeks| Months `xM` `1M` — one month, `2M` — two months, `100M` — one hundred months| Years `xM` months `12M` — one year, `24M` — two years, `48M` — four years | | | | | | | | | | | | | | | | | | | | | | | | | | |

You can also omit the number of units if it is equal to `1`. For example, you can use `D` instead of `1D` and `W` instead of `1W`.

## Set up resolution on the chart[​](#set-up-resolution-on-the-chart "Direct link to Set up resolution on the chart")

The resolution is [initialized](#default-resolution) in the Widget Constructor and can be changed [in the UI](#in-ui) or [using the API](#using-api).

To get the current resolution, use the [`resolution`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resolution) method.

```
widget.onChartReady(() => {  
    widget.activeChart().resolution();  
});
```

### Default resolution[​](#default-resolution "Direct link to Default resolution")

You can specify the default resolution using the [`interval`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#interval) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

```
new TradingView.widget({  
    // ...  
    interval: '1D',  
});
```

### In UI[​](#in-ui "Direct link to In UI")

Users can change the resolution in the following ways:

* Use the *Resolution* button on the top toolbar.

![Change resolution via top toolbar](/charting-library-docs/v29/assets/images/change-resolution-27d11071efbc4b89dfd760528abf653e.gif)

* Use the *Resolution* button in the [*Legend*](/charting-library-docs/v29/ui_elements/Legend).

![Change resolution in Legend](/charting-library-docs/v29/assets/images/change-resolution-legend-53e5e1f28a07048eb2d70471f63dd191.gif)

* Press any digit key or the `,` (comma) key.

![Change resolution using shortcuts](/charting-library-docs/v29/assets/images/change-resolution-shortcut-9cdd50b118ea1410f8eed9d084a944c2.gif)

To disable any of the methods above, refer to [Disable resolution changing](#disable-resolution-changing).

### Using API[​](#using-api "Direct link to Using API")

You can use the [`setResolution`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#setresolution) method to change the resolution on the fly.

```
widget.onChartReady(() => {  
    widget.activeChart().setResolution('2M');  
});
```

caution

In the UI, users can enter values like `2h` to specify a number of hours. However, you should specify hour resolutions in minutes, for example `120`, if you change the resolution using the API.

## Configure resolutions in datafeed[​](#configure-resolutions-in-datafeed "Direct link to Configure resolutions in datafeed")

You should configure resolutions in your [datafeed](/charting-library-docs/v29/connecting_data/datafeed-api/) to display data correctly.
To do this, follow the steps below:

1. Specify resolutions that the chart and a certain symbol support.
2. Enable specific resolutions that you use, for example, a resolution in seconds or days.
3. Implement the corresponding method in the datafeed.

### 1. Specify supported resolutions[​](#1-specify-supported-resolutions "Direct link to 1. Specify supported resolutions")

To enable any resolution, specify the following properties:

* [`DatafeedConfiguration.supported_resolutions`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#supported_resolutions) contains all resolutions that the chart should support.
* [`LibrarySymbolInfo.supported_resolutions`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#supported_resolutions) contains all resolutions that a certain symbol should support.

The resolutions should be listed in a specific [format](#resolution-format). For example, `["1", "15", "240", "D", "6M"]` stands for 1 minute, 15 minutes, 4 hours, 1 day, and 6 months. If the certain symbol does not support some chart resolutions, they are disabled for this symbol in the UI.

![Supported resolutions](data:image/png;base64,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)

If a user switches to another symbol, that does not support the selected resolution, the library changes the resolution to the first available one for this symbol.

#### Additional resolutions[​](#additional-resolutions "Direct link to Additional resolutions")

The library can combine smaller intervals into larger ones to build new resolutions. For instance, it can build 2-minute bars from 1-minute bars.
Therefore, you can enable resolutions that your datafeed does not explicitly provide. To do this, add these resolutions to the `supported_resolutions` arrays mentioned [above](#1-specify-supported-resolutions).

If you want to [disable resolution rebuilding](#disable-resolution-rebuilding), use the [`disable_resolution_rebuild`](/charting-library-docs/v29/customization/Featuresets#disable_resolution_rebuild) featureset.

caution

The library **cannot** build the following resolutions:

* daily, weekly, or monthly resolutions using intraday data
* resolutions higher than seconds using tick data

### 2. Enable required resolutions[​](#2-enable-required-resolutions "Direct link to 2. Enable required resolutions")

Follow the instructions below to enable the required resolutions.

#### Resolution in seconds[​](#resolution-in-seconds "Direct link to Resolution in seconds")

To enable resolution in seconds, additionally configure the following properties:

* Enable the [`seconds_resolution`](/charting-library-docs/v29/customization/Featuresets#seconds_resolution) featureset. To do this, include `seconds_resolution` to the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.
* Set [`has_seconds`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_seconds) to `true`.
* Specify [`seconds_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#seconds_multipliers) that contains the resolutions provided by the datafeed.

Additionally, if your datafeed supports tick data for a symbol, you can tell the library to build seconds bars from ticks. To do this, set [`build_seconds_from_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#build_seconds_from_ticks) to `true`. Note that this feature is available in Trading Platform only.

#### Resolution in minutes (intraday)[​](#resolution-in-minutes-intraday "Direct link to Resolution in minutes (intraday)")

To enable intraday resolution (in minutes), additionally configure the following properties:

* Set [`has_intraday`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_intraday) to `true`.
* Specify [`intraday_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#intraday_multipliers) that contains the resolutions that the datafeed provides.

#### Resolution in days[​](#resolution-in-days "Direct link to Resolution in days")

To enable resolution in days, additionally configure the following properties:

* Set [`has_daily`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_daily) to `true`.
* Specify [`daily_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#daily_multipliers) that contains the resolutions that the datafeed provides.

#### Resolution in weeks / months[​](#resolution-in-weeks--months "Direct link to Resolution in weeks / months")

To enable resolution in weeks or months, additionally configure the following properties:

* Set [`has_weekly_and_monthly`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_weekly_and_monthly) to `true`.
* Specify [`weekly_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#weekly_multipliers) or [`monthly_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#monthly_multipliers) that contains the resolutions that the datafeed provides.

#### Resolution in ticks[​](#resolution-in-ticks "Direct link to Resolution in ticks")

To enable resolution in ticks, additionally configure the following properties:

* Enable the [`tick_resolution`](/charting-library-docs/v29/customization/Featuresets#tick_resolution) featureset. To do this, include `tick_resolution` to the [`enabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#enabled_features) array.
* Set [`has_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_ticks) to `true`.

Additionally, you can tell the library to build seconds bars from ticks. To do this, set [`build_seconds_from_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#build_seconds_from_ticks) to `true`. Note that this feature is available in Trading Platform only.

### 3. Implement method in datafeed[​](#3-implement-method-in-datafeed "Direct link to 3. Implement method in datafeed")

The library requests data from the datafeed based on the current resolution selected on the chart. All resolutions that your datafeed explicitly supports should be listed in the `*_multipliers` properties ([`seconds_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#seconds_multipliers), [`daily_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#daily_multipliers), etc.) and implemented in the [`getBars`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#getbars) method.

### Example[​](#example "Direct link to Example")

Consider the following example. The datafeed has 1-minute and 2-minute bars. Also, you would like to support a 5-minute resolution. In this case, you should configure the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) properties as follows:

```
//...  
"has_intraday": true,  
"supported_resolutions": ["1", "2", "5"],  
"intraday_multipliers": ["1", "2"], // The library can request 1-minute and 2-minute bars, and will build 5-minute bars from 1-minute data  
//...
```

The example of the `getBars` implementation is demonstrated below:

```
getBars(symbolInfo, resolution, periodParams, onHistoryCallback, onErrorCallback) {  
    if (resolution === '1') {  
        const bars = getBarsFor1MinuteResolution(periodParams);  
        onHistoryCallback(bars);  
        ​  
        return;  
    }  
    ​  
    if (resolution === '2') {  
        const bars = getBarsFor2MinuteResolution(periodParams);  
        onHistoryCallback(bars);  
        ​  
        return;  
    }  
  
    //...  
}  
  
function getBarsFor1MinuteResolution(periodParams) {  
    // Your custom logic  
}  
  
function getBarsFor2MinuteResolution(periodParams) {  
    // Your custom logic  
}
```

## Additional settings[​](#additional-settings "Direct link to Additional settings")

You can use [featuresets](/charting-library-docs/v29/customization/Featuresets) to adjust resolution settings.

### Disable resolution rebuilding[​](#disable-resolution-rebuilding "Direct link to Disable resolution rebuilding")

The library aligns bars to the nearest expected bar position. For example, if [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) is `0915-1530` and the chart shows a 5-minute resolution, the library expects the following bar timestamps: `[09:15, 09:20, 09:25, ...]`.
If your datafeed provides a bar with the `09:17` timestamp, the library changes this timestamp to `09:15`.
You can use the [`disable_resolution_rebuild`](/charting-library-docs/v29/customization/Featuresets#disable_resolution_rebuild) featureset to display bars exactly as your datafeed provides.

info

If you enable the `disable_resolution_rebuild` featureset, the library cannot build resolutions that your datafeed does not explicitly provide. For example, the library cannot build a 5-minute resolution from 1-minute data.

### Enable custom resolutions[​](#enable-custom-resolutions "Direct link to Enable custom resolutions")

You can use the [`custom_resolutions`](/charting-library-docs/v29/customization/Featuresets#custom_resolutions) featureset to allow users to add custom resolutions. Note that if a user adds a resolution that the symbol does not support, this resolution will be disabled in the UI.

![Add custom resolution](/charting-library-docs/v29/assets/images/add-custom-resolution-d8557c90a073238a4d2c2c1dffd061dc.png)

### Disable resolution changing[​](#disable-resolution-changing "Direct link to Disable resolution changing")

You can use the [`header_resolutions`](/charting-library-docs/v29/customization/Featuresets#header_resolutions) featureset to remove the *Resolution* button from the top toolbar.

![Remove resolution button](data:image/png;base64,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)

To disable resolution changing in the [*Legend*](/charting-library-docs/v29/ui_elements/Legend), use the [`legend_inplace_edit`](/charting-library-docs/v29/customization/Featuresets#legend_inplace_edit) featureset.
If you want to completely remove the *Resolution* button from the *Legend*, use the [`hide_resolution_in_legend`](/charting-library-docs/v29/customization/Featuresets#hide_resolution_in_legend) featureset.

![Remove resolution from Legend](/charting-library-docs/v29/assets/images/no-resolution-legend-d2ff263da43b9adaccb9f03d4c14f1a3.png)

To disable the *Resolution* shortcut, use the [`show_interval_dialog_on_key_press`](/charting-library-docs/v29/customization/Featuresets#show_interval_dialog_on_key_press) featureset.