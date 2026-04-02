# Connecting Data: Trading sessions

Source: https://www.tradingview.com/charting-library-docs/v29/connecting_data/Trading-Sessions

* [Connecting Data](/charting-library-docs/v29/connecting_data/)* Trading sessions

On this page

# Trading sessions

A trading session defines the hours in a week when a symbol is actively traded on an exchange. A session is passed to the library in the [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) field of the [`LibrarySymbolInfo`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo) object. Session time should be in the **exchange time zone**.

Note that the last (rightmost) time of any session is **non-inclusive**. For example, if you specify a `0930-1630` session and select
the one‑hour resolution, the following bars are displayed on the chart: `[09:30, 10:30, 11:30, 12:30, 13:30, 14:30, 15:30]`. The period of the last bar starts at 15:30 and ends at 16:30 that coincides with the end of the trading session.

caution

The [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) value affects how the library arranges data on the chart. Make sure you specify this property correctly to avoid potential issues, such as [shifted bars](/charting-library-docs/v29/connecting_data/Datafeed-Issues#library-shifts-bar-time).

## Session formats[​](#session-formats "Direct link to Session formats")

A trading session is defined by a string. This format allows you to describe a variety of sessions.

tip

You can use the [Session Parser](https://charting-library.tradingview-widget.com/checksession.html) to check your session string.

### 24/7 sessions[​](#247-sessions "Direct link to 24/7 sessions")

A session that runs 24 hours a day, 7 days a week, including Saturday and Sunday. It starts at 00:00 and ends at 00:00 the following day.

* `24x7`

### Intraday sessions[​](#intraday-sessions "Direct link to Intraday sessions")

A session within a day. For example:

* `0930-1600` starts at 09:30 and ends at 16:00 from Monday to Friday.
* `0000-0000` starts at 00:00 and ends at 00:00 the following day from Monday to Friday.

### Overnight sessions[​](#overnight-sessions "Direct link to Overnight sessions")

In the library, an **overnight** session is a session that starts **before** the trading day. For example, the trading day is Monday, but the session starts on Sunday.
A session is considered overnight by default in the following cases:

* The start time is more than the end time, for example, `1600-0930`. The session starts at 16:00 on the previous day and ends at 09:30 on the current day.
* The start time is equal to the end time, for example, `1700-1700`. The session starts at 17:00 on the previous day and ends at 17:00 on the current day. Note that the `0000-0000` value is considered to be an [intraday](#intraday-sessions) session.

In other cases, you can use the `F` character to specify the time for the previous day. For example:

* `1700F-2200` starts at 17:00 on the previous day and ends at 22:00 on the current day. For example, a Wednesday session starts at 17:00 on Tuesday and ends at 22:00 on Wednesday.
* `1900F-2350F` starts at 19:00 on the previous day and ends at 23:50 on the previous day. For example, a Monday session starts at 19:00 on Sunday and ends at 23:50 on Sunday.

To specify a session that starts several days before the trading day, use `Fn`, where `n` is the number of days. Note that the number of days cannot be more than 6. For example:

* `1900F3-1900` starts at 19:00 three days ago and ends at 19:00 on the current day. For example, a Monday session starts at 19:00 on Friday and ends at 19:00 on Monday.
* `1900F3-2350F3` starts at 19:00 three days ago and ends at 23:50 three days ago. For example, a Friday session starts at 19:00 on Tuesday and ends at 23:50 on Tuesday.

info

To specify a session that spans midnight but is not an overnight session in the library context, use time values larger than `2400`.
For example, `0930-2730`. In this case, a Monday session starts at 09:30 on Monday and ends at 03:30 on Tuesday.

### Multiple sessions[​](#multiple-sessions "Direct link to Multiple sessions")

There may be several sessions in one trading day. In this case, you should specify all sessions, separated by commas. For example, `0930-1400,1430-1700`. The first session starts at 09:30 and ends at 14:00. The second session starts at 14:30 and ends at 17:00.

### Different sessions for different days[​](#different-sessions-for-different-days "Direct link to Different sessions for different days")

By default, sessions take place from Monday to Friday. There are no sessions on Saturday and Sunday. You can specify a session for a certain day by adding `:n`, where `n` is a day number. Day numbers are `1` for Sunday and `7` for Saturday (`2` — Monday, `3` — Tuesday, etc.). Therefore, you can specify a Saturday/Sunday session. A session can relate to multiple days. For example, `0900-1400:23` means that the session starts at 09:00 and ends at 14:00 on Mondays and Tuesdays.

* `0900-1400:2|0900-1630` on Mondays the session starts at 09:00 and ends at 14:00. On all other days the session starts at 09:00 and ends at 16:30.
* `2200-2200:3456|1700F-2200:2` a Monday session starts at 17:00 on Sunday and ends at 22:00 on Monday. On all other days the session starts at 22:00 on the previous day and ends at 22:00 on the current day.
* `0930-1630:34567` starts at 09:30 and ends at 16:30 on Tuesday, Wednesday, Thursday, Friday, and Saturday.

### First trading day[​](#first-trading-day "Direct link to First trading day")

You can specify the first trading day of the week using semicolon:

* `1;0900-1630|0900-1400:2` — the first day of the week is Sunday.
* `0900-1630|0900-1400:2;6` — the first day of the week is Saturday.
* `0900-1630|0900-1400:2` — the first day of the week is Monday (default value).

### Forex sessions[​](#forex-sessions "Direct link to Forex sessions")

In Forex trading, sessions typically cover a full 24-hour period, five days a week, and use the time zone "Etc/UTC".
For example, you can configure a Forex session as `2200-2200`.

## Note about bar timestamps[​](#note-about-bar-timestamps "Direct link to Note about bar timestamps")

The first bar timestamp coincides with the session opening time. All the following bar timestamps are calculated from the first one. For example, the session starts at 09:15, and the timestamp of the first bar is 09:15. The selected resolution is 1 hour. In this case, the second bar timestamp is 10:15, the third is 11:15, etc. If you want to display timestamps like `[09:15, 10:00, 11:00,...]`, you should set [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) to `0900-HHMM` and [`session_display`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session_display) to `0915-HHMM`.

## Examples[​](#examples "Direct link to Examples")

* `0900-1630|0900-1400:2`

  All weekdays except Mondays have one session that starts at 09:00 and ends at 16:30. A Monday's session starts at 09:00 and ends at 14:00.

  |  |  |  |  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Fragment Meaning|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 0900‑1630 A session 0900-1630. This session will be assigned by default to all non-weekend days because it's not followed by the `:` specifier.| | Sessions separator. This character divides different sessions.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 0900‑1400 A session 0900-1400. It's the session for a day #2 (see below).|  |  |  |  | | --- | --- | --- | --- | | : Day specifier. This character follows the session hours and is followed by the day numbers.|  |  | | --- | --- | | 2 The day number for the session above (Monday). | | | | | | | | | | | |
* `1715F-0300,0915-1200,1300-1630:3456|1715F3-0300F2,0915-1200,1300-1630:2`

  Tuesday, Wednesday, Thursday, and Friday have three sessions. The first starts at 17:15 on the previous day and ends at 03:00 on the current day, the second starts at 09:15 on the current day and ends at 12:00, and the third starts at 13:00 and ends at 16:30.

  Monday also has three sessions. The first starts at 17:15 on Friday and ends at 03:00 on Saturday, the second starts at 09:15 on Monday and ends at 12:00, and the third one starts at 13:00 and ends at 16:30.

  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Fragment Meaning|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1715F‑0300 A session starts at 17:15 the day before and ends at 03:00.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 0915‑1200 A session starts at 09:15 and ends at 12:00 .|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1300‑1630 A session starts at 13:00 and ends at 16:30.|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | : Day specifier. This character follows the session hours and is followed by the day numbers.|  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 3456 The day numbers for the sessions above (Tuesday, Wednesday, Thursday, and Friday).|  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | Sessions separator. This character divides different sessions.|  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1715F3‑0300F2 A session starts at 17:15 three days ago and ends at 03:00 two days ago.|  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | | 0915‑1200 A session starts at 09:15 and ends at 12:00.|  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | | 1300‑1630 A session starts at 13:00 and ends at 16:30.|  |  |  |  | | --- | --- | --- | --- | | : Day specifier.|  |  | | --- | --- | | 2 The day number for the session above (Monday). | | | | | | | | | | | | | | | | | | | | | | | |

## Session history[​](#session-history "Direct link to Session history")

If session time has changed in the past, you can specify the history of session changes in the [`session`](/charting-library-docs/v29/api/interfaces/Charting_Library.LibrarySymbolInfo#session) property. To do this, provide a string that has the `SESSION#YYYYMMDD/SESSION` format and consists of the following elements:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Element Description Example|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | SESSION Trading hours specified in the [required format](#session-formats). `0930‑1700`| # A separator between the session and the day when it was rescheduled. | YYYYMMDD A day when the session was rescheduled. `20181114`| ∕ A separator between the sessions. | SESSION Trading hours of the current session. `1100‑1800` | | | | | | | | | | | | | | | | | |

Note that the string should include only past sessions and the current one. You cannot specify changes that will happen in the future.

tip

If you want to specify changes for a specific day, use the [`corrections`](/charting-library-docs/v29/connecting_data/Symbology#corrections) property.

### Session switch[​](#session-switch "Direct link to Session switch")

The session switch happens on the first day of the week according to the new session. For example, if the new session runs from Wednesday till Friday, Wednesday is considered the first day of the week.Otherwise, if the switch date falls midweek, the old session will stay in effect for the remainder of the current week. Consider the following cases:

1. The switch date coincides with the first day of week

   * Session: `09:30-17:00:3456#20240108/10:00-18:00`
   * Session switch date: 2024‑01‑08 (Monday)
   * First day of the week: Monday

   Since the switch date aligns with the first day of the week, the new session schedule begins on 2024‑01‑08.
2. The switch date does not coincide with the first day of week

   * Session: `09:30-17:00:3456#20240110/10:00-18:00`
   * Session switch date: 2024‑01‑10 (Wednesday)
   * First day of the week: Monday

   Since the switch day does not coincide with the first day of week, the new session schedule begins on the next Monday 2024‑01‑15.
   Until then, the previous session schedule (09:30-17:00) remains in effect.