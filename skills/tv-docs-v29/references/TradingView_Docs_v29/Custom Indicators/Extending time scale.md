# Custom Indicators: Extending time scale

Source: https://www.tradingview.com/charting-library-docs/v29/custom_studies/Studies-Extending-The-Time-Scale

* [Custom Indicators](/charting-library-docs/v29/custom_studies/)* Extending time scale

On this page

# Extending the time scale

The tick marks on the [time scale](/charting-library-docs/v29/ui_elements/Time-Scale) are defined by the times in the main series.

Most studies calculate their values from the bars of the main series. The simplest example of this is the Volume study - each bar of the main series has a volume associated with it and the Volume study simply shows that volume at the same time point as the bar. Because of this it is natural that the times of study values correspond 1-to-1 with the times of the main series.

For example, on the chart of weekly data, you can see there is one Volume bar for each bar of the main series.

![Image of a simple volume study on a chart](/charting-library-docs/v29/assets/images/simple_volume_example-03337eaa5c58a4c4652e58e2a30ee4fe.png)

## Mapping times[​](#mapping-times "Direct link to Mapping times")

In some cases a study needs to calculate its values from a series of bars that are not the same as the main series. In this case it is necessary to map each study value to the time of one of the main series' bars.

Consider the example of the built-in Moving Average study.
You can provide a symbol input that is different to the symbol of the main study. The library will resolve and then use this input to calculate the Moving Average.

The chart below has a symbol "A" for the main series and a Moving Average study for symbol "B". You can see 5 daily bars from 2022-12-26 to 2022-12-31.

![Image of a moving average study on a chart](/charting-library-docs/v29/assets/images/moving_average_adopt_example-99daf3779e01381cf21ca28ceb7ddb2a.png)

Although you cannot tell by looking at the chart in this example the symbol B actually has more bars than symbol A: symbol A is missing a bar for 2022-12-29.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A time B time Shown on chart?|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-12-26 2022-12-26 Yes|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-12-27 2022-12-27 Yes|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-12-28 2022-12-28 Yes|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-12-29 No|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 2022-12-30 2022-12-30 Yes|  |  |  | | --- | --- | --- | | 2022-12-31 2022-12-31 Yes | | | | | | | | | | | | | | | | | | | | |

By default studies can only display data at a time point on the chart if the main series has a bar at that time point. This is done by mapping (or "adopting") the values of the study that correspond to a time in the main series. There are two ways of mapping times from one series to another: precise and continuous.

### Precise mapping[​](#precise-mapping "Direct link to Precise mapping")

Precise mapping means that each bar time of the main series will be mapped to at most once.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main series time Study time Study value Displayed value|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2023-01-01 2022-01-01 1.11 1.11|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2023-01-02 2022-01-02 1.50 1.50|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-01-02 2.30 |  |  |  |  | | --- | --- | --- | --- | | 2023-01-03 2022-01-03 3.00 3.00 | | | | | | | | | | | | | | | | | | | |

### Continuous mapping[​](#continuous-mapping "Direct link to Continuous mapping")

Continuous mapping means that each main series bar time may be mapped to more than once. If the study time does not exist in the main series then the closest time greater than the study time is used.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main series time Study time Study value Displayed value|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2023-01-01 2022-01-01 1.11 1.11|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 2023-01-02 2022-01-02 1.50 1.50|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 2022-01-02 2.30 3.00|  |  |  |  | | --- | --- | --- | --- | | 2023-01-03 2022-01-03 3.00 3.00 | | | | | | | | | | | | | | | | | | | |

## Extending the time scale feature[​](#extending-the-time-scale-feature "Direct link to Extending the time scale feature")

There is a feature that allows studies to define their points on a time scale.
For studies that use this feature, the restriction that the time exists in the main series is removed.
This allows you to create custom studies that show bars at a higher resolution than the main series.
For example, you can create a study showing the weekly average of a monthly symbol.

