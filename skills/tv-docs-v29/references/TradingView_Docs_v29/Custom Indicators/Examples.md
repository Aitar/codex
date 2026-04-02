# Custom Indicators: Examples

Source: https://www.tradingview.com/charting-library-docs/v29/custom_studies/Custom-Studies-Examples

* [Custom Indicators](/charting-library-docs/v29/custom_studies/)* Examples

On this page

# Custom Studies Examples

## Requesting Data for Another Ticker[​](#requesting-data-for-another-ticker "Direct link to Requesting Data for Another Ticker")

1. Come up with a new ticker name to display your data and set up your server to return valid SymbolInfo for this new ticker.
2. Also, set up the server to return valid historical data for this ticker.
3. Add [custom\_indicators\_getter](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_indicators_getter) key to the widget constructor. Its value is a function that returns a Promise object with a list of custom indicators.
4. *(Optional)* Update your widget's initialization code to [create](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudy) this indicator when the chart is ready.

* JavaScript* TypeScript

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            name: 'Equity',  
            metainfo: {  
                _metainfoVersion: 51,  
                id: 'Equity@tv-basicstudies-1',  
                description: 'Equity',  
                shortDescription: 'Equity',  
                is_price_study: true,  
                isCustomIndicator: true,  
                format: {  
                    type: 'price',  
                    // Precision is set to one digit, e.g. 777.7  
                    precision: 1,  
                },  
  
                plots: [{id: 'plot_0', type: 'line'}],  
                defaults: {  
                    styles: {  
                        plot_0: {  
                            linestyle: 0,  
                            visible: true,  
  
                            // Make the line thinner  
                            linewidth: 1,  
  
                            // Plot type is Line  
                            plottype: 2,  
  
                            // Show price line  
                            trackPrice: true,  
  
                            // Set the plotted line color to dark red  
                            color: '#880000'  
                        }  
                    },  
  
                    inputs: {}  
                },  
                styles: {  
                    plot_0: {  
                        // Output name will be displayed in the Style window  
                        title: 'Equity value',  
                        histogramBase: 0,  
                    }  
                },  
                inputs: [],  
            },  
  
            constructor: function() {  
                this.init = function(context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    // Define the symbol to be plotted.  
                    // Symbol should be a string.  
                    // You can use PineJS.Std.ticker(this._context) to get the selected symbol's ticker.  
                    // For example,  
                    //    var symbol = 'AAPL';  
                    //    var symbol = '#EQUITY';  
                    //    var symbol = PineJS.Std.ticker(this._context) + '#TEST';  
                    const symbol = '#EQUITY'; // #EQUITY should be replaced with the symbol you want to resolve  
                    this._context.new_sym(symbol, PineJS.Std.period(this._context));  
                };  
  
                this.main = function(context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
                    // Select the main symbol  
                    this._context.select_sym(0);  
                    const mainSymbolTime = this._context.new_var(this._context.symbol.time);  
  
                    // Select the secondary symbol  
                    this._context.select_sym(1);  
                    const secondarySymbolTime = this._context.new_var(this._context.symbol.time);  
  
                    // Align the times of the secondary symbol to the main symbol  
                    const secondarySymbolClose  = this._context.new_var(PineJS.Std.close(this._context));  
                    const alignedClose = secondarySymbolClose.adopt(secondarySymbolTime, mainSymbolTime, 1);  
  
                    // Select the main symbol again  
                    this._context.select_sym(0);  
  
                    return [alignedClose];  
                }  
            }  
        }  
    ]);  
},
```

```
/* Within the Widget constructor options */  
custom_indicators_getter: PineJS => {  
    return Promise.resolve<CustomIndicator[]>([  
  
        /* Requesting data for another ticker */  
        {  
            name: 'Equity',  
            metainfo: {  
                _metainfoVersion: 51,  
                id: 'Equity@tv-basicstudies-1' as RawStudyMetaInfoId,  
                description: 'Equity',  
                shortDescription: 'Equity',  
                is_price_study: true,  
                isCustomIndicator: true,  
                format: {  
                    type: 'price',  
                    // Precision is set to one digit, e.g. 777.7  
                    precision: 1,  
                },  
  
                plots: [{ id: 'plot_0', type: StudyPlotType.Line }],  
                defaults: {  
                    styles: {  
                        plot_0: {  
                            linestyle: 0,  
                            visible: true,  
  
                            // Make the line thinner  
                            linewidth: 1,  
  
                            // Plot type is Line  
                            plottype: 2 as StudyLinePlotPreferences['plottype'],  
  
                            // Show price line  
                            trackPrice: true,  
  
                            // Set the plotted line color to dark red  
                            color: '#880000',  
                        },  
                    },  
  
                    inputs: {},  
                },  
                styles: {  
                    plot_0: {  
                        // Output name will be displayed in the Style window  
                        title: 'Equity value',  
                        histogramBase: 0,  
                    },  
                },  
                inputs: [],  
            },  
  
            constructor: function (  
                this: LibraryPineStudy<IPineStudyResult>  
            ) {  
                this.init = function (context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    const symbol = '#EQUITY'; // #EQUITY should be replaced with the symbol you want to resolve  
                    this._context.new_sym(  
                        symbol,  
                        PineJS.Std.period(this._context)  
                    );  
                };  
  
                this.main = function (context, inputCallback) {  
                       this._context = context;  
                    this._input = inputCallback;  
                    // Select the main symbol  
                    this._context.select_sym(0);  
                    const mainSymbolTime = this._context.new_var(this._context.symbol.time);  
  
                    // Select the secondary symbol ("#EQUITY")  
                    this._context.select_sym(1);  
                    const secondarySymbolTime = this._context.new_var(this._context.symbol.time);  
  
                    // Align the times of the secondary symbol to the main symbol  
                    const secondarySymbolClose  = this._context.new_var(PineJS.Std.close(this._context));  
                    const alignedClose = secondarySymbolClose.adopt(secondarySymbolTime, mainSymbolTime, 1);  
  
                    // Select the main symbol again  
                    this._context.select_sym(0);  
  
                    return [alignedClose];  
                };  
            },  
        },  
    ]);  
},
```

## Coloring Bars[​](#coloring-bars "Direct link to Coloring Bars")

![/img/bar_colorer.png](data:image/png;base64,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)

* JavaScript* TypeScript

```
custom_indicators_getter: function (PineJS) {  
    return Promise.resolve([  
        {  
            name: 'Bar Colorer Demo',  
            metainfo: {  
                _metainfoVersion: 51,  
  
                id: "BarColoring@tv-basicstudies-1",  
                name: "BarColoring",  
                description: "Bar Colorer Demo",  
                shortDescription: "Bar Coloring",  
  
                isCustomIndicator: true,  
                is_price_study: true,  
  
                format: {  
                    type: 'price',  
                    precision: 4,  
                },  
  
                defaults: {  
                    palettes: {  
                        palette_0: {  
                            // palette colors  
                            // change it to the default colors that you prefer,  
                            // but note that the user can change them in the Style tab  
                            // of indicator properties  
                            colors: [  
                                { color: '#FFFF00' },  
                                { color: '#0000FF' }  
                            ]  
                        }  
                    }  
                },  
                inputs: [],  
                plots: [{  
                    id: 'plot_0',  
  
                    // plot type should be set to 'bar_colorer'  
                    type: 'bar_colorer',  
  
                    // this is the name of the palette that is defined  
                    // in 'palettes' and 'defaults.palettes' sections  
                    palette: 'palette_0'  
                }],  
                palettes: {  
                    palette_0: {  
                        colors: [  
                            { name: 'Color 0' },  
                            { name: 'Color 1' }  
                        ],  
  
                        // the mapping between the values that  
                        // are returned by the script and palette colors  
                        valToIndex: {  
                            100: 0,  
                            200: 1  
                        }  
                    }  
                }  
            },  
            constructor: function() {  
                this.main = function(context, input) {  
                    this._context = context;  
                    this._input = input;  
  
                    var valueForColor0 = 100;  
                    var valueForColor1 = 200;  
  
                    // perform your calculations here and return one of the constants  
                    // that is specified as a key in 'valToIndex' mapping  
                    var result =  
                        Math.random() * 100 % 2 > 1 ? // we randomly select one of the color values  
                            valueForColor0 : valueForColor1;  
  
                    return [result];  
                }  
            }  
        }  
    ]);  
},
```

```
/* Within the Widget constructor options */  
custom_indicators_getter: PineJS => {  
    return Promise.resolve<CustomIndicator[]>([  
  
        /* Coloring bars */  
        {  
            name: 'Bar Colorer Demo',  
            metainfo: {  
                _metainfoVersion: 51,  
  
                id: 'BarColoring@tv-basicstudies-1' as RawStudyMetaInfoId,  
                name: 'BarColoring',  
                description: 'Bar Colorer Demo',  
                shortDescription: 'BarColoring',  
  
                isCustomIndicator: true,  
                is_price_study: true,  
  
                format: {  
                    type: 'price',  
                    precision: 4,  
                },  
  
                defaults: {  
                    palettes: {  
                        palette_0: {  
                            // palette colors  
                            // change it to the default colors that you prefer,  
                            // but note that the user can change them in the Style tab  
                            // of indicator properties  
                            colors: [{ color: '#FFFF00' }, { color: '#0000FF' }],  
                        },  
                    },  
                },  
                inputs: [],  
                plots: [  
                    {  
                        id: 'plot_0',  
  
                        // plot type should be set to 'bar_colorer'  
                        type: StudyPlotType.BarColorer,  
  
                        // this is the name of the palette that is defined  
                        // in 'palettes' and 'defaults.palettes' sections  
                        palette: 'palette_0',  
                    },  
                ],  
                palettes: {  
                    palette_0: {  
                        colors: [{ name: 'Color 0' }, { name: 'Color 1' }],  
  
                        // the mapping between the values that  
                        // are returned by the script and palette colors  
                        valToIndex: {  
                            100: 0,  
                            200: 1,  
                        },  
                    },  
                },  
            },  
            constructor: function (  
                this: LibraryPineStudy<IPineStudyResult>  
            ) {  
                this.main = function (context, input) {  
                    this._context = context;  
                    this._input = input;  
  
                    const valueForColor0 = 100;  
                    const valueForColor1 = 200;  
  
                    // perform your calculations here and return one of the constants  
                    // that is specified as a key in 'valToIndex' mapping  
                    const result =  
                        (Math.random() * 100) % 2 > 1 // we randomly select one of the color values  
                            ? valueForColor0  
                            : valueForColor1;  
  
                    return [result];  
                };  
            },  
        },  
    ]);  
},
```

## Custom Styles for Every Point[​](#custom-styles-for-every-point "Direct link to Custom Styles for Every Point")

![/img/custom_styles_for_every_point.png](/charting-library-docs/v29/assets/images/custom_styles_for_every_point-417160519d071500e84be1dacf63e2c4.png)

* JavaScript* TypeScript

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            name: 'Custom Styles For Every Point',  
            metainfo: {  
                _metainfoVersion: 51,  
                id: 'CustomStylesForEveryPoint@tv-basicstudies-1',  
                description: 'Custom Styles For Every Point',  
                shortDescription: 'Custom Styles For Every Point',  
                is_price_study: false,  
                isCustomIndicator: true,  
                plots: [  
                    {  
                        'id': 'plot_0',  
                        'type': 'line',  
                    },  
                    {  
                        'id': 'plot_1',  
                        'type': 'colorer',  
                        'target': 'plot_0',  
                        'palette': 'paletteId1',  
                    },  
                ],  
                palettes: {  
                    paletteId1: {  
                        colors: {  
                            0: {  
                                    name: 'First color',  
                            },  
                            1: {  
                                    name: 'Second color',  
                            },  
                        },  
                    },  
                },  
                defaults: {  
                    palettes: {  
                        paletteId1: {  
                            colors: {  
                                0: {  
                                    color: 'red',  
                                    width: 1,  
                                    style: 0,  
                                },  
                                1: {  
                                    color: 'blue',  
                                    width: 3,  
                                    style: 1,  
                                },  
                            },  
                        },  
                    },  
                    styles: {},  
                    precision: 4,  
                    inputs: {},  
                },  
                styles: {  
                    plot_0: {  
                        title: 'Equity value',  
                        histogramBase: 0,  
                    },  
                },  
                inputs: [],  
                format: {  
                    type: 'price',  
                    precision: 4,  
                },  
            },  
            constructor: function() {  
                this.main = function(context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    const value = Math.random() * 200;  
                    const colorIndex = value > 100 ? 0 : 1;  
  
                    return [value, colorIndex];  
                }  
            }  
        }  
    ]);  
},
```

