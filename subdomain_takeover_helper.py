import argparse
import dns.resolver
import requests

def check_subdomain(subdomain):
    """
    Checks CNAME and HTTP response to detect potential takeover.
    Returns a tuple: (subdomain, cname, status, notes)
    """
    try:
        answers = dns.resolver.resolve(subdomain, 'CNAME')
        cname = str(answers[0].target).rstrip(".")
    except dns.resolver.NoAnswer:
        cname = None
    except dns.resolver.NXDOMAIN:
        return (subdomain, None, None, "NXDOMAIN - Subdomain does not exist")
    except Exception as e:
        return (subdomain, None, None, f"DNS Error: {e}")

    try:
        resp = requests.get(f"http://{subdomain}", timeout=10)
        status = resp.status_code
        content = resp.text.lower()
        # Basit kontrol: Cloudflare / GitHub / Heroku gibi takeover response stringleri
        takeover_signs = ["there isn't a github pages site here", "heroku app not found", "no such app", "project not found", "site not found"]
        notes = ""
        for sign in takeover_signs:
            if sign in content:
                notes = "Potential takeover detected!"
                break
    except requests.RequestException:
        status = None
        notes = "Request failed"

    return (subdomain, cname, status, notes)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Takeover Detector Helper")
    parser.add_argument("--input", required=True, help="Input file with subdomains")
    parser.add_argument("--output", required=True, help="Output file to save results")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        subdomains = [line.strip() for line in f if line.strip()]

    results = []
    for sub in subdomains:
        print(f"🔍 Checking {sub}")
        res = check_subdomain(sub)
        results.append(res)

    with open(args.output, "w", encoding="utf-8") as f:
        for subdomain, cname, status, notes in results:
            f.write(f"{subdomain} | CNAME: {cname} | Status: {status} | Notes: {notes}\n")

    print(f"✅ Subdomain takeover check completed. Results saved to {args.output}")
