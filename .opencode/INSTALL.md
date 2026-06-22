# Installing Unofficial Naval Skills for OpenCode

Add this repository to the `plugin` array in your global or project `opencode.json`:

```json
{
  "plugin": ["naval@git+https://github.com/thepraggyverse/naval.git"]
}
```

Restart OpenCode after changing the config. The OpenCode plugin registers this repository's `skills/` directory directly.

To pin a commit or tag, append a ref:

```json
{
  "plugin": ["naval@git+https://github.com/thepraggyverse/naval.git#main"]
}
```

## Local Development

From a checkout, point OpenCode at the package path:

```json
{
  "plugin": ["/path/to/naval"]
}
```

Restart OpenCode after changing the package source.

Validate a local checkout before linking it:

```bash
python3 scripts/validate_public.py
python3 scripts/check_coverage.py
python3 scripts/validate_direct_install.py
```

Optional saved reviews and learnings are configured through `n-setup`; memory remains off unless the user explicitly enables it.
