import whois

def get_domain_info(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    domain = input("Enter the domain to look up: ")
    info = get_domain_info(domain)
    print(info)