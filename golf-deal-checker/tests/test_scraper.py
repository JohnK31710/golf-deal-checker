def test_facebook_scraper():
    # Test the Facebook scraper functionality
    from backend.scraper.facebook import scrape_facebook_listing

    # Sample input for testing
    sample_listing = {
        'title': 'TaylorMade Golf Clubs Set',
        'description': 'Includes driver, irons, and putter.',
        'price': 250
    }

    result = scrape_facebook_listing(sample_listing)
    
    assert result['title'] == 'TaylorMade Golf Clubs Set'
    assert 'driver' in result['description']
    assert result['price'] == 250

def test_ebay_scraper():
    # Test the eBay scraper functionality
    from backend.scraper.ebay import get_average_price

    # Sample input for testing
    club_names = ['TaylorMade Driver', 'Callaway Iron', 'Odyssey Putter']
    
    average_price = get_average_price(club_names)
    
    assert isinstance(average_price, float)
    assert average_price > 0  # Assuming there are sold items for these clubs

def test_item_extractor():
    # Test the item extractor functionality
    from backend.utils.item_extractor import extract_items

    sample_description = "TaylorMade Golf Clubs Set includes driver, irons, and putter."
    
    items = extract_items(sample_description)
    
    assert 'driver' in items
    assert 'irons' in items
    assert 'putter' in items

def test_price_analyzer():
    # Test the price analyzer functionality
    from backend.utils.price_analyzer import calculate_profit

    total_value = 400
    listing_price = 250
    
    profit = calculate_profit(total_value, listing_price)
    
    assert profit == 150  # Expected profit calculation