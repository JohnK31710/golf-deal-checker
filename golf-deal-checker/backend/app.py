from flask import Flask, request, jsonify
from scraper.facebook import scrape_facebook_listing
from scraper.ebay import get_ebay_prices
from utils.item_extractor import extract_items
from utils.price_analyzer import analyze_prices

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate_deal():
    data = request.json
    facebook_link = data.get('link')

    # Scrape data from Facebook
    title, description, listing_price = scrape_facebook_listing(facebook_link)

    # Extract items from the title and description
    items = extract_items(title, description)

    # Get average prices from eBay
    ebay_prices = get_ebay_prices(items)

    # Analyze prices and calculate potential profit
    total_value, potential_profit = analyze_prices(ebay_prices, listing_price)

    return jsonify({
        'title': title,
        'description': description,
        'listing_price': listing_price,
        'items': items,
        'total_value': total_value,
        'potential_profit': potential_profit
    })

if __name__ == '__main__':
    app.run(debug=True)