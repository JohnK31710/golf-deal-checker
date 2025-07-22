# Golf Deal Checker

## Overview
The Golf Deal Checker is a web application designed to automate the process of evaluating the value of used golf clubs listed on Facebook Marketplace. By scraping data from Facebook and eBay, the application helps users determine if a listing is a good deal based on average selling prices.

## Project Structure
```
golf-deal-checker
├── backend
│   ├── app.py
│   ├── scraper
│   │   ├── facebook.py
│   │   └── ebay.py
│   ├── utils
│   │   ├── item_extractor.py
│   │   └── price_analyzer.py
│   └── requirements.txt
├── frontend
│   ├── static
│   │   ├── script.js
│   │   └── styles.css
│   └── templates
│       └── index.html
├── tests
│   └── test_scraper.py
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd golf-deal-checker
   ```

2. **Install Backend Dependencies**
   Navigate to the `backend` directory and install the required Python packages:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. **Run the Backend Server**
   Start the backend application:
   ```
   python app.py
   ```

4. **Access the Frontend**
   Open your web browser and go to `http://localhost:5000` to access the Golf Deal Checker interface.

## Usage
- Input the link to a Facebook Marketplace listing in the provided text area.
- Click the "Evaluate Deal" button to analyze the listing.
- The application will scrape the necessary data and display the potential profit based on eBay average prices.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.