# Getting Started: Package Content

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/Package-Content

* [Getting Started](/charting-library-docs/v29/getting_started/)* Package Content

On this page

# Package Content

The package is available on GitHub. You may check out the latest stable version (`master` branch). Please get in touch with us to get access to this repository.

You can check the library version by entering the `TradingView.version()` command in a browser console.

### Package content[​](#package-content "Direct link to Package content")

```
    +/charting_library  
        + /bundles  
        - charting_library.js  
        - charting_library.d.ts  
        - charting_library.cjs.js  
        - charting_library.esm.js  
        - charting_library.standalone.js  
        - datafeed-api.d.ts  
        - package.json  
    +/datafeeds  
        + /udf  
    - index.html  
    - mobile_black.html  
    - mobile_white.html  
    - test.html
```

* `/charting_library` contains all the library files.
* `/charting_library/charting_library*` files contain an external library widget interface, they is not supposed to be edited.
  + `.js` is an [UMD](https://github.com/umdjs/umd) module (for backward compatibility).
  + `.esm.js` is an native JavaScript module, see [import](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import).
  + `.cjs.js` is an [CommonJS](https://en.wikipedia.org/wiki/CommonJS) module.
  + `.standalone.js` is an [iife](https://en.wikipedia.org/wiki/Immediately_invoked_function_expression) module.
  + `.d.ts` contains TypeScript definitions for the widget interface.
* `/charting_library/datafeed-api.d.ts` contains TypeScript definitions for the data feed interface.
* `/charting_library/bundles` stores library internal content and is not intended for other purposes, it should be like "black box" for you so it could be changed anytime without a notice.
* `/charting_library/datafeeds/udf/` contains [UDF-compatible](/charting-library-docs/v29/connecting_data/UDF) datafeed wrapper (implements [Datafeed API](/charting-library-docs/v29/connecting_data/datafeed-api/) to connect to library and UDF to connect to datafeed). Sample datafeed wrapper implements pulse real-time emulation. You are free to edit its code.
* `/index.html` is an example of using library widget on your web page.
* `/test.html` is an example of using different library customization features.
* `/mobile*.html` are also examples of Widget customization.

All internal JS and CSS codes of the library are inlined and minified to reduce the page load time. Files that are expected to be edited by you were not minified.