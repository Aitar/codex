# Customization: Theme

Source: https://www.tradingview.com/charting-library-docs/v29/customization/theme

* [Customization](/charting-library-docs/v29/customization/)* Theme

On this page

# Theme

The library supports dark and light themes. Use the [`theme`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#theme) parameter in [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) to specify a theme. The default value is `light`. The chart layout does not contain buttons to switch the theme in the UI. Therefore, users cannot switch the theme unless you develop this option outside the library.

tip

If you want to override the default colors of the light and dark themes, you can use the [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes).

## Theme switching[​](#theme-switching "Direct link to Theme switching")

You should switch the chart's theme when the theme of your website changes. To do this, use the [`changeTheme`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#changetheme) method that changes the theme on the fly.

```
widget.onChartReady(function() {  
    widget.changeTheme("dark");  
});
```

You can call the [`getTheme`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#gettheme) method to get the current theme.

Note that the `theme` value is stored in the chart's configuration. Therefore, if you restore the chart that has the dark theme, you may see a black chart background in the light theme. In this case, you should apply the theme once again using the [`changeTheme`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#changetheme) method.

![Theme is not fully applied](/charting-library-docs/v29/assets/images/theme-issue-4943b67e7800de0821a89981a5ad6bd7.png)