async function evaluateDeal() {
    const text = document.getElementById('listingText').value;
    const listingPrice = parseFloat(document.getElementById('price').value);
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = "Analyzing...";

    // Simulate Item Extraction
    const simulatedItems = ["TaylorMade Burnder Driver", "Callaway RAZR X 7 Iron", "Odyssey Tri-Ball SRT Putter"];

    let totalValue = 0;
    let table = "<table border='1'><tr><th>Item</th><th>eBay Avg</th></tr>";

    for (const item of simulatedItems) {
        const avg = Math.floor(Math.random() * 100) + 50 // Simulate pricing
        totalValue += avg;
        table += `<tr><td>${item}</td><td>$${avg}</td></tr>`;
    }

    table += `</table><p>Total Estimated Value: $${totalValue.toFixed(2)}</p>`;
    table += `<p>Listing Price: $${listingPrice}</p>`;
    table += `<p><strong>Potential Profit: $${(totalValue - listingPrice).toFixed(2)}</strong></p>`;
    resultsDiv.innerHTML = table;
}