# Module-System Formatting

Use `format_module_scripts.py` for Warband module-system files. It is a
conservative formatter: by default it only reports whether enabled cleanup
flags would change files. It does not normalize leading tabs, strip trailing
whitespace, rebuild Warband operation-block indentation, or wrap long lines
unless you ask it to.

Preview changes for all Expanded module files:

```bash
python3 tools/format_module_scripts.py --diff
```

Check whether files would change:

```bash
python3 tools/format_module_scripts.py --check
```

Write changes:

```bash
python3 tools/format_module_scripts.py --write
```

Strip trailing whitespace too:

```bash
python3 tools/format_module_scripts.py --strip-trailing-whitespace --write
```

Normalize leading tabs:

```bash
python3 tools/format_module_scripts.py --normalize-leading-tabs --write
```

Format one file:

```bash
python3 tools/format_module_scripts.py --write "Source/Source - Floris Expanded Mod Pack/Module/module_troops_part1.py"
```

Preview nested Warband operation indentation fixes for one file:

```bash
python3 tools/format_module_scripts.py --fix-operation-indent --diff "Source/Source - Floris Expanded Mod Pack/Module/module_scripts_part5.py"
```

Write nested Warband operation indentation fixes for one file:

```bash
python3 tools/format_module_scripts.py --fix-operation-indent --write "Source/Source - Floris Expanded Mod Pack/Module/module_scripts_part5.py"
```

Preview safe long-line wrapping for one file:

```bash
python3 tools/format_module_scripts.py --wrap-long-lines --max-line-length 180 --diff "Source/Source - Floris Expanded Mod Pack/Module/module_troops_part1.py"
```

Write safe long-line wrapping for one file:

```bash
python3 tools/format_module_scripts.py --wrap-long-lines --max-line-length 180 --write "Source/Source - Floris Expanded Mod Pack/Module/module_troops_part1.py"
```

The `--normalize-leading-tabs` and `--strip-trailing-whitespace` flags are
opt-in because this project has a lot of old whitespace, and removing all of it
can make diffs noisy.

The `--wrap-long-lines` flag is opt-in. It only splits one-line tuple/list
records that can be parsed confidently at top-level commas.

The `--fix-operation-indent` flag is also opt-in. It adjusts mixed tab/space
indentation inside nested Warband operation blocks, using `try_begin`,
`try_for_*`, `else_try`, and `try_end` as the structure markers. The older
`--troops` flag formats literal troop records into grouped header/stat lines
with expanded inventory rows, but it is broad and should only be used after
reviewing a diff.

Avoid generic Python formatters on these files. They usually destroy the
long table-style troop and item definitions.
