# Getting Started: Cross Origin Hosting

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/Hosting-Library-Cross-Origin

* [Getting Started](/charting-library-docs/v29/getting_started/)* Cross Origin Hosting

On this page

# Cross Origin Hosting

If you need to host the library files on a separate origin (domain) to the page
containing the chart then please ensure that the
[`library_path` widget constructor parameter](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#library_path)
is configured as follows:

* The `library_path` value should start with either `http://` or `https://`,
  followed by the url to the folder containing the library's static
  files.
  + example: `library_path: 'https://example.com/charting_library/'`
* `library_path` should end with a trailing forward slash.

## Example: Loading the standalone version from separate origin[​](#example-loading-the-standalone-version-from-separate-origin "Direct link to Example: Loading the standalone version from separate origin")

If you hosted the library files within a folder named `charting_library` on the
`example.com` domain then you would configure the library as follows.

### Loading the standalone script[​](#loading-the-standalone-script "Direct link to Loading the standalone script")

Place the following script tag within the `<head>` of the page.

```
<script  
    type="text/javascript"  
    src="https://example.com/charting_library/charting_library.standalone.js"  
></script>
```

### Specifying the `library_path` parameter[​](#specifying-the-library_path-parameter "Direct link to specifying-the-library_path-parameter")

When evoking the widget constructor, ensure that the `library_path` value starts
with `http` as described above.

```
var widget = (window.tvWidget = new TradingView.widget({  
    library_path: 'https://example.com/charting_library/',  
  
    symbol: 'A',  
    interval: '1D',  
    container: 'tv_chart_container',  
    datafeed: new Datafeeds.UDFCompatibleDatafeed(  
        'https://demo_feed.tradingview.com'  
    ),  
}));
```

## Server setup[​](#server-setup "Direct link to Server setup")

Make sure that the server hosting the library files is configured to allow
cross-origin requests from the origin of the page containing the chart element.
Please see this MDN article for more information:
[Access-Control-Allow-Origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Origin)

### Demo Charts and Study Templates Storage Server[​](#demo-charts-and-study-templates-storage-server "Direct link to Demo Charts and Study Templates Storage Server")

Please note that the
demo charts and [study template storage server](/charting-library-docs/v29/saving_loading/save-load-rest-api/#use-demo-storage)
(`http://saveload.tradingview.com`) isn't compatible with requests from any
origin except `localhost` and `tradingview.com`. Attempting to use this server
from any other origin will still result in a CORS error.

Please see [Saving and Loading Charts](/charting-library-docs/v29/saving_loading/) for an
overview on how to setup your own storage server.