```
/* Within the Widget constructor options */  
custom_indicators_getter: PineJS => {  
    return Promise.resolve<CustomIndicator[]>([  
  
        /* Custom styles for every point */  
       {  
            name: 'Custom Styles For Every Point',  
            metainfo: {  
                _metainfoVersion: 51,  
                id: 'CustomStylesForEveryPoint@tv-basicstudies-1' as RawStudyMetaInfoId,  
                description: 'Custom Styles For Every Point',  
                shortDescription: 'Custom Styles For Every Point',  
                is_price_study: false,  
                isCustomIndicator: true,  
                plots: [  
                    {  
                        id: 'plot_0',  
                        type: StudyPlotType.Line,  
                    },  
                    {  
                        id: 'plot_1',  
                        type: StudyPlotType.Colorer,  
                        target: 'plot_0',  
                        palette: 'paletteId1',  
                    },  
                ],  
                palettes: {  
                    paletteId1: {  
                        colors: {  
                            0: {  
                                name: 'First color',  
                            },  
                            1: {  
                                name: 'Second color',  
                            },  
                        },  
                    },  
                },  
                defaults: {  
                    palettes: {  
                        paletteId1: {  
                            colors: {  
                                0: {  
                                    color: 'red',  
                                    width: 1,  
                                    style: 0,  
                                },  
                                1: {  
                                    color: 'blue',  
                                    width: 3,  
                                    style: 1,  
                                },  
                            },  
                        },  
                    },  
                    styles: {},  
                    precision: 4,  
                    inputs: {},  
                },  
                styles: {  
                    plot_0: {  
                        title: 'Equity value',  
                        histogramBase: 0,  
                    },  
                },  
                inputs: [],  
                format: {  
                    type: 'price',  
                    precision: 4,  
                },  
            },  
            constructor: function (  
                this: LibraryPineStudy<IPineStudyResult>  
            ) {  
                this.main = function (context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    const value = Math.random() * 200;  
                    const colorIndex = value > 100 ? 0 : 1;  
  
                    return [value, colorIndex];  
                };  
            },  
        },  
    ]);  
},
```

