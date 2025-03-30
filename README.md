# DNSTester

![OPT](https://github.com/davift/DNSTester/blob/main/image.png)

This tool aggregates multiple DNS sources, sorts them, and filters only the unique ones. Then, it tests if they effectively resolve domains and optionally evaluates their performance.

- `dns-sources.list`
  – URLs of DNS sources.
- `dns-unique.list`
  – Unique, sorted DNS servers.

## Usage

```
usage: tester.py [-h] [--fetch] [--test] [--all]

Open DNS Tester

options:
  -h, --help  show this help message and exit
  --fetch     Fetch DNS lists
  --test      Test DNS servers
  --all       All steps: fetch and test
```

## Dependencies

```
pip install -r requirements.txt
```
