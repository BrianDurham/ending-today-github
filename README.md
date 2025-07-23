# ending-today-github

A minimalist CLI tool for identifying available domain names from an Estibot "ending today" CSV file. It sorts domains by their Estibot appraised value and checks availability using your local `tldx` command-line tool.

---

## Features

- Reads Estibot CSV files (with `domain` and `appraised_value` columns)
- Sorts by highest Estibot value
- Uses `tldx` to check domain availability
- Prints results to stdout only — no database, no email, no fluff

---

## Usage

```bash
python ending-today-github.py estibot_endingtoday_2025-06-20.csv
```

Output will look like:

```
almaesami.com                  $18000
ivig.net                       $8100
poketbike.com                  $5300
```

---

## Requirements

- Python 3.7+
- `tldx` available in your `$PATH`  
  (It must return `"is available"` for available domains)

---

## Input Format

The script expects a CSV file with at least the following headers:

```
domain,appraised_value
```

Example row:

```
almaesami.com,18000
```

---

## ⚖️ License

MIT — do whatever you want, just don’t blame me if a domain sucks.

---

## 🧠 Author

Brian Durham  
Project page: [briandurham.net](https://briandurham.net)

