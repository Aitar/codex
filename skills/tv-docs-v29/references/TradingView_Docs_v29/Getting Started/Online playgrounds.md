# Getting Started: Online playgrounds

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/Online-Editors

* [Getting Started](/charting-library-docs/v29/getting_started/)* Online playgrounds

On this page

# Online playgrounds

Online code editors like CodePen and JSFiddle are the fastest way to create examples, reproduce bugs, or experiment with the Advanced Charts and Trading Platform, all without any local setup.
This guide shows you how to use our hosted library files to get a chart running in seconds.
For the quickest start, we recommend using one of our pre-made [starter templates](#starter-templates).

## Starter templates[​](#starter-templates "Direct link to Starter templates")

We currently provide starter templates for CodePen and JSFiddle.
While other online editors may work, our hosted files use a security policy (CORS) that can prevent the chart from loading on unsupported sites.
For more information on how to use the library when the HTML page and the library bundles aren't on the same origin, see [Cross-Origin Hosting](/charting-library-docs/v29/getting_started/Hosting-Library-Cross-Origin).

The starter templates below are the fastest and most reliable way to get started.
Simply open one, fork it, and start coding.

### CodePen[​](#codepen "Direct link to CodePen")

* [Advanced Charts](https://codepen.io/tradingview/pen/PwPZrBK)
* [Trading Platform](https://codepen.io/tradingview/pen/NPGxZLY)
* [Themed Advanced Charts](https://codepen.io/tradingview/pen/VYveJEK)

### JSFiddle[​](#jsfiddle "Direct link to JSFiddle")

* [Advanced Charts](https://jsfiddle.net/TradingView/8301r7nc/)
* [Trading Platform](https://jsfiddle.net/TradingView/60vemsp8/)
* [Themed Advanced Charts](https://jsfiddle.net/TradingView/v8x1hsdf/)

## Important limitations[​](#important-limitations "Direct link to Important limitations")

When using our hosted library files, be aware of the following restrictions.

* The hosted files always point to the latest version from the `master` branch of the [charting\_library GitHub repository](https://github.com/tradingview/charting_library "The repository is private.")  🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")). To [use a specific version](#using-specific-version), link to your hosted library files and ensure your server allows CORS for the code playground site of your choice.
* The [demo storage](/charting-library-docs/v29/saving_loading/save-load-rest-api/#use-demo-storage) for chart layouts and indicator templates isn't compatible with requests from any origin except `localhost` and `tradingview.com`. Attempting to use this server from any other origin will result in a CORS error.
* When specifying a custom CSS file via the [`custom_css_url`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_css_url) property, be aware that the CSS URL should be specified relative to the [`library_path`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#library_path) property.

## How to set up[​](#how-to-set-up "Direct link to How to set up")

The starter templates are ready to go, but if you want to understand how they work or build an example from scratch, follow the steps below.

Before proceeding with the steps, choose the correct domain for the library you are using.
These base URLs point to the latest build of the library:

* `https://charting-library.tradingview-widget.com` (for Advanced Charts)
* `https://trading-terminal.tradingview-widget.com` (for Trading Platform)

Then integrate the library using either the [latest version](#using-latest-version) or a [specific version](#using-specific-version).
The examples below will use the Advanced Charts domain.

### Using latest version[​](#using-latest-version "Direct link to Using latest version")

1. Within the head of your HTML file, load two scripts: the standalone version of the library and the demo datafeed implementation:

   ```
   <script type="text/javascript" src="https://charting-library.tradingview-widget.com/charting_library/charting_library.standalone.js"></script>  
   <script type="text/javascript" src="https://charting-library.tradingview-widget.com/datafeeds/udf/dist/bundle.js"></script>
   ```
2. In your JavaScript, set the [`library_path`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#library_path) property to the `charting_library` subfolder of the domain of your choice.

   ```
   new TradingView.widget({  
     /* Other Widget Constructor properties */  
     
     library_path: 'https://charting-library.tradingview-widget.com/charting_library/',  
   })
   ```

### Using specific version[​](#using-specific-version "Direct link to Using specific version")

1. Within the head of your HTML file, load two scripts: the standalone version of the library and the demo datafeed implementation. For the library script, specify the version path you'd like to use, for example, `/versions/28.4.0`.

   ```
   <script type="text/javascript" src="https://charting-library.tradingview-widget.com/versions/28.4.0/charting_library/charting_library.standalone.js"></script>  
   <script type="text/javascript" src="https://charting-library.tradingview-widget.com/datafeeds/udf/dist/bundle.js"></script>
   ```
2. In your JavaScript, set the [`library_path`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#library_path) property to point to the exact same version you specified in the HTML file.

   ```
   new TradingView.widget({  
     /* Other Widget Constructor properties */  
     
     library_path: 'https://charting-library.tradingview-widget.com/versions/29.0.0/charting_library/',  
   })
   ```