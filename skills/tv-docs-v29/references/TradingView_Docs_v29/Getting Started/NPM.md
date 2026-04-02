# Getting Started: NPM

Source: https://www.tradingview.com/charting-library-docs/v29/getting_started/NPM

* [Getting Started](/charting-library-docs/v29/getting_started/)* NPM

On this page

# NPM

You can install the library as an NPM dependency. Follow the steps below to set it up.

## 1. Configure package.json[​](#1-configure-packagejson "Direct link to 1. Configure package.json")

Specify the library version number.

```
{  
  "dependencies": {  
    "charting_library": "git@github.com:tradingview/charting_library.git#semver:28.0.0"  
  }  
}
```

Note that files located in `node_modules/charting_library/` are not bundled during the build process.
You need to ensure that these files are included on the server and can be accessed by a specific path.
To do this, add a script to copy the files into a folder that serves static assets. In this example, the `public` folder is used, but this may vary based on your project structure.
Adjust the `copy-files` command accordingly.

```
{  
  "scripts": {  
    "postinstall": "npm run copy-files",  
    "copy-files": "cp -R node_modules/charting_library/ public"  
  },  
  "dependencies": {  
    "charting_library": "git@github.com:tradingview/charting_library.git#semver:28.0.0"  
  }  
}
```

## 2. Run npm install[​](#2-run-npm-install "Direct link to 2. Run npm install")

This command also triggers the `postinstall` script, which copies the static files into the specified directory.

info

The library repository is private. `npm install` will only work if the Git client is logged into an account with access to the repository.
Refer to [Getting Access](/charting-library-docs/v29/getting_started/quick-start#getting-access) for more information.

If you encounter installation issues, ensure your [SSH public key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) is added to your GitHub account and set for verification. If the `ssh -T git@github.com` command works, your SSH is set up correctly.