## Complex Filled Areas[​](#complex-filled-areas "Direct link to Complex Filled Areas")

See the Pen [Complex Filled Areas](https://codepen.io/tradingview/pen/mdYEjdW) by TradingView ([@tradingview](https://codepen.io/tradingview))
on [CodePen](https://codepen.io).

## Advanced Shapes Use[​](#advanced-shapes-use "Direct link to Advanced Shapes Use")

![/img/advanced_shapes_use.png](/charting-library-docs/v29/assets/images/advanced_shapes_use-64e071e8f356ff318f548fe27e21169b.png)

* JavaScript* TypeScript

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            name: 'Mondays',  
            metainfo: {  
                _metainfoVersion: 51,  
                defaults: {  
                    styles: {  
                        plot_0: {  
                            color: '#FF5252',  
                            textColor: '#2196F3',  
                            plottype: 'shape_circle',  
                            location: 'Bottom',  
                            visible: true  
                        }  
                    },  
                    inputs: {}  
                },  
                plots: [  
                    {  
                        id: 'plot_0',  
                        type: 'shapes'  
                    }  
                ],  
                styles: {  
                    plot_0: {  
                        isHidden: false,  
                        location: 'Bottom',  
                        text: 'Monday',  
                        title: 'Shapes'  
                    }  
                },  
                description: 'Mondays',  
                shortDescription: 'Mondays',  
                is_price_study: true,  
                inputs: [],  
                id: 'Mondays@tv-basicstudies-1',  
                format: {  
                    type: 'inherit',  
                },  
            },  
            constructor: function() {  
                this.main = function(context, inputCallback) {  
                    // If we don't have a time, then we cannot determine the day of week  
                    if (isNaN(context.symbol.time)) {  
                        return [NaN]  
                    }  
  
                    // Check if the day of the week is Monday  
                    const dayofweek = PineJS.Std.dayofweek(context);  
                    const shouldBeShapeVisible = dayofweek === 2;  
                    // 1 is plot value, it'll be displayed in legend of the indicator  
                    // NaN means that there is no value for that plot and shape should be hidden for that bar  
                    const plotValue = shouldBeShapeVisible ? 1 : NaN;  
                    return [plotValue];  
                }  
            }  
        },  
    ]);  
},
```

```
/* Within the Widget constructor options */  
custom_indicators_getter: PineJS => {  
    return Promise.resolve<CustomIndicator[]>([  
  
       /* Advanced Shapes use */  
        {  
            name: 'Mondays',  
            metainfo: {  
                _metainfoVersion: 51,  
                defaults: {  
                    styles: {  
                        plot_0: {  
                            color: '#FF5252',  
                            textColor: '#2196F3',  
                            plottype: 'shape_circle' as StudyShapesPlotPreferences['plottype'],  
                            location: 'Bottom' as StudyShapesPlotPreferences['location'],  
                            visible: true  
                        }  
                    },  
                    inputs: {},  
                },  
                plots: [  
                    {  
                        id: 'plot_0',  
                        type: StudyPlotType.Shapes,  
                    },  
                ],  
                styles: {  
                    plot_0: {  
                        isHidden: false,  
                        location: 'Bottom' as StudyShapesPlotPreferences['location'],  
                        plottype: 'shape_circle' as StudyShapesPlotPreferences['plottype'],  
                        text: 'Monday',  
                        title: 'Shapes',  
                    },  
                },  
                description: 'Mondays',  
                shortDescription: 'Mondays',  
                is_price_study: true,  
                inputs: [],  
                id: 'Mondays@tv-basicstudies-1' as RawStudyMetaInfoId,  
                format: {  
                    type: 'inherit',  
                },  
            },  
            constructor: function (  
                this: LibraryPineStudy<IPineStudyResult>  
            ) {  
                this.main = function (context, inputCallback) {  
                    // If we don't have a time, then we cannot determine the day of week  
                    if (isNaN(context.symbol.time)) {  
                        return [NaN]  
                    }  
  
                    // Check if the day of the week is Monday  
                    const dayofweek = PineJS.Std.dayofweek(context);  
                    const shouldBeShapeVisible = dayofweek === 2;  
                    // 1 is plot value, it'll be displayed in legend of the indicator  
                    // NaN means that there is no value for that plot and shape should be hidden for that bar  
                    const plotValue = shouldBeShapeVisible ? 1 : NaN;  
                    return [plotValue];  
                };  
            },  
        },  
    ]);  
},
```

## Advanced Colouring Candles[​](#advanced-colouring-candles "Direct link to Advanced Colouring Candles")

![/img/colouring_candles.png](/charting-library-docs/v29/assets/images/colouring_candles-585dac0a7e311183c0a7b92c23771aa8.png)

* JavaScript* TypeScript

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            name: 'Advanced Coloring Candles',  
            metainfo: {  
                _metainfoVersion: 51,  
  
                id: 'advancedcolouringcandles@tv-basicstudies-1',  
                name: 'Advanced Coloring Candles',  
                description: 'Advanced Coloring Candles',  
                shortDescription: 'Advanced Coloring Candles',  
  
                isCustomIndicator: true,  
  
                is_price_study: false, // whether the study should appear on the main series pane.  
                linkedToSeries: true, // whether the study price scale should be the same as the main series one.  
  
                format: {  
                    type: 'price',  
                    precision: 2,  
                },  
  
                plots: [  
                    {  
                        id: 'plot_open',  
                        type: 'ohlc_open',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_high',  
                        type: 'ohlc_high',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_low',  
                        type: 'ohlc_low',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_close',  
                        type: 'ohlc_close',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_bar_color',  
                        type: 'ohlc_colorer',  
                        palette: 'palette_bar',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_wick_color',  
                        type: 'wick_colorer',  
                        palette: 'palette_wick',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_border_color',  
                        type: 'border_colorer',  
                        palette: 'palette_border',  
                        target: 'plot_candle',  
                    },  
                ],  
  
                palettes: {  
                    palette_bar: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                    palette_wick: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                    palette_border: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                },  
  
                ohlcPlots: {  
                    plot_candle: {  
                        title: 'Candles',  
                    },  
                },  
  
                defaults: {  
                    ohlcPlots: {  
                        plot_candle: {  
                            borderColor: '#000000',  
                            color: '#000000',  
                            drawBorder: true,  
                            drawWick: true,  
                            plottype: 'ohlc_candles',  
                            visible: true,  
                            wickColor: '#000000',  
                        },  
                    },  
  
                    palettes: {  
                        palette_bar: {  
                            colors: [  
                                { color: '#1948CC', width: 1, style: 0 },  
                                { color: '#F47D02', width: 1, style: 0 },  
                            ],  
                        },  
                        palette_wick: {  
                            colors: [  
                                { color: '#0C3299', },  
                                { color: '#E65000', },  
                            ],  
                        },  
                        palette_border: {  
                            colors: [  
                                { color: '#5B9CF6', },  
                                { color: '#FFB74D', },  
                            ],  
                        },  
                    },  
  
                    precision: 2,  
                    inputs: {},  
                },  
                styles: {},  
                inputs: [],  
            },  
            constructor: function () {  
                this.main = function (context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    this._context.select_sym(0);  
  
                    const o = PineJS.Std.open(this._context);  
                    const h = PineJS.Std.high(this._context);  
                    const l = PineJS.Std.low(this._context);  
                    const c = PineJS.Std.close(this._context);  
  
                    // Color is determined randomly  
                    const colour = Math.round(Math.random());  
                    return [o, h, l, c, colour /*bar*/, colour /*wick*/, colour /*border*/];  
                };  
            },  
        },  
    ]);  
},
```

