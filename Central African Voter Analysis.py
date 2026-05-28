
import pandas as pd

# Load your datasets
voters_df = pd.read_csv('Vlist.csv', encoding='utf-8-sig')
voters_df.columns = voters_df.columns.str.strip()

# CSV containing Central African names (expected columns: 'First Name', 'Last Name')
central_african_names_df = pd.read_csv('Names list WArabchristians.csv', encoding='cp1252')

# New dataset with precincts and city council districts
districts_df = pd.read_csv('precincts_city_council_districts.csv')

# Remove .1 from precinct numbers in voters_df
voters_df['Precinct'] = voters_df['Precinct'].astype(str).str.replace(r'\.1$', '', regex=True)

# Extract first and last names into separate lists
first_names = central_african_names_df['First Name'].tolist()
last_names = central_african_names_df['Last Name'].tolist()

def is_central_african_voter(row):
    """
    Determine if a voter matches any Central African name.
    Checks first name against both first and last name lists,
    and last name against both lists.
    """
    first = str(row.get('Name First', '')).strip()
    last = str(row.get('Name Last', '')).strip()
    return (
        (first in first_names) or
        (first in last_names) or
        (last in first_names) or
        (last in last_names)
    )

# Apply the function to filter Central African voters
central_african_voters = voters_df[voters_df.apply(is_central_african_voter, axis=1)]

# Ensure 'Precinct' column in districts_df is a string
districts_df['Precinct'] = districts_df['Precinct'].astype(str)

# Merge voters data with districts data on precincts
voters_with_districts = pd.merge(voters_df, districts_df, on='Precinct', how='left')
central_african_voters_with_districts = pd.merge(central_african_voters, districts_df, on='Precinct', how='left')

# Calculate total voters and Central African voters by city council district
total_voters_by_district = voters_with_districts.groupby('City_Council_District')['Voter ID'].count()
central_african_voters_by_district = central_african_voters_with_districts.groupby('City_Council_District')['Voter ID'].count()

# Calculate percentages by city council district
percentage_by_district = (central_african_voters_by_district / total_voters_by_district) * 100

# Create a DataFrame with the results
results_df = pd.DataFrame({
    'City_Council_District': percentage_by_district.index,
    'Total_Voters': total_voters_by_district.values,
    'Central_African_Voters': central_african_voters_by_district.values,
    'Percentage_Central_African_Voters': percentage_by_district.values
})

# Fill NaN with 0 and round to 2 decimal places
results_df['Percentage_Central_African_Voters'] = results_df['Percentage_Central_African_Voters'].fillna(0).round(2)

# Sort the DataFrame by City Council District
results_df = results_df.sort_values('City_Council_District')

# Export the results to a CSV file
results_df.to_csv('central_african_voters_by_district.csv', index=False)

# Display results
print("Results exported to 'central_african_voters_by_district.csv'")
print("\nPercentage of Central African voters by City Council District:")
print(results_df[['City_Council_District', 'Percentage_Central_African_Voters']])
