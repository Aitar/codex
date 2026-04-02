# Saving and loading charts: Saving drawings separately

Source: https://www.tradingview.com/charting-library-docs/v29/saving_loading/saving_drawings_separately

* [Saving and loading charts](/charting-library-docs/v29/saving_loading/)* Saving drawings separately

On this page

# Saving drawings separately

The library API offers an alternative approach for saving charts where the drawings can be stored separately from the chart layout. This behaviour is activated by the [`saveload_separate_drawings_storage`](/charting-library-docs/v29/customization/Featuresets#saveload_separate_drawings_storage) featureset found in the library settings.

## Key advantages[​](#key-advantages "Direct link to Key advantages")

Storing drawings independently boasts several benefits:

* **Per-symbol Drawings**: Drawings can now be associated with individual symbols, enabling reuse and flexibility across different layouts or charts.
* **Efficient Data Size Management**: Separating drawings and chart layout properties potentially reduces the size of saved objects, optimizing load times and data storage on your server.

## Save load adapter[​](#save-load-adapter "Direct link to Save load adapter")

When you enable the [`saveload_separate_drawings_storage`](/charting-library-docs/v29/customization/Featuresets#saveload_separate_drawings_storage) featureset, two extra methods `saveLineToolsAndGroups` and `loadLineToolsAndGroups` are expected in your implementation of the [`IExternalSaveLoadAdapter`](/charting-library-docs/v29/api/interfaces/Charting_Library.IExternalSaveLoadAdapter) interface.

Consider the following example which implements the new methods:

```
class SaveLoadAdapterWithDrawings extends SaveLoadAdapter {  
    constructor() {  
        super();  
        this.drawings = {};  
    }  
  
    async saveLineToolsAndGroups(layoutId, chartId, state) {  
        const drawings = state.sources;  
  
        if (!this.drawings[this._getDrawingKey(layoutId, chartId)]) {  
            this.drawings[this._getDrawingKey(layoutId, chartId)] = {}  
        }  
  
        for (let [key, state] of drawings) {  
            if (state === null) {  
                delete this.drawings[this._getDrawingKey(layoutId, chartId)][key];  
            } else {  
                this.drawings[this._getDrawingKey(layoutId, chartId)][key] = state;  
            }  
        }  
    }  
  
    async loadLineToolsAndGroups(layoutId, chartId) {  
        const rawSources = this.drawings[this._getDrawingKey(layoutId, chartId)];  
        if (!rawSources) return null;  
        const sources = new Map();  
  
        for (let [key, state] of Object.entries(rawSources)) {  
            sources.set(key, state);  
        }  
        return {  
            sources  
        };  
    }  
  
    _getDrawingKey(layoutId, chartId) {  
        return `${layoutId}/${chartId}`  
    }  
}
```

### Saving drawings per symbol[​](#saving-drawings-per-symbol "Direct link to Saving drawings per symbol")

If you want to save the drawings independently of the chart layout, you can use the following TypeScript example, which extends the [localStorage example](/charting-library-docs/v29/saving_loading/save-load-adapter#localstorage).

```
const drawingSourceStorageKey = 'LocalStorageSaveLoadAdapter_drawingSourceSymbol';  
export class LocalStorageDrawingsPerSymbolSaveLoadAdapter extends LocalStorageSaveLoadAdapter {  
    private _drawingSourceSymbols: Record<string, string> = {};  
    public constructor() {  
        super();  
        this._drawingSourceSymbols = this._getFromLocalStorage<Record<string, string>>(drawingSourceStorageKey) ?? {};  
    }  
  
    protected override _saveAllToLocalStorage(): void {  
        super._saveAllToLocalStorage();  
        this._saveToLocalStorage(drawingSourceStorageKey, this._drawingSourceSymbols);  
    }  
  
    public override async saveLineToolsAndGroups(layoutId: string,  
        chartId: string | number,  
        state: LineToolsAndGroupsState): Promise<void> {  
        const drawings = state.sources;  
        if (!drawings) return;  
  
        for (let [key, state] of drawings) {  
            const symbolCheckKey = `${layoutId}/${chartId}/${key}`;  
            const symbol = state?.symbol ?? this._drawingSourceSymbols[symbolCheckKey];  
            if (!this._drawings[symbol]) this._drawings[symbol] = {};  
            if (state === null) {  
                delete this._drawings[symbol][key];  
                delete this._drawingSourceSymbols[symbolCheckKey];  
            } else {  
                this._drawings[symbol][key] = state;  
                this._drawingSourceSymbols[symbolCheckKey] = symbol;  
            }  
        }  
    }  
  
    public override async loadLineToolsAndGroups(  
        _layoutId: string | undefined,  
        _chartId: string | number,  
        _requestType: LineToolsAndGroupsLoadRequestType,  
        requestContext: LineToolsAndGroupsLoadRequestContext  
    ): Promise<Partial<LineToolsAndGroupsState> | null> {  
        // We only care about the symbol of the chart  
        const symbol = requestContext.symbol;  
        if (!symbol) return null;  
        const rawSources = this._drawings[symbol];  
        const sources = new Map();  
  
        for (let [key, state] of Object.entries(rawSources)) {  
            sources.set(key, state);  
        }  
  
        return {  
            sources  
        };  
    }  
}
```

### saveLineToolsAndGroups[​](#savelinetoolsandgroups "Direct link to saveLineToolsAndGroups")

This method lets you capture and store the current drawings state from your chart.

It accepts three parameters:

* `layoutId`: Denotes the specific chart layout
* `chartId`: Identifies a particular chart within the layout
* `state`: An instance of a `LineToolsAndGroupsState` object encapsulating the present state of the drawings

### loadLineToolsAndGroups[​](#loadlinetoolsandgroups "Direct link to loadLineToolsAndGroups")

Enables the loading of saved drawings back to the chart.

It takes these parameters:

* `layoutId`: Represents the current chart layout
* `chartId`: Specifies a distinct chart within the layout
* `requestType`: Defines the type of load request ('mainSeriesLineTools', 'lineToolsWithoutSymbol', 'allLineTools', or 'studyLineTools')
* `requestContext`: Captures contextual details for the request. It can contain specific data useful for certain custom behaviors but isn't always needed for creating the response

## REST API[​](#rest-api "Direct link to REST API")

If you use the [REST API](/charting-library-docs/v29/saving_loading/save-load-rest-api/) for chart storage, you should implement the following endpoints in addition to the endpoints mentioned in the [Develop your own storage](/charting-library-docs/v29/saving_loading/save-load-rest-api/#develop-your-own-storage) section.

### Save drawings[​](#save-drawings "Direct link to Save drawings")

`POST` request: `charts_storage_url/charts_storage_api_version/drawings?client=client_id&user=user_id&chart=chart_id&layout=layout_id`

1. `state`: `LineToolsAndGroupsState` object

RESPONSE: JSON Object

1. `status`: `ok` or `error`

### Load drawings[​](#load-drawings "Direct link to Load drawings")

`GET` request: `charts_storage_url/charts_storage_api_version/drawings?client=client_id&user=user_id&chart=chart_id&layout=layout_id`

RESPONSE: JSON Object

1. `status`: `ok` or `error`
2. `data`: Object
   1. `state`: `LineToolsAndGroupsState` object

## Low-level API methods[​](#low-level-api-methods "Direct link to Low-level API methods")

The [low-level API](/charting-library-docs/v29/saving_loading/low-level-api) has additional methods on the chart widget when you enable the [`saveload_separate_drawings_storage`](/charting-library-docs/v29/customization/Featuresets#saveload_separate_drawings_storage) featureset.

### getLineToolsState[​](#getlinetoolsstate "Direct link to getLineToolsState")

This function captures the current drawings state from the chart. You can benefit from this if you need to programmatically capture and store the drawings state.

```
const state = widget.activeChart().getLineToolsState();  
// Send or save state as required...
```

### applyLineToolsState[​](#applylinetoolsstate "Direct link to applyLineToolsState")

Enable restoring the drawings on the chart by implementing a previously saved `LineToolsAndGroupsState` object.

```
const state = // previously saved state  
widget.activeChart().applyLineToolsState(state).then(() => {  
    console.log('Drawings state restored!');  
});
```

### reloadLineToolsFromServer[​](#reloadlinetoolsfromserver "Direct link to reloadLineToolsFromServer")

Triggers a re-request of drawings from the server (via the Save Load Adapter or REST API depending on your implementation).

```
widget.activeChart().reloadLineToolsFromServer();
```

## Customizing the chart save method[​](#customizing-the-chart-save-method "Direct link to Customizing the chart save method")

The `save` method on the [`IChartingLibraryWidget`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget) interface now includes options to adjust its behavior. There is an `includeDrawings` option in `SaveChartOptions` which determines whether to include drawings in the chart layout object returned by the `save` method. This can be useful in conjunction with the [low-level API methods](#low-level-api-methods) described above.

```
widget.save(state => {  
  // Handle saved state...  
}, { includeDrawings: false });
```

## Understanding the LineToolsAndGroupsState interface[​](#understanding-the-linetoolsandgroupsstate-interface "Direct link to Understanding the LineToolsAndGroupsState interface")

The [`LineToolsAndGroupsState`](/charting-library-docs/v29/api/interfaces/Charting_Library.LineToolsAndGroupsState) interface plays a crucial role in maintaining the state of chart drawings, providing a structure for both individual drawings and drawing groups.

The `sources` property is a `Map`, which constructs key-value pairs to represent a distinct drawing. The key, in this case, is an identifier or UUID for a drawing, and the value accompanies a state object exclusive to that drawing. The state object also encapsulates the symbol associated with the drawings, adding another defining layer to the data representation.

Similarly, the `groups` property is a `Map` accounting for groups of drawings. Each key-value pair comprises an identifier key or UUID and an array of UUIDs forming the drawing group.

For both `sources` and `groups`, a UUID associated with a `null` value indicates that the respective drawing or drawing group is to be removed. This signifies when a previously existing drawing has been deleted by the user and is no longer present on the chart.

caution

It's important to note that the state objects (`LineToolState` and `LineToolsGroupState`) which represent the drawings' state should be treated essentially as black boxes. They are managed by the library and are not expected to be directly modified outside of it.

## Migration[​](#migration "Direct link to Migration")

The process of migrating chart layouts saved with the [`saveload_separate_drawings_storage`](/charting-library-docs/v29/customization/Featuresets#saveload_separate_drawings_storage) featureset, after the feature is enabled, can be undertaken following certain steps. The library will still support loading chart layouts with drawings even when the [`saveload_separate_drawings_storage`](/charting-library-docs/v29/customization/Featuresets#saveload_separate_drawings_storage) featureset is enabled. This allows you to load layouts saved using the pre-existing combined approach (when the drawings are saved in the chart layout) and then save them with the new separated approach (when this featureset is enabled).

Along with the saved data, it is recommended that you store a flag that signifies in which mode the layout was saved. Such that when you load the layout you know whether you need to migrate the data or not. Handling the saving and loading of this optional flag falls outside the API's scope and remains a detail to be implemented within your code.

To migrate a layout, listen for the [`chart_load_requested`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#chart_load_requested) event to occur and then evoke the [`saveChartToServer`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#savecharttoserver) method on the widget to trigger the layout to be saved again.

If you use the [low-level API methods](#low-level-api-methods), saving the chart layout would require storing the following two pieces of data.

```
widget.save(  
  (chartLayoutState) => {  
    const drawings = widget.activeChart().getLineToolsState();  
    // Send or save state as required...  
    //    save drawings  
    //    save chartLayoutState  
  },  
  { includeDrawings: false }  
);
```