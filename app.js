// Point this to your live Vercel URL
const API_URL = "/api"; 
const API_KEY = "my_secret_landmark_key"; 

const FETCH_OPTIONS = {
    headers: { "x-api-key": API_KEY }
};

function resetView() {
    document.getElementById('resultsView').style.display = 'none';
    document.getElementById('searchView').style.display = 'block';
}

function extractCost(feeString) {
    if (!feeString || feeString.toLowerCase() === "free") return 0;
    const match = feeString.match(/\d+(\.\d+)?/);
    return match ? parseFloat(match[0]) : 0;
}

async function findMatches() {
    const budget = parseFloat(document.getElementById("budgetInput").value);
    const duration = parseInt(document.getElementById("durationInput").value);
    const btn = document.querySelector('.primary-btn');
    
    if (!budget || !duration) {
        alert("Please enter both budget and duration.");
        return;
    }

    btn.textContent = "Calculating...";

    try {
        // This fetch uses the API_KEY header so it won't get a 401 Error
        const response = await fetch(`${API_URL}/landmarks`, FETCH_OPTIONS);
        
        if (!response.ok) throw new Error(`API Error: ${response.status}`);
        const data = await response.json();
        
        const matches = [];
        
        data.landmarks.forEach(landmark => {
            const dailyCost = extractCost(landmark.entry_fee);
            const tripTotal = dailyCost * duration;
            const spare = budget - tripTotal;
            
            if (spare >= 0) {
                matches.push({ data: landmark, dailyCost, tripTotal, spare });
            }
        });

        document.getElementById('matchCount').textContent = matches.length;
        renderCards(matches, duration);
        
        document.getElementById('searchView').style.display = 'none';
        document.getElementById('resultsView').style.display = 'block';
        
    } catch (error) {
        console.error(error);
        alert("Unable to connect to the API. Make sure it is deployed correctly.");
    } finally {
        btn.textContent = "Find Matches";
    }
}

function renderCards(matches, duration) {
    const grid = document.getElementById('cardsGrid');
    grid.innerHTML = "";

    matches.forEach(match => {
        const landmark = match.data;
        const card = document.createElement("div");
        card.className = "match-card";
        
        // Formats the spare money with commas (e.g., 4,999)
        const formattedSpare = match.spare.toLocaleString();

        card.innerHTML = `
            <div style="position: relative;">
                <span class="tag">${landmark.site_type}</span>
                <img src="${landmark.icon}" alt="${landmark.title}" class="card-img" onerror="this.src='https://via.placeholder.com/300x180?text=No+Image'">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <div>
                        <h3>${landmark.title}</h3>
                        <p>${landmark.country}</p>
                    </div>
                    <div class="icon-btn">✎</div>
                </div>
                <div class="stat-row">
                    <span class="label">EST. PER DAY</span>
                    <span class="value green">${match.dailyCost === 0 ? 'Free' : '$' + match.dailyCost}</span>
                </div>
                <div class="stat-row">
                    <span class="label">${duration}-DAY TOTAL</span>
                    <span class="value">$${match.tripTotal}</span>
                </div>
            </div>
            <div class="card-footer">
                $${formattedSpare} to spare
            </div>
        `;
        grid.appendChild(card);
    });
}