```
/* Within the Widget constructor options */  
custom_indicators_getter: PineJS => {  
    return Promise.resolve<CustomIndicator[]>([  
  
       /* Advanced Colouring Candles */  
        {  
            name: 'Advanced Coloring Candles',  
            metainfo: {  
                _metainfoVersion: 51,  
  
                id: 'advancedcolouringcandles@tv-basicstudies-1' as RawStudyMetaInfoId,  
                name: 'Advanced Coloring Candles',  
                description: 'Advanced Coloring Candles',  
                shortDescription: 'Advanced Coloring Candles',  
  
                isCustomIndicator: true,  
  
                is_price_study: false, // whether the study should appear on the main series pane.  
                linkedToSeries: true, // whether the study price scale should be the same as the main series one.  
  
                format: {  
                    type: 'price',  
                    precision: 2,  
                },  
  
                plots: [  
                    {  
                        id: 'plot_open',  
                        type: StudyPlotType.OhlcOpen,  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_high',  
                        type: StudyPlotType.OhlcHigh,  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_low',  
                        type: StudyPlotType.OhlcLow,  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_close',  
                        type: StudyPlotType.OhlcClose,  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_bar_color',  
                        type: StudyPlotType.OhlcColorer,  
                        palette: 'palette_bar',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_wick_color',  
                        type: StudyPlotType.CandleWickColorer,  
                        palette: 'palette_wick',  
                        target: 'plot_candle',  
                    },  
                    {  
                        id: 'plot_border_color',  
                        type: StudyPlotType.CandleBorderColorer,  
                        palette: 'palette_border',  
                        target: 'plot_candle',  
                    },  
                ],  
  
                palettes: {  
                    palette_bar: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                    palette_wick: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                    palette_border: {  
                        colors: [{ name: 'Colour One' }, { name: 'Colour Two' }],  
  
                        valToIndex: {  
                            0: 0,  
                            1: 1,  
                        },  
                    },  
                },  
  
                ohlcPlots: {  
                    plot_candle: {  
                        title: 'Candles',  
                    },  
                },  
  
                defaults: {  
                    ohlcPlots: {  
                        plot_candle: {  
                            borderColor: '#000000',  
                            color: '#000000',  
                            drawBorder: true,  
                            drawWick: true,  
                            plottype: OhlcStudyPlotStyle.OhlcCandles,  
                            visible: true,  
                            wickColor: '#000000',  
                        },  
                    },  
  
                    palettes: {  
                        palette_bar: {  
                            colors: [  
                                { color: '#1948CC', width: 1, style: 0 },  
                                { color: '#F47D02', width: 1, style: 0 },  
                            ],  
                        },  
                        palette_wick: {  
                            colors: [{ color: '#0C3299' }, { color: '#E65000' }],  
                        },  
                        palette_border: {  
                            colors: [{ color: '#5B9CF6' }, { color: '#FFB74D' }],  
                        },  
                    },  
  
                    precision: 2,  
                    inputs: {},  
                },  
                styles: {},  
                inputs: [],  
            },  
            constructor: function (  
                this: LibraryPineStudy<IPineStudyResult>  
            ) {  
                this.main = function (context, inputCallback) {  
                    this._context = context;  
                    this._input = inputCallback;  
  
                    this._context.select_sym(0);  
  
                    const o = PineJS.Std.open(this._context);  
                    const h = PineJS.Std.high(this._context);  
                    const l = PineJS.Std.low(this._context);  
                    const c = PineJS.Std.close(this._context);  
  
                    // Color is determined randomly  
                    const colour = Math.round(Math.random());  
                    return [  
                        o,  
                        h,  
                        l,  
                        c,  
                        colour /*bar*/,  
                        colour /*wick*/,  
                        colour /*border*/,  
                    ];  
                };  
            },  
        },  
    ]);  
},
```