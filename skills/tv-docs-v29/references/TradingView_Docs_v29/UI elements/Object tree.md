# UI elements: Object tree

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/object-tree

* [UI elements](/charting-library-docs/v29/ui_elements/)* Object tree

On this page

# Object tree

The *Object tree* is a feature that allows managing (hiding, showing, or removing) drawings, indicators, and symbols on the chart.

The *Object tree* is enabled by default but you can hide it by disabling the [`show_object_tree`](/charting-library-docs/v29/customization/Featuresets#show_object_tree) featureset.
Users can access the *Object tree* through the left toolbar (in Advanced Charts) or the right toolbar (in Trading Platform).

![Object tree](/charting-library-docs/v29/assets/images/object-tree-c83fd8d2c6ebaeb76da81224b7a3488c.png)

## Fix undefined values[​](#fix-undefined-values "Direct link to Fix undefined values")

The `undefined` string appears in the *Object tree* when the [`exchange`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#exchange) and [`listed_exchange`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#listed_exchange) properties are missing from the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object.
You should provide this object via the [`resolveSymbol`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) callback.

To resolve this issue, ensure these properties have appropriate values in the `LibrarySymbolInfo` object.
Alternatively, you can hide the symbol exchange display by enabling the [`hide_object_tree_and_price_scale_exchange_label`](/charting-library-docs/v29/customization/Featuresets#hide_object_tree_and_price_scale_exchange_label) featureset.