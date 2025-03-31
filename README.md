# DNSTester

![OPT](https://github.com/davift/DNSTester/blob/main/image.png)

This tool aggregates multiple DNS sources, sorts them, and filters only the unique ones. Then, it tests if they effectively resolve domains and optionally evaluates their performance.

- `dns-sources.list`
  - URLs of DNS sources.
- `dns-unique.list`
  - Unique, sorted DNS servers.
- `dns-latency.list`
  - Tested servers sorted by lowest latency.
- `dns-popular.list`
  - The most popular free DNS providers.
- `dns-geographic.list`
  - Geographically distributed servers.

## Usage - tester.py

```
usage: tester.py [-h] [--fetch] [--test] [--all]

Open DNS Tester

options:
  -h, --help  show this help message and exit
  --fetch     Fetch DNS lists
  --test      Test DNS servers
  --all       All steps: fetch and test
```

## Usage - propagation.py

```
usage: propagation.py [-h] --domain DOMAIN [--timeout TIMEOUT]

DNS Propagation Checker

options:
  -h, --help          show this help message and exit
  --domain DOMAIN     Domain to check propagation for
  --timeout TIMEOUT   Timeout in seconds for DNS queries (default: 5)
```

## Dependencies

```
pip install -r requirements.txt
```
