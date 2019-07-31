# Git Checkout
An interactive Git client!

<a href="https://asciinema.org/a/ByGs7AeXHOlUMIKMjHmM7N9k5" target="_blank"><img src="https://asciinema.org/a/ByGs7AeXHOlUMIKMjHmM7N9k5.png" /></a>

## Installation
Requirements: Python 3.*

Run this scripts https://git.io/fNfqh:
```
wget -L https://git.io/fNfqh -O- | bash

# or (if you don't have wget)
source <(curl -s https://git.io/fNfqh)
```

This script installs `ginteract` with `--user`. Thus, you need to make sure that your python bin folder is in your `PATH`. Add the following `export` to your shell startup script (ie. `.bashrc`, `.zshrc`).
```
# MacOS
export PATH="/Users/<user>/Library/Python/<version>/bin:$PATH"

# Linux
export PATH="/home/<user>/Library/Python/<version>/bin:$PATH"
```
> To find our where `ginteract` is installed, run `python3 -c "import ginteract; print(ginteract.__file__)"`. This will print out something like `/Users/jacob/Library/Python/3.7/lib/python/site-packages/ginteract/__init__.py`.

## Usage
```
git ch  # checkout a branch
git mg  # merge a branch into current branch
git dl  # delete branches

# or use the commands directly
ginteract checkout
ginteract merge
ginteract delete
```

## TODO
- [x] Add GIF
- [x] Add tests
- [x] Bash script to install
- [x] Add delete support
- [x] Add merge support
- [ ] Remote support
