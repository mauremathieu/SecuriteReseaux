from app.tools.reconnaissance import WhoisTool

# Test manuel
domain = "google.com"
result = WhoisTool.parse_whois_data(domain)
print(result)