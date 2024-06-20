

Example repo showing how we are having trouble with cross-file analysis.


Tracking from source->sink works fine when in a single file, but fails when we split those files up into different packages.


Running ` semgrep --config ./rules --pro .`

Expected to have multiple findings (one on code/main.py and another on code/all_in_one_file/main.py)

This now works once we added `code/folder/__init__.py` so there seeing some weirdness with module resolution (python is fun isn't it).
