# security semgrep rules 

Semgrep rules and example scan targets for security scanning source code (especially third party libraries).

## Usage example

If you dont already have semgrep:

```
# install semgrep
pip3 install semgrep
```

Start scan: (after cloning repo)

```
# use the python/ rules; for other language rules use that folder instead
semgrep -c python/ /path/to/code/

# for example, to scan the test code:
semgrep -c python/  test-scripts/
```