* Monthly symbol and a weekly study on the chart* Monthly symbol on the chart

![Image of a monthly symbol and a weekly study on a chart](/charting-library-docs/v29/assets/images/extended_time_scale_example-17b3441c006b77c1567e655f6f512eac.png)

![Image of a monthly symbol on the chart](/charting-library-docs/v29/assets/images/non_extended_time_scale_example-eb0b2622e5fe5d062518716db00eaa3f.png)

There are two options available to enable the time scale extension feature:

* [for any custom study](#for-any-custom-study)
* [for the Overlay study only](#for-overlay-study)

### For any custom study[​](#for-any-custom-study "Direct link to For any custom study")

To enable the feature for any [custom study](/charting-library-docs/v29/custom_studies/), follow the steps below.

1. Enable the [`studies_extend_time_scale`](/charting-library-docs/v29/customization/Featuresets#studies_extend_time_scale) featureset.
2. Add `canExtendTimeScale: true` to the study's [metainfo](/charting-library-docs/v29/custom_studies/metainfo/).

In the example below, if a symbol input is chosen that contains more bars than the main series, the time scale will be extended to show those extra bars.
Note that the example will resolve the other symbol with the same resolution as the main series.
However, you can customize it by changing the resolution parameter.

```
{  
    name: 'Extend Time Scale Example',  
    metainfo: {  
        id: 'Extend Time Scale Example@tv-basicstudies-1',  
        name: 'Extend Time Scale Example',  
        _metainfoVersion: 51,  
        description: 'Extend Time Scale Example',  
        shortDescription: 'Extend Time Scale Example',  
        is_price_study: true,  
        defaults: {  
            styles: {  
                plot_0: {  
                    plottype: 0,  
                    visible: true,  
                    color: 'orange'  
                },  
            },  
            inputs: {  
                symbol: '',  
            }  
        },  
        plots: [{  
            id: 'plot_0',  
            type: 'line'  
        }],  
        styles: {  
            plot_0: {  
                title: 'Plot',  
            },  
        },  
        inputs: [  
            {  
                id: 'symbol',  
                name: 'Other Symbol',  
                type: 'symbol',  
            },  
        ],  
        format: { type: 'inherit' },  
        canExtendTimeScale: true, // important!  
    },  
    constructor:  
        function () {  
            this.init = function (ctx, inputCallback) {  
                this._context = ctx;  
  
                var symbol = inputCallback(0);  
                if (symbol !== '') {  
                    const resolution = PineJS.Std.period(this._context);  
                    this._context.new_sym(symbol, resolution);  
                }  
            }  
  
            this.main = function (ctx, inputCallback) {  
                this._context = ctx;  
                this._input = inputCallback;  
  
                var symbol = inputCallback(0);  
  
                if (symbol !== '') {  
                    this._context.select_sym(1);  
                }  
  
                var close = this._context.new_var(PineJS.Std.close(this._context));  
  
                return [close];  
            };  
        }  
}
```

### For Overlay study[​](#for-overlay-study "Direct link to For Overlay study")

The library includes the built-in Overlay study, which allows you to display multiple symbols on a single chart for easy comparison.
To make [compared symbols](/charting-library-docs/v29/ui_elements/indicators/#add-and-compare-new-series) extend the time scale, enable the [`secondary_series_extend_time_scale`](/charting-library-docs/v29/customization/Featuresets#secondary_series_extend_time_scale) featureset.
This featureset only applies to the Overlay study and enables the *Allow extend time scale* option within the *Compare symbol* dialog.

For example, when comparing BTCUSD to AAPL, you can see the points on the time scale where only BTCUSD has data.
The image below shows that the upper chart allows the Overlay study to extend the time scale, while the bottom chart does not.

![Extending time scale when comparing BTCUSD with AAPL](/charting-library-docs/v29/assets/images/extended-time-scale-for-overlay-c0e98b44b9386e2d1da4e876280d0add.png)