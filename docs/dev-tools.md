
pymarkdownlnt
=============

- Link: <https://pymarkdown.readthedocs.io/en/latest/>

```bash
# Scan recursively from the root of the repo
uv run pymarkdown scan -r .
uv run pymarkdown scan README.md

# Auto-fix issues where possible
uv run pymarkdown fix -r .
uv run pymarkdown fix README.md

```

Pre-commit
==========

```bash
uv run pre-commit install
uv run pre-commit run --all-files
uv run pre-commit run <hook-id>
uv run pre-commit run black
uv run pre-commit run mypy
```
