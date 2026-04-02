# Custom Indicators: Metainfo

Source: https://www.tradingview.com/charting-library-docs/v29/custom_studies/metainfo/

* [Custom Indicators](/charting-library-docs/v29/custom_studies/)* Metainfo

On this page

# Metainfo

## Overview[​](#overview "Direct link to Overview")

`metainfo` is a required field in the [`CustomIndicator`](/charting-library-docs/v29/api/interfaces/Charting_Library.CustomIndicator) object that you should specify to create a [custom indicator](/charting-library-docs/v29/custom_studies/).

```
custom_indicators_getter: function(PineJS) {  
    return Promise.resolve([  
        {  
            // Indicator object  
            metainfo: {  
                // ...  
            },  
            // ...  
        }  
    ]);  
},
```

This field defines [plot](/charting-library-docs/v29/getting_started/glossary#plot) types that represent the indicator and contains the indicator's metadata, such as a name, description, style defaults, colors, plot types, inputs, and more.
The information should be arranged in a specific format and supplied as a [`StudyMetaInfo`](/charting-library-docs/v29/api/modules/Charting_Library#studymetainfo) object. The indicator's *Settings* dialog is generated based on this object.

info

`StudyMetaInfo` is initialized once and cannot be changed after the chart is created.

This article describes the most important `StudyMetaInfo` properties. You can find the complete list of properties in the [API](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo) section.

tip

Consider the [how-to guide](/charting-library-docs/v29/tutorials/create-custom-indicator/metainfo-implementation) that demonstrates an example of the `metainfo` implementation.

## Service information[​](#service-information "Direct link to Service information")

You should specify the properties below to provide service information on the indicator.

### \_metainfoVersion[​](#_metainfoversion "Direct link to _metainfoVersion")

The [`_metainfoVersion`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#_metainfoversion) property represents a version number of metadata. The current version is `53`, and the default one is `0`. Even though this property is optional, we recommend that you always specify it and use the latest version. Therefore, your indicator is more compatible with newer versions of the library.

```
metainfo: {  
    // ...  
    _metainfoVersion: 53,  
}
```

### id[​](#id "Direct link to id")

The [`id`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#id) property is a string that has the `<study name>@tv-basicstudies-1` format. The `id` value should be unique.

```
metainfo: {  
    // ...  
    id: 'Custom indicator@tv-basicstudies-1',  
}
```

## Indicator name[​](#indicator-name "Direct link to Indicator name")

You should use the properties below to specify the indicator's name in the UI.

### description[​](#description "Direct link to description")

The [`description`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#description) property contains the indicator's name that is displayed in the *Indicators* dialog and the *Object Tree*. You should use the `description` value as a `name` argument if you create an indicator using the [`createStudy`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudy) method.

![Indicator&#39;s description](/charting-library-docs/v29/assets/images/description-property-9f4e31c9669a89c071b1501cde1b4832.png)

```
metainfo: {  
    // ...  
    description: 'Custom Indicator',  
}
```

### shortDescription[​](#shortdescription "Direct link to shortDescription")

The [`shortDescription`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#shortdescription) property contains the indicator's name that is displayed in the [*Legend*](/charting-library-docs/v29/ui_elements/Legend), the *Settings* dialog, and the corresponding label on the [*Price Scale*](/charting-library-docs/v29/ui_elements/Price-Scale).

![Short description of indicator](/charting-library-docs/v29/assets/images/short-description-92484c2a1028ff0b132ae2e1cba9d78a.png)

```
metainfo: {  
    // ...  
    shortDescription: 'Custom Indicator Short Description',  
}
```

## Data[​](#data "Direct link to Data")

You should use the properties below to specify data that the indicator uses.

### format[​](#format "Direct link to format")

Depending on the indicator data, the [*Price Scale*](/charting-library-docs/v29/ui_elements/Price-Scale) displays price, volume, or percent values. To specify the indicator's data type, assign either a [`StudyPlotValueInheritFormat`](/charting-library-docs/v29/api/interfaces/Charting_Library.StudyPlotValueInheritFormat) or [`StudyPlotValuePrecisionFormat`](/charting-library-docs/v29/api/interfaces/Charting_Library.StudyPlotValuePrecisionFormat) object to the [`format`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#format) property.

If the data has the same type and precision as the [source symbol](/charting-library-docs/v29/getting_started/glossary#source-symbol), create a `StudyPlotValueInheritFormat` object with the `type` property set to `inherit`.
Otherwise, create a `StudyPlotValuePrecisionFormat` object with the desired `type` and `precision`. For example, the code sample below specifies price values with two decimal places.

```
metainfo: {  
    // ...  
    format: {precision: 2, type: 'price'},  
}
```

### inputs[​](#inputs "Direct link to inputs")

The [`inputs`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#inputs) property defines input parameters that the indicator has. Input properties depend on the [input type](/charting-library-docs/v29/api/modules/Charting_Library#studyinputinfo).

```
metainfo: {  
    // ...  
    inputs: [  
        {  
            id: "length",  
            name: "Length",  
            defval: 9,  
            type: "integer",  
            min: 1,  
            max: 10000,  
        },  
        {  
            id: "source",  
            name: "Source",  
            defval: "close",  
            type: "source",  
            options: [  
                "open",  
                "high",  
                "low",  
                "close",  
                "hl2",  
                "hlc3",  
                "ohlc4",  
            ],  
        },  
    ]  
}
```

Options on the *Inputs* tab of the *Settings* dialog are generated based on `inputs`. Additionally, you should specify default values for input parameters in [`defaults`](#defaults).

```
metainfo: {  
    // ...  
    defaults: {  
        // ...  
        inputs: {  
            length: 9,  
            source: "close",  
        },  
    }  
}
```

![Inputs](/charting-library-docs/v29/assets/images/inputs-custom-indicator-3bea3a4208fb6aa48883cd1fd9e4549f.png)

Refer to the [Inputs](/charting-library-docs/v29/custom_studies/metainfo/Custom-Studies-Inputs) article for more information.

### symbolSource[​](#symbolsource "Direct link to symbolSource")

The [`symbolSource`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#symbolsource) property allows you to specify a symbol that will be used as a data source for the indicator. The default source is the main [series](/charting-library-docs/v29/getting_started/glossary#series) that represents the main symbol on the chart.

## Visual representation[​](#visual-representation "Direct link to Visual representation")

You should use the properties below to specify visual elements that the indicator consists of.

### plots[​](#plots "Direct link to plots")

The [`plots`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#plots) property defines simple elements, for example, lines and drawings, that the indicator consists of. Refer to the [StudyPlotType](/charting-library-docs/v29/api/enums/Charting_Library.StudyPlotType) page to see the list of all plot types.

```
metainfo: {  
    // ...  
    plots: [  
        {  
            id: 'plot_0',  
            type: 'line',  
        },  
    ],  
}
```

Each plot requires additional information that should be specified in [`styles`](#styles) and [`defaults`](#defaults).

```
metainfo: {  
    // ...  
    defaults: {  
        // ...  
        styles: {  
            plot_0: {  
                linestyle: 0,  
                linewidth: 1,  
                plottype: 1,  
                trackPrice: false,  
                transparency: 0,  
                visible: true,  
                color: '#000080',  
            }  
        },  
    },  
    styles: {  
        plot_0: {  
            title: "Plot",  
            histogramBase: 0,  
            joinPoints: false,  
        },  
    },  
}
```

For more information about plots, refer to the [Custom Studies Plots](/charting-library-docs/v29/custom_studies/Custom-Studies-Plots) article.

### ohlcPlots[​](#ohlcplots "Direct link to ohlcPlots")

The [`ohlcPlots`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#ohlcplots) property defines open-high-low-close (OHLC) plots that are used to display OHLC indicators.
Refer to the [Custom Studies OHLC](/charting-library-docs/v29/custom_studies/Custom-Studies-OHLC-Plots) article for more information.

### bands[​](#bands "Direct link to bands")

The [`bands`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#bands) property defines bands (horizontal lines) and their settings that users cannot change.

![Bands](/charting-library-docs/v29/assets/images/bands-755c6be9e65db211ac47b7dfc63b7373.png)

```
metainfo: {  
    // ...  
    bands: [  
        {  
            id: 'hline_0',  
            name: 'UpperLimit',  
            zorder: -1.1,  
        },  
        {  
            id: 'hline_1',  
            name: 'LowerLimit',  
            zorder: -1.11,  
        },  
    ]  
}
```

Additionally, you should specify default values for settings that the user can change on the *Styles* tab, for example, colors and styles, in the [`defaults`](#defaults) properties.

```
metainfo: {  
    // ...  
    // ...  
    defaults: {  
        bands: [  
            {  
                color: '#787B86',  
                linestyle: 2,  
                linewidth: 1,  
                visible: true,  
                value: 1,  
            },  
            {  
                color: '#787B86',  
                linestyle: 2,  
                linewidth: 1,  
                visible: true,  
                value: 0,  
            }  
        ]  
    }  
}
```

![Bands in UI](/charting-library-docs/v29/assets/images/bands-ui-settings-81021018fea423b59321b7ada1d04aa0.png)

### filledAreas[​](#filledareas "Direct link to filledAreas")

The [`filledAreas`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#filledareas) property defines color areas. These areas can be drawn between two [plot](#plots) lines or two [bands](#bands), but not between a band and a plot line.
Consider the [Complex Filled Areas](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#complex-filled-areas) example that shows how to use `filledAreas`.

![Bands](/charting-library-docs/v29/assets/images/filled-area-13dd65b40f1a2cb7493517b9f0d91955.png)
![Filled Areas in UI](/charting-library-docs/v29/assets/images/filled-areas-ui-settings-ea7b21aea988ca2230b3e66d8f40e591.png)

## Appearance and visibility[​](#appearance-and-visibility "Direct link to Appearance and visibility")

You should use the properties below to specify the indicator's appearance.

### defaults[​](#defaults "Direct link to defaults")

The [`defaults`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#defaults) property contains default values for other properties in [`StudyMetaInfo`](/charting-library-docs/v29/api/modules/Charting_Library#studymetainfo) like [`plots`](#plots), [`inputs`](#inputs), [`styles`](#styles), and others. In the *Settings* dialog, users can reset all settings or override default values using the *Defaults* dropdown list.

![Defaults dropdown list](/charting-library-docs/v29/assets/images/defaults-ui-700c6cc5962552892f1156f2976f1afa.png)

All properties that you can specify in `defaults` are listed in [`StudyDefaults`](/charting-library-docs/v29/api/interfaces/Charting_Library.StudyDefaults). Refer to the [Custom Studies Defaults](/charting-library-docs/v29/custom_studies/metainfo/Custom-Studies-Defaults) for more information.

### styles[​](#styles "Direct link to styles")

The [`styles`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#styles) property contains style settings for each plot defined in [`plots`](#plots). Users cannot change these settings in the UI.

```
metainfo: {  
    // ...  
    styles: {  
        plot_0: {  
            title: 'Plot',  
            histogramBase: 0,  
            joinPoints: false,  
        }  
    }  
}
```

Additionally, you should specify default values for plot settings that the user can change in the *Styles* tab, for example, colors and styles, in the [`defaults`](#defaults) properties.

```
metainfo: {  
    // ...  
    defaults: {  
        styles: {  
            plot_0: {  
                linestyle: 0,  
                linewidth: 1,  
                plottype: 1,  
                trackPrice: false,  
                transparency: 0,  
                visible: true,  
                color: '#000080',  
            }  
        }  
    }  
}
```

![Styles tab](/charting-library-docs/v29/assets/images/styles-tab-d4b0d1c8f7d0ca6476ccbc839f8df0d2.png)

### palettes[​](#palettes "Direct link to palettes")

The [`palettes`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#palettes) property defines color palettes that are required if you use [plot](#plots) types such as `Colorer`, `BarColorer`, `OhlcColorer`, and others. These plot types allow you to draw an indicator that consists of lines, bars, or other elements of different colors. Consider the [Coloring Bars](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples#coloring-bars) example that shows how to use `palettes`.

### is\_hidden\_study[​](#is_hidden_study "Direct link to is_hidden_study")

The [`is_hidden_study`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#is_hidden_study) property allows you to hide a custom indicator in the *Indicators* dialog. To do this, set this property to `true`. The default value is `false`.

```
metainfo: {  
    // ...  
    is_hidden_study: true,  
}
```

### is\_price\_study[​](#is_price_study "Direct link to is_price_study")

The [`is_price_study`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#is_price_study) property specifies whether the indicator should be displayed on the same pane with the main [series](/charting-library-docs/v29/getting_started/glossary#series).

![Price study](/charting-library-docs/v29/assets/images/is-price-study-4b07b5538bfc54246a4ff1b66b5553bc.png)

### linkedToSeries[​](#linkedtoseries "Direct link to linkedToSeries")

The [`linkedToSeries`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#linkedtoseries) property specifies whether the indicator should use the same [price scale](/charting-library-docs/v29/ui_elements/Price-Scale) as the main [series](/charting-library-docs/v29/getting_started/glossary#series). If the property is `false`, you can move the series to another pane without the indicator.

![linkedToSeries](/charting-library-docs/v29/assets/images/linkedToSeries-9fdd289c2648c6aa80661189fb3bfdec.png)

You should set `linkedToSeries` to `true` if you create an indicator that does not make sense without the series. In this case, the *Move to* option is hidden in the UI.