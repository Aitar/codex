# Customization: Common issues

Source: https://www.tradingview.com/charting-library-docs/v29/customization/customization-issues

* [Customization](/charting-library-docs/v29/customization/)* Common issues

On this page

# Common issues

This article describes common customization issues.

## General troubleshooting[​](#general-troubleshooting "Direct link to General troubleshooting")

To debug any customization issue, consider the following:

1. Refer to the [Customization precedence](/charting-library-docs/v29/customization/customization-precedence) article to understand how different customization-related settings work and which ones take priority in case of conflicts.
2. Check your customization-related settings defined in both the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) and the [`onChartReady`](/charting-library-docs/v29/core_concepts/widget-methods#onchartready) implementation to identify and resolve potential conflicts.
3. Ensure that your settings are not overriden by [user settings](#user-settings-override-default-ones).

## Settings are not applied[​](#settings-are-not-applied "Direct link to Settings are not applied")

The library supports extensive customization through a set of APIs. Some settings, such as the chart background color, can be adjusted with different API approaches.

If your setting does not take effect, it might be overridden by another API approach. Refer to the [Customization precedence](/charting-library-docs/v29/customization/customization-precedence) article to understand API priorities, and consider using an alternative approach if needed.

## User settings override default ones[​](#user-settings-override-default-ones "Direct link to User settings override default ones")

In the library, [user settings](/charting-library-docs/v29/saving_loading/user-settings) take precedence over default configurations specified with the API. Therefore, replacing settings defined through [`overrides`](/charting-library-docs/v29/customization/customization-precedence#overrides) and [`custom_themes`](/charting-library-docs/v29/customization/customization-precedence#customThemes) with user input is expected behavior.

By default, user settings are stored in [`localStorage`](/charting-library-docs/v29/customization/customization-precedence#localStorage). To override them, you should adjust these settings with another API approach that has higher priority according to the [table](/charting-library-docs/v29/customization/customization-precedence#approaches).

You can also disable saving settings to the local storage using the [`use_localstorage_for_settings`](/charting-library-docs/v29/customization/Featuresets#use_localstorage_for_settings) featureset. Alternatively, you can use [`settings_adapter`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#settings_adapter) to implement your preferred storage method.

## Theme is not switched[​](#theme-is-not-switched "Direct link to Theme is not switched")

The library supports light and dark [themes](/charting-library-docs/v29/customization/theme), which are applied to the entire widget. However, the toolbar and the chart colors are managed separately. The chart color is picked from [user settings](/charting-library-docs/v29/saving_loading/user-settings) that take precedence over default configurations.

In some case, the theme may not be fully applied, meaning that the chart color differs from the toolbar one. Consider the example.

* The chart and toolbar colors are dark.
* A user switches to another page, where the chart color and the theme of the application are light.
  At this stage, the chart color is saved to user settings.
* The user goes back to the dark-themed page. The toolbars are dark as expected, but the chart remains light.
  This happens because the chart color is picked from the user settings.

![Theme issue](/charting-library-docs/v29/assets/images/theme-switching-issue-4d146a5c654cca9a29d9b53fa4d6b71c.png)

To resolve this issue, you should apply the theme once again using the [`changeTheme`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#changetheme) method.

```
widget.onChartReady(function() {  
    widget.changeTheme("dark");  
});
```

You can also implement a trigger for a conditional theme change.

```
widget.changeTheme("dark").then(() => {  
    widget.chart().applyOverrides({ "paneProperties.background": "black", });  
});
```

tip

The chart colors can be managed with multiple APIs approaches that can override each other. If your color is not applied, make sure that this setting is not changed with another API approach. Refer to the [Customization precedence](/charting-library-docs/v29/customization/customization-precedence) article for more information.