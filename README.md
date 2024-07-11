

Example repo showing how we are having trouble with cross-file analysis.




Running ` semgrep --config ./rules --pro .`


# Current ISSUES

- test_import_by_module
  - when we do a module import rather than directly importing a function semgrep seems to not be able to follow. so `module.function()` is not followed while `function()` is.
  - see source.py, and play with commenting and uncommenting
