from fastapi import FastAPI, HTTPException, Header, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="World Heritage Sites API",
    description="A REST API containing 50 historical landmarks and sites globally.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Landmark(BaseModel):
    id: int
    title: str
    site_type: str
    established_year: int
    visitor_rating: str
    governing_body: str
    notable_architects: str
    icon: str
    description: str
    country: str
    city: str
    region: str
    protection_status: str
    annual_visitors: str
    entry_fee: str
    currency: str
    hotel_rate: int 

# 
landmarks = [
    {"id": 1, "title": "Banaue Rice Terraces", "site_type": "Cultural Landscape", "established_year": 100, "visitor_rating": "4.9/5", "governing_body": "UNESCO", "notable_architects": "Ifugao Ancestors", "icon": "/images/banaue.jpg", "description": "2,000-year-old terraces carved into the mountains.", "country": "Philippines", "city": "Banaue", "region": "Southeast Asia", "protection_status": "National Treasure", "annual_visitors": "120K", "entry_fee": "50 PHP", "currency": "PHP", "hotel_rate": 2500},
    {"id": 2, "title": "Historic City of Vigan", "site_type": "Cultural Heritage", "established_year": 1572, "visitor_rating": "4.8/5", "governing_body": "UNESCO", "notable_architects": "Spanish Builders", "icon": "/images/vigan.jpg", "description": "Best-preserved example of a planned Spanish colonial town.", "country": "Philippines", "city": "Vigan", "region": "Southeast Asia", "protection_status": "Historic Center", "annual_visitors": "450K", "entry_fee": "Free", "currency": "PHP", "hotel_rate": 3000},
    {"id": 3, "title": "Colosseum", "site_type": "Ancient Monument", "established_year": 80, "visitor_rating": "4.9/5", "governing_body": "Ministry of Culture", "notable_architects": "Flavian Dynasty", "icon": "/images/colosseum.jpg", "description": "Iconic oval amphitheatre in the centre of Rome.", "country": "Italy", "city": "Rome", "region": "Europe", "protection_status": "Archeological Site", "annual_visitors": "6.0M", "entry_fee": "16 EUR", "currency": "EUR", "hotel_rate": 150},
    {"id": 4, "title": "Machu Picchu", "site_type": "Ancient Ruin", "established_year": 1450, "visitor_rating": "5.0/5", "governing_body": "UNESCO", "notable_architects": "Inca Civilization", "icon": "/images/machu.jpg", "description": "15th-century Inca citadel in the Eastern Cordillera.", "country": "Peru", "city": "Aguas Calientes", "region": "South America", "protection_status": "Historic Sanctuary", "annual_visitors": "1.5M", "entry_fee": "175 PEN", "currency": "PEN", "hotel_rate": 400},
    {"id": 5, "title": "Taj Mahal", "site_type": "Cultural Monument", "established_year": 1653, "visitor_rating": "4.9/5", "governing_body": "ASI", "notable_architects": "Ustad Ahmad Lahori", "icon": "/images/taj.jpg", "description": "Ivory-white marble mausoleum on the river Yamuna.", "country": "India", "city": "Agra", "region": "South Asia", "protection_status": "Protected Monument", "annual_visitors": "6.5M", "entry_fee": "1100 INR", "currency": "INR", "hotel_rate": 4500},
    {"id": 6, "title": "Great Wall of China", "site_type": "Historical Fortification", "established_year": -221, "visitor_rating": "4.8/5", "governing_body": "SACH", "notable_architects": "Ming Dynasty", "icon": "/images/greatwall.jpg", "description": "Fortifications built across the historical northern borders.", "country": "China", "city": "Beijing", "region": "East Asia", "protection_status": "National Site", "annual_visitors": "10.0M", "entry_fee": "40 CNY", "currency": "CNY", "hotel_rate": 600},
    {"id": 7, "title": "Pyramids of Giza", "site_type": "Ancient Ruin", "established_year": -2560, "visitor_rating": "4.7/5", "governing_body": "SCA", "notable_architects": "Ancient Egyptians", "icon": "/images/pyramid.jpg", "description": "The oldest of the Seven Wonders of the Ancient World.", "country": "Egypt", "city": "Giza", "region": "North Africa", "protection_status": "World Heritage", "annual_visitors": "14.0M", "entry_fee": "240 EGP", "currency": "EGP", "hotel_rate": 1200},
    {"id": 8, "title": "Acropolis of Athens", "site_type": "Ancient Citadel", "established_year": -447, "visitor_rating": "4.8/5", "governing_body": "Ministry of Culture", "notable_architects": "Ictinus", "icon": "/images/athens.jpg", "description": "Ancient citadel located on a rocky outcrop.", "country": "Greece", "city": "Athens", "region": "Europe", "protection_status": "National Site", "annual_visitors": "3.0M", "entry_fee": "20 EUR", "currency": "EUR", "hotel_rate": 130},
    {"id": 9, "title": "Angkor Wat", "site_type": "Temple Complex", "established_year": 1150, "visitor_rating": "4.9/5", "governing_body": "APSARA", "notable_architects": "Khmer Empire", "icon": "/images/angkor.png", "description": "Largest religious structure in the world.", "country": "Cambodia", "city": "Siem Reap", "region": "Southeast Asia", "protection_status": "Archaeological Park", "annual_visitors": "2.6M", "entry_fee": "150000 KHR", "currency": "KHR", "hotel_rate": 200000},
    {"id": 10, "title": "Chichen Itza", "site_type": "Ancient City", "established_year": 600, "visitor_rating": "4.8/5", "governing_body": "INAH", "notable_architects": "Mayan Civilization", "icon": "/images/chichen.jpg", "description": "Large pre-Columbian city built by the Maya people.", "country": "Mexico", "city": "Tinum", "region": "Latin America", "protection_status": "Archaeological Zone", "annual_visitors": "2.5M", "entry_fee": "600 MXN", "currency": "MXN", "hotel_rate": 1500},
    {"id": 11, "title": "Petra", "site_type": "Historical City", "established_year": -312, "visitor_rating": "4.9/5", "governing_body": "PDTRA", "notable_architects": "Nabataeans", "icon": "/images/petra.jpg", "description": "Famous for its rock-cut architecture.", "country": "Jordan", "city": "Wadi Musa", "region": "Middle East", "protection_status": "Archaeological Park", "annual_visitors": "1.1M", "entry_fee": "50 JOD", "currency": "JOD", "hotel_rate": 90},
    {"id": 12, "title": "Statue of Liberty", "site_type": "Historical Monument", "established_year": 1886, "visitor_rating": "4.7/5", "governing_body": "NPS", "notable_architects": "Frédéric-Auguste Bartholdi", "icon": "/images/liberty.jpg", "description": "Colossal neoclassical sculpture in New York Harbor.", "country": "United States", "city": "New York", "region": "North America", "protection_status": "National Monument", "annual_visitors": "4.4M", "entry_fee": "24 USD", "currency": "USD", "hotel_rate": 250},
    {"id": 13, "title": "Eiffel Tower", "site_type": "Historical Monument", "established_year": 1889, "visitor_rating": "4.8/5", "governing_body": "SETE", "notable_architects": "Gustave Eiffel", "icon": "/images/eiffel.jpg", "description": "Wrought-iron lattice tower in Paris.", "country": "France", "city": "Paris", "region": "Europe", "protection_status": "Historic Monument", "annual_visitors": "6.2M", "entry_fee": "26 EUR", "currency": "EUR", "hotel_rate": 180},
    {"id": 14, "title": "Fushimi Inari Taisha", "site_type": "Shinto Shrine", "established_year": 711, "visitor_rating": "4.9/5", "governing_body": "Shinto Shrine Management", "notable_architects": "Hata Clan", "icon": "/images/fushimi.jpg", "description": "Head shrine of the kami Inari.", "country": "Japan", "city": "Kyoto", "region": "East Asia", "protection_status": "Cultural Property", "annual_visitors": "3.0M", "entry_fee": "Free", "currency": "JPY", "hotel_rate": 15000},
    {"id": 15, "title": "Christ the Redeemer", "site_type": "Cultural Monument", "established_year": 1931, "visitor_rating": "4.8/5", "governing_body": "ICMBio", "notable_architects": "Paul Landowski", "icon": "/images/christ.jpg", "description": "Art Deco statue of Jesus Christ.", "country": "Brazil", "city": "Rio de Janeiro", "region": "South America", "protection_status": "National Heritage", "annual_visitors": "2.0M", "entry_fee": "110 BRL", "currency": "BRL", "hotel_rate": 450},
    {"id": 16, "title": "Stonehenge", "site_type": "Prehistoric Monument", "established_year": -3000, "visitor_rating": "4.5/5", "governing_body": "English Heritage", "notable_architects": "Neolithic Builders", "icon": "/images/stone.jpg", "description": "Prehistoric monument on Salisbury Plain.", "country": "United Kingdom", "city": "Salisbury", "region": "Europe", "protection_status": "Scheduled Monument", "annual_visitors": "1.6M", "entry_fee": "23 GBP", "currency": "GBP", "hotel_rate": 110},
    {"id": 17, "title": "Alhambra Palace", "site_type": "Palace and Fortress", "established_year": 1238, "visitor_rating": "4.9/5", "governing_body": "Patronato", "notable_architects": "Nasrid Dynasty", "icon": "/images/alhambra.jpg", "description": "Palace and fortress complex in Andalusia.", "country": "Spain", "city": "Granada", "region": "Europe", "protection_status": "Historic Site", "annual_visitors": "2.7M", "entry_fee": "14 EUR", "currency": "EUR", "hotel_rate": 120},
    {"id": 18, "title": "Borobudur Temple", "site_type": "Buddhist Temple", "established_year": 825, "visitor_rating": "4.8/5", "governing_body": "Ministry of Culture", "notable_architects": "Gunadharma", "icon": "/images/boro.jpg", "description": "World's largest Buddhist temple.", "country": "Indonesia", "city": "Magelang", "region": "Southeast Asia", "protection_status": "Cultural Property", "annual_visitors": "2.1M", "entry_fee": "375000 IDR", "currency": "IDR", "hotel_rate": 800000},
    {"id": 19, "title": "Sydney Opera House", "site_type": "Performing Arts", "established_year": 1973, "visitor_rating": "4.8/5", "governing_body": "Trust", "notable_architects": "Jørn Utzon", "icon": "/images/sydney.jpg", "description": "Multi-venue performing arts centre.", "country": "Australia", "city": "Sydney", "region": "Oceania", "protection_status": "State Heritage", "annual_visitors": "10.0M", "entry_fee": "43 AUD", "currency": "AUD", "hotel_rate": 250},
    {"id": 20, "title": "Hagia Sophia", "site_type": "Historical Architecture", "established_year": 537, "visitor_rating": "4.9/5", "governing_body": "Ministry of Culture", "notable_architects": "Isidore", "icon": "/images/hagia.jpg", "description": "Major cultural and historical monument.", "country": "Turkey", "city": "Istanbul", "region": "Europe", "protection_status": "Historical Reserve", "annual_visitors": "3.7M", "entry_fee": "850 TRY", "currency": "TRY", "hotel_rate": 2500},
    {"id": 21, "title": "Burj Khalifa", "site_type": "Modern Skyscraper", "established_year": 2010, "visitor_rating": "4.8/5", "governing_body": "Emaar", "notable_architects": "Adrian Smith", "icon": "/images/burj.jpg", "description": "The tallest building in the world.", "country": "United Arab Emirates", "city": "Dubai", "region": "Middle East", "protection_status": "Commercial Landmark", "annual_visitors": "17.0M", "entry_fee": "180 AED", "currency": "AED", "hotel_rate": 800},
    {"id": 22, "title": "Mount Fuji", "site_type": "Natural Landmark", "established_year": 0, "visitor_rating": "4.9/5", "governing_body": "Ministry of Environment", "notable_architects": "Nature", "icon": "/images/Mount-Fuji.jpg", "description": "Japan's highest mountain and active volcano.", "country": "Japan", "city": "Fujinomiya", "region": "East Asia", "protection_status": "National Park", "annual_visitors": "5.0M", "entry_fee": "1000 JPY", "currency": "JPY", "hotel_rate": 12000},
    {"id": 23, "title": "Table Mountain", "site_type": "Natural Landmark", "established_year": 0, "visitor_rating": "4.8/5", "governing_body": "SANParks", "notable_architects": "Nature", "icon": "/images/table.jpg", "description": "Flat-topped mountain forming a prominent landmark.", "country": "South Africa", "city": "Cape Town", "region": "Africa", "protection_status": "National Park", "annual_visitors": "1.1M", "entry_fee": "400 ZAR", "currency": "ZAR", "hotel_rate": 1800},
    {"id": 24, "title": "Sagrada Familia", "site_type": "Basilica", "established_year": 1882, "visitor_rating": "4.8/5", "governing_body": "Catholic Church", "notable_architects": "Antoni Gaudí", "icon": "/images/sagrada.jpg", "description": "Unfinished Roman Catholic minor basilica.", "country": "Spain", "city": "Barcelona", "region": "Europe", "protection_status": "UNESCO", "annual_visitors": "4.5M", "entry_fee": "26 EUR", "currency": "EUR", "hotel_rate": 150},
    {"id": 25, "title": "Banff National Park", "site_type": "National Park", "established_year": 1885, "visitor_rating": "4.9/5", "governing_body": "Parks Canada", "notable_architects": "Nature", "icon": "/images/banff.jpg", "description": "Canada's oldest national park in the Rockies.", "country": "Canada", "city": "Banff", "region": "North America", "protection_status": "National Park", "annual_visitors": "4.1M", "entry_fee": "11 CAD", "currency": "CAD", "hotel_rate": 280},
    {"id": 26, "title": "Neuschwanstein Castle", "site_type": "Palace", "established_year": 1886, "visitor_rating": "4.7/5", "governing_body": "Bavarian Palace Dept", "notable_architects": "Eduard Riedel", "icon": "/images/castle.jpg", "description": "19th-century historicist palace on a rugged hill.", "country": "Germany", "city": "Schwangau", "region": "Europe", "protection_status": "Historic Monument", "annual_visitors": "1.4M", "entry_fee": "15 EUR", "currency": "EUR", "hotel_rate": 140},
    {"id": 27, "title": "Grand Canyon", "site_type": "Natural Landmark", "established_year": 1919, "visitor_rating": "4.9/5", "governing_body": "NPS", "notable_architects": "Nature", "icon": "/images/grandcanyon.jpg", "description": "Steep-sided canyon carved by the Colorado River.", "country": "United States", "city": "Grand Canyon Village", "region": "North America", "protection_status": "National Park", "annual_visitors": "5.9M", "entry_fee": "35 USD", "currency": "USD", "hotel_rate": 200},
    {"id": 28, "title": "Victoria Falls", "site_type": "Waterfall", "established_year": 1952, "visitor_rating": "4.9/5", "governing_body": "Zambia Wildlife", "notable_architects": "Nature", "icon": "/images/victoria.jpg", "description": "Spectacular waterfall on the Zambezi River.", "country": "Zambia", "city": "Livingstone", "region": "Africa", "protection_status": "World Heritage", "annual_visitors": "1.0M", "entry_fee": "300 ZMW", "currency": "ZMW", "hotel_rate": 1500},
    {"id": 29, "title": "Blue Lagoon", "site_type": "Geothermal Spa", "established_year": 1992, "visitor_rating": "4.6/5", "governing_body": "Private", "notable_architects": "Nature/Modern", "icon": "/images/bluelagoon.jpg", "description": "Famous geothermal spa in a lava field.", "country": "Iceland", "city": "Grindavík", "region": "Europe", "protection_status": "Protected Area", "annual_visitors": "1.3M", "entry_fee": "8500 ISK", "currency": "ISK", "hotel_rate": 35000},
    {"id": 30, "title": "Golden Gate Bridge", "site_type": "Suspension Bridge", "established_year": 1937, "visitor_rating": "4.8/5", "governing_body": "Highway District", "notable_architects": "Joseph Strauss", "icon": "/images/goldengate.jpg", "description": "Iconic red suspension bridge spanning the Golden Gate.", "country": "United States", "city": "San Francisco", "region": "North America", "protection_status": "Historic Civil Engineering", "annual_visitors": "10.0M", "entry_fee": "Free", "currency": "USD", "hotel_rate": 280},
    {"id": 31, "title": "Mount Everest", "site_type": "Natural Landmark", "established_year": 0, "visitor_rating": "4.9/5", "governing_body": "Nepal Tourism Board", "notable_architects": "Nature", "icon": "/images/everest.jpg", "description": "Earth's highest mountain above sea level.", "country": "Nepal", "city": "Khumbu", "region": "South Asia", "protection_status": "National Park", "annual_visitors": "35K", "entry_fee": "3000 NPR", "currency": "NPR", "hotel_rate": 1500},
    {"id": 32, "title": "Yellowstone National Park", "site_type": "National Park", "established_year": 1872, "visitor_rating": "4.9/5", "governing_body": "NPS", "notable_architects": "Nature", "icon": "/images/yellowstone.jpg", "description": "First national park in the US, famous for geysers.", "country": "United States", "city": "West Yellowstone", "region": "North America", "protection_status": "National Park", "annual_visitors": "4.5M", "entry_fee": "35 USD", "currency": "USD", "hotel_rate": 250},
    {"id": 33, "title": "Serengeti National Park", "site_type": "Wildlife Reserve", "established_year": 1951, "visitor_rating": "4.9/5", "governing_body": "TANAPA", "notable_architects": "Nature", "icon": "/images/serengeti.jpg", "description": "Famous for its annual migration of over 1.5 million wildebeest.", "country": "Tanzania", "city": "Arusha", "region": "Africa", "protection_status": "World Heritage", "annual_visitors": "350K", "entry_fee": "175000 TZS", "currency": "TZS", "hotel_rate": 500000},
    {"id": 34, "title": "Venice and its Lagoon", "site_type": "Historic City", "established_year": 421, "visitor_rating": "4.7/5", "governing_body": "UNESCO", "notable_architects": "Venetian Republic", "icon": "/images/venice.jpg", "description": "City built on 118 small islands separated by canals.", "country": "Italy", "city": "Venice", "region": "Europe", "protection_status": "World Heritage", "annual_visitors": "20.0M", "entry_fee": "5 EUR", "currency": "EUR", "hotel_rate": 200},
    {"id": 35, "title": "Galápagos Islands", "site_type": "Archipelago", "established_year": 1535, "visitor_rating": "4.9/5", "governing_body": "Ecuadorian Government", "notable_architects": "Nature", "icon": "/images/galapagos.jpg", "description": "Volcanic archipelago famous for its unique wildlife.", "country": "Ecuador", "city": "Puerto Ayora", "region": "South America", "protection_status": "National Park", "annual_visitors": "275K", "entry_fee": "100 USD", "currency": "USD", "hotel_rate": 150},
    {"id": 36, "title": "Yosemite National Park", "site_type": "National Park", "established_year": 1890, "visitor_rating": "4.9/5", "governing_body": "NPS", "notable_architects": "Nature", "icon": "/images/yosemite.jpg", "description": "Famed for its giant, ancient sequoia trees and granite cliffs.", "country": "United States", "city": "Mariposa", "region": "North America", "protection_status": "World Heritage", "annual_visitors": "3.3M", "entry_fee": "35 USD", "currency": "USD", "hotel_rate": 300},
    {"id": 37, "title": "Great Barrier Reef", "site_type": "Coral Reef", "established_year": 0, "visitor_rating": "4.8/5", "governing_body": "GBRMPA", "notable_architects": "Nature", "icon": "/images/reef.jpg", "description": "World's largest coral reef system.", "country": "Australia", "city": "Cairns", "region": "Oceania", "protection_status": "Marine Park", "annual_visitors": "2.0M", "entry_fee": "7 AUD", "currency": "AUD", "hotel_rate": 200},
    {"id": 38, "title": "Pamukkale", "site_type": "Thermal Springs", "established_year": 0, "visitor_rating": "4.8/5", "governing_body": "Ministry of Culture", "notable_architects": "Nature", "icon": "/images/pamukkale.jpg", "description": "Natural site in Denizli famous for its carbonate mineral terraces.", "country": "Turkey", "city": "Denizli", "region": "Europe/Asia", "protection_status": "World Heritage", "annual_visitors": "2.5M", "entry_fee": "700 TRY", "currency": "TRY", "hotel_rate": 1500},
    {"id": 39, "title": "Uluru", "site_type": "Sandstone Formation", "established_year": 0, "visitor_rating": "4.8/5", "governing_body": "Parks Australia", "notable_architects": "Nature", "icon": "/images/uluru.jpg", "description": "Massive sandstone monolith in the heart of the Northern Territory.", "country": "Australia", "city": "Yulara", "region": "Oceania", "protection_status": "National Park", "annual_visitors": "300K", "entry_fee": "38 AUD", "currency": "AUD", "hotel_rate": 350},
    {"id": 40, "title": "Iguazu Falls", "site_type": "Waterfalls", "established_year": 1934, "visitor_rating": "4.9/5", "governing_body": "National Parks Admin", "notable_architects": "Nature", "icon": "/images/iguazu.jpg", "description": "Largest waterfall system in the world.", "country": "Argentina", "city": "Puerto Iguazú", "region": "South America", "protection_status": "National Park", "annual_visitors": "1.5M", "entry_fee": "10000 ARS", "currency": "ARS", "hotel_rate": 25000},
    {"id": 41, "title": "Prague Castle", "site_type": "Castle Complex", "established_year": 870, "visitor_rating": "4.7/5", "governing_body": "Czech Presidency", "notable_architects": "Bohemian Kings", "icon": "/images/prague.jpg", "description": "Largest ancient castle in the world.", "country": "Czech Republic", "city": "Prague", "region": "Europe", "protection_status": "National Monument", "annual_visitors": "1.8M", "entry_fee": "450 CZK", "currency": "CZK", "hotel_rate": 2000},
    {"id": 42, "title": "Dubrovnik Old City", "site_type": "Historic City", "established_year": 700, "visitor_rating": "4.8/5", "governing_body": "UNESCO", "notable_architects": "Republic of Ragusa", "icon": "/images/dubrovnik.jpg", "description": "Prominent tourist destination known for its massive stone walls.", "country": "Croatia", "city": "Dubrovnik", "region": "Europe", "protection_status": "World Heritage", "annual_visitors": "1.2M", "entry_fee": "35 EUR", "currency": "EUR", "hotel_rate": 180},
    {"id": 43, "title": "Mont Saint-Michel", "site_type": "Island Commune", "established_year": 708, "visitor_rating": "4.8/5", "governing_body": "Centre des monuments", "notable_architects": "William de Volpiano", "icon": "/images/mont.jpg", "description": "Tidal island topped by a gravity-defying medieval monastery.", "country": "France", "city": "Normandy", "region": "Europe", "protection_status": "Historic Monument", "annual_visitors": "3.0M", "entry_fee": "11 EUR", "currency": "EUR", "hotel_rate": 140},
    {"id": 44, "title": "Kinkaku-ji", "site_type": "Zen Temple", "established_year": 1397, "visitor_rating": "4.7/5", "governing_body": "Shokoku-ji", "notable_architects": "Ashikaga Yoshimitsu", "icon": "/images/kinkaku.jpg", "description": "Golden Pavilion Zen Buddhist temple.", "country": "Japan", "city": "Kyoto", "region": "East Asia", "protection_status": "Cultural Property", "annual_visitors": "2.0M", "entry_fee": "500 JPY", "currency": "JPY", "hotel_rate": 15000},
    {"id": 45, "title": "Moai Statues", "site_type": "Megalithic Statues", "established_year": 1250, "visitor_rating": "4.8/5", "governing_body": "CONAF", "notable_architects": "Rapa Nui people", "icon": "/images/moai.jpg", "description": "Monolithic human figures carved by the Rapa Nui people.", "country": "Chile", "city": "Easter Island", "region": "South America", "protection_status": "World Heritage", "annual_visitors": "100K", "entry_fee": "80 USD", "currency": "USD", "hotel_rate": 180},
    {"id": 46, "title": "Plitvice Lakes", "site_type": "National Park", "established_year": 1949, "visitor_rating": "4.8/5", "governing_body": "Plitvice Authority", "notable_architects": "Nature", "icon": "/images/plitvice.jpg", "description": "Forest reserve known for a chain of 16 terraced lakes.", "country": "Croatia", "city": "Plitvička Jezera", "region": "Europe", "protection_status": "National Park", "annual_visitors": "1.0M", "entry_fee": "40 EUR", "currency": "EUR", "hotel_rate": 120},
    {"id": 47, "title": "Ha Long Bay", "site_type": "Limestone Karsts", "established_year": 0, "visitor_rating": "4.7/5", "governing_body": "Quang Ninh Province", "notable_architects": "Nature", "icon": "/images/halongbay.jpg", "description": "Emerald waters and thousands of towering limestone islands.", "country": "Vietnam", "city": "Ha Long", "region": "Southeast Asia", "protection_status": "World Heritage", "annual_visitors": "2.5M", "entry_fee": "290000 VND", "currency": "VND", "hotel_rate": 1500000},
    {"id": 48, "title": "Forbidden City", "site_type": "Palace Complex", "established_year": 1420, "visitor_rating": "4.7/5", "governing_body": "Palace Museum", "notable_architects": "Kuai Xiang", "icon": "/images/forbidden.jpg", "description": "Former Chinese imperial palace and winter residence.", "country": "China", "city": "Beijing", "region": "East Asia", "protection_status": "World Heritage", "annual_visitors": "19.0M", "entry_fee": "60 CNY", "currency": "CNY", "hotel_rate": 600},
    {"id": 49, "title": "Pompeii", "site_type": "Ancient Ruins", "established_year": -600, "visitor_rating": "4.8/5", "governing_body": "Ministry of Culture", "notable_architects": "Osci People", "icon": "/images/pompeii.jpg", "description": "Vast archaeological site once buried in ash by Mt. Vesuvius.", "country": "Italy", "city": "Pompei", "region": "Europe", "protection_status": "Archaeological Park", "annual_visitors": "3.8M", "entry_fee": "19 EUR", "currency": "EUR", "hotel_rate": 110},
    {"id": 50, "title": "Tikal", "site_type": "Ancient City", "established_year": 200, "visitor_rating": "4.8/5", "governing_body": "Ministry of Culture", "notable_architects": "Mayan Civilization", "icon": "/images/tikal.jpg", "description": "Ruins of an ancient city found in a rainforest.", "country": "Guatemala", "city": "Flores", "region": "Central America", "protection_status": "National Park", "annual_visitors": "300K", "entry_fee": "150 GTQ", "currency": "GTQ", "hotel_rate": 500}
]

