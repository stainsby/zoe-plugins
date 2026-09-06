# Registering a plugin in this marketplace

Plugins are added by creating a pull request (PR) with the changes below.

## 1. Add your plugin

You need to have created a zipped archive of your plugin already.

From the root of this repository:

```sh
scripts/update-plugin.py path/to/your-plugin.zip
```

This copies the plugin into `plugins/<surface>/<plugin-name>/` and adds
its entry to `.claude-plugin/marketplace.json`, copying `name`, `version`,
`description` and `author` from your plugin config. You shouldn't edit those
fields in the marketplace entry.

## 2. Add the catalogue fields

Add a `category` to aid finding your plugin in listings.

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

## 3. Validate

Validate the whole marketplace with:

```sh
scripts/validate.py
```

## 4. Create a PR

Open a pull request targeting `main` with the above changes in it and paste
the output of `scripts/validate.py` into the description.
