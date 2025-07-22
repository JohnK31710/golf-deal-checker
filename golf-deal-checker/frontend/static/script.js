// frontend/static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const evaluateButton = document.getElementById('evaluateButton');
    evaluateButton.addEventListener('click', async function() {
        const link = document.getElementById('listingLink').value;
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = "Analyzing...";

        try {
            const response = await fetch('/api/evaluate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ link: link })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const data = await response.json();
            displayResults(data);
        } catch (error) {
            resultsDiv.innerHTML = "Error: " + error.message;
        }
    });

    function displayResults(data) {
        let table = "<table border='1'><tr><th>Item</th><th>eBay Avg</th></tr>";
        let totalValue = 0;

        data.items.forEach(item => {
            table += `<tr><td>${item.name}</td><td>$${item.avgPrice}</td></tr>`;
            totalValue += item.avgPrice;
        });

        table += `</table><p>Total Estimated Value: $${totalValue.toFixed(2)}</p>`;
        table += `<p>Listing Price: $${data.listingPrice}</p>`;
        table += `<p><strong>Potential Profit: $${(totalValue - data.listingPrice).toFixed(2)}</strong></p>`;
        document.getElementById('results').innerHTML = table;
    }
});