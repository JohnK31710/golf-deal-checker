def scrape_facebook_listing(url):
    # This function will scrape the Facebook Marketplace listing at the given URL
    # and return the title, description, and price of the golf clubs listed.

    import requests
    from bs4 import BeautifulSoup

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to load page")

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.find('h1').text.strip()

    # Extract price
    price = soup.find('span', class_='price').text.strip()

    # Extract description
    description = soup.find('div', class_='description').text.strip()

    return {
        'title': title,
        'price': price,
        'description': description
    }