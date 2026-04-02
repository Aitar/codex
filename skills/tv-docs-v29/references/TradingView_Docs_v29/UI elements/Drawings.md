# UI elements: Drawings

Source: https://www.tradingview.com/charting-library-docs/v29/ui_elements/drawings/

* [UI elements](/charting-library-docs/v29/ui_elements/)* Drawings

On this page

# Drawings

Drawings (shapes) are the tools that can help you analyze the charts and make clear annotations to them.
The drawings toolbar is located on the left panel.
Follow the [Drawings List](/charting-library-docs/v29/ui_elements/drawings/Drawings-List) article for a complete list of tools included in the drawing toolbar.

## Style customization[​](#style-customization "Direct link to Style customization")

Each drawing tool has its own default properties, such as color and size, that users can change in the UI.

![Style customization](/charting-library-docs/v29/assets/images/drawings_style_customization-6fb158b2216fceb45f1a798f1b5edd67.png)

You can also customize the drawing style using the API.
Refer to the [Drawing Overrides](/charting-library-docs/v29/customization/overrides/Drawings-Overrides) article for more information.

## Drawing toolbar[​](#drawing-toolbar "Direct link to Drawing toolbar")

You can show/hide the drawing toolbar on the fly as follows:

```
widget.activeChart().executeActionById("drawingToolbarAction");
```

Note that the toolbar is hidden in the fullscreen mode. To display the toolbar, enable the [`side_toolbar_in_fullscreen_mode`](/charting-library-docs/v29/customization/Featuresets#side_toolbar_in_fullscreen_mode) featureset.

### Favorite tools[​](#favorite-tools "Direct link to Favorite tools")

You can specify a default list of favorite drawings using the [`favorites`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#favorites) property in [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

In the UI, users can mark drawings as favorites using the *Add to favorites* button. The selected drawings are added to *Favorite Drawings Toolbar* that appears on the chart.
If you do not want users to specify favorites, you should disable the [`items_favoriting`](/charting-library-docs/v29/customization/Featuresets#items_favoriting) featureset. As a result, the *Add to favorites* button will be hidden in the UI.

![Favorite tool](/charting-library-docs/v29/assets/images/drawings_favorite_tool-3772bc5ed33702eaf569d62f07a1f0ca.png)

### Custom restrictions[​](#custom-restrictions "Direct link to Custom restrictions")

You can hide some drawings from the toolbar or apply custom restrictions to the chart.
To do this, use the [`drawings_access`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#drawings_access) property of [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
For example, you can choose which tools will be shown to users or hidden/disabled from them.

![Disabling drawings](/charting-library-docs/v29/assets/images/drawings_custom_restrictions-1eefe01d8740df8b3d74d257d15d12cd.png)

## Drawing features[​](#drawing-features "Direct link to Drawing features")

### Templates[​](#templates "Direct link to Templates")

info

These feature is only available in [Trading Platform](/charting-library-docs/v29/trading_terminal/).

Users can use the template appliance option for multiple drawings of the same type.
This option is available in the floating toolbar.
To disable this feature, include the `drawing_templates` [featureset](/charting-library-docs/v29/customization/Featuresets) in the [`disabled_features`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#disabled_features) array.

![Template](/charting-library-docs/v29/assets/images/drawings_template-cfe3e64e9361bb002f10a7a48d3cfb55.png)

tip

To save drawing templates on your server, you can use the [predefined REST API](/charting-library-docs/v29/saving_loading/save-load-rest-api/) or implement [API handlers](/charting-library-docs/v29/saving_loading/save-load-adapter).

## Drawing API[​](#drawing-api "Direct link to Drawing API")

The library allows you to create and manage drawings using the built-in API. You can also combine drawings into groups and subscribe to drawing-related events. Refer to [Drawings API](/charting-library-docs/v29/ui_elements/drawings/drawings-api) for more information.