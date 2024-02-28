# prettyson

**DEPRECATED: this formatter is deprecated. Its main use case was pre-commit hooks, but there is a
much better hook to use in that case:
<https://github.com/pre-commit/pre-commit-hooks/tree/main?tab=readme-ov-file#pretty-format-json>.
Please use that one instead.**

---

![CI](https://github.com/kokkonisd/prettyson/workflows/CI/badge.svg)
![codecov](https://codecov.io/gh/kokkonisd/prettyson/branch/master/graph/badge.svg)

A Python-based JSON file formatter, inspired by [Black](https://github.com/psf/black).

## installation

You can install `prettyson` via `pip`:

```text
$ python3 -m pip install prettyson
```

## how to use

Using `prettyson` is very simple; you just pass it the JSON files you want to format.

```text
$ prettyson my_json_file.json my_json_files/*.json
```

By default, `prettyson` will reformat your files in-place if they are incorrectly
formatted. If you just want to check your files, but not reformat them (as you would
in a pre-commit or CI context for example), you can use the _dry run_ option:

```text
$ prettyson --dry-run my_json_file.json
```

If you also want it to sort the JSON keys, use the _sort_ option:

```text
$ prettyson --sort my_json_file.json
```

By default, the indentation that is used is four spaces; you could specify a different
amount of spaces via the _indent_ option, or use tabs instead via the _use tabs_ option:

```text
$ prettyson --indent 2 my_json_file.json # 2-space indentation
$ prettyson --use-tabs my_json_file.json # tab indentation
```

You can get an exhaustive list of options by running:

```text
$ prettyson --help
```
