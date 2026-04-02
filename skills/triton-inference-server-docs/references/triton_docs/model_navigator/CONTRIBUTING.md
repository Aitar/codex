* Contributing

# Contributing[#](#contributing "Link to this heading")

Contributions are welcome, and they are much appreciated! Every little
helps, and we will always give credit.

## Types of Contributions[#](#types-of-contributions "Link to this heading")

### Report Bugs[#](#report-bugs "Link to this heading")

Report bugs at [triton-inference-server/model\_navigator#issues](https://github.com/triton-inference-server/model_navigator/issues).

If you are reporting a bug, include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs[#](#fix-bugs "Link to this heading")

Look through the GitHub issues for bugs. Anything tagged with âbugâ and âhelp
wantedâ is open to whoever wants to implement it.

### Implement Features[#](#implement-features "Link to this heading")

Look through the GitHub issues for features. Anything tagged with âenhancementâ and âhelp wantedâ is open to whoever would like to implement it.

### Write Documentation[#](#write-documentation "Link to this heading")

The Triton Model Navigator could always use more documentation, whether as part of
the official Triton Model Navigator docs, in docstrings, or even on the web in blog posts,
articles, and such.

### Submit Feedback[#](#submit-feedback "Link to this heading")

The best way to send feedback is to file an issue at [triton-inference-server/model\_navigator#issues](https://github.com/triton-inference-server/model_navigator/issues).

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible to make it easier to implement.

## Sign your Work[#](#sign-your-work "Link to this heading")

We require that all contributors âsign-offâ on their commits. This certifies that
the contribution is your original work, or you have the rights to submit it under
the same license or a compatible license.

Any contribution which contains commits that are not Signed-Off will not be accepted.

To sign off on a commit, you simply use the `--signoff` (or `-s`) option when committing your changes:

```
$ git commit -s -m "Add cool feature.
```

This will append the following to your commit message:

```
Signed-off-by: Your Name <your@email.com>
```

By doing this, you certify the below:

```
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.
1 Letterman Drive
Suite D4700
San Francisco, CA, 94129

Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.


Developer's Certificate of Origin 1.1

By making a contribution to this project, I certify that:

(a) The contribution was created in whole or in part by me and I have the right to submit it under the open source license indicated in the file; or

(b) The contribution is based upon previous work that, to the best of my knowledge, is covered under an appropriate open source license and I have the right under that license to submit that work with modifications, whether created in whole or in part by me, under the same open source license (unless I am permitted to submit under a different license), as indicated in the file; or

(c) The contribution was provided directly to me by some other person who certified (a), (b) or (c) and I have not modified it.

(d) I understand and agree that this project and the contribution are public and that a record of the contribution (including all personal information I submit with it, including my sign-off) is maintained indefinitely and may be redistributed consistent with this project or the open source license(s) involved.
```

## Get Started![#](#get-started "Link to this heading")

Ready to contribute? Hereâs how to set up the `Triton Model Navigator` for local development.

1. Fork the `Triton Model Navigator` repo on GitHub.
2. Clone your fork locally:

```
$ git clone git@github.com:your_name_here/model-navigator.git
```

3. Install your local copy into a virtualenv. Assuming you have virtualenvwrapper installed, this is how you set up your fork for local development:

```
$ mkvirtualenv model_navigator
$ cd model_navigator/
$ make install-dev
```

4. Create a branch for local development:

```
$ git checkout -b name-of-your-bugfix-or-feature
```

Now you can make your changes locally.

5. When youâre done making changes, check that your changes pass linters and the
   tests, including testing other Python versions with tox:

```
$ make lint  # will run i.a. flake8 and pytype linters
$ make test  # will run a test with on your current virtualenv
$ make test-fw  # will run a framework test inside framework container
```

6. Commit your changes and push your branch to GitHub:

```
$ git add .
$ git commit -s -m "Your detailed description of your changes."
$ git push origin name-of-your-bugfix-or-feature
```

7. Submit a pull request through the GitHub website.

### Pull Request Guidelines[#](#pull-request-guidelines "Link to this heading")

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.
2. If the pull request adds functionality, you should update the docs. Put
   your new functionality into a function with a docstring, and add the
   feature to the list in README.md.

### Tips[#](#tips "Link to this heading")

To run a subset of tests:

```
$ pytest tests.test_model_navigator
```

## Releasing[#](#releasing "Link to this heading")

As a reminder for the maintainers on how to deploy -
make sure all your changes are committed (including an entry in CHANGELOG.md) into the master branch.
Then run:

```
$ bump2version patch # possible: major / minor / patch
$ git push
$ git push --tags
```

## Documentation[#](#documentation "Link to this heading")

Add/update docstrings as defined in the [Google Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

## Contributor License Agreement (CLA)[#](#contributor-license-agreement-cla "Link to this heading")

Triton requires that all contributors (or their corporate entity) send
a signed copy of the [Contributor License
Agreement](https://github.com/NVIDIA/triton-inference-server/blob/master/Triton-CCLA-v1.pdf)
to triton-cla@nvidia.com.
*NOTE*: Contributors with no company affiliation can fill `N/A` in the
`Corporation Name` and `Corporation Address` fields.

