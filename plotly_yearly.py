import pandas as pd
import plotly.express as px
import textwrap

# Load the CSV file, skipping the first row and assuming no header
csv_file = 'Partnerzy_yearly.csv'
df = pd.read_csv(csv_file, header=None, skiprows=1)

# Rename columns for clarity
df.columns = ['year', 'name']

# Ensure 'year' column is treated as integer
df['year'] = df['year'].astype(int)

# Ensure 2023 is included in the range
min_year = df['year'].min()
max_year = max(df['year'].max(), 2023)  # Guarantee 2023 is included
all_years = pd.DataFrame({'year': range(min_year, max_year + 1)})

# Group by year and count the frequency of names
yearly_counts = df.groupby('year').size().reset_index(name='frequency')

# Create a list of names for each year
yearly_names = df.groupby('year')['name'].apply(list).reset_index(name='names')

# Merge data, ensuring missing years get default values
yearly_data = all_years.merge(yearly_counts, on='year', how='left').fillna({'frequency': 0})
yearly_data = yearly_data.merge(yearly_names, on='year', how='left')

# ✅ Fix: Replace NaN values in 'names' column with an empty list correctly
yearly_data['names'] = yearly_data['names'].apply(lambda x: x if isinstance(x, list) else [])

# Wrap names for better hover display
yearly_data['wrapped_names'] = yearly_data['names'].apply(
    lambda names: '<br>'.join(textwrap.wrap(', '.join(names), width=50)) if names else 'No partners'
)

# Create an interactive histogram using Plotly
fig = px.bar(yearly_data, x='year', y='frequency', 
             title='Polonium Foundation Partners by Year',
             labels={'year': 'Year', 'frequency': 'Frequency'},
             hover_data={'wrapped_names': True})

# Center the title
fig.update_layout(title_x=0.5)

# Customize hover template to ensure wrapped names display correctly
fig.update_traces(
    hovertemplate='<b>Year:</b> %{x}<br><b>Frequency:</b> %{y}<br><b>Names:</b> %{customdata[0]}'
)

# Improve hover box styling and ensure it fits within the page
fig.update_layout(
    hoverlabel=dict(
        bgcolor="white",  # Background color of the hover box
        font_size=14,      # Larger font for readability
        font_family="Arial",
        namelength=-1,     # Prevents truncation of long names
    ),
    margin=dict(l=150, r=150, t=80, b=20)  # Adjusted margins to fit hover box
)

# Show the plot
fig.show()

# Save as interactive
fig.write_html("Partnerzy_yearly.html")

