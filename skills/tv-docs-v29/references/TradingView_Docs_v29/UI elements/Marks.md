# UI elements: Marks

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/Marks

* [UI elements](/charting-library-docs/v29/ui_elements/)* Marks

On this page

# Marks

Marks allow you to display some extra information like news, bar patterns, splits/dividends, and more [on the chart](#marks-on-the-chart) or [time scale](#marks-on-the-time-scale).

Use the [`subscribe`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#subscribe) method to handle events raised when users interact with marks. You can also [refresh](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#refreshmarks) and [clear](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#clearmarks) marks using the chart methods.

## Marks on the chart[​](#marks-on-the-chart "Direct link to Marks on the chart")

Marks on the chart are circles that are attached to bars and contain a character inside. You can customize the circle size and color. If you want to display two characters (like 'ED', 'AB', 'CD', etc.), you should enable the [`two_character_bar_marks_labels`](/charting-library-docs/v29/customization/Featuresets) featureset.

One bar can have several marks. When a user clicks on the mark, the tooltip appears. The tooltip can only contain plain text. HTML code is not supported.

![Marks](/charting-library-docs/v29/assets/images/marks-e3d4efc0469bff734c228ef715f5fd8f.png)

Marks are requested from your datafeed if you set [`supports_marks`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#supports_marks) to `true`. The library calls [`getMarks`](/charting-library-docs/v29/connecting_data/datafeed-api/additional-methods#getmarks) or requests [/marks](/charting-library-docs/v29/connecting_data/UDF#marks) to get mark data for the visible data range.

## Marks on the time scale[​](#marks-on-the-time-scale "Direct link to Marks on the time scale")

Marks on the time scale are figures above the time scale. Each mark has a character inside and a pop-up tooltip with information strings. The tooltip does not support HTML code. You can specify a time scale mark shape using the [`shape`](/charting-library-docs/v29/api/interfaces/Charting_Library.TimescaleMark#shape) property. Images can be displayed within time scale marks by providing an image URL in the [`imageUrl`](/charting-library-docs/v29/api/interfaces/Charting_Library.TimescaleMark#imageurl) property.

![Timescale marks](/charting-library-docs/v29/assets/images/timescale_marks-2591c5f6c3081fd416fe559667eb3efb.png)

Time scale marks are requested from your datafeed if you set [`supports_timescale_marks`](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration#supports_timescale_marks) to `true`. The library calls [`getTimescaleMarks`](/charting-library-docs/v29/connecting_data/datafeed-api/additional-methods#gettimescalemarks) or requests [/timescale\_marks](/charting-library-docs/v29/connecting_data/UDF#timescale-marks) to get mark data for the visible data range.