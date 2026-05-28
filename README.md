This script analyzes voter registration data to identify individuals matching a list of Central African names (first and last), then calculates the total number of voters and the number/proportion of Central African voters within each city council district (based on precinct-to-district mapping).

Key features:

Loads three data sources: voter roll, a CSV of Central African names (with First Name and Last Name columns), and a precinct-to-district lookup table.

Cleans precinct numbers (removes trailing .1).

Matches voters using flexible logic (first name compared against both first and last name lists, and similarly for last name).

Merges precinct-level data with city council districts.

Outputs a CSV containing, for each district: total voters, number of Central African voters, and percentage.

Handles missing districts gracefully (fills percentage with 0).

Use case:
Designed for political campaigns, community organizations, or researchers studying the geographic distribution of a specific ethnic or cultural group (Central African diaspora) across city council districts. The approach can be easily adapted to any name‑based demographic analysis.

Requirements:

Python 3.6+

pandas

Input files (adjust paths as needed):

Copy of Malik_RR.csv – voter file with columns Precinct, Name First, Name Last, Voter ID

Names list WArabchristians.csv – Central African names (must contain First Name and Last Name)

precincts_city_council_districts.csv – mapping precincts to City_Council_District
