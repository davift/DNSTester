#!/usr/bin/python3
import dns.resolver
import concurrent.futures
import os
import argparse
import itertools

# DNS
def resolution(server, domain):
  try:
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [server]
    resolver.lifetime = 2
    resolver.timeout = 2
    answer = resolver.resolve(domain, "A")
    return [rdata.address for rdata in answer]
  except:
    pass
  return

def server_group(source, domain):
  with open(source, 'r') as file:
    servers = [line.strip() for line in file if line.strip()]
  print("[ DNS Propagation Tester ]")
  results = []
  with concurrent.futures.ThreadPoolExecutor(max_workers=(os.cpu_count()*32)) as executor:
    for i, result in enumerate(executor.map(resolution, servers, itertools.repeat(domain)), start=1):
      results.append(result)
      if result is not None:
        sorted_ips = sorted(result, key=lambda ip: list(map(int, ip.split('.'))))
        print(f'  ■ {sorted_ips}', flush=True)
      else:
        print('  ☐ failed', flush=True)

# MAIN FUNCTION
def main():
  parser = argparse.ArgumentParser(description="Propagation Tester")
  parser.add_argument('domain', type=str, help='Name to be resolved')
  parser.add_argument('--all', action='store_true', help='Test against all DNS servers')
  parser.add_argument('--geo', action='store_true', help='Only on geographically located DNS')
  parser.add_argument('--pop', action='store_true', help='Only on popular DNS services')
  args = parser.parse_args()
  domain = args.domain

  if args.all:
    server_group("dns-latency.list", domain)
    exit()
  if args.geo:
    server_group("dns-geographic.list", domain)
    exit()
  if args.pop:
    server_group("dns-popular.list", domain)
    exit()
  else:
    print('')
    print('Invalid option')
    print('')
    exit()

if __name__ == "__main__":
  main()
