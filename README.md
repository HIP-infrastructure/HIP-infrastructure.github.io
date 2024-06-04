# HIP user documentation

User documentation for the Human Intracerebral EEG Platform, written with [Sphinx](https://www.sphinx-doc.org/en/master/index.html).
The dedicated website [hip-infrastructure.github.io](https://hip-infrastructure.github.io/) is automatically [deployed](https://github.com/HIP-infrastructure/HIP-infrastructure.github.io/settings/pages) when a commit is pushed to the `master` branch (this takes a few minutes).

# Installation

You need Python3, GIT and [Sphinx](https://www.sphinx-doc.org/en/master/usage/installation.html) installed on the computer you plan to use. Preferably, a computer running Ubuntu 20.04+ as it will make things easier.

In a `Terminal`:

```bash
sudo apt-get install -y python3
sudo apt-get install -y git
sudo apt-get install -y python3-sphinx
```

# How to use

#### Copy the repository
First you need to clone [the repository](https://github.com/HIP-infrastructure/HIP-infrastructure.github.io), so you have a local version of the documentation on your computer:

```bash
git clone git@github.com:HIP-infrastructure/HIP-infrastructure.github.io.git
```

Then you need to move inside the `docs` directory:

```bash
cd HIP-infrastructure.github.io/docs
```

#### Edit the source files

In the `docs` directory, you will find a `source` folder and a `build` folder:
* The `build` folder contains the html pages used for the website. You do not want to edit those files.
* The `source` folder contains the source files used to build the html pages. You want to edit those files. Source files have an `.rst ` extension.

Sphinx uses reStructuredText (reST) markup language and you may take a look at the [documentation](https://www.sphinx-doc.org/en/master/index.html) to learn how to edit `.rst ` files. You can also take the existing `.rst ` files as examples. You can use any text editor to edit those files, but do not change the extension.

#### Check the website locally

Once you have edited or created new `.rst ` files, you need to build the project using the following command:

```bash
make html
```

You can then check the result by opening the `HIP-infrastructure.github.io/docs/build/html/index.html` file in any web browser.
You will be able to navigate a local version of the website. If you are making several builds, don't forget to refresh the webpage you are viewing so the changes are taken into account. If this does not work, you may try to re-build the html pages from scratch using the commands:

```bash
make clean
make html
```

#### Publish the documentation

In order to publish your edits, you need to push your local version of the documentation to the [remote repository](https://github.com/HIP-infrastructure/HIP-infrastructure.github.io):

```bash
cd ..
git add .
git commit -m "My edits."
git push
```

Replace  `My edits.` with a message giving insights on the modifications you have made to the documentation.

Wait a couple of minutes before checking the new version of the documentation at [hip-infrastructure.github.io](https://hip-infrastructure.github.io/build/html/index.html)

# Acknowledgement

This research was supported by the EBRAINS research infrastructure, funded from the European Union’s Horizon 2020 Framework Programme for Research and Innovation under the Specific Grant Agreement No. 945539 (Human Brain Project SGA3).

This platform received funding from the Swiss State Secretariat for Education, Research and Innovation (SERI) as part of the Horizon Europe project “EBRAINS 2.0”, contract number 23.00638.
