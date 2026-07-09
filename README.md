# DNSTester

[![DNSTester](https://healthchecks.io/b/2/665c2144-c2f2-4af3-8fa4-7c62c7801753.svg)](https://github.com/davift/DNSTester) ![Static Badge](https://img.shields.io/badge/Python-blue?style=social&logo=Python)

![tester](https://github.com/davift/DNSTester/blob/main/image-tester.png)

![propagation](https://github.com/davift/DNSTester/blob/main/image-propagation.png)

This tool aggregates multiple DNS sources, sorts them, and filters only the unique ones. Then, it tests whether they effectively resolve domains and optionally evaluates their performance.

- `dns-sources.list`
  - URLs of DNS sources.
- `dns-unique.list`
  - Unique, sorted DNS servers.
- `dns-latency.list`
  - Tested servers sorted by lowest latency.
- `dns-popular.list`
  - The most popular free DNS providers.
- `dns-geographic.list`
  - Geographically distributed servers, two per continent.
    - Africa
    - Asia
    - Europe
    - North America
    - Oceania
    - South America

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
usage: propagation.py [-h] [--all] [--geo] [--pop] domain

DNS Propagation Checker

positional arguments:
  domain      Name to be resolved

options:
  -h, --help  show this help message and exit
  --all       Test against all DNS servers (dns-latency.list)
  --geo       Only geographically located DNS (dns-geographic.list)
  --pop       Only popular DNS services (dns-popular.list)
```

## Dependencies

```
pip install -r requirements.txt
```
