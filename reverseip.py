import requests
import sys


def main():
	if len(sys.argv) < 2:
		print("Usage: python reverseip.py <taregt>")
		sys.exit(1)

	url = "https://domains.yougetsignal.com/domains.php"
	payload = {
		"remoteAddress": sys.argv[1],
		"key": "",
		"_": ""
	}

	res = requests.post(url, data=payload, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"})
	api = res.json()

	print("""
Found {} domain hosted on the same web server as {} ({}).
	""".format(api["domainCount"], api["remoteAddress"], api["remoteIpAddress"]))
	for lst in api.get("domainArray", []):
		print(lst[0])


if __name__ == "__main__":
	main()