import requests

def wiki_page_exists(title):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "titles": title,
        "format": "json"
    }

    headers = {
        "User-Agent": "MyWikiChecker/1.0 (dubacsil@students.zhaw.com)"
    }

    response = requests.get(url, params=params, headers=headers)

    # Debug: check what's actually returned
    if response.status_code != 200:
        print("HTTP error:", response.status_code)
        return False

    if not response.text.strip():
        print("Empty response!")
        return False

    try:
        data = response.json()
    except Exception:
        print("Not JSON! Response was:")
        print(response.text[:500])
        return False

    pages = data["query"]["pages"]
    
    print(pages)

    for page_id in pages:
        if page_id == "-1":
            return False
        else:
            page_url = get_page_url(page_id)
            print(page_url)

    return True

def get_page_url(page_id):
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "pageids": page_id,
        "prop": "info",
        "inprop": "url",
        "format": "json"
    }

    headers = {
        "User-Agent": "MyWikiChecker/1.0"
    }

    res = requests.get(url, params=params, headers=headers)
    data = res.json()

    page = data["query"]["pages"][str(page_id)]
    return page.get("fullurl")


print(wiki_page_exists("Mbosi meteorite"))