# Darwin Skillpacks Installer

Install scenario skillpacks from GitHub with one `npx` command.

## Usage

```bash
npx @githoldder/darwin-skillpacks list
npx @githoldder/darwin-skillpacks install all --target ./skills
npx @githoldder/darwin-skillpacks install 01-academic-writing --target ./skills
```

## Commands

| Command | Description |
|---|---|
| `list` | Show available skillpacks |
| `install <name>` | Clone one skillpack by name |
| `install all` | Clone all skillpacks |

## Notes

- This package shells out to `git clone`.
- Existing target directories are skipped by default.
- Use `--force` to replace an existing target directory.

