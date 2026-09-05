# Registering a plugin in this marketplace

Plugins are added by creating a pull request (PR) with the changes below.

## 1. Copy in the plugin files

The plugin's files should be copied into `plugins/<surface>/<plugin-name>/`.
The plugin's `.claude-plugin/plugin.json` goes directly under there along
with the rest of your plugin's files (skills, etc.).

## 2. Add a marketplace entry

Add an entry for your plugin under `plugins` in
`.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    …
    {
      "name": "your-plugin",
      "description": "One sentence saying what it does.",
      "version": "1.0.0",
      "author": {
        "name": "Your Name",
        "email": "you@example.com"
      },
      "source": "./plugins/claude/your-plugin",
      "category": "productivity"
    }
  ]
}
```

Use exactly the same fields as above, with appropriate values for the
plugin.

Note:

- `source` is a path in this repository and must start with `./`.
- `version`, `description` and `author` **must** match your plugin's own `plugin.json`.
- `category` belongs here, not in `plugin.json`, where it is ignored.

## 3. Validate the marketplace entry

Check the entry by running `scripts/validate.py`. It checks the catalogue and every
plugin it lists, and exits non-zero if anything is wrong.

## 4. Create the PR

Open a pull request targetting `main` with the above changes in it and paste
the output of `scripts/validate.py` into the description.
