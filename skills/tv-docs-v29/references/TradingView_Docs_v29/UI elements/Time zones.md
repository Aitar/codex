# UI elements: Time zones

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/timezones

* [UI elements](/charting-library-docs/v29/ui_elements/)* Time zones

On this page

# Time zones

## Overview[​](#overview "Direct link to Overview")

Time on the [time scale](/charting-library-docs/v29/ui_elements/Time-Scale) is displayed according to the chart time zone.
To set the default time zone, specify the [`timezone`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#timezone) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

```
var widget = window.tvWidget = new TradingView.widget({  
    // ...  
    overrides: {  
        "timezone": "America/New_York",  
    }  
});
```

You can change the default time zone on the fly using the [`applyOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#applyoverrides) method.

```
widget.applyOverrides({ "timezone": "Europe/Belgrade"});
```

caution

Besides the time zone of the chart, you should also specify the time zone for each symbol. Make sure you provide correct values as it affects how the library aligns and displays the data. Refer to [Symbology](/charting-library-docs/v29/connecting_data/Symbology#time-zone) for more information.

### Manage time zone[​](#manage-time-zone "Direct link to Manage time zone")

Call the [`getTimezoneApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#gettimezoneapi) method to get an instance of the [`ITimezoneApi`](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimezoneApi) interface. This interface provides an extensive API for managing time zone settings. For example, you can change the current time zone as follows:

```
widget.activeChart().getTimezoneApi().setTimezone("America/Chicago");
```

In the UI, users can switch the time zone from the drop-down list at the bottom of the chart or through the *Settings* dialog.

## Supported time zones[​](#supported-time-zones "Direct link to Supported time zones")

The library supports the following time zones:

* `Etc/UTC`
* `Africa/Cairo`
* `Africa/Casablanca`
* `Africa/Johannesburg`
* `Africa/Lagos`
* `Africa/Nairobi`
* `Africa/Tunis`
* `America/Anchorage`
* `America/Argentina/Buenos_Aires`
* `America/Bogota`
* `America/Caracas`
* `America/Chicago`
* `America/El_Salvador`
* `America/Juneau`
* `America/Lima`
* `America/Los_Angeles`
* `America/Mexico_City`
* `America/New_York`
* `America/Phoenix`
* `America/Santiago`
* `America/Sao_Paulo`
* `America/Toronto`
* `America/Vancouver`
* `Asia/Astana`
* `Asia/Ashkhabad`
* `Asia/Bahrain`
* `Asia/Bangkok`
* `Asia/Chongqing`
* `Asia/Colombo`
* `Asia/Dhaka`
* `Asia/Dubai`
* `Asia/Ho_Chi_Minh`
* `Asia/Hong_Kong`
* `Asia/Jakarta`
* `Asia/Jerusalem`
* `Asia/Karachi`
* `Asia/Kathmandu`
* `Asia/Kolkata`
* `Asia/Kuala_Lumpur`
* `Asia/Kuwait`
* `Asia/Manila`
* `Asia/Muscat`
* `Asia/Nicosia`
* `Asia/Qatar`
* `Asia/Riyadh`
* `Asia/Seoul`
* `Asia/Shanghai`
* `Asia/Singapore`
* `Asia/Taipei`
* `Asia/Tehran`
* `Asia/Tokyo`
* `Asia/Yangon`
* `Atlantic/Azores`
* `Atlantic/Reykjavik`
* `Australia/Adelaide`
* `Australia/Brisbane`
* `Australia/Perth`
* `Australia/Sydney`
* `Europe/Amsterdam`
* `Europe/Athens`
* `Europe/Belgrade`
* `Europe/Berlin`
* `Europe/Bratislava`
* `Europe/Brussels`
* `Europe/Bucharest`
* `Europe/Budapest`
* `Europe/Copenhagen`
* `Europe/Dublin`
* `Europe/Helsinki`
* `Europe/Istanbul`
* `Europe/Lisbon`
* `Europe/London`
* `Europe/Luxembourg`
* `Europe/Madrid`
* `Europe/Malta`
* `Europe/Moscow`
* `Europe/Oslo`
* `Europe/Paris`
* `Europe/Prague`
* `Europe/Riga`
* `Europe/Rome`
* `Europe/Stockholm`
* `Europe/Tallinn`
* `Europe/Vienna`
* `Europe/Vilnius`
* `Europe/Warsaw`
* `Europe/Zurich`
* `Pacific/Auckland`
* `Pacific/Chatham`
* `Pacific/Fakaofo`
* `Pacific/Honolulu`
* `Pacific/Norfolk`
* `US/Mountain`

If your time zone is not supported, you can request it on [GitHub Issues](https://github.com/tradingview/charting_library/issues "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) or add your [custom time zone](#custom-time-zones).

## Custom time zones[​](#custom-time-zones "Direct link to Custom time zones")

You can specify a custom time zone using the [`custom_timezones`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_timezones) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
Just like the built-in time zones, custom time zones will appear in the drop-down list and chart settings. You can also use them to specify time zones for symbols.

You should map (alias) a custom time zone to either a [built-in](#supported-time-zones) or [GMT-based time zone](#gmt-based-time-zones) one.
Ensure that the alias time zone correctly matches your desired time zone in all aspects including daylight saving time dates.

The code sample below adds the following time zones:

* the Cape Town time zone aliased to the built-in time zone of Johannesburg.
* the Nuuk time zone aliased to a GMT-based time zone.

```
var widget new TradingView.widget({  
    // ...  
  
    custom_timezones: [  
        {  
            id: "Africa/Cape_Town",  
            alias: "Africa/Johannesburg",  
            title: "Cape Town",  
        },  
        {  
            id: "America/Nuuk",  
            alias: "Etc/GMT+3",  
            title: "Nuuk",  
        },  
    ],  
}));
```

### GMT-based time zones[​](#gmt-based-time-zones "Direct link to GMT-based time zones")

You can map your custom time zone to a GMT-based time zone. GMT-based time zones can only be used in the [`alias`](/charting-library-docs/v29/api/interfaces/Charting_Library.CustomAliasedTimezone#alias) property of a custom time zone object.

The GMT-based time zones should be specified in the following format:

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Element Description|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | `Etc/GMT` The default beginning.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | `+` or `-` The sign showing the offset direction.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | Number The number of hours offset.|  |  |  |  | | --- | --- | --- | --- | | : A separator between hours and minutes.|  |  | | --- | --- | | Number (Optional) The number of minutes offset. | | | | | | | | | | | |

To conform with the [POSIX](https://en.wikipedia.org/wiki/POSIX) style, time zone names use a sign that is reversed from the standard [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_offsets_from_UTC) convention. In the `Etc/` namespace, time zones west of GMT have a positive sign, and those east of GMT have a negative sign.

#### Examples[​](#examples "Direct link to Examples")

* `Etc/GMT+0` : same as `Etc/UTC`
* `Etc/GMT+2` : 2 hours behind GMT
* `Etc/GMT-4` : 4 hours ahead of GMT
* `Etc/GMT-3:21` : 3 hours and 21 minutes ahead of GMT