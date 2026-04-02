# Releases: Release Notes

Source: https://www.tradingview.com/charting-library-docs/v29/releases/release-notes

* Releases* Release Notes

On this page

# Release Notes

tip

You can check the library version by executing `TradingView.version()` in a browser console.

## Version 29.6.0[​](#version-2960 "Direct link to Version 29.6.0")

*Date: Wed Aug 13 2025*

### Improvements[​](#v29_6-improvement "Direct link to Improvements")

* **Added a `label` property to StudyOrDrawingAddedToChartEventParams.** The [`label`](/charting-library-docs/v29/api/interfaces/Charting_Library.StudyOrDrawingAddedToChartEventParams#label) property contains the indicator's name as defined in the [`description`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#description) field of its [metainfo](/charting-library-docs/v29/custom_studies/metainfo/).[#](#v29_6-label_studyordrawingaddedtocharteventparams)

---

## Version 29.5.0[​](#version-2950 "Direct link to Version 29.5.0")

*Date: Tue Aug 05 2025*

### Improvements[​](#v29_5-improvement "Direct link to Improvements")

* **Improved crosshair movement in tracking mode on mobile.** Previously, the crosshair moved incorrectly in tracking mode when `vert_touch_drag_scroll` was disabled. Now, page scrolling is disabled in tracking mode, allowing the crosshair to move on touch.[#](#v29_5-improved_crosshair_movement_in_tracking_mode_on_mobile)

#### Trading Platform only[​](#v29_5-improvement-tp-only "Direct link to Trading Platform only")

* **Added `setLayoutSizes` method to `IChartingLibraryWidget`.** The [`setLayoutSizes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#setlayoutsizes) method can be used to resize the charts in [multiple-chart layouts](/charting-library-docs/v29/trading_terminal/#multiple-chart-layout).[#](#v29_5-setlayoutsizes_method)

### Bug Fixes[​](#v29_5-bugfix "Direct link to Bug Fixes")

* **Fixed an issue where setMinimumAdditionalDepth would be ignored.** Fixed an issue where custom studies would sometimes not request enough historic bars after calling [`setMinimumAdditionalDepth`](/charting-library-docs/v29/api/interfaces/Charting_Library.IContext#setminimumadditionaldepth).[#](#v29_5-fixed_setminimumadditionaldepth_issue)
* **Fixed an issue where pivot points could be drawn on the wrong bar for overnight sessions.** Fixed an issue where pivot points could be drawn on the wrong bars for symbols with overnight sessions when calculating with a daily timeframe.[#](#v29_5-fixed_pivot_points_overnight_sessions)

---

## Version 29.4.0[​](#version-2940 "Direct link to Version 29.4.0")

*Date: Tue Jun 25 2025*

### New Features[​](#v29_4-feature "Direct link to New Features")

* **Added new legend property.** A new overrides property `paneProperties.legendProperties.showSeriesLegendCloseOnMobile` was added to hide/show the close value in the legend when on mobile. The default value is `true`.[#](#v29_4-added_showserieslegendcloseonmobile_legend_property)

#### Trading Platform only[​](#v29_4-feature-tp-only "Direct link to Trading Platform only")

* **Support multiple tick resolution.** The library now supports multiple [tick resolutions](/charting-library-docs/v29/core_concepts/Resolution#resolution-in-ticks). Previously, it was possible to set only `1T` resolution.  
  Note that the library does not support tick multipliers. This means it is not possible to build a higher resolution (e.g., `10T`) from a lower one (e.g., `1T`). Therefore, your datafeed must explicitly provide each required resolution.[#](#v29_4-support_multiple_tick_resolution)
* **Enabled custom price formatting for Watchlist values.** `priceFormatterFactory` from [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_formatters) can now be used to format values displayed in the Watchlist columns titled *Last* and *Chg*.[#](#v29_4-custom-formatter-watchlist)

### Improvements[​](#v29_4-improvement "Direct link to Improvements")

* **Updated snapshots functionality in the top toolbar.** Now, handling and storing [snapshots](/charting-library-docs/v29/ui_elements/Snapshots) rely solely on the [`snapshot_url`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#snapshot_url) property.
  This means all server-side snapshot actions (*Copy link*, *Open in new tab*, *Tweet image*) must be implemented using your own server.
  For details on how to set up your own server, see our guide to [implementing a snapshot server](/charting-library-docs/v29/tutorials/implement-snapshots-server).[#](#v29_4-chart_snapshot_menu_options)
* **Added the `use_symbol_name_for_header_toolbar` featureset.** This featureset allows you to show the symbol name over the ticker in the *Symbol Search* dialog.[#](#v29_4-use_symbol_name_for_header_toolbar)
* **Added `searchSource` parameter to `searchSymbols`.** [`searchSymbols`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#searchsymbols) now receives a new parameter `searchSource` to indicate where the search was triggered from.[#](#v29_4-feature_improvement)
* **Added a new property to the `BrokerCustomUI` interface.** [`showReversePositionDialog`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerCustomUI#showreversepositiondialog) allows overriding the default *Reverse position* dialog with a custom implementation.[#](#v29_4-override-reverse-position-dialog)
* **Added VWAP insufficient data warning.** Users will now see a warning icon and message in the legend if there isn't enough data loaded to calculate VWAP.[#](#v29_4-vwap_insufficient_data_warning)
* **Add featureset to display inactivity gaps on intraday charts.** The new `intraday_inactivity_gaps` featureset enables the display of inactivity gaps on intraday charts. These gaps represent periods within the trading session when there has been no trading activity, resulting in missing bars on the chart.  
  When `intraday_inactivity_gaps` is enabled, a checkbox appears in the chart settings dialog, allowing users to toggle inactivity gaps on or off. The featureset also exposes the [`intradayInactivityGaps`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#intradayinactivitygaps) watched value on the Widget API for programmatic control.[#](#v29_4-intraday_inactivity_gaps)
* **Improved data loading efficiency by throttling data requests during user scrolling.** This significantly reduces the frequency of small, incremental requests to the Datafeed API.[#](#v29_4-scroll_data_throttling)

#### Trading Platform only[​](#v29_4-improvement-tp-only "Direct link to Trading Platform only")

* **Order & Position lines display the same information on desktop and mobile.** Users can now benefit from the same design on both desktop and mobile when an order/position is displayed on the chart.[#](#v29_4-Order_Position_lines_display_the_same_information_on_desktop_and_mobile)

### Bug Fixes[​](#v29_4-bugfix "Direct link to Bug Fixes")

* **Fixed indicator template favorite menu bug.** Fixed an issue where favoriting an indicator template with leading whitespace in its name caused the quick access button in the header menu to appear empty.[#](#v29_4-fix_indicator_template_favorite_menu_bug)
* **Fixed Relative Strength Index indicator.** The Relative Strength Index indicator was broken in version 29.2.0 and has now been fixed.[#](#v29_4-fix_relative_strength_indicator)
* **Fixed a bug where switching chart type to a Japanese one would lead to an error in the console.** [#](#v29_4-japanese_chart_types_throw_error)
* **Fixed vertical line drawing bug.** Fixed an issue where it was impossible to move an existing vertical line drawing to the right of the most recent bar on the chart.[#](#v29_4-fix_vertical_line_drawing_bug)
* **Fixed an error when drawing execution shapes on the chart led to an invalid chart state.** Fixes [#9109](https://github.com/tradingview/charting_library/issues/9109)[#](#v29_4-fixed_an_error_when_drawing_execution_shapes_on_the_chart_led_to_an_invalid_chart_state)
* **Fixed the spread operator issue in the Compare symbol dialog.** Spread operators now function correctly in the *Compare symbol* dialog, ensuring consistency with the *Symbol Search* dialog.[#](#v29_4-compare_spread_operators)
* **Fix for sameorigin.html loading from relative path.** This fix ensures proper loading of the `sameorigin.html` file when using the `iframe_loading_same_origin` featureset and the current page is not the root page.[#](#v29_4-sameorigin-html-loading-from-relative-path)

#### Trading Platform only[​](#v29_4-bugfix-tp-only "Direct link to Trading Platform only")

* **The `_getStyleOverrides` error message.** Fixed a bug where the `_getStyleOverrides` error message could be seen in the console when instantiating the chart with pre-existing orders or positions.[#](#v29_4-_getstyleoverrides)
* **Fix rendering of multiple execution shapes on a single bar.** Fixed an issue where adding multiple [execution shapes](/charting-library-docs/v29/ui_elements/drawings/drawings-api#createexecutionshape) to a single bar would only render the first shape.[#](#v29_4-executionshape_render_fix)

### Documentation[​](#v29_4-documentation "Direct link to Documentation")

* **New tutorial.** Check out our [new tutorial](/charting-library-docs/v29/tutorials/implement-broker-api/) on how to implement the required methods to enable basic trading functionality using the Broker API.
  By the end of this tutorial, you will learn how to enable trading UI and how to store, return, and update orders to make the trading flow functional.[#](#v29_4-broker_api_tutorial)
* **New troubleshooting article.** Explore a new article on common [customization issues](/charting-library-docs/v29/customization/customization-issues) and potential solutions.[#](#v29_4-documentation_update)
* **Other enhancements.** Updated the [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes) article and added a new [example](https://codepen.io/tradingview/pen/xbGRaKd) to demonstrate how chart colors can be adjusted using this API.[#](#v29_4-documentation_update1)

---

## Version 29.3.0[​](#version-2930 "Direct link to Version 29.3.0")

*Date: Thu May 08 2025*

### New Features[​](#v29_3-feature "Direct link to New Features")

* **Added HLC bars chart style.** The HLC bars chart style is the same as regular bars but doesn't display the open price. When exporting a series or [overlay](/charting-library-docs/v29/ui_elements/indicators/#add-and-compare-new-series) indicator that uses the HLC bars chart style, open values are not included. Open values also do not appear in the data window or [legend](/charting-library-docs/v29/ui_elements/Legend) for series or overlay indicators using this style.[#](#v29_3-added_hlc_bars_chart_style)

### Improvements[​](#v29_3-improvement "Direct link to Improvements")

* **Added price scale details to context menu event.** When invoking the [context menu](/charting-library-docs/v29/ui_elements/context-menu) on the price scale, it now returns the following details:
  + `id` of the price scale
  + `paneIndex` which is the index of the pane the price scale is linked to
  + `chartIndex` which is the index of the chart the price scale is linked to[#](#v29_3-pricescale-context-menu)
* **Added icon to dropdown items.** A new property `icon` was added to the [`DropdownItem`](/charting-library-docs/v29/api/interfaces/Charting_Library.DropdownItem) interface.[#](#v29_3-dropdown-item-icon)

### Bug Fixes[​](#v29_3-bugfix "Direct link to Bug Fixes")

* **Empty context menu.** Fixed an issue where the [context menu](/charting-library-docs/v29/ui_elements/context-menu) would be partially empty on mobile[#](#v29_3-empty_context_menu)
* **onContextMenu callback received incorrect arguments.** Fixed a bug where the [`onContextMenu`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#oncontextmenu) callback received an object instead of the expected arguments.[#](#v29_3-oncontextmenu_callback_arguments)
* **Autosave won't trigger with empty text box created during autosave delay.** [#](#v29_3-autosave-autodelay)
* **Fixed an error where vertical lines would revert to their previous position when moved beyond latest bar.** Fixes [#8894](https://github.com/tradingview/charting_library/issues/8894)[#](#v29_3-fixed_an_error_where_vertical_lines_would_revert_to_their_previous_position_when_moved_beyond_latest_bar)

### Documentation[​](#v29_3-documentation "Direct link to Documentation")

* **The following enhancements were made.**   
  + Added a new section explaining how to [programmatically open and close Symbol Search](/charting-library-docs/v29/ui_elements/Symbol-Search#openclose-symbol-search).
  + Updated the [Customization overview](/charting-library-docs/v29/customization/) and [Time zones](/charting-library-docs/v29/ui_elements/timezones) articles.[#](#v29_3-documentation_update)

---

## Version 29.2.0[​](#version-2920 "Direct link to Version 29.2.0")

*Date: Tue Apr 08 2025*

### New Features[​](#v29_2-feature "Direct link to New Features")

* **Added new methods to Trading Host.** The [Trading Host](/charting-library-docs/v29/trading_terminal/trading-concepts/#trading-host) now includes three new methods designed to clear specific caches and trigger fresh data fetches:
  + [`ordersFullUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#ordersfullupdate)
  + [`positionsFullUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#positionsfullupdate)
  + [`individualPositionsFullUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#individualpositionsfullupdate)[#](#v29_2-new_trading_host_methods)

#### Trading Platform only[​](#v29_2-feature-tp-only "Direct link to Trading Platform only")

* **Added cross-tab synchronization for watchlists.** This feature is enabled by default and requires the `use_localstorage_for_settings` [featureset](/charting-library-docs/v29/customization/Featuresets) to be enabled.
  To disable the cross-tab synchronization, use the `watchlist_cross_tab_sync` featureset.[#](#v29_2-watchlist_cross_tab_sync)

### Improvements[​](#v29_2-improvement "Direct link to Improvements")

* **New `resetCache` method.** The new `resetCache` method allows you to delete previously loaded data for all symbol and resolution combinations known to the datafeed at once. You can use this method instead of [`onResetCacheNeededCallback`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#subscribebars) to clear the cache before calling [`resetData`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resetdata). In this case, you do not need to wait for [`subscribeBars`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#subscribebars) to be called to access the callback.[#](#v29_2-added_resetcache_method)

### Bug Fixes[​](#v29_2-bugfix "Direct link to Bug Fixes")

* **Save button tooltip still shows shortcut when `save_shortcut` is disabled.** Fixed a bug where the *Save* button's tooltip still showed the shortcut when the `save_shortcut` featureset was disabled. Fixes [#8925](https://github.com/tradingview/charting_library/issues/8925)[#](#v29_2-save_button_tooltip_still_shows_shortcut_when_save_shortcut_is_disabled)
* **Compare Symbol search dialog behavior.** Fixed an issue where the library would try to resolve a symbol that may not exist when users pressed *Enter* whenever the featureset `allow_arbitrary_symbol_search_input` would be enabled.[#](#v29_2-compare_symbol_search_dialog_behavior)
* **Adding a custom interval could cause an error.** Adding a custom interval after enabling the [`custom_resolution`](/charting-library-docs/v29/customization/Featuresets#custom_resolutions) featureset used to cause a console error.[#](#v29_2-custom_resolution_fix)
* **Fixed an issue where on some occasions PineJS functions would not return the right values when internally comparing it to MIN\_VALUE or MAX\_VALUE.** [#](#v29_2-fixed_an_issue_where_on_some_occasions_pinejs_functions_would_not_return_the_right_values_when_inter)
* **Future bar time extrapolation with `disable_resolution_rebuild`.** Fixed an issue where future bar times would be extrapolated incorrectly when the `disable_resolution_rebuild` featureset was enabled, and daily bars that do not consider the January 1 to be the first day of the year were provided to the library.[#](#v29_2-future_bar_time_extrapolation_with_disable_resolution_rebuild)
* **Compare symbol legend context menu.** Fixed an issue where the context menu for compared symbols would show the *Add this indicator to favorites* item.[#](#v29_2-compare_symbol_legend_context_menu)
* **Main series context menu.** Fixed an issue where the [context menu](/charting-library-docs/v29/ui_elements/context-menu) for the main series would show a blank space instead of the *Add SYMBOL to watchlist* item.[#](#v29_2-main_series_context_menu)
* **Watchlist item counter.** Fixed an issue where the watchlist item count would include section titles in its calculation.[#](#v29_2-watchlist_item_counter)
* **Fixed an issue with time scale marks that couldn't contain any underscore character.** [#](#v29_2-fixed_an_issue_with_time_scale_marks_that_couldnt_contain_any_underscore_character)
* **Fixed a bug where `getBars` failed to display error messages containing semicolons.** [#](#v29_2-getbars_onerror)
* **Fixed drawing keyboard shortcuts.** Fixed an issue where using keyboard shortcuts to add drawings would sometimes open the *Symbol Search* dialog instead of adding the intended drawing.[#](#v29_2-fixed_drawing_keyboard_shortcuts)

### Documentation[​](#v29_2-documentation "Direct link to Documentation")

* **The following enhancements were made.**   
  + Added a new section explaining how to [display pre- and post-market price lines](/charting-library-docs/v29/connecting_data/Extended-Sessions#enable-the-price-line).
  + Added a new section explaining how to [provide profit and loss values](/charting-library-docs/v29/trading_terminal/trading-concepts/positions#provide-profit-and-loss) in Trading Platform.
  + Updated the [Trading Session](/charting-library-docs/v29/connecting_data/Trading-Sessions) article with information on how to specify [session history](/charting-library-docs/v29/connecting_data/Trading-Sessions#session-history)[#](#v29_2-documentation_update)

---

## Version 29.1.0[​](#version-2910 "Direct link to Version 29.1.0")

*Date: Fri Mar 07 2025*

### New Features[​](#v29_1-feature "Direct link to New Features")

* **Added the *Another symbol* input field to Moving Average Multiple, Moving Average Triple, and Pivot Points Standard.** This field allows users to specify a different symbol for calculating the indicator. By default, the current symbol on the chart is used.[#](#v29_1-added_other_symbol_to_moving_average_multiple_and_triple)

#### Trading Platform only[​](#v29_1-feature-tp-only "Direct link to Trading Platform only")

* **Pre-/post-market lines.** Added the `pre_post_market_price_line` featureset that allows you to enable or disable the pre-/post-market price lines. To display the pre-/post-market lines, you need to provide the `rtc` property in [quotes](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues).[#](#v29_1-pre_post_market_lines)

### Improvements[​](#v29_1-improvement "Direct link to Improvements")

* **Adds an offset input to the Bollinger Bands indicator.** [#](#v29_1-add_offset_input_to_bollinger_bands)
* **Allow overriding the default shortcuts.** Now, you can override the default shortcuts using the [`onShortcut`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#onshortcut) method. Note that modal dialogs shortcuts cannot be changed.[#](#v29_1-allow_overriding_the_default_shortcuts)

### Documentation[​](#v29_1-documentation "Direct link to Documentation")

* **New articles.** Explore our latest articles:
  + [Object tree](/charting-library-docs/v29/ui_elements/object-tree) — an overview of the feature.
  + [Quotes](/charting-library-docs/v29/trading_terminal/trading-concepts/quotes) — an article explaining the importance of quotes in Trading Platform.[#](#v29_1-new-articles)
* **Other updates.** The following enhancements were made:
  + Updated the guide on [how to add a custom page to the Account Manager](/charting-library-docs/v29/tutorials/create-custom-page-in-account-manager). It now describes how to make the symbol name clickable on the custom page.
  + Added a guide on how to troubleshoot when [quotes are not displayed or refreshed](/charting-library-docs/v29/connecting_data/Datafeed-Issues#quotes-are-not-displayed-or-refreshed).
  + Added a guide on how to troubleshoot [delays in Trading Platform UI elements](/charting-library-docs/v29/connecting_data/Datafeed-Issues#delays-in-trading-platform-ui-elements).
  + Added a new FAQ — [Does the library set cookies](/charting-library-docs/v29/getting_started/Frequently-Asked-Questions#other-questions).[#](#v29_1-documentation_update)

---

## Version 29.0.0[​](#version-2900 "Direct link to Version 29.0.0")

*Date: Wed Feb 05 2025*

This major release introduces new features and enhancements focused on expanding UI customization options. Users now have greater control over drawings and indicators, allowing for a more tailored and flexible experience.

This release also includes several [breaking changes](/charting-library-docs/v29/releases/release-notes#v29_0-breaking-change) that impact the library API. Consider them to ensure compatibility with your implementation.

Key updates:

* Better chart management with [leftmost bar visibility](/charting-library-docs/v29/releases/release-notes#v29_0-leftmost_bar_visibility)
* Advanced [customization](/charting-library-docs/v29/releases/release-notes#v29_0-customize_order_and_position_lines) in Trading Platform
* An alternative [loading mode](/charting-library-docs/v29/releases/release-notes#version-2810)
* Enhanced [visualization](/charting-library-docs/v29/releases/release-notes#v28_3-symbol_name_in_the_watchlist_and_details_widgets) in the Watchlist and Details widgets
* Removal of [Trading API](/charting-library-docs/v29/releases/release-notes#v29_0-removed_trading_api_methods_from_advanced_charts) methods from Advanced Charts

For a detailed breakdown of changes, refer to the sections below.

### Breaking Changes[​](#v29_0-breaking-change "Direct link to Breaking Changes")

* **Removed trading API methods from Advanced Charts.** The following methods are now available exclusively in Trading Platform. If you’re using Advanced Charts, these methods will no longer be accessible.
  + [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline)
  + [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline)
  + [`createExecutionShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createexecutionshape)[#](#v29_0-removed_trading_api_methods_from_advanced_charts)
* **Changed the `getPositionDialogOptions` signature.** The [`getPositionDialogOptions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerCommon#getpositiondialogoptions) method is asynchronous and returns a promise now. The method also expects a symbol as a parameter.[#](#v29_0-changed_the_getpositiondialogoptions_signature)
* **Broker API simplification.** To further improve and simplify the library, we have merged the two existing APIs, `IBrokerWithoutRealtime` and `IBrokerTerminal`, and now exclusively expose the latter. Additionally, we have removed the `subscribeDOM`/`unsubscribeDOM` methods, as they were rarely used and duplicated the functionality of [`subscribeDepth`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#subscribedepth)/[`unsubscribeDepth`](/charting-library-docs/v29/connecting_data/datafeed-api/trading-platform-methods#unsubscribedepth). This change ensures that the datafeed fully handles all data management responsibilities.[#](#v29_0-broker_api_simplification)
* **Removed the Anchored Note drawing.** [#](#v29_0-removed_the_anchored_note_drawing)
* **Renamed the Note drawing to Pin.** [#](#v29_0-renamed_the_note_drawing_to_pin)
* **Updated the default colors for drawings/indicators with Volume Profiles.** [#](#v29_0-updated_the_default_colors_for_drawingsindicators_with_volume_profiles)
* **Added MACD smoothing inputs.** [#](#v29_0-added_macd_smoothing_inputs)
* **Drawing creation methods now return Promises instead of synchronous values.** The drawing creation methods ([`createShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createshape), [`createMultipointShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createmultipointshape), and [`createAnchoredShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createanchoredshape)) now return Promises that resolve to the drawing ID. The methods also throw an Error through a rejected Promise when the drawing creation fails, instead of returning `null`.[#](#v29_0-createshape-async)

#### Trading Platform only[​](#v29_0-breaking-change-tp-only "Direct link to Trading Platform only")

* **Trading Platform methods for drawing creation now return Promises instead of synchronous values.** The ([`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline), [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline), and [`createExecutionShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createexecutionshape)) methods now return Promises that resolve to the corresponding API interface. [#](#v29_0-create-trading-shape-async)

### New Features[​](#v29_0-feature "Direct link to New Features")

* **Added the *Another symbol* input field to Ichimoku Cloud, Bollinger Bands, and Average Price.** This field allows users to specify a different symbol for calculating the indicator. By default, the current symbol on the chart is used.[#](#v29_0-added_other_symbol_field_to_indicators)

#### Trading Platform only[​](#v29_0-feature-tp-only "Direct link to Trading Platform only")

* **New properties for customizing order and position lines.** You can now override the style of order and position lines created with the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api).
  The [`trading_customization`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#trading_customization) option in the Widget Constructor now supports `brokerOrder` and `brokerPosition` properties.
  For more details, see the [Trading Overrides](/charting-library-docs/v29/customization/overrides/trading-overrides#created-with-broker-api) article.[#](#v29_0-customize_order_and_position_lines)

### Improvements[​](#v29_0-improvement "Direct link to Improvements")

* **Added an option to keep the leftmost bar visible after resolution switching.** By default, the library resets the chart to the latest data when the resolution is changed. To keep the current time range, users can enable the Save chart left edge position when changing interval option in *Chart settings* → *Scales*.[#](#v29_0-leftmost_bar_visibility)
* **Added option to hide/show scroll to the most recent bar button.** The presence of the *Scroll to the most* recent bar button now depends on the Navigation buttons settings (*Chart settings* → *Canvas* → *Buttons* → *Navigation*).[#](#v29_0-added_option_to_hideshow_scroll_to_the_most_recent_bar_button)
* **Added a new `paneIndex` getter to the `StudyAPI`.** The [`paneIndex`](/charting-library-docs/v29/api/interfaces/Charting_Library.IStudyApi#paneindex) function returns the index of the pane the indicator belongs to.[#](#v29_0-added_a_new_paneindex_getter_to_the_studyapi)
* **Enabled users to adjust coordinates of Parallel Channel within the drawing settings.** [#](#v29_0-enabled_users_to_adjust_coordinates_of_parallel_channel_within_the_drawing_settings)
* **Enabled users to reverse the Long/Short Position drawings.** [#](#v29_0-enabled_users_to_reverse_the_longshort_position_drawings)
* **Buy/Sell buttons' visibility can now be changed for each chart in the layout.** [#](#v29_0-buysell_buttons_visibility_can_now_be_changed_for_each_chart_in_the_layout)
* **Added the Volume option for the Date Range and Date & Price Range tools.** [#](#v29_0-added_the_volume_option_for_the_date_range_and_date__price_range_tools)
* **Added multiline option for Parallel Channel.** Additional level lines have been added.[#](#v29_0-added_multiline_option_for_parallel_channel)
* **Show price line of Heikin Ashi on real price when the real price label is selected.** On Heikin Ashi chart, the price line now matches the position of the *Last price* label when the *Real prices on price scale (instead of Heikin-Ashi price)* setting is enabled.[#](#v29_0-show_price_line_of_heikin_ashi_on_real_price_when_the_real_price_label_is_selected)
* **Added new time zone Azores (UTC-1).** [#](#v29_0-added_new_time_zone_azores_utc-1)
* **Added an error message for unsupported resolutions.** If the selected resolution is not supported by the current symbol, an error message appears on the chart along with a button to switch to a supported resolution.[#](#v29_0-added_unsupported_resolutions_error_message)
* **Implemented dynamic loading for drawings to optimize bundle size.** Drawings have been refactored to utilize dynamic imports, reducing the initial bundle size by loading these components on-demand. This optimization results in faster initial page loads and improved application startup time, while maintaining full drawing functionality through lazy loading when tools are actually accessed by users.[#](#v29_0-drawing-tools-dynamic-loading)
* **Added a star icon to chart context menu for indicator.** This icon is displayed next to the *Add this indicator to favorites / Remove this indicator* from favorites option in the indicator context menu.[#](#v29_0-added_a_star_icon_to_chart_context_menu_for_indicator)

#### Trading Platform only[​](#v29_0-improvement-tp-only "Direct link to Trading Platform only")

* **Changed the return type for `OrderPreviewResult`.** When implementing [`previewOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#previeworder), you can specify links to external URLs now. The links will be displayed within the `warnings` or `errors` block. [#](#v29_0-changed_the_return_type_for_orderpreviewresult)

### Bug Fixes[​](#v29_0-bugfix "Direct link to Bug Fixes")

* **Fixed unreliable onChartReady callback with cached bundles.** When using `iframe_loading_compatibility_mode` with cached library bundles, the `onChartReady` callback would sometimes fail to execute. Fixes [#8889](https://github.com/tradingview/charting_library/issues/8889)[#](#v29_0-on-chart-ready-bug-fix)
* **Long/Short Position tools are extended to the right if the next bar crosses stop/profit level.** Fixed a bug where Long/Short Position would get partially extended to the right if the next bar crossed the stop/profit level.[#](#v29_0-longshort_position_tools_are_extended_to_the_right_if_the_next_bar_crosses_stopprofit_level)
* **Fixed hovering on the indicator legend.** Now, when an indicator is deleted via the legend, the hover state shifts to the legend of the next indicator below.[#](#v29_0-fixed_hovering_on_the_indicator_legend)
* **Fixed an issue when cloning drawings that were not selected.** Fixed a bug where *Ctrl+Drag* would create copies of the last selected drawings on chart, even if they were no longer selected. Now, this shortcut enables area selection.[#](#v29_0-fixed_an_issue_when_cloning_drawings_that_were_not_selected)

### Documentation[​](#v29_0-documentation "Direct link to Documentation")

* **New how-to guide.** Check out a new [guide](/charting-library-docs/v29/tutorials/add-custom-button-to-top-toolbar) on how to add a custom button to the top toolbar.[#](#v29_0-new_how-to_guide)
* **Other updates.** The following enhancements were made:
  + Added a new section that explains [multiple symbol resolving](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#multiple-symbol-resolving).
  + Updated information on how to [change colors of the *Buy/Sell* buttons](/charting-library-docs/v29/customization/styles/CSS-Color-Themes#buysell-buttons-properties).
  + Updated the [Toolbars](/charting-library-docs/v29/ui_elements/Toolbars) article.
  + Added a new [section](/charting-library-docs/v29/ui_elements/Chart#execute-action-by-id) that describes how to trigger specific actions, such as opening the *Chart settings* dialog, using the [`executeActionById`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#executeactionbyid) method.
  + Added an [overview](/charting-library-docs/v29/getting_started/product-comparison) of other TradingView products.[#](#v29_0-documentation_update)

---

## Version 28.5.0[​](#version-2850 "Direct link to Version 28.5.0")

*Date: Wed Dec 18 2024*

**New Features**

* **Added `baselinePosition` property for column series.** The [`baselinePosition`](/charting-library-docs/v29/api/interfaces/Charting_Library.ColumnStylePreferences#baselineposition) property allows column series to be drawn relative to the specified baseline value.
  + The default value is `'bottom'`, which draws columns with the bottom of the chart pane as their baseline.
  + Setting the value to `'zero'` draws columns with a baseline of 0, displayed as either 0% or 0.00 depending on the price scale mode.[#](#v28_5-added_baselineposition_property_for_column_series)
* **Added the *Another symbol* input field to Moving Average Double.** This field allows users to specify a different symbol for calculating the indicator. By default, the current symbol on the chart is used.[#](#v28_5-added_other_symbol_to_moving_average_double)

**Documentation**

* **New how-to guide.** Check out a new [guide](/charting-library-docs/v29/tutorials/create-custom-page-in-account-manager) that explains how to create a custom page in the Account Manager.[#](#v28_5-new_how-to_guide)
* **Other updates.** The following enhancements were made:
  + Added a new section that explains how to enable and specify [last day change values](/charting-library-docs/v29/ui_elements/Legend#last-day-change-values).
  + Updated information on [overnight sessions](/charting-library-docs/v29/connecting_data/Trading-Sessions#overnight-sessions).
  + Updated information on how to [close](/charting-library-docs/v29/trading_terminal/trading-concepts/positions#close-positions) and [reverse](/charting-library-docs/v29/trading_terminal/trading-concepts/positions#reverse-positions) positions.
  + Updated API overview page.[#](#v28_5-documentation_update)

## Version 28.4.0[​](#version-2840 "Direct link to Version 28.4.0")

*Date: Thu Nov 28 2024*

**New Features**

* **Added `includeOHLCValuesForSingleValuePlots` option when exporting data.** When set to `true`, this option forces all four OHLC plot values to be exported, even if the plot has a single value. This applies, for example, when the symbol has `visible_plots_set: 'c'` or when the exported plot is a single-value style (Area, Baseline, Line, Line with markets, Stepline, or Column).[#](#v28_4-include_ohlc_values_in_export_data)

**Improvements**

* **Added logging of quotes events.** Added extra logging of quote events when [debug mode](/charting-library-docs/v29/tutorials/enable-debug-mode#enable-debug-mode-for-data-connection) is enabled. The logs will contain information about quote data requests, real-time subscribe and unsubscribe events, and alerts for data requests that do not respond within 10 seconds.[#](#v28_4-added_logging_of_quotes_events)

**Bug Fixes**

* **Fixed an issue where missing translations caused errors when opening the settings dialog of the Ichimoku Cloud indicator.**[#](#v28_4-fixed_an_issue_with_missing_ichimoku_cloud_translation)
* **Fixed an issue where the Point and Figure series would not be displayed.**[#](#v28_4-fixed_an_issue_with_point_and_figure_series)

**Documentation**

* **New articles.** Explore our latest articles:
  + [Positions](/charting-library-docs/v29/trading_terminal/trading-concepts/positions) — an article that overviews position types supported in the library and describes how to manage them.
  + [UI elements](/charting-library-docs/v29/ui_elements/) — an overview of the library's UI elements.
  + [News](/charting-library-docs/v29/trading_terminal/news) — an article that explains how to connect data to the *News* widget.[#](#v28_4-documentation_update)
* **Other updates.** The following articles were improved:
  + [NPM](/charting-library-docs/v29/getting_started/NPM)
  + [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes)
  + [CSS color themes](/charting-library-docs/v29/customization/styles/CSS-Color-Themes)
  + [Market Status](/charting-library-docs/v29/ui_elements/market-status)[#](#v28_4-documentation_update1)

## Version 28.3.0[​](#version-2830 "Direct link to Version 28.3.0")

*Date: Thu Oct 24 2024*

**New Features**

* **Symbol name in the Watchlist and Details widgets.** Now, the [`DatafeedQuoteValues.short_name`](/charting-library-docs/v29/api/interfaces/Datafeed.DatafeedQuoteValues#short_name) value is displayed as a symbol's short name in the [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List) and [Details](/charting-library-docs/v29/trading_terminal/#details).
  You can disable the [`prefer_quote_short_name`](/charting-library-docs/v29/customization/Featuresets#prefer_quote_short_name) featureset to revert to the old behavior. In this case, the [`ticker`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#ticker) value will be used instead.

  Trading Platform Only

  [#](#v28_3-symbol_name_in_the_watchlist_and_details_widgets)

**Bug Fixes**

* **Anchored Note in multi-layout.** Fixed an issue where plotting a saved Anchored Note in multi-layout would raise an error.

  Trading Platform Only

  [#](#v28_3-anchored_note_in_multi-layout)
* **Fixed symbol logo persistence in legend.** Resolved an issue where a failed image load (e.g., a 404 error) for a symbol logo would cause the previous logo to persist in the legend. Now, the legend correctly updates to reflect the absence of a logo when loading fails. See the [Symbol logos](/charting-library-docs/v29/ui_elements/Legend#symbol-logos) section of the Legend documentation for more details on the feature.[#](#v28_3-fixed_symbol_logo_persistence)
* **Fixed ordering of symbol logos.** Fixed an issue where symbol logos with two URLs defined in [`logo_urls`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#logo_urls) were displayed in an inconsistent order. The order has been corrected on the chart legend and within the Account Manager table.[#](#v28_3-fixed_ordering_symbol_logos)

## Version 28.2.0[​](#version-2820 "Direct link to Version 28.2.0")

*Date: Tue Oct 01 2024*

**New Features**

* **Added `Rank Correlation Index` indicator.**
* **Support building seconds bars from ticks.** Trading Platform now supports building seconds bars from ticks for symbols configured to support it. Compatible symbols must set the [`build_seconds_from_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#build_seconds_from_ticks) flag to `true`. Additionally, [`has_seconds`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_seconds) and [`has_ticks`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#has_ticks) must be `true`, and [`seconds_multipliers`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#seconds_multipliers) must be an empty array or only contain multipliers that the datafeed provides itself.

  Trading Platform Only

**Improvements**

* **Added an option to customize the default Volume MA calculation in the Volume indicator.** By default, the Volume MA, optionally plotted in the Volume indicator, used the SMA calculation. We have now introduced two additional options: EMA and WMA.
* **Added new event to `SubscribeEventsMap`.** The [`timeframe_interval`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#timeframe_interval) event is triggered when the one of the bottom left intervals is selected or the [`setTimeFrame`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#settimeframe) API is used.
* **Added a symbol change to MACD indicator.** It is now possible to change the targeted symbol when plotting MACD indicator without using the main series.
* **Sped up sorting animation in the Account Manager.** Raised by [#8760](https://github.com/tradingview/charting_library/issues/8760)

  Trading Platform Only

## Version 28.1.0[​](#version-2810 "Direct link to Version 28.1.0")

*Date: Wed Sep 04 2024*

**Breaking Changes**

* **Deprecated API methods.** [`activateBottomWidget`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#activatebottomwidget) is now marked `deprecated`. Please use [`setAccountManagerVisibilityMode`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setaccountmanagervisibilitymode) instead.
  If you want to retrieve the current state of the Account Manager please use [`getAccountManagerVisibilityMode`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#getaccountmanagervisibilitymode)

**New Features**

* **Added `iframe_loading_same_origin` featureset.** The `iframe_loading_same_origin` featureset ensures the library's iframe is loaded from the same domain as the `library_path` files.

**Improvements**

* **Added new event to `SubscribeEventsMap`.** The [`study_dialog_save_defaults`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#study_dialog_save_defaults) event is triggered when the *Save as default* option is selected in the indicator settings.
* **Changed the return type for `OrderPreviewResult`.** When implementing [`previewOrder`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#previeworder), you can specify links to external URLs now. The links will be displayed within the `warnings` or `errors` block.

  Trading Platform Only
* **Added an item counter for custom pages.** By default, custom pages added to the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/) do not display the number of items in their corresponding table. Enabling [`displayCounterInTab`](/charting-library-docs/v29/api/interfaces/Charting_Library.AccountManagerPage#displaycounterintab) will show this number next to the tab title.

  Trading Platform Only

**Bug Fixes**

* **charting\_library\_debug\_mode.** Fixed an issue where enabling the featureset `charting_library_debug_mode` was of no effect.
* **Instant display of refreshed marks.** Fixed an issue where new [marks](/charting-library-docs/v29/ui_elements/Marks) added after calling [`refreshMarks`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#refreshmarks) were not immediately displayed on the chart. Previously, these marks only appeared after user interaction, but now they are instantly visible once the data is provided.
* **Fixed an issue with `multiple_watchlists` featureset.** When the `multiple_watchlists` featureset was disabled, it was still possible to see the `Create a new list` option under the Watchlist drop-down menu.

**Documentation**

* **New how-to guide.** Check out a new guide on [enabling debug modes](/charting-library-docs/v29/tutorials/enable-debug-mode) to help identify potential issues when implementing your app and ensure it is running smoothly.

## Version 28.0.0[​](#version-2800 "Direct link to Version 28.0.0")

*Date: Wed Aug 14 2024*

**Breaking Changes**

* **Removed `full_name`.** The `LibrarySymbolInfo.full_name` property was removed from public API. The property contained strings in the `'EXCHANGE:SYMBOL'` format and was used to request data from the datafeed. Therefore:

  + Now, you should use either the [`name`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#name) or [`ticker`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#ticker) property to specify an identifier for a certain symbol. For more information, refer to the [Symbology](/charting-library-docs/v29/connecting_data/Symbology#symbol-name) article.
  + Instead of `'EXCHANGE:SYMBOL'`, the library will send either `name` or `ticker` values to the datafeed when calling methods such as [`getBars`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#getbars), [`getQuotes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedQuotesApi#getquotes), and [`subscribeQuotes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedQuotesApi#subscribequotes).
  + The `'EXCHANGE:SYMBOL'` strings are no longer displayed in the Trading Platform UI. The symbol name will be used instead. You can disable the [`prefer_symbol_name_over_fullname`](/charting-library-docs/v29/customization/Featuresets#prefer_symbol_name_over_fullname) featureset to revert to the old behavior.

    Trading Platform Only
* **Deprecated API methods.** The following methods are now marked `deprecated` for the Advanced Charts users.

  + [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline)
  + [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline)
  + [`createExecutionShape`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createexecutionshape)

  These methods will be removed from the Advanced Charts library in the next major version.
  However, they will still be available in Trading Platform.[#](#v28-0-item1)
* **Make `cancelOrders` optional.** The [`cancelOrders`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#cancelorders) method is marked as optional because the library calls it only for the [Depth of Market](/charting-library-docs/v29/trading_terminal/#depth-of-market) widget.

  Trading Platform Only

  [#](#v28-0-item2)
* **Removed the `calculatePLUsingLast` flag.** The `calculatePLUsingLast` [broker configuration flag](/charting-library-docs/v29/trading_terminal/trading-concepts/trading-features-configuration) has been removed.

  Trading Platform Only

  [#](#v28-0-item2)
* **Symbol search dialog behavior.** Previously, when users pressed *Enter* in the [*Symbol Search*](/charting-library-docs/v29/ui_elements/Symbol-Search) dialog, they could enter arbitrary input directly. This input was passed to the datafeed for resolution and loading, regardless of whether the input matched any search results.  
  Now, pressing *Enter* selects the top search result unless the user has explicitly chosen another item. If there are no search results, pressing *Enter* will have no effect. You can enable the [`allow_arbitrary_symbol_search_input`](/charting-library-docs/v29/customization/Featuresets#allow_arbitrary_symbol_search_input) featureset to use the old behavior.
* **Change custom translation API.** Change the [custom\_translate\_function](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_translate_function) interface to accept different parameters: the original text, the singular original text, and the translated text. For example "prices", "price", "prix".
* **Changed the behavior of data display in the Depth of Market widget.** Now, data is displayed in static mode.
  This means that the price series is fixed, while the current price moves within, above, or below the designated range.
  To center on the current price, click the centering button () or use the *Shift + Alt/Option + C* shortcut.
  Previously, centering was applied dynamically.
* **Renamed the Symbol Info dialog.** The *Symbol Info* dialog and the corresponding items in context menus are called *Security Info* now. [#8444](https://github.com/tradingview/charting_library/issues/8444)
* **Renamed ErrorCallback to DatafeedErrorCallback.** `ErrorCallback` used in `IDatafeedChartApi` has been renamed to `DatafeedErrorCallback`.
* **Updated `selectedCurrency` behavior.** In `CurrencyInfo`, the [`selectedCurrency`](/charting-library-docs/v29/api/interfaces/Charting_Library.CurrencyInfo#selectedcurrency) property now returns `null` instead of `"Mixed"` when price scales contain mixed currencies.
* **Deprecated property.** The `brokerConfig` property in the [`TradingTerminalWidgetOptions`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions) interface is deprecated and will be removed in the next major release.
  Use the [`broker_config`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_config) property instead.

**New Features**

* **New Custom themes API.** This API allows you to customize colors of the chart elements including toolbars, dialogs, and buttons.
  To do this, you should specify your own theme with a custom color palette.
  For more information, refer to the [Custom themes API](/charting-library-docs/v29/customization/styles/custom-themes) article.
* **Added Volume Candles chart style.** This chart style allows for a visual assessment of the volume of trades for each candle. These are still candlesticks, but the width of each candle depends on the volume of trades during the period of formation of this candle. The greater the trading volume during the formation period of the candle, the larger the width of the candle.
  To display Volume Candles, select the corresponding option in the drop-down menu on the top toolbar.

**Improvements**

* **Behavior change for `chartContextMenuActions`.** When the [`chartContextMenuActions`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal#chartcontextmenuactions) method returns an empty array, the *Trade* item within the chart [context menu](/charting-library-docs/v29/ui_elements/context-menu) will not be displayed. Previously, the item was rendered but grayed out.

  Trading Platform Only

  [#](#v28-0-item12)
* **Added the `library_custom_fields` property to the `LibrarySymbolInfo` interface.** This property is used to include additional metadata in the symbol information. The metadata will not be processed by the library.[#](#v28-0-item13)
* **Added extra properties to `symbolExt` method.** The [`symbolExt`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#symbolext) method now returns additional properties including `ticker`.[#](#v28-0-item14)
* **Added the `debug_broker` option to the Widget Constructor.** When [`debug_broker`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#debug_broker) is specified, the library logs calls and responses to [`IBrokerTerminal`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerTerminal) and [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost) in the browser console. You can set `debug_broker` to one of the debug levels defined by [`BrokerDebugMode`](/charting-library-docs/v29/api/modules/Charting_Library#brokerdebugmode).

  Trading Platform Only

  [#](#v28-0-item15)
* **Updated the Anchored VWAP drawing.** Add bands settings to the Anchored VWAP drawing.[#](#v28-0-item16)
* **Added new methods to the Trading Host.** The `getOrderTicketSetting` and `setOrderTicketSetting` methods have been added to the [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost) interface. These methods allow you to read and adjust Order Ticket settings.

  Trading Platform Only

  [#](#v28-0-item17)
* **Changed `const enum` to `enum` in the library type declarations.** This change allows you to import enums from the library in a TypeScript environment with the [`isolatedModules`](https://www.typescriptlang.org/tsconfig/#isolatedModules) option enabled, such as when using Vite or similar tools.[#](#v28-0-item18)
* **Added the `hideStudiesFromLegend` option to `ClientSnapshotOptions`.** When `hideStudiesFromLegend` is set to true, the legend within the generated screenshots won't contain any studies applied to the chart.[#](#v28-0-item19)
* **Exposed `connectionStatusUpdate` from `IBrokerConnectionAdapterHost`.** An existing [`connectionStatusUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#connectionstatusupdate) API has been exposed for [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost) to help reflect connection status changes throughout the application lifecycle.

  Trading Platform Only

  [#](#v28-0-item20)
* **New keyboard shortcuts.** The following [shortcuts](/charting-library-docs/v29/getting_started/Shortcuts) were added:

  + *Shift* + *Mouse wheel* — scroll the chart horizontally
  + *Shift* + *Alt* + *B* — place limit order to buy
  + *Shift* + *Alt* + *S* — place limit order to sell
* **Enabled in-place editing for drawing texts.** For the following drawings, users can now add custom text and edit it on the chart:

  + *Fib Retracement*
  + *Trend-based Fib Extension*
  + *Horizontal* and *Vertical Line*
  + *Trend Line*
  + *Info Line*
  + *Ray*
  + *Extended Line*
  + *Signpost*
  + *Note*
  + *Anchored Note*
  + *Comment*
  + *Rectangle*
  + *Ellipse*
  + *Circle*

  To enter the text, users should click the *+Add text* placeholder that appears on hover.
* **Disabled color pickers in Chart settings.** If a certain price label or line is hidden on the chart, users cannot adjust the color of this label/line in the *Chart settings* dialog.
* **Time zones.** Time zone updates:

  + Changed the Almaty (UTC+6) time zone to Astana (UTC+5).
  + Added the new Kuala Lumpur (UTC+8) time zone.
* **Visibility of price labels for risk-reward drawings.** Previously, price labels for the *Long position* and *Short position* drawings could be either hidden entirely or always displayed.
  Now, if the price labels are disabled for a certain drawing, the labels will be displayed when the drawing is selected.
* **Accessibility improvement.** Users can now select the following elements in the *Legend* when navigating with the keyboard.

  + The *More* () button and items in the corresponding menu
  + The *Remove* () button
* **Added new multiple-chart layouts combinations.**

  Trading Platform Only
* **New style settings for the Note drawing.** Now:

  + The *Background* and *Border* settings are optional.
  + The default color of the drawing depends on the current chart [theme](/charting-library-docs/v29/customization/theme).

**Bug Fixes**

* **Fixed the *Pivot Points Standard* compatibility with Japanese chart types.** The *Pivot Points Standard* indicator used to cause the *Assertion failed: data must have unique sorted times* error when applied to chart types such as Line Break, Renko, Kagi, and Point-and-Figure under certain data conditions.
* **Workaround for corrupted chart layouts.** In rare cases, chart layouts can become corrupted and cause a *DEFAULT\_SYMBOL is not defined* error when loaded by the library. To work around this error, set [`symbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol) to be used as a fallback for any corrupted charts.
* **Fixed an issue where 0-volume data were not displayed in the Legend.** [#8662](https://github.com/tradingview/charting_library/issues/8662)
* **Fixed the time indicator.** The time indicator now correctly moves across the timeline in the [Market Status](/charting-library-docs/v29/ui_elements/Symbol-Status) pop-up.
* **Fixed resizing for risk-reward tools.** The resizing of *Long position* and *Short position* drawings works correctly now. [#8513](https://github.com/tradingview/charting_library/issues/8513)
* **Fixed changing of drawing coordinates.** The setting dialog used to crash when users changed coordinates of drawings such as *Anchored Volume Profile*, *Fixed Range Volume Profile*, and *Regression Trend*.
* **Fixed the drawing settings bug.** Previously, when users clicked *Hide/Show* on a drawing, the settings applied to this drawing would override the default ones. Now, changing drawing visibility does not affect the default settings. [#8434](https://github.com/tradingview/charting_library/issues/8434)
* **Fixed colors of the scale buttons.** The colors of the *A* (auto) and *L* (log) scale buttons match the chart background color now. [#8459](https://github.com/tradingview/charting_library/issues/8459)
* **Fixed bugs on the multiple-chart layout.**

  Trading Platform Only

  The following bugs were fixed:
  + The *Long/Short Position* drawing used to cause errors if the drawing was hidden for a certain resolution and that resolution was currently displayed on the chart.
  + Synchronized *Path* and *Polyline* drawings were not displayed on larger resolutions if the first two points of the drawing were set at the same level on a smaller resolution.
  + The *Curve* and *Double Curve* drawings used to cause errors if a user moved the drawing before enabling layout synchronization.
  + Changing the Profit/Stop level of the synchronized *Long/Short Position* drawing used to cause errors if the drawing was hidden for a certain resolution and that resolution was currently displayed on the chart.

**Documentation**

* **Updated types for overrides.** The following categories of overrides within the
  [`ChartPropertiesOverrides`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartPropertiesOverrides)
  have been added or updated:
  + Added types for the Step line chart style (`mainSeriesProperties.steplineStyle.*`).
  + Updated the types for `paneProperties.*`.
  + Added overrides that affect Trading Platform features (`tradingProperties.*`).
* **New articles.** Explore our latest articles:
  + [How to create a custom indicator](/charting-library-docs/v29/tutorials/create-custom-indicator/) — a step-by-step tutorial that demonstrates the Moving Average implementation.
  + [Custom indicators. Inputs](/charting-library-docs/v29/custom_studies/metainfo/Custom-Studies-Inputs) — an overview of how to specify and manage input parameters for a custom indicator.
  + [Authentication](/charting-library-docs/v29/trading_terminal/trading-concepts/authentication) — an article that outlines possible authentication approaches.

    Trading Platform Only

## Version 27.006[​](#version-27006 "Direct link to Version 27.006")

*Date: Tue May 21 2024*

**Bug Fixes**

* **Resolve quotes with ticker instead of symbol name.** The library will now request quote data using the [`ticker`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#ticker) property. If `ticker` is not provided in the `LibrarySymbolInfo` object, the `name` property will be used instead. This should resolve an issue some customers were experiencing where quote data was not being properly displayed in the [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List) and [Legend](/charting-library-docs/v29/ui_elements/Legend).

## Version 27.005[​](#version-27005 "Direct link to Version 27.005")

*Date: Tue May 07 2024*

**Improvements**

* **Update the Anchored AVWAP drawing.** Add bands settings to the Anchored VWAP drawing.
* **Subscribe to widget bar visibility events.** A new [`study_event`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#study_event) type was added: `widgetbar_visibility_changed`. It returns the visibility state of the widget bar.

**Bug Fixes**

* **Fixed a bug in the Market Status pop-up.** [Corrections](/charting-library-docs/v29/connecting_data/Extended-Sessions#corrections-for-extended-sessions) specified for the extended session in the [`session-correction`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySubsessionInfo#session-correction) properties were not displayed in the *Market Status* pop-up window.

## Version 27.004[​](#version-27004 "Direct link to Version 27.004")

*Date: Wed Apr 17 2024*

**Breaking Changes**

* **Fixed time parameters in CrossHairMovedEventParams.** In version 26.001, we changed the `time` property of [`CrossHairMovedEventParams`](/charting-library-docs/v29/api/interfaces/Charting_Library.CrossHairMovedEventParams) to be a timestamp in the selected time zone.
  In this version, we reverted that change, and `time` represents a UTC timestamp again. Additionally, we introduced a new [`userTime`](/charting-library-docs/v29/api/interfaces/Charting_Library.CrossHairMovedEventParams#usertime) property that represents a timestamp in the selected time zone.

**Improvements**

* **Added ability to disable pulse animation when chart type is set to Line.** New *disable\_pulse\_animation* featureset allows users to disable the pulse animation when chart type is set to Line.

**Bug Fixes**

* **Fixed the price scale placement.** The [price scale](/charting-library-docs/v29/ui_elements/Price-Scale) should be placed back to its original position when a change made through the *Settings* dialog is canceled. Fixes [#4991](https://github.com/tradingview/charting_library/issues/4991)
* **Fixed the 52 Week High/Low indicator issue.** The 52 Week High/Low indicator no longer adds an empty space to the price scale when less than 52 weeks of historic bars are available. Fixes [#8137](https://github.com/tradingview/charting_library/issues/8137) [#8469](https://github.com/tradingview/charting_library/issues/8469)
* **Only calculate VWAP value when entire anchor period is loaded.** The VWAP indicator will only calculate values for the input anchor period if all bars in that period have been loaded.
* **Fixed a trailing stop modification dialog error.** Fixed a problem where opening the Order Ticket for a trailing stop position caused a "ReferenceError: isPositionLikeItem is not defined" error to be thrown.
* **Fixed the incorrect point position for the Long Position drawing.** The `getPositionPoints()` method will now return correct point positions. Fixes [#8230](https://github.com/tradingview/charting_library/issues/8230)
* **`BREAKING CHANGE` Position line price label does not use the correct price formatter.** The price scale will now correctly reflect the value when a formatter is used with [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline).
  Both [`createOrderLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline) and [`createPositionLine`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline) methods behave similarly to the corresponding actions made in the UI via [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket).
  Fixes [#8413](https://github.com/tradingview/charting_library/issues/8413) [#8324](https://github.com/tradingview/charting_library/issues/8324)

**Documentation**

* **New User accounts article.** Refer to [User accounts](/charting-library-docs/v29/trading_terminal/account-manager/user-accounts) for information on how to manage user accounts in the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/).
* **Session documentation updates.** The [Symbology](/charting-library-docs/v29/connecting_data/Symbology#session) and [Extended sessions](/charting-library-docs/v29/connecting_data/Extended-Sessions) articles now include more information on how to specify sessions and corrections for them.
* **New Save user settings article.** Refer to the [Save user settings](/charting-library-docs/v29/saving_loading/user-settings) article for information on how to store user settings.
* **Updated Watchlist article.** Explore our latest [Watchlist](/charting-library-docs/v29/trading_terminal/Watch-List) article that describes how to customize and handle the watchlist's data.

## Version 27.003[​](#version-27003 "Direct link to Version 27.003")

*Date: Thu Mar 14 2024*

**Improvements**

* **Added the resetLayoutSizes method.** Use [`resetLayoutSizes`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#resetlayoutsizes) to reset the sizes of all charts within a multiple-chart layout back to their initial default values.

  Trading Platform Only
* **Added the unloadUnusedCharts method.** The [`unloadUnusedCharts`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#unloadunusedcharts) method deletes non-visible charts from a multiple-chart layout. Use this method to
  prevent the library's inherent behavior to restore previously displayed charts instead of creating new
  charts when changing layouts.

  Trading Platform Only
* **Added a new type that reflects the ID of the created indicator.** A new [`study_event`](/charting-library-docs/v29/api/interfaces/Charting_Library.SubscribeEventsMap#study_event) type was added: `create`. It returns the `id` of the newly created indicator.

**Bug Fixes**

* **Displaying volume indicator on chart load when visible\_plots\_set is not specified.** The chart will now correctly display the volume indicator if the `create_volume_indicator_by_default` featureset is enabled even if the symbols [LibrarySymbolInfo](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) doesn't specify the optional [`visible_plots_set`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#visible_plots_set) property.
* **Prioritise widget constructor symbol over saved state.** The [`symbol`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol) property in the widget constructor will now have priority over symbols loaded from saved chart states when using [`saved_data`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#saved_data) or [`load_last_chart`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#load_last_chart). Fixes [#7922](https://github.com/tradingview/charting_library/issues/7922) [#8473](https://github.com/tradingview/charting_library/issues/8473) [#7926](https://github.com/tradingview/charting_library/issues/7926) [#8168](https://github.com/tradingview/charting_library/issues/8168)
* **Fixed an issue where the time\_frames description was ignored.**

## Version 27.002[​](#version-27002 "Direct link to Version 27.002")

*Date: Thu Feb 22 2024*

**Improvements**

* **Add positive and negative filled areas to Spread.** The Spread indicator now has a positive and negative filled area above and below the baseline value of 0. The colors of the filled areas are green and red respectively.

**Bug Fixes**

* **Brush drawing\_event is now raising a `create` event when starting drawing.**

**Documentation**

* **Improved drawing documentation.** Explore our latest articles about drawings.
  + New [Drawings API](/charting-library-docs/v29/ui_elements/drawings/drawings-api) article describes how to manage drawings in the code.
  + Updated [Drawing Overrides](/charting-library-docs/v29/customization/overrides/Drawings-Overrides) article now includes more information on how to customize drawings.

## Version 27.001[​](#version-27001 "Direct link to Version 27.001")

*Date: Fri Feb 2 2024*

**Improvements**

* **Custom indicators can now dynamically hide indicator inputs in the legend when plots are hidden.** The `hideWhenPlotsHidden` option has been added for a custom indicator's input. It enables you to hide an input's value in the legend text when the user hides all of the specified plots.

**Bug Fixes**

* **Allow studies that extend the time scale to load historic bars before the leftmost bar of the main series.**

**Documentation**

* **New articles**
  + [Context menu](/charting-library-docs/v29/ui_elements/context-menu)
  + [Orders](/charting-library-docs/v29/trading_terminal/trading-concepts/orders)
  + [Snapshots](/charting-library-docs/v29/ui_elements/Snapshots)

## Version 27[​](#version-27 "Direct link to Version 27")

*Date: Wed Jan 17 2024*

**Breaking Changes**

* **Custom study plot style text property moved.** The chars and shapes custom study plots `text` style property was moved from `metainfo.defaults.styles.[plot id].text` to `metainfo.styles.[plot id].text`. See this GitHub issue for more details [#8184](https://github.com/tradingview/charting_library/issues/8184)
* **Changed context menu behavior of the 'Plus' button and removed the 'show\_context\_menu\_in\_crosshair\_if\_only\_one\_item' featureset.** Now, the context menu of the *Plus* button opens even if the menu has only one item. Previously, the item's action was immediately executed if there was only one item in the context menu. Additionally, the `show_context_menu_in_crosshair_if_only_one_item` featureset has been removed.

**Breaking Changes: Trading Platform**

* **Changed parameter type in the showPositionDialog method.** The `position` parameter type of the [`showPositionDialog`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerCustomUI#showpositiondialog) method in the [`BrokerCustomUI`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerCustomUI) interface has been changed to `Position | IndividualPosition`.
* **Renamed flags in the BrokerConfigFlags interface.** The following flags have been renamed in the [`BrokerConfigFlags`](/charting-library-docs/v29/api/interfaces/Charting_Library.BrokerConfigFlags) interface:
  + `supportTrades` flag has been renamed to `supportPositionNetting`;
  + `supportTradeBrackets` flag has been renamed to `supportIndividualPositionBrackets`;
  + `supportCloseTrade` flag has been renamed to `supportCloseIndividualPosition`;
  + `supportPartialCloseTrade` flag has been renamed to `supportPartialCloseIndividualPosition`;
  + `requiresFIFOCloseTrades` flag has been renamed to `requiresFIFOCloseIndividualPositions`.
* **Renamed TradeBase and Trade interfaces.** The `TradeBase` interface has been renamed to [`IndividualPositionBase`](/charting-library-docs/v29/api/interfaces/Charting_Library.IndividualPositionBase) and the `Trade` interface has been renamed to [`IndividualPosition`](/charting-library-docs/v29/api/interfaces/Charting_Library.IndividualPosition) respectfully.
  All fields and their types has been left unchanged.
* **Renamed tradeColumns field in the AccountManagerInfo interface.** The `tradesColumns` field in the [AccountManagerInfo](/charting-library-docs/v29/api/interfaces/Broker.AccountManagerInfo) interface has been renamed to `individualPositionColumns`.
* **Renamed Trade member to IndividualPosition in the ParentType enum.** The `Trade` member of the [`ParentType`](/charting-library-docs/v29/api/enums/Charting_Library.ParentType) enum has been renamed to `IndividualPosition`.
* **Renamed trade related methods in the IBrokerConnectionAdapterHost interface.** The following methods in the [`IBrokerConnectionAdapterHost`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost) have been changed:
  + the `tradeUpdate` method has been renamed to [`individualPositionUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#individualpositionupdate). The `trade` parameter of the method has been renamed to `individualPosition`. Also, the type of that parameter has been changed to `IndividualPosition`;
  + the `tradePartialUpdate` method has been renamed to [`individualPositionPartialUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#individualpositionpartialupdate). The type of the `changes` parameter has been changed to `Partial<IndividualPosition>`;
  + the `tradePLUpdate` method has been renamed to [`individualPositionPLUpdate`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#individualpositionplupdate);
  + the type of the `position` parameter of the [`showPositionBracketsDialog`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#showpositionbracketsdialog) method has been changed to `Position | IndividualPosition`.
* **Renamed methods in the IBrokerWithoutRealtime interface.** The following changes have been made in the [`IBrokerWithoutRealtime`](https://www.tradingview.com/charting-library-docs/v27/api/interfaces/Charting_Library.IBrokerWithoutRealtime.md) interface:
  + The `closeTrade` method has been renamed to `closeIndividualPosition`;
  + The `editTradeBrackets` method has been renamed to `editIndividualPositionBrackets`.
* **Renamed trade method in the IBrokerCommon interface.** The `trades` method in the [`IBrokerCommon`](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerCommon) has been renamed to `individualPositions`. The return type of that method has been changed to `Promise<IndividualPosition[]>`.
* **Removed the Order Panel button from the right toolbar.** To open [*Advanced Order Ticket*](/charting-library-docs/v29/trading_terminal/#advanced-order-ticket), users should use the *Trade* button in *Account Manager* now.

**New Features**

* **Enabled in-place editing in Legend.** Users can change a symbol and resolution right from the [*Legend*](/charting-library-docs/v29/ui_elements/Legend) now. [#7966](https://github.com/tradingview/charting_library/issues/7966)
* **Added Quick Search.** The *Quick Search* dialog allows users to search for drawings, UI settings, and functions, such as *Remove Indicators*.
  To open this dialog, users should click the *Quick Search* button on the top toolbar or use the *Ctrl/Cmd* + *K* shortcut.
* **Added ability to show daily change in the chart legend.** New *Last day change values* option allows users to show/hide the last day change values in the main series legend.
  To make this option available in the *Chart Settings* dialog, use the [`legend_last_day_change`](/charting-library-docs/v29/customization/Featuresets#legend_last_day_change) featureset. [#8193](https://github.com/tradingview/charting_library/issues/8193)
* **Updated drawing icons.** New icons for the *Text*, *Anchored Text*, *Note*, and *Anchored Note* drawings. [#8181](https://github.com/tradingview/charting_library/issues/8181)

**Improvements**

* **`BREAKING CHANGE` Refactoring of the Ichimoku Cloud indicator.** Following feedback we've re-written the Ichimoku indicator and have brought the following changes:
  + 'Leading Span B' input is now 'Leading Span Periods'.
  + 'Lagging Span' input is now 'Lagging Span Periods'.
  + 'Leading Shift Periods' is a brand new input that aligns better to the original definition of the indicator.
  + Previously, 'Lagging span' was shifting both cloud and lagging lines. This should no longer apply as 'Leading Shift Periods' now handles the offset change for 'Lagging Span'.
* **`BREAKING CHANGE` Inputs renaming for Stochastic indicator.** Inputs for the Stochastic indicator have been renamed for consistency across our products.
* **`BREAKING CHANGE` Broker API clean up.**

  Trading Platform Only

  The `positionDialogOptions` object has been removed from the Broker's Configuration. Please use the `getPositionDialogOptions` method to customize the Position dialog.
* **Added new keyboard navigation shortcut.** Starting from version [26.002](/charting-library-docs/v29/releases/release-notes#version-26002), the library supports a keyboard navigation activated via the *Alt/Opt* + *Z* shortcut. Now, you can change this default navigation shortcut to *Tab*. To do this, enable the new [`accessible_keyboard_shortcuts`](/charting-library-docs/v29/customization/Featuresets#accessible_keyboard_shortcuts) featureset. For more information, refer to [Keyboard navigation](/charting-library-docs/v29/getting_started/accessibility#keyboard-navigation).
* **Added ability to cancel order dragging by pressing Esc.** If a user presses *Esc* while dragging the order, the order will be returned to its initial position.

**Bug Fixes**

* **Market status text during pre-market and post-market sessions.** The countdown text in the market status pop-up tooltip (in the legend area) has been fixed for pre-market and post-market sessions. The market status icon now shows an orange sunrise icon for pre-market and a blue moon icon for post-market.
* **Floating drawing toolbar context menu.** It wasn't possibly to override the context menu for the floating drawing toolbar.
* **Missing translation for No data here.** No data here message that is displayed on the chart whenever no bars are returned for a given symbol was missing its translation.
* **Disabling the 'open\_account\_manager' featureset now works as expected.**

  Trading Platform Only
* **Order Panel Custom Input Fields Reactivity.**

  Trading Platform Only

  The reactivity of UI elements within the order panel when using custom fields has been improved (Fixes [#6607](https://github.com/tradingview/charting_library/issues/6607)).
* **Fixed the pane buttons on the collapsed pane.** The pane buttons used to overlap the *Scroll to the Most Recent Bar* button when the pane is collapsed. [#8213](https://github.com/tradingview/charting_library/issues/8213)
* **The precision setting can be applied to all charts now.** To do this, users should specify precision in the *Chart settings* dialog and click the *Apply to all* button. [#8343](https://github.com/tradingview/charting_library/issues/8343)

  Trading Platform Only
* **Fix the color of high/low price label.** Now, the color of high/low labels on the price scale corresponds to the color of the high/low lines. Users can specify this color in the *Chart settings* dialog. [#8255](https://github.com/tradingview/charting_library/issues/8255)

**Documentation**

* **Chart customization precedence article added.** The library offers multiple approaches for changing the chart appearance and behavior.
  Explore our latest article on [customization precedence](/charting-library-docs/v29/customization/customization-precedence)
  for a comprehensive understanding of customization methods/properties and the sequence in which they are applied.
* **Order Ticket dialog article added.** Refer to [Order Ticket](/charting-library-docs/v29/trading_terminal/order-ticket) to learn how to provide custom fields, enable an order preview, implement your custom Order Ticket, and more.
* **New how-to guide on metainfo.** Explore our latest [guide](/charting-library-docs/v29/tutorials/create-custom-indicator/metainfo-implementation) on how to implement the `metainfo` field when you create a custom indicator. For more information about custom indicators and `metainfo`, refer to the updated [Custom indicators](/charting-library-docs/v29/custom_studies/) and [Metainfo](/charting-library-docs/v29/custom_studies/metainfo/) articles.
* **Bracket orders article added.** Explore our latest article on [bracket orders](/charting-library-docs/v29/trading_terminal/trading-concepts/brackets) in Trading Platform.
* **Account Manager article added.** Refer to [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/) for more information on creating pages, customizing columns, and configuring the Account Manager behavior.
* **Accessibility article added.** Refer to the new [Accessibility](/charting-library-docs/v29/getting_started/accessibility) article for information about accessibility features that the library includes.
* **Other documentation updates.** The new documentation version includes:
  + Updated [Resolution](/charting-library-docs/v29/core_concepts/Resolution) and [Price Scale](/charting-library-docs/v29/ui_elements/Price-Scale) articles.
  + A full list of overrides for built-in indicators. Refer to the [Indicator Overrides](/charting-library-docs/v29/customization/overrides/indicator-overrides#list-of-overrides) article for information.

**Other**

* **`BREAKING CHANGE` Deprecated customFormatters and brokerFactory.** Use [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_formatters)
  and [`broker_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_factory) instead.
* **`BREAKING CHANGE` Deprecated RawStudyMetaInfo.precision.** Use the [`format`](/charting-library-docs/v29/api/interfaces/Charting_Library.RawStudyMetaInfo#format) property instead. For more information, refer to the [Metainfo](/charting-library-docs/v29/custom_studies/metainfo/) article.

## Version 26.004[​](#version-26004 "Direct link to Version 26.004")

*Date: Thu Nov 16 2023*

**New Features**

* **Add methods to handle trading quantity.** The broker API now exposes a getter [getQty](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#getqty) and a setter [setQty](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#setqty) along with a subscription [subscribeSuggestedQtyChange](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#subscribesuggestedqtychange) and its dependant to unsubscribe [unsubscribeSuggestedQtyChange](/charting-library-docs/v29/api/interfaces/Charting_Library.IBrokerConnectionAdapterHost#unsubscribesuggestedqtychange).

**Improvements**

* **Added anchor option to VWAP indicator.** The VWAP indicator now has input options for source and anchor.
  + Source allows customisation of the price source for the indicator. Defaults to `hlc3`.
  + Anchor period setting specifies how frequently the VWAP calculation will be reset. This Defaults to `'Session'`.

**Bug Fixes**

* **VWAP Indicator behaviour.** The default behaviour for the VWAP indicator has been fixed. Previously it would anchor to the earliest available data point instead of the start of each session.
* **Displaying DOM widget data on non-tradable symbols.**

  Trading Platform Only

  When a symbol is non-tradable (`isTradable()` in the Broker API is returning `false`) it is now possible to display depth data in the DOM widget provided via the datafeed.
* **The price source text is visible in the screenshot.**
* **Fix display of price sources in Overlay study.** Price sources for symbols in the Overlay study were not being shown when the main series symbol did not have the same price source
* **Both Trend Strength Index and Linear Regression Slope indicators were missing their zero-based property to properly plot them using a histogram.**
* **onChartReady inconsistency on Safari.** Fixed an issue where `onChartReady` wouldn't reliably get called on specific versions of Safari.

**Documentation**

* **New article on core trading concepts.** We have added a new article describing [trading concepts](/charting-library-docs/v29/trading_terminal/trading-concepts/) in Trading Platform.
  Learn how to integrate trading functionality into your application using the Broker API and Trading Host.

## Version 26.003[​](#version-26003 "Direct link to Version 26.003")

*Date: Thu Oct 05 2023*

**Bug Fixes**

* **Do not save to localstorage when the use\_localstorage\_for\_settings feature is disabled.** Fixed a bug where use\_localstorage\_for\_settings did not stop some settings from being saved to localstorage.
* **Disabling `drawing_templates` completely removes the ability to save it when using line tools.**
* **Renaming a section within watchlist was throwing an error.**
* **Fixed an issue where it wasn't possible to set the background colour of a Renko bar to transparent.**

## Version 26.002[​](#version-26002 "Direct link to Version 26.002")

*Date: Mon Sep 18 2023*

**Improvements**

* **IOrderLineAdapter and IPositionLineAdapter now support positioning with pixel units.** The
  [setLineLength](/charting-library-docs/v29/api/interfaces/Charting_Library.IOrderLineAdapter#setlinelength)
  method in the IOrderLineAdapter (returned by
  [createOrderLine](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createorderline))
  and IPositionLineAdapter
  ([createPositionLine](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createpositionline))
  interfaces now support setting the unit to `'pixel'`.
  + Additionally, when using pixel unit, you can specify a negative number to
    position from the left edge of the chart instead.
* **Added keyboard navigation.** Keyboard navigation (activated via alt/opt + z keyboard shortcut) and many other accessibility improvements have been added to the library.
  + A featureset `accessibility` (on by default) has been added to control this behaviour.
* **Menu name is provided to items\_processor (context menu API).** [items\_processor](/charting-library-docs/v29/api/interfaces/Charting_Library.ContextMenuOptions#items_processor) within the [context\_menu](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#context_menu) API now includes details about the name of menu, and the ids of the related item (such as the series, drawing, study, order, or position).
* **Support more kinds of extended sessions.** The library now supports specifying only one of the postmarket or premarket sessions without the other.

**Bug Fixes**

* **On mobile devices, fixed an issue for when scrolling the pricescale with one finger while another one was holding the crosshair.**
* **Fixed an issue where it wasn't possible to set the background colour of a candle to transparent.**
* **52 Week High/Low indicator compatibility with empty supported\_resolutions array.** Fixes [#7884](https://github.com/tradingview/charting_library/issues/7884) issue.
* **Fixed an issue where any added indicator on the chart couldn't be undone.**
* **Fixed issue with locking visible time range while resizing chart.** When resizing the chart window with percentage right margin, and the `lock_visible_time_range_on_resize` featureset enabled then the visible range wasn't locked correctly.
* **SuperTrend Indicator Starting Point.** The SuperTrend would previously start drawing from zero for the first bar, instead of only drawing the indicator after the initial length (defined in the indicator's inputs) when all the possible data for a symbol has been loaded.
* **Changing the LineStyle for a position is again available.**
* **Styles tab for Pivot Point Standard indicator.** Resolved an issue where the style tab for the Pivot Point Standard indicator would not function correctly when the type option was set to 'Floor'.

**Other**

* **Custom Translation Function.** The following changes have been made to the [custom\_translate\_function](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_translate_function)
  + The interface name for the options has changed from `TranslateOptions` to `CustomTranslateOptions`.
  + The `plural` field in `CustomTranslateOptions` can now be either a single string, or an array of strings.
  + A third boolean argument is now provided. When this is true then the key provided is already translated.

## Version 26.001[​](#version-26001 "Direct link to Version 26.001")

*Date: Tue Aug 08 2023*

**New Features**

* **Add series and study values to crosshair move event.** The [`crossHairMoved` subscription](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#crosshairmoved) now exposes the study and series values in the event object. The values are the same as the values shown in the data window.
* **Adding a new Floor type for calculating Pivot.**
* **Add the onHoveredSourceChanged method to the widget API.** See [`onHoveredSourceChanged`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#onhoveredsourcechanged).

**Improvements**

* **Added optional variable\_tick\_size property to symbol info.**
* **Added onMoving to the Order Line Adapter.** [onMoving](/charting-library-docs/v29/api/interfaces/Charting_Library.IOrderLineAdapter#onmoving)

**Bug Fixes**

* **Selecting an incorrect symbol within a study no longer prevents the study from recovering when a valid symbol is chosen later.**
* **Fix drawing tools not affecting undo/redo stack and chart layout saving buttons.** Drawing actions can now be undone/redone and will affect the saving of the chart layout
* **Disabling the 'open\_account\_manager' featureset now works as expected.**

**Other**

* **Watchlist sections featureset added for adjusting the visibility of the 'Add Section' button.** The UI for creating watchlist sections can now be hidden by disabling the [watchlist\_sections](/charting-library-docs/v29/customization/Featuresets#watchlist_sections) featureset.

## Version 26[​](#version-26 "Direct link to Version 26")

*Date: Tue Jul 18 2023*

**Breaking Changes**

* **Remove Lines item and submenu from background and symbol context menu.** The "lines" item has been removed from the context menu of the chart and the legend of the main series.

**New Features**

* **In bottom toolbar, tooltip text for date ranges has changed.** Hovering over the time frame buttons will provide more details to understand how chart is constructed.
* **Add setting for visibility of A (auto) and L (log) scale buttons.** In Chart settings, Scale tab, a new setting has been introduced to enable shortcuts for Auto & Logarithmic modes.
* **Bug in compare data displayed in Data window.** There was an issue where OHLC values would only be displayed in the data window widget when using the cross hair selection instead of displaying the data from the latest available bar if nothing was selected. Fixes [#7769](https://github.com/tradingview/charting_library/issues/7769)
* **Update chart maximization icon and remove animation.** Maximization button restyled
* **Price scale resizing while scrolling chart in mobile browser.** When scrolling into history the price scale expands to accommodate the values, but doesn't retract when the values become shorter. This is done to make the scale less twitchy during scrolling. The scale's width is reset on data loading.

**Improvements**

* **Fixed a bug where on some DPR there was no separator between the right widget panel and the order panel.** Now the separator line is always visible.
* **No bracket settings in chart settings.** Bracket settings were added to the Chart settings in the Trading tab.
* **Symbol logos within the Legend and Account Manager.** Symbol logos can now be displayed within the [Legend](/charting-library-docs/v29/ui_elements/Legend#symbol-logos) and the Account Manager panel (

  Trading Platform Only

  ) if the `show_symbol_logos` featureset is enabled.
  + `show_symbol_logo_in_legend` featureset can be disabled to hide the logos within the legend.
  + `show_symbol_logo_for_compare_studies` featureset can be disabled to hide the logos within the legend for compare overlay studies.
  + `show_symbol_logo_in_account_manager` featureset can be disabled to hide the logos within the Account Manager panel (

    Trading Platform Only

    ).
* **Added setter and getter methods for CSS custom properties defined within the iframe.** The widget API now includes [setCSSCustomProperty](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#setcsscustomproperty) and [getCSSCustomPropertyValue](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#getcsscustompropertyvalue) methods for controlling CSS custom properties within the chart's iframe element.

**Other**

* **Deprecated properties and methods.** The following properties and methods are marked as deprecated and will be removed in the next major release:
  + `customFormatters` in the [ChartingLibraryWidgetOptions](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions) interface. Use [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_formatters) instead.
  + `customFormatters` and `brokerFactory` in the [TradingTerminalWidgetOptions](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions) interface. Use [`custom_formatters`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#custom_formatters) and [`broker_factory`](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#broker_factory) instead.

## Version 25.002[​](#version-25002 "Direct link to Version 25.002")

*Date: Wed Jul 12 2023*

**New Features**

* **Add 52 Week High/Low study.**
* **Enable hiding price scales when all studies or series are hidden.** Adds the `hide_price_scale_if_all_sources_hidden` feature. When enabled price scales will be hidden when all studies (or the main series) attached to the price scale are hidden.
* **Option to always show legend values for studies on mobile.** By default, when on mobile, the legend won't display any values for studies.
  Enabling this new `always_show_legend_values_on_mobile` featureset allows you to display the values.

**Improvements**

* **Sections can now be added within the Watchlist.** Sections dividers can now be added within the watchlist (

  Trading Platform Only

  ).
  + Any item within a list which is prefixed with `###` will be considered a section divider. [API Reference](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#watchlist)
* **Symbol and exchange logos can now be shown within the Compare Dialog.** The [symbol info](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) provided by [resolveSymbol](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#resolvesymbol) should now include 'exchange\_logo' if you would like to use the 'show\_exchange\_logos' featureset.

**Bug Fixes**

* **Watermark API's content provider is now used for all charts within a multi-chart layout.**
* **Fixed issue with resetData.** When resetting the data for a chart, any existing studies would become unlinked from the data source. Fixes [#7802](https://github.com/tradingview/charting_library/issues/7802)
  + The `request_only_visible_range_on_reset` featureset now defaults to `disabled`.

## Version 25.001[​](#version-25001 "Direct link to Version 25.001")

*Date: Mon Jun 26 2023*

**Breaking Changes**

* **price\_sources moved to symbol info.** To allow price sources resolved on-demand with the associated symbol the `price_sources` property has been removed from [the datafeed configuration object](/charting-library-docs/v29/api/interfaces/Charting_Library.DatafeedConfiguration) and added to the [symbol info object](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo).

**New Features**

* **Added Market status state getter.** [marketStatus](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#marketstatus) method is provided within [IChartWidgetApi](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi) which returns a watched value of the charts symbols current [market status](/charting-library-docs/v29/api/enums/Charting_Library.MarketStatus).
* **Symbol and exchange logos.** It is now possible to specify logo images for symbols and exchanges. These will be visible within the search dialog, and watchlist (Trading Platform). The `show_symbol_logos` and `show_exchange_logos` featuresets should be enabled, and your datafeed should be updated to provide urls as part of the symbol info supplied by the `resolveSymbol` method, and results supplied by the `searchSymbols` method.
* **Enable custom studies to extend the time scale.** Enable custom studies to extend the time scale with points that don't exist in the main series.
  + [See this article for more info](/charting-library-docs/v29/custom_studies/Studies-Extending-The-Time-Scale)
* **Added Custom Symbol Status API.** The new [Custom Symbol Status API](/charting-library-docs/v29/api/interfaces/Charting_Library.ICustomSymbolStatusApi) enables the creation and customisation of an additional status to be displayed for the symbol within the legend area.
  + The Custom Symbol Status API can be accessed via the [`customSymbolStatus`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#customsymbolstatus) method on the chart widget.
  + An example is provided on the [Symbol Status](/charting-library-docs/v29/ui_elements/Symbol-Status) page.
* **Featureset added for clearing the price scale on errors.** Added new `clear_price_scale_on_error_or_empty_bars` featureset to automatically clear pane price scales when the main series has an error or has no bars.
* **Adding Anchored VWAP in Trend line tools.** A new Trend line tool has been added to the already long list: Anchored VWAP.

**Improvements**

* **Added Watermark API.** The new [Watermark API](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatermarkApi) enables the customisation of the watermark text in addition to providing [WatchedValues](/charting-library-docs/v29/api/interfaces/Charting_Library.IWatchedValue) for the color and visibility properties.
  + The Watermark API can be accessed via the [`watermark`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#watermark) method on the chart widget.
* **Updated broker API sample to support bracket orders.** The sample broker API has been updated to support brackets (stop loss, and take profit) orders.

  Trading Platform Only
* **Drawings in saved charts now restore with the saved settings for lock and disableSelection.** The `lock` and `disableSelection` settings for a created shape will now be saved and restored correctly. [#6761](https://github.com/tradingview/charting_library/issues/6761)
* **Fullscreen button can now be used to exit fullscreen mode as well.** When using the `header_in_fullscreen_mode` featureset, it is now possible to use the fullscreen button to exit fullscreen mode.
* **Added method to programmatically set the time frame for the active chart.** The [setTimeFrame](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#settimeframe) method has been added to the widget which can set the time frame in a similar manner to the [Timeframes at the bottom of the chart](/charting-library-docs/v29/ui_elements/Time-Scale#timeframes-at-the-bottom-of-the-chart) buttons.
* **Renaming precision dropdown values in Chart settings.** To limit confusion when dealing with the Chart settings/Precision dropdown values, some fractional ones have been renamed to more readable ones.
* **Changing Source option in line-break & renko chart.** In Trading Platform, it was unnecessary to offer the option to change the source of data for both Renko and Line Break, as the data is taken from the close value.

**Bug Fixes**

* **Timescale marks will adjust correctly when widget theme is changed.**
* **onAutoSaveNeeded event emitted when removing all drawings via toolbar button.**
* **removeChart within the save load adapter will await the promise before updating the UI.**
* **First getBars request after resetting data no longer has a countback of zero.**
* **Market status pop up text could sometimes display Infinity or NaN values and not update on the dot.**
* **Fix custom field validators.** Fixes a bug where custom broker field validator functions were not called if provided.
* **Fixed rendering on price and time axes when a Trend Angle line drawing is selected.**

**Other**

* **Changed validation warning message within the close position UI.** Message changed from 'Specified value is more than the instrument maximum' to 'The amount entered exceeds the position size'.
* **Corrected the strings for the ThemeName type definition.** The possible values should have been lowercase: 'dark' & 'light'.
* **Moved Session breaks from Events to Appearance tab in chart options.** This reverts a breaking change made in `v25.0`.
* **Adding snippets for Trading Platform datafeed methods.** Some functions were lacking an out of the box snippet to use within their application.

## Version 25[​](#version-25 "Direct link to Version 25")

*Date: Mon May 22 2023*

**Breaking Changes**

* **Save and Load Chart Templates.** Add methods to the [save/load adapter](/charting-library-docs/v29/saving_loading/) to support chart templates.
* **Renew design for send order and buy sell buttons.** Renew design for send order and buy sell buttons:
  + Buttons are now rounded
  + Selected item and underline are now black
* **New TV logo.** What is changing:
  + Changing the size, boldness of the text
  + Indentation of the logo from the borders of the chart
* **One row for grid lines settings.** The grid lines settings have been combined into one row.
* **Remove magnet icon near cursor - Reverting feature.** Following reviews this piece of work was reverted.
* **Update the library branding.** Branding font and position is slightly changed.
* **Do not load Euclid font for the branding logo on chart.** The Euclid font will not load if there is an animated logo on the chart.
* **When the chart data is reset, the new request for data will only be for the visible range.** The previous behavior was that when [resetData](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#resetdata) was evoked, that the datafeed would be requested to provide data for the entire range of data already loaded for that symbol. The new behavior is that the request is now only for the current visible range. This more closely matches the behavior of the first load. If you require the old behavior then you can disable the `request_only_visible_range_on_reset` featureset.
* **Remove timezone & session breaks section from scale gear menu.** Time zone and Session breaks section has been removed from gear menu.
* **Update chart types icons.** Changed icons for Line, Area and Baseline chart types.
* **Move Session breaks from Appearance to Events tab.** Session breaks setting is moved to events tab.
* **Changed the gear icon.** Changed the icon for price scale settings button ('gear' in bottom-right corner).
* **Chart navigation buttons.** Navigation buttons at the bottom of the chart have a slightly new design.

**New Features**

* **Adding a new chart type HLC Area.** HLC Area is a new chart type available.
* **Handle variable-tick-size.** Added support for variable tick size.
* **Add new stats position for info line drawing "auto".** Option of automatic positioning of information block for infoline drawings was added "auto" (in addition to existing left, center, right).
* **Add new checkboxes for price range in Info Line drawing box.** Added 2 settings in linetools context menu:
  + Percent change
  + Change in pips
* **Add ability to move anchors continuously - not by bars.** Smooth resizing of icons, stickers and emojis was implemented.
* **Correct Chart settings text Price scale labels.** "LABELS" group in "Scales" tab of Chart settings has been renamed to "LABELS ON PRICE SCALE".
* **Show + button on cursor by hotkey.** Added hotkeys Alt+Ctrl (win) or Opt+Command (mac) for the appearance of the plus button under the cursor.
* **Add Data window item to context/legend three dots menu.** Added new item to context/legend three dots menu - "Data window..." with a shortcut. Opens Data Window in the right panel.
* **Add Volume profile indicators on the top of chart series.** Changed the default z-order for Volume Profile indicators and VP drawings. They are now located above the main series.
* **Added new time zone Anchorage Alaska.** Added new time zone Anchorage Alaska (UTC-9).
* **Separate chart types Line with markers and Stepline.** Step line and Line with markers types are added to the top toolbar chart types menu.
* **Added new time zone Casablanca.** Timezone Casablanca (UTC) has been added.
* **Try to load line tools code dynamically.** Fixed floating toolbar for Price Note to show color and text settings like for other drawings.
* **Add sticker drawing tool.** Add the ability to use stickers with `createMultipointShape` or `selectLineTool`.
* **Add Accelerator Oscillator indicator.**

**Improvements**

* **Theming support for pop-up menus.** Additional CSS custom properties have been added for styling pop-up menus. Pop-up (as known as 'pop-over') menus include toolbar menus, and context menus. See the full list of CSS custom properties in the [CSS Color Themes](/charting-library-docs/v29/customization/styles/CSS-Color-Themes) article.
* **Add date and time input UI for custom studies.** [Custom studies](/charting-library-docs/v29/custom_studies/) now support defining inputs of the `'time'` type and having a GUI element (date and time pickers) in the indicators settings dialog window.
* **setActiveChart added to the Widget API.** The currently active chart in a multi-chart layout (available on Trading Platform only) can now be changed using the `setActiveChart` method. [more info](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#setactivechart)

**Bug Fixes**

* **Include missing PriceAxisLastValueMode and LineStyle enums in type documentation.**

**Documentation**

* **The Overrides article update.** We have updated the [Overrides](/charting-library-docs/v29/customization/overrides/) article. Now it contains general information about the Overrides API. For information on how to customize elements on the chart, refer to a new [Chart Overrides](/charting-library-docs/v29/customization/overrides/chart-overrides) article.

## Version 24.004[​](#version-24004 "Direct link to Version 24.004")

*Date: Mon Apr 24 2023*

**New Features**

* **Indicators can now be favorited.** Indicators can now be favorited by tapping on the star icon to the left of the
  indicator name. Favorited indicators will appear at the top of the indicator
  list.
  + The `items_favoriting` featureset should be enabled. [more info](/charting-library-docs/v29/customization/Featuresets)
* **Adding two featuresets to hide the right\_toolbar or its tabs.** There are 2 new featuresets `hide_right_toolbar` & `hide_right_toolbar_tabs` plus an additional WidgetBar API [changeWidgetBarVisibility](/charting-library-docs/v29/api/interfaces/Charting_Library.IWidgetbarApi#changewidgetbarvisibility) to control the right toolbar.
  + `hide_right_toolbar` allows you to instantiate the toolbar without showing it in the UI.
  + `hide_right_toolbar_tabs` will do the same with the exception of not showing tabs when displaying the right toolbar.

**Improvements**

* **Added a middle band for the RSI indicator.** Unlike on tradingview.com RSI was not presenting the option to plot a middle limit.
* **Indicators favorites can now be defined within widget constructor.** Indicators can now be defined as favorites using the [`favorites`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#favorites) property of the widget constructor options. See [Favorites.indicators](/charting-library-docs/v29/api/interfaces/Charting_Library.Favorites#indicators) for more information.
* **Add a way to independently clear bar marks/timescale marks.** [`clearMarks`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#clearmarks) method has been enhanced to pass in an option to choose which marks should be cleared on the chart.
  + By default behaviour will remain similar and both bar & TimeScale marks will be removed.
  + Passing `ClearMarksMode.BarMarks` will only remove bar marks.
  + Passing `ClearMarksMode.TimeScaleMarks` will only remove TimeScale marks.
* **`BREAKING CHANGE` Discrepancy in chart style/type methods.** Only TypeScript breaking change as an interface has been renamed to better reflect its purpose.
  `SeriesStyle` is now [SeriesType](/charting-library-docs/v29/api/enums/Charting_Library.SeriesType).

**Bug Fixes**

* **load\_study\_template event is not emitted.** load\_study\_template event was not emitted when applying a template on the chart.
* **Fixed autosize bug occurring on Chrome iOS when rotating the device.** Workaround fix for a browser bug until Chrome resolves the issue on their side.
* **Fixed the type definitions for a few of the PineJS Std library functions.** [PineJSStd documentation](/charting-library-docs/v29/api/interfaces/Charting_Library.PineJSStd).

**Documentation**

* **New Key Features article.** We have added the [Key Features](/charting-library-docs/v29/getting_started/Key-Features) article that lists features supported/unsupported in Advanced Charts and Trading Platform.
* **How to connect data via Datafeed API.** We have added a new [tutorial on connecting data via Datafeed API](/charting-library-docs/v29/tutorials/implement_datafeed_tutorial/).
  It will help you implement datafeed and real-time data streaming to the library step-by-step.

**Other**

* **Incorrect watermark property key.** Deprecated `symbolWatermarkProperties` property has now been removed.
  Please use [settings\_adapter](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#settings_adapter) with `symbolWatermark` key instead or `applyOverrides` to change values.

## Version 24.003[​](#version-24003 "Direct link to Version 24.003")

*Date: Tue Apr 11 2023*

**New Features**

* **Images within bar marks.** Bar marks now support the rendering of images as the background by specifying the `imageUrl` property. Please see the [Mark](/charting-library-docs/v29/api/interfaces/Charting_Library.Mark) interface for more details.
* **Price Source and Long Description symbol info fields.** Add support for displaying the price source and long description fields from the symbol info.
  + To enable the price source first add `symbol_info_price_source` to the list of enabled features. Then it will be shown in the legend, if available. It can be hidden through the legend context menu and the series property dialog.
  + To enable the long description first add `symbol_info_long_description` to the list of enabled features. Then it will be shown in the legend, if available. It can be hidden through the legend context menu and the series property dialog.

**Improvements**

* **Added more styling options for bar marks.** The styling options for bar marks has been expanded to include options for styling the border.
  + Border color can be set using the `border` property within `color` of the Mark interface. See [MarkCustomColor](/charting-library-docs/v29/api/interfaces/Charting_Library.MarkCustomColor)
  + Border width can be set using `borderWidth` and `hoveredBorderWidth`. See [Mark](/charting-library-docs/v29/api/interfaces/Charting_Library.Mark)
* **Drawing tools favorites can now be defined within widget constructor.** Drawing tools can now be defined as favorites using the [`favorites`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#favorites) property of the widget constructor options. See [Favorites.drawingTools](/charting-library-docs/v29/api/interfaces/Charting_Library.Favorites#drawingtools) for more information.
* **Context menu API can now be used within the Watchlist.** `watchlist_context_menu` featureset is enabled by default. See [onContextMenu](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#oncontextmenu) for more details.
* **Improved typings within package.json.** The `package.json` bundled with the library has been improved to support newer versions of node, and offer improved typings. See [NPM](/charting-library-docs/v29/getting_started/NPM) for more details.
* **Price scale now supports numbers with more than 10 decimal points.**
* **Timezone data has been updated.**

**Bug Fixes**

* **Chart type won't change when restoring default options.** The chart type will no longer change when restoring the default options within the chart settings dialog.
* **Last visible bar value in legend for overlay studies.** When `use_last_visible_bar_value_in_legend` featureset is enabled, overlay studies will display the value for the last visible item on the chart. This now matches the behavior for the main series.
* **Fixed zoom behavior for percentage right margin option.** Incorrect zooming behavior has been fixed for zoom buttons appearing on the chart, and the keyboard shortcuts. See `show_percent_option_for_right_margin` [featureset](/charting-library-docs/v29/customization/Featuresets) for more information.

**Documentation**

* **Add FAQ about unsubscribeBars delay.** Added [a new FAQ](/charting-library-docs/v29/getting_started/Frequently-Asked-Questions) about [`unsubscribeBars`](/charting-library-docs/v29/connecting_data/datafeed-api/required-methods#unsubscribebars) being called with a delay.

**Other**

* **Added symbol information to datafeed error messages.** Added symbol information to realtime subscription error messages to improve the developer experience.
* **Updated localisation list.** The [list of support localisations](/charting-library-docs/v29/core_concepts/Localization) has been updated. Additionally, the chart will now fallback to english (with a console warning) if an unsupported locale is specified in the widget constructor options.

## Version 24.002[​](#version-24002 "Direct link to Version 24.002")

**New Features**

* **Added support for specifying custom timezones.**
  + Additional custom timezones can now be specified for use within the library. Please see the [Adding Custom Timezones](/charting-library-docs/v29/ui_elements/timezones#custom-time-zones) section within the Timezones page.
* **Images within timescale marks.**
  + Timescale marks now support the rendering of images within the circular shape by specifying the `imageUrl` property. Please see the [TimescaleMark](/charting-library-docs/v29/api/interfaces/Charting_Library.TimescaleMark) interface for more details.
* **Support different margin rates for different order types.** [6607](https://github.com/tradingview/charting_library/issues/6607)
  + `marginRate` has been deprecated
  + A [`supportLeverageButton`](/charting-library-docs/v29/api/interfaces/Broker.BrokerConfigFlags#supportleveragebutton) flag that displays a leverage button has been added to the Broker configuration.
  + The [`supportLeverage`](/charting-library-docs/v29/api/interfaces/Broker.BrokerConfigFlags#supportleverage) flag enables leverage calculation by getting information from `leverageInfo`.

**Enhancements**

* Add horizontal line at 0 for Momentum study.

**Bug fixes**

* [`setUserEditEnabled`](/charting-library-docs/v29/api/interfaces/Charting_Library.IStudyApi#setusereditenabled) does not hide 3 dots in Legend. [6765](https://github.com/tradingview/charting_library/issues/6765) | [6165](https://github.com/tradingview/charting_library/issues/6165)

  widget.activeChart().getAllStudies().forEach(({ id }) => {
  console.log(id);
  tvWidget.activeChart().getStudyById(id).setUserEditEnabled(false);
  });

  + setUserEditEnabled(false) should mask all icons except the "eye".
  + setUserEditEnabled(true) should restore all the icons.
* `priceFormatter` could previously only be used for main series. `priceFormatter` now applies to secondary series as well.
* `right_toolbar` featureset didn't have a default `on` value.
* Empty time frames at the bottom toolbar if `data_status: endofday`
* Export data doesn’t include projected data.

  + Projected data can be included by setting [`includeOffsetStudyValues`](/charting-library-docs/v29/api/interfaces/Charting_Library.ExportDataOptions#includeoffsetstudyvalues) to `true`.
  + `await widget.activeChart().exportData({ includeOffsetStudyValues: true });`
* Highest PineJS.Std function doesn’t work correctly with negative numbers.
* Missing types in bundled definition file. [7445](https://github.com/tradingview/charting_library/issues/7445) | [7446](https://github.com/tradingview/charting_library/issues/7446)
* Exposing `icon` prop in `CreateShapeOptionsBase`. [6723](https://github.com/tradingview/charting_library/issues/6723)
* Wrong extended session background color [7443](https://github.com/tradingview/charting_library/issues/7443)

**Documentation**

* Added [migration guide](/charting-library-docs/v29/trading_terminal/#how-to-migrate-from-advanced-charts) from Advanced Charts to Trading Platform.
* Added additional documentation for [Drawings](/charting-library-docs/v29/ui_elements/drawings/).
* Missing overrides in documentation. [7457](https://github.com/tradingview/charting_library/issues/7457)
* Updated documentation for [Marks](/charting-library-docs/v29/ui_elements/Marks).
* Align ChartMetaInfo & ChartData.

**Other**

* Removed `Australia/ACT` from the list of [timezones](/charting-library-docs/v29/ui_elements/timezones) within our documentation. Please use either the Sydney timezone or [specify your own custom timezone](/charting-library-docs/v29/ui_elements/timezones#custom-time-zones).

## Version 24.001[​](#version-24001 "Direct link to Version 24.001")

**New Features**

* **Adding originalText as an additional field to UndoRedoState.** Event should mention the name of the action in plain English in addition to also being translated to the corresponding language. [UndoRedoState](/charting-library-docs/v29/api/interfaces/Charting_Library.UndoRedoState#originalundotext)
* **Add the ability to change X-Axis margin % from Chart Properties.** A new [featureset](/charting-library-docs/v29/customization/Featuresets) has been added `show_percent_option_for_right_margin` that adds additional percentage option to the right margin section of the chart settings dialog.
* **Display rightmost visible value when in percent mode.** A new [featureset](/charting-library-docs/v29/customization/Featuresets) has been added `use_last_visible_bar_value_in_legend` to show the most recent “global” bar value. When this feature is enabled the rightmost bar in the visible range is used instead.
* **Ability to change on the fly the Currency and Unit label setting.** [currencyAndUnitVisibility API](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#currencyandunitvisibility)
* **Add simple SSR support.** Allow the library to be imported within a NodeJS context. This improves support for frameworks such as Remix.
* **Added [`clearUndoHistory`](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#clearundohistory).**

**Improvements**

* **Name to be used instead of ticker.** Allow a human friendly name to be returned from [`symbol_search_complete`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol_search_complete).

**Bug Fixes**

* **Incomplete indicators when using Heikin-Ashi.** Indicator line should draw to all the visible data points.
* **Compare study doesn’t save and restore ticker name correctly.** The compare study should work for custom ticker names just like it does for ticker names which match our format (with the colon).
* **VPFR: Right point is automatically moving when dragging start point.** When drawing the VPFR, or moving one of the anchor points, it is expected that the right anchor point should not move one bar further to the right.
* **Selecting Apply Defaults option within chart settings doesn’t work.** Some Settings even if not validated are not restored to their original values when Apply Defaults is selected.
* **Decentralised app browser loading error.** Chart fails to load in wallet apps like MetaMask, Trust & Phantom. Enable the `iframe_loading_compatibility_mode` [featureset](/charting-library-docs/v29/customization/Featuresets) to enable compatibility with these browsers.
* **When disabled, widget bar still present a significant margin.** Even when there aren't any pages or widget in the right toolbar and IF right\_toolbar is disabled, contrary to the drawing toolbar that vanishes the widget bar stays there with the pill button to expand it whereas there isn't anything to expand.
* **Can’t enable header\_compare feature without header\_symbol\_search.**
  + Disabling header\_symbol\_search should only hide the search button
  + Disabling header\_compare should only hide the compare button
* **Removed section of PostCSS syntax in bundled css files.**

**Other**

* **New Documentation site.** 🎉
* **Add `shape` to TimeScale.** Shape property is described in [TimescaleMark interface](/charting-library-docs/v29/api/interfaces/Charting_Library.TimescaleMark#shape).
* **Remove magnet icon near cursor.**

## Version 24[​](#version-24 "Direct link to Version 24")

* `preset` Widget-Constructor parameter has been removed. Users can still use some featuresets to mimic the same behavior by disabling the following list:
  + `'left_toolbar', 'header_widget', 'timeframes_toolbar', 'edit_buttons_in_legend', 'context_menus', 'control_bar', 'border_around_the_chart'`
* `chart_style_hilo` featureset is now enabled by default. This adds the High-low option to chart style controls dropdown. This featureset has been available since 1.15 but was previously disabled by default.
* Added typings for custom indicators. Typescript equivalents of our existing examples are available here: [Custom Studies Typescript Examples](/charting-library-docs/v29/custom_studies/Custom-Studies-Examples).
* [`symbol_search_complete`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#symbol_search_complete) has changed. The function now takes an additional search result object parameter, and returns an additional human-friendly symbol name.
* [Mark](/charting-library-docs/v29/ui_elements/Marks) tooltips do not support HTML anymore.

**UI changes**

* With this version you will notice that the top toolbar has been redesigned with the following changes:

  + Button padding & separator size have been reduced
  + Compare button has shifted next to Symbol
  + Drawing icon is now more prominent
  + New fullscreen icon
  + Save button style better highlights when there's a change
  + Top toolbar now extends to left & right edges
  + UI font changes to a default system one
  + Undo/redo buttons are now relocated next to the save button

**Trading Platform**

* Default formatter `textNoWrap` has been removed.
* `columnId` field of [SortingParameters](/charting-library-docs/v29/api/interfaces/Broker.SortingParameters) has been renamed to `property`.
* Required `id` field has been added to [column description](/charting-library-docs/v29/api/interfaces/Broker.AccountManagerColumnBase#id).
* Type of `formatter` field in [column description](/charting-library-docs/v29/api/interfaces/Broker.AccountManagerColumnBase#formatter) has been changed to [StandardFormatterName | FormatterName](/charting-library-docs/v29/api/enums/Charting_Library.StandardFormatterName).
* `property` field has been removed from `column description`. Use [dataFields](/charting-library-docs/v29/api/interfaces/Broker.AccountManagerColumnBase#datafields) field instead.
* Type of `formatter` field in [SummaryField](/charting-library-docs/v29/api/interfaces/Broker.AccountManagerSummaryField) has been changed to [StandardFormatterName](/charting-library-docs/v29/api/enums/Charting_Library.StandardFormatterName).

## Version 23[​](#version-23 "Direct link to Version 23")

* `Average close price line` is now masked by default in Chart settings and can be shown by using `show_average_close_price_line_and_label` featureset.

## Version 22[​](#version-22 "Direct link to Version 22")

* Methods getTimezone and setTimezone have been deprecated and will be removed in future versions. Use [getTimezoneApi](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#gettimezoneapi) instead.
* POST request data format sent to [snapshot\_url](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#snapshot_url) has been changed.
  Since this version this request contains `multipart/form-data` with the field `preparedImage` that represents binary data of the snapshot image in `image/png` format.
* Optional `inputs` arguments for [createStudy](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi#createstudy) has been changed from using an array of ordered values to an object with named properties. You can still use array-like inputs but it will be removed in further releases.
* The set of inputs for Moving Average study has been changed and the first input now is a symbol. If you used `createStudy` to create Moving Average study you will have to modify the list of inputs by simply adding an empty string as the first element:

  ```
  tvWidget.activeChart().createStudy('Moving Average', true, false, ['', 9]);
  ```

  instead of

  ```
  tvWidget.activeChart().createStudy('Moving Average', true, false, [9]);
  ```
* Study `Ichimoku` has been modified with some `Inputs` & `Style` properties renamed.
* Both `scrollPosition` and `defaultScrollPosition` from [Chart-Methods](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartWidgetApi) have been deprecated in favour of [rightOffset](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimeScaleApi#rightoffset) and [defaultRightOffset](/charting-library-docs/v29/api/interfaces/Charting_Library.ITimeScaleApi#defaultrightoffset) accordingly.
* The `rest.html` file and `datafeeds/rest` directory have been removed.
* When [subscribed](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#subscribe) to `drawing_event` a `click` is no longer emitted when a drawing is created. A `create` event is emitted instead.
* Study `True Strength Indicator` has been renamed to `True Strength Index` and modified with its style elements being properly named with 1st `Plot` becoming `True Strength Index` & second `Plot` becoming `Signal`.

**Trading Platform**

* The `watchList` method now returns a promise that resolves a watchlist API object when the watchlist widget has loaded.
* `suggestedQty` has been removed from the `Trading Host`.
* `dome_widget` featureset which controls the DOM widget visibility has be deprecated in favour of `dom_widget`.

## Version 21[​](#version-21 "Direct link to Version 21")

* Featureset `show_dialog_on_snapshot_ready` has been removed. [takeScreenshot](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#takescreenshot) makes a snapshot silently, so you can use the URL from [onScreenshotReady](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget#subscribe) callback to show your own dialog instead.
* Field `holidays` from [SymbolInfo](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) has been renamed to [`session_holidays`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session_holidays).
* `changeTheme` from [Widget Methods](/charting-library-docs/v29/api/interfaces/Charting_Library.IChartingLibraryWidget) now returns a Promise. You can apply other style modifications after the promise is fulfilled.
* Symbol type `bitcoin` has been renamed to `crypto`.
* The symbol search dialog suggestions list uses the `full_name` instead of the `exchange` and `symbol` value. This data is provided by your implementation of [searchSymbols](/charting-library-docs/v29/api/interfaces/Charting_Library.IDatafeedChartApi#searchsymbols).

**Trading Platform**

* `supportModifyOrder` flag has been marked deprecated and will be removed in future versions. Use `supportModifyOrderPrice`, `supportEditAmount` and `supportModifyBrackets` instead.
* `empty` formatter has been removed.
* Flag `durationForMarketOrders` has been removed from Broker Configuration `configFlags` object. To use duration with market orders, add appropriate order type to `supportedOrderTypes` array.
* `supportReducePosition` flag has been removed from the Broker Configuration `configFlags` object.
* `supportExecutions` flag has been added. If broker supports executions you need to set the flag to `true`.
* The default value of `asc` field of the [SortingParameters](/charting-library-docs/v29/api/interfaces/Broker.SortingParameters#asc) has been changed to `true`.
* The `customFormatters` field has been removed from the [accountManagerInfo](/charting-library-docs/v29/trading_terminal/account-manager/).
* `id`, `modificationProperty`, `fixedWidth`, `showOnMobile` and `showTooltipOnCell` fields have been removed from the [Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/) `column description`. The `property` field has been made mandatory, so you can use it instead of `id`.
* The string `id` field has been made mandatory in each `table` ([Account Manager](/charting-library-docs/v29/trading_terminal/account-manager/)) row.
* The return value of the method `placeOrder` in the [Broker API](/charting-library-docs/v29/trading_terminal/trading-concepts/#broker-api) has been changed from `Promise<void>` to `Promise<PlaceOrderResult>`.
* `contextMenuEvent` type in `contextMenuActions` in `AccountManagerInfo` interface has been changed from `MouseEvent` to `MouseEvent | TouchEvent`.
* The shape of the `news_provider` property in the [Widget Constructor options](/charting-library-docs/v29/api/interfaces/Charting_Library.TradingTerminalWidgetOptions#news_provider) has changed. The `is_news_generic` and `get_news` properties have been replaced with a single function.