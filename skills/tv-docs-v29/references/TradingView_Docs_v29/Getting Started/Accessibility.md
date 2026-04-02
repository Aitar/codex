# Getting Started: Accessibility

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/accessibility

* [Getting Started](/charting-library-docs/v29/getting_started/)* Accessibility

On this page

# Accessibility

## Disclaimer[​](#disclaimer "Direct link to Disclaimer")

The TradingView team is actively working to make the library more accessible and compliant with [Web Content Accessibility Guidelines (WCAG) 2.2](https://www.w3.org/TR/WCAG22/). We understand that our product is complex and feature-rich, and achieving full accessibility for everyone is an ongoing journey. It is important to note that certain components might not fully meet accessibility requirements.

If you encounter any accessibility issues or have suggestions for improvements, kindly contact us at `inclusion.feedback@tradingview.com`. Note that this email is exclusively for accessibility matters. All other questions should be directed to [GitHub Issues](https://github.com/tradingview/charting_library/issues "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")).

At this stage, the library ships with the following accessibility features.

## Keyboard navigation[​](#keyboard-navigation "Direct link to Keyboard navigation")

Users can navigate through elements on the top, bottom, and drawing toolbars using the `Tab` and arrow keys.

![Keyboard navigation](/charting-library-docs/v29/assets/images/keyboard-navigation-3b31fbd6f4be1baaf77d4cb219886d3e.gif)

By default, users should press `Alt` + `Z` to start navigation. Alternatively, you can enable the [`accessible_keyboard_shortcuts`](/charting-library-docs/v29/customization/Featuresets#accessible_keyboard_shortcuts) featureset to start the navigation with `Tab`. In this case, the built-in [shortcuts](/charting-library-docs/v29/getting_started/Shortcuts) listed in the table below are also changed.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action Default shortcut `accessible_keyboard_shortcuts`|  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Start keyboard navigation `Alt` + `Z` `Tab`| Switch between charts `Tab` `Shift` + `→`| Switch between charts in reverse order `Shift` + `Tab` `Shift` + `←` | | | | | | | | | | | |

tip

The library includes built-in shortcuts that allow users to perform actions in the UI. You can also add custom shortcuts. For more information, refer to [Shortcuts](/charting-library-docs/v29/getting_started/Shortcuts).

## Color and contrast[​](#color-and-contrast "Direct link to Color and contrast")

Colors on the chart are compliant with the [WCAG 2.2 AA standard](https://www.w3.org/TR/WCAG22/#contrast-minimum). The library also provides multiple customization options. For example, you can configure colors for different UI elements, resize the chart size, and adjust fonts. For more information, refer to the [Customization](/charting-library-docs/v29/customization/) section.

## Screen reader compatibility[​](#screen-reader-compatibility "Direct link to Screen reader compatibility")

The library supports the following screen readers.

* [VoiceOver](https://support.apple.com/en-us/guide/voiceover-guide/welcome/web) on macOS
* [Narrator](https://support.microsoft.com/en-us/windows/complete-guide-to-narrator-e4397a0d-ef4f-b386-d8ae-c172f109bdb1)/[JAWS](https://www.freedomscientific.com/products/software/jaws/)/[NVDA](https://www.nvaccess.org/about-nvda/) on Windows

To use a screen reader, users should download and enable it.