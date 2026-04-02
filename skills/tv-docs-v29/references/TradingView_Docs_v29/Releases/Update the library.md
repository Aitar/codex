# Releases: Update the library

Source: https://www.tradingview.com/charting-library-docs/v29/releases/Update-Library

* Releases* Update the library

On this page

# Update the library

This article describes how to update Advanced Charts and Trading Platform. To do this, follow the steps below.

info

We are committed to keeping up with the latest technology trends and ensuring the library is compatible with evolving platforms and browsers.
Therefore, we encourage you to regularly update the library's version.
By keeping the library up-to-date, you can enhance your app performance and make sure it works smoothly on the latest browsers.

## 1. Check a library version[​](#1-check-a-library-version "Direct link to 1. Check a library version")

Check your current library version. To do this, run the following command in a browser console:

```
TradingView.version()
```

## 2. Review release notes[​](#2-review-release-notes "Direct link to 2. Review release notes")

Review [release notes](/charting-library-docs/v29/releases/release-notes) that describe changes in a version you would like to install. If your current version is more than one release behind the desired one, you should also check release notes for the previous versions.

Pay special attention to **breaking changes**. These changes can cause errors and require some enhancements in your code.

## 3. Download a new version[​](#3-download-a-new-version "Direct link to 3. Download a new version")

Go to the [Advanced Charts](https://github.com/tradingview/charting_library) 🔐 or [Trading Platform](https://github.com/tradingview/trading_platform "The repository is private.") 🔐 (access is [restricted](/charting-library-docs/v29/getting_started/quick-start#getting-access "Click to open the 'Getting Access' section.")) repository and download the latest version of the `master` branch.

![Download a new version](/charting-library-docs/v29/assets/images/update_library-772e6e6743b48954e6044ef0d9785a8f.png)

If you want to download a version that is older than the latest, find the desired version among commits and reset the repository state to that commit.

![Old versions](/charting-library-docs/v29/assets/images/old-versions-e991cf1c2ed3bab831e0b45c68948538.png)

caution

Advanced Charts and Trading Platform should only be downloaded from the official TradingView repositories provided within this documentation. Obtaining the library from third-party services is strictly prohibited and may lead to legal consequences.

The library is not redistributable. Therefore, it is prohibited to use any part of the library in public repositories.

## 4. Unzip an archive[​](#4-unzip-an-archive "Direct link to 4. Unzip an archive")

When you download a ZIP archive, extract files from it to any folder you prefer.
We recommend that you do not replace an old version with a new one in the existing project, but put this version in a new place. In this case, you keep a working copy that you can check with.

## 5. Run the new version[​](#5-run-the-new-version "Direct link to 5. Run the new version")

To test the new version, run the following command in a command line:

```
npx serve <PATH_TO_YOUR_FOLDER>
```

As a result, you get a URL that you need to copy and insert into your browser's address bar. [Check the library version](#1-check-a-library-version) in a browser console to ensure you have installed the new version successfully.

## 6. Implement new features[​](#6-implement-new-features "Direct link to 6. Implement new features")

Implement new features if necessary. For more information about them, refer to the dedicated documentation sections that are introduced together with the features in the [release notes](/charting-library-docs/v29/releases/release-notes).

Everything that you worked on in previous versions should be compatible with the new version. However, you should always test your project on any versions you update to. If issues appear, make sure you have addressed all breaking changes.