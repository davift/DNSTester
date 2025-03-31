#!/usr/bin/python3
import dns.resolver
import concurrent.futures
import time
import os
import re
import argparse
import requests

# FETCHING DNS LISTS
def fetch_lists():
  print("[ Fetching DNS Lists ]", flush=True)
  with open("dns-sources.list", "r") as file:
    sources = [line.strip() for line in file if line.strip()]
  servers = set()
  i = 0
  for source in sources:
    i += 1
    try:
      response = requests.get(source, timeout=10)
      response.raise_for_status()
      servers.update(response.text.splitlines())
      print('■', end='', flush=True)
    except requests.RequestException as e:
      print('☐', end='', flush=True)
    if i % 100 == 0:
      print("\n", end="", flush=True)
  print("", flush=True)
  with open("dns-unique.list", "w") as file:
    for dns_entry in sorted(servers):
      match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', dns_entry)
      if match:
        server = match.group(1)
        if not (server.startswith("0.0.0.0") or server.startswith("10.") or server.startswith("172.16.") or server.startswith("172.31.") or server.startswith("192.168.")):
          file.write(f"{server}\n")

# TESTING DNS SERVERS
def dns_test(server):
  try:
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]
    resolver.lifetime = 2
    resolver.timeout = 2
    start_time = time.time()
    resolver.resolve("example.com", "A")
    duration = time.time() - start_time
    return server, duration
  except:
    pass
  return

def test_dns_servers():
  with open("dns-unique.list", 'r') as file:
    servers = [line.strip() for line in file if line.strip()]
  print("[ Testing DNS Servers ]")
  results = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=(os.cpu_count()*10)) as executor:
    for i, result in enumerate(executor.map(dns_test, servers), start=1):
      results.append(result)
      if result is not None:
        print('■', end='', flush=True)
      else:
        print('☐', end='', flush=True)
      if i % 100 == 0:
        print("\n", end="", flush=True)
  results = [result for result in results if result is not None]
  results.sort(key=lambda x: x[1])
  print("\n  [ Fastest DNS Servers ]")
  i = 0
  with open("dns-latency.list", "w") as file:
    for server, duration in results:
      i += 1
      if i <= 10:
        print(f"  {server} ({duration:.3f}s)")
      file.write(f"{server}\n")

# MAIN FUNCTION
def main():
  parser = argparse.ArgumentParser(description="DNS Tester")
  parser.add_argument('--fetch', action='store_true', help='Fetch DNS server lists')
  parser.add_argument('--test', action='store_true', help='Test DNS servers')
  parser.add_argument('--all', action='store_true', help='All steps: Fetch and Test')
  args = parser.parse_args()

  if args.fetch:
    fetch_lists()
    exit()
  if args.test:
    test_dns_servers()
    exit()
  if args.all:
    fetch_lists()
    test_dns_servers()
    exit()
  else:
    if input("Fetch DNS lists? (y/n): ").strip().lower() == 'y':
      fetch_lists()
    if input("Test all servers? (y/n): ").strip().lower() == 'y':
      test_dns_servers()
    exit()

if __name__ == "__main__":
  main()
