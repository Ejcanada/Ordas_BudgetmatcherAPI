Heritage Travels Budget Matcher

Heritage Travels Budget Matcher is a web application that allows users to discover historical landmarks and gentle escapes matched to their travel budget and trip duration.

The website gets its destination information from a custom FastAPI REST API instead of storing the landmark data directly inside the frontend.

How the Website Uses the API

The website connects to the Heritage Travels API to retrieve the available worldwide landmark data.

The API provides information such as:

* Landmark title
* Site type
* Country and City
* Description
* Established year
* Governing body
* Protection status
* Annual visitors
* Entry fee and local currency
* Estimated daily hotel rate

The frontend sends a secure, authenticated request to the API and receives the landmark data in JSON format to calculate matches based on the user's budget.

Example request:

GET /landmarks
x-api-key: my_secret_landmark_key
