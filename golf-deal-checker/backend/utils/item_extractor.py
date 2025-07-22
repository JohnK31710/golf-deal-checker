def extract_items(title, description):
    """
    Extracts golf clubs and bags from the given title and description.

    Args:
        title (str): The title of the Facebook listing.
        description (str): The description of the Facebook listing.

    Returns:
        list: A list of extracted items (golf clubs and bags).
    """
    items = []
    # Simple keyword-based extraction logic (can be improved)
    keywords = ['driver', 'iron', 'putter', 'wood', 'bag']
    
    # Combine title and description for extraction
    combined_text = title.lower() + " " + description.lower()
    
    for keyword in keywords:
        if keyword in combined_text:
            items.append(keyword.capitalize())
    
    return items