validated_landmarks = [Landmark(**landmark).model_dump() for landmark in landmarks]
landmarks = validated_landmarks

# ==========================================
# API KEY AUTHENTICATION
# ==========================================
API_KEY = "my_secret_landmark_key" # my password

def verify_api_key(x_api_key: Optional[str] = Header(default=None)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=401,
            detail="401 error Invalid, Missing api key."
        )
    return True

# HOME (Public)
@app.get("/")
def home():
    return {
        "message": "Welcome to the World Heritage Sites API!",
        "count": len(landmarks),
        "endpoints": [
            "/health",
            "/landmarks",
            "/landmarks/{id}",
            "/landmarks/search"
        ]
    }

# HEALTH CHECK (Public)
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "World Heritage Sites API",
        "version": "2.0.0",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

# GET ALL LANDMARKS (Protected)
@app.get("/landmarks", response_model=dict, dependencies=[Depends(verify_api_key)])
def get_landmarks():
    return {
        "count": len(landmarks),
        "landmarks": landmarks
    }

# SEARCH LANDMARKS (Protected)
@app.get("/landmarks/search", response_model=dict, dependencies=[Depends(verify_api_key)])
def search_landmarks(q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    
    for item in landmarks:
        searchable_text = (
            f"{item['title']} "
            f"{item['site_type']} "
            f"{item['country']} "
            f"{item['region']} "
            f"{item['governing_body']} "
            f"{item['established_year']} "
            f"{item['notable_architects']} "
            f"{item['protection_status']} "
            f"{item['description']}"
        ).lower()

        if q in searchable_text:
            results.append(item)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

# GET ONE LANDMARK (Protected)
@app.get("/landmarks/{landmark_id}", response_model=Landmark, dependencies=[Depends(verify_api_key)])
def get_landmark(landmark_id: int):
    for item in landmarks:
        if item["id"] == landmark_id:
            return item

    raise HTTPException(
        status_code=404,
        detail="Landmark not found."
    )