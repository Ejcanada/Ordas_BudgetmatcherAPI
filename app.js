// Point this to your live Vercel URL
const API_URL = "https://ordas-budgetmatcher-api.vercel.app"; 
const API_KEY = "my_secret_landmark_key"; 

const FETCH_OPTIONS = {
    headers: { "x-api-key": API_KEY }
};

let currentMatches = [];

function resetView() {
    document.getElementById('resultsView').style.display = 'none';
    document.getElementById('searchView').style.display = 'block';
}

// Fixes the image paths to use your local "images" folder
function getImageUrl(icon) {
    if (!icon || icon.trim() === "") return "";
    if (icon.startsWith("http")) return icon; 
    if (icon.includes("images/")) {
        return icon.startsWith("/") ? icon.substring(1) : icon;
    } else {
        const cleanIcon = icon.startsWith("/") ? icon.substring(1) : icon;
        return `images/${cleanIcon}`;
    }
}

function extractCost(feeString) {
    if (!feeString || feeString.toLowerCase() === "free") return 0;
    const match = feeString.match(/\d+(\.\d+)?/);
    return match ? parseFloat(match[0]) : 0;
}

async function findMatches() {
    const budgetInput = document.getElementById("budgetInput").value;
    const durationInput = document.getElementById("durationInput").value;
    
    if (!budgetInput || !durationInput) {
        alert("Please enter both your budget and duration.");
        return;
    }

    const budget = parseFloat(budgetInput);
    const duration = parseInt(durationInput);
    const btn = document.querySelector('.primary-btn');
    btn.textContent = "Calculating...";

    try {
        // Fetches from your live Vercel API
        const response = await fetch(`${API_URL}/landmarks`, FETCH_OPTIONS);
        if (!response.ok) throw new Error("API Connection Failed");
        const data = await response.json();
        
        const matches = [];
        
        data.landmarks.forEach(landmark => {
            const dailyCost = extractCost(landmark.entry_fee);
            const tripTotal = dailyCost * duration;
            const spare = budget - tripTotal;
            
            if (spare >= 0) {
                matches.push({
                    data: landmark,
                    dailyCost: dailyCost,
                    tripTotal: tripTotal,
                    spare: spare
                });
            }
        });

        currentMatches = matches;
        
        document.getElementById('matchCount').textContent = matches.length;
        renderCards(matches, duration);
        
        document.getElementById('searchView').style.display = 'none';
        document.getElementById('resultsView').style.display = 'block';
        
    } catch (error) {
        console.error(error);
        alert("Unable to connect to the API. Check the console for details.");
    } finally {
        btn.textContent = "Find Matches";
    }
}

function renderCards(matches, duration) {
    const grid = document.getElementById('cardsGrid');
    grid.innerHTML = "";

    if (matches.length === 0) {
        grid.innerHTML = `<p style="grid-column: 1/-1; text-align:center; color: #808080;">No destinations found for this budget.</p>`;
        return;
    }

    matches.forEach((match, index) => {
        const landmark = match.data;
        const card = document.createElement("div");
        card.className = "match-card";
        const formattedSpare = match.spare.toLocaleString();

        card.innerHTML = `
            <div style="position: relative;">
                <span class="tag">${landmark.site_type}</span>
                <img src="${getImageUrl(landmark.icon)}" alt="${landmark.title}" class="card-img" onerror="this.src='https://via.placeholder.com/300x180?text=No+Image'">
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