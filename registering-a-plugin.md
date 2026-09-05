# Registering a plugin in this marketplace

Open a pull request with your entry added to `.claude-plugin/marketplace.json`.

About your entry:

- Point to the zipped plugin
  - typically via a release tag
  - `latest-release` is the default tag

    ```
    https://raw.githubusercontent.com/you/your-plugin/latest-release/dist/plugin.zip
    ```

  - the URL must point to a real resource, or the PR will be rejected.

What you add to `plugins` in `.claude-plugin/marketplace.json`:

```json
{
  "plugins": [
    …
    {
      "name": "your-plugin",
      "description": "One sentence saying what it does.",
      "source": {
        "source": "archive",
        "url": "https://raw.githubusercontent.com/you/your-plugin/latest-release/dist/plugin.zip"
      }
    }
  ]
}
```
