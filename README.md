# mats-utils

utility scripts for migrants & the state, particularly for data parity tracking

## Notes

- To access the M&TS Research Workspace (RW) mounted volume, follow [these instructions](https://nyu.service-now.com/sp?id=kb_article&sysparm_article=KB0016464&sys_kb_id=9fca03f4db3a8b802db91aac0b96194b) using project name `migrants_state`


## Prerequisites

You'll need Python, Git, and poetry installed to use the data and run the scripts available in `/lib`. On mac, we recommend using [Homebrew](https://brew.sh/) and [asdf](https://asdf-vm.com/). 

If you already have Homebrew [installed](https://docs.brew.sh/Installation):

### 1. Install asdf:

```sh
brew install coreutils curl git gh
brew install asdf
```

Then follow [the instructions](https://asdf-vm.com/guide/getting-started.html#_3-install-asdf) for your system to add `asdf` to your shell's `PATH`. If you're using ZSH, for example, you'll run:

```sh
echo -e "\n. $(brew --prefix asdf)/libexec/asdf.sh" >> ${ZDOTDIR:-~}/.zshrc
source ~/.zshrc
```

### 2. Install python via asdf
```sh
asdf plugin-add python
asdf plugin-add direnv
asdf direnv setup --shell zsh --version latest # if using ZSH! can replace with bash
```

### 3. Install pipx and poetry
```sh
brew install pipx
pipx ensurepath 
source ~/.zshrc # if using ZSH! can replace with ~/.bashrc
```

## Using this repo

### 1. Clone the project repo and set up local python

``` sh
gh repo clone migrants-and-the-state/mats-utils && cd mats-utils
adsf install python
poetry install
```
### 2. Run the scipts (e.g., catalog pairing)

``` sh
poetry run python lib/subset_relevant_catalog.py
```

