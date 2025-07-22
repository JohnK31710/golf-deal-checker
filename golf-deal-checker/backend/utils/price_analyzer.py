def analyze_prices(item_prices, listing_price):
    total_value = sum(item_prices)
    potential_profit = total_value - listing_price
    return total_value, potential_profit

def get_average_price(prices):
    if not prices:
        return 0
    return sum(prices) / len(prices)

def evaluate_deal(item_prices, listing_price):
    total_value, potential_profit = analyze_prices(item_prices, listing_price)
    is_good_deal = potential_profit > 0
    return {
        "total_value": total_value,
        "potential_profit": potential_profit,
        "is_good_deal": is_good_deal
    }