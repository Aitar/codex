# Core Concepts: Localization

Source: https://www.tradingview.com/charting-library-docs/v29/core_concepts/Localization

* Core Concepts* Localization

On this page

# Localization

## Set up language[​](#set-up-language "Direct link to Set up language")

To set up a default language, specify the [`locale`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#locale) property in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).
Check out the [Widget Constructor tutorial](https://www.youtube.com/watch?v=bdvmM3FNnSY&t=1353s) on YouTube for an implementation example.

## Supported languages[​](#supported-languages "Direct link to Supported languages")

The languages that the library supports are listed below.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Language `locale` value|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Arabic `ar`| Catalan (Spain) `ca_ES`| Chinese (Taiwan) `zh_TW`| Chinese `zh`| English `en`| French `fr`| German (Germany) `de`| Hebrew (Israel) `he_IL`| Indonesian (Indonesia) `id_ID`| Italian `it`| Japanese `ja`| Korean `ko`| Malay (Malaysia) `ms_MY`| Polish `pl`| Portuguese `pt`| Russian `ru`| Spanish `es`| Swedish `sv`| Thai (Thailand) `th`| Turkish `tr`| Vietnamese `vi` | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

## Multiple languages[​](#multiple-languages "Direct link to Multiple languages")

To support several languages, you need to create a custom [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor) for each of them
and recreate the widget every time users switch the language.

## Unsupported locale[​](#unsupported-locale "Direct link to Unsupported locale")

If an unsupported locale is specified in the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor), the chart falls back to English with a console warning *locale isn't supported*.

## Custom translations[​](#custom-translations "Direct link to Custom translations")

If you want to provide custom translations for UI strings,
use the [`custom_translate_function`](/charting-library-docs/v29/api/interfaces/Charting_Library.ChartingLibraryWidgetOptions#custom_translate_function) property of the [Widget Constructor](/charting-library-docs/v29/core_concepts/Widget-Constructor).

## Right-to-left alignment[​](#right-to-left-alignment "Direct link to Right-to-left alignment")

The library supports right-to-left (RTL) alignment for RTL languages such as Arabic and Hebrew.
Note that the alignment affects only toolbars, dialogs, and other UI elements except the chart.