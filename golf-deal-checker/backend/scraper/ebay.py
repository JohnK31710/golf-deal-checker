def fetch_sold_prices(club_names):
    import requests
    from bs4 import BeautifulSoup

    sold_prices = {}

    for club in club_names:
        search_url = f"https://www.ebay.com/sch/i.html?_nkw={club.replace(' ', '+')}&_sop=12"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find sold items
        sold_items = soup.find_all('div', class_='s-item__info')
        prices = []

        for item in sold_items:
            price_tag = item.find('span', class_='s-item__price')
            if price_tag:
                price_text = price_tag.text.replace('$', '').replace(',', '')
                try:
                    price = float(price_text)
                    prices.append(price)
                except ValueError:
                    continue

        if prices:
            avg_price = sum(prices) / len(prices)
            sold_prices[club] = avg_price

    return sold_prices

def main():
    # Example usage
    club_names = ["TaylorMade Burner Driver", "Callaway RAZR X 7 Iron", "Odyssey Tri-Ball SRT Putter"]
    prices = fetch_sold_prices(club_names)
    print(prices)

if __name__ == "__main__":
    main()