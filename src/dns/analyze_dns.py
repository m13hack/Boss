import dns.resolver
import tldextract
import numpy as np
import time
import random
import string

def domain_entropy(domain):
    return len(set(domain)) / len(domain)

def simulate_dns_traffic():
    domains = ["example.com", "test-login.xyz", "secure.paypa1.com"]
    results = []
    for domain in domains:
        entropy = domain_entropy(domain)
        resolver = dns.resolver.Resolver()
        try:
            start = time.time()
            resolver.resolve(domain, 'A')
            duration = time.time() - start
            known = "google" in resolver.nameservers[0]  # crude check
        except:
            duration = -1
            known = False

        results.append({
            "domain": domain,
            "entropy": round(entropy, 2),
            "query_time": duration,
            "known_resolver": known
        })
    return results
