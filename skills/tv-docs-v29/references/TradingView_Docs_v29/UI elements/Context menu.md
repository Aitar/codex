# UI elements: Context menu

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/context-menu

* [UI elements](/charting-library-docs/v29/ui_elements/)* Context menu

On this page

# Context menu

The **context menu** is a dialog that users access through a right-mouse-click or ellipsis menu (…).

## Override context menu[​](#override-context-menu "Direct link to Override context menu")

You can override the default items in the context menu in two ways:

* [using Widget Constructor](#using-widget-constructor)
* [using API](#using-api)

info

Both approaches override all context menus.
If you only want to override specific menus, you should implement your own filtering logic for that particular use case.

### Using Widget Constructor[​](#using-widget-constructor "Direct link to Using Widget Constructor")

You can register a custom function for overriding default items when the context menu is created.
To do this, use the [`context_menu`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#context_menu) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
`context_menu` has two properties:

* [`items_processor`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#items_processor) allows you to modify the items displayed in the context menu.
  For example, you can provide a function that adds new items and removes or reorders existing ones.
  The library calls this function each time users want to display the context menu.
  This function should return an array of items to display.
* [`renderer_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#renderer_factory) allows you to override the default renderer for the context menu so you can adjust existing menu items.

tip

You can also use the `context_menu` property to retrieve a list of items in the menu.
Check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=3715s) on YouTube for an implementation example.

#### Examples[​](#examples "Direct link to Examples")

The code sample below shows how to add a new item to the context menu using [`items_processor`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#items_processor).

See the Pen [UI. Add new button to context menu](https://codepen.io/tradingview/pen/NWJddbz) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

The code sample below shows how to adjust existing items of the context menu using [`renderer_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#renderer_factory).

See the Pen [UI. Adjust context menu items](https://codepen.io/tradingview/pen/OJqWgQZ) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

#### Determine evoked menu[​](#determine-evoked-menu "Direct link to Determine evoked menu")

Both [`items_processor`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#items_processor) and [`renderer_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#renderer_factory) provide menu names
and the associated IDs for items like series, drawings, indicators, orders, and positions.
You can determine which menu was triggered using the properties of the [`CreateContextMenuParams`](/charting-library-docs/v29/api/interfaces/Charting_Library.CreateContextMenuParams) interface.

### Using API[​](#using-api "Direct link to Using API")

If you want to change the menu dynamically, use the [`onContextMenu`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#oncontextmenu) method.

```
widget.onChartReady(function() {  
    widget.onContextMenu(function(unixtime, price) {  
        return [{  
            position: "top",  
            text: "First top menu item, time: " + unixtime + ", price: " + price,  
            click: function() { alert("First item clicked."); }  
        },  
        { text: "-", position: "top" }, // Adds a separator between buttons  
        { text: "-Paste" },             // Removes the existing item from the menu  
        {  
            position: "top",  
            text: "Second top menu item 2",  
            click: function() { alert("Second item clicked."); }  
        }, {  
            position: "bottom",  
            text: "Bottom menu item",  
            click: function() { alert("Third item clicked."); }  
        }];  
    });  
});
```