# Grep + Regex Cheat Sheet

## 1. Basic Grep Usage

- `grep pattern file`: Search for lines matching pattern in file.
- `grep -i pattern file`: Case-insensitive search.
- `grep -v pattern file`: Invert match (show lines NOT matching).
- `grep -r pattern dir`: Recursive search in directory.

## 2. Anchors

| Pattern     | Meaning                         |
|-------------|----------------------------------|
| `^pattern`  | Matches lines starting with pattern |
| `pattern$`  | Matches lines ending with pattern |

## 3. Wildcards

| Pattern     | Meaning                                  |
|-------------|-------------------------------------------|
| `.`         | Matches any single character              |
| `*`         | Matches 0 or more of the previous character |
| `[]`        | Matches any one character in brackets     |
| `[^]`       | Matches any one character not in brackets |

**Examples**:
- `grep l.rts word.py` → Matches `alerts`, `blurts`, `flirts`
- `grep ^fruit word.py` → Lines starting with `fruit`
- `grep cat$ word.py` → Lines ending with `cat`

## 4. Extended Regex (with `grep -E`)

| Pattern     | Meaning                        |
|-------------|---------------------------------|
| `+`         | One or more                     |
| `?`         | Zero or one                     |
| `{n}`       | Exactly n repetitions           |
| `{n,}`      | n or more repetitions           |
| `{n,m}`     | Between n and m repetitions     |
| `|`         | OR operator                     |
| `()`        | Group expressions               |

**Examples**:
- `grep -E 'cat(s|fish)' file` → Match `cats` or `catfish`
- `grep -E '^a.{2,4}z$' file` → Match strings that start with `a`, end with `z`, and have 2–4 characters in between.

## 5. Useful Flags

| Flag      | Description                        |
|-----------|------------------------------------|
| `-n`      | Show line numbers                  |
| `-c`      | Count of matching lines            |
| `-l`      | Show filenames with matches        |
| `-H`      | Print filename before matching line|
| `--color` | Highlight matching text            |

---

🧠 Tip: Combine grep with `sort`, `uniq`, `cut`, `awk` for powerful text processing!
