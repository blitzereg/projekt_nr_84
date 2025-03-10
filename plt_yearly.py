import pandas as pd
import matplotlib.pyplot as plt
import mplcursors
import textwrap

# Load the CSV file, skipping the first row and assuming no header
csv_file = 'partnerzy_yearly.csv'
df = pd.read_csv(csv_file, header=None, skiprows=1)

# Rename columns for clarity
df.columns = ['year', 'name']

# Group by year and count the frequency of names
yearly_counts = df.groupby('year').size().reset_index(name='frequency')

# Create a list of names for each year
yearly_names = df.groupby('year')['name'].apply(list).reset_index(name='names')

# Merge the counts and names
yearly_data = pd.merge(yearly_counts, yearly_names, on='year')

# Create a bar plot (histogram) using matplotlib
fig, ax = plt.subplots()
bars = ax.bar(yearly_data['year'], yearly_data['frequency'], color='skyblue')

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Frequency')
ax.set_title('Polonium Foundation Partners by Year')

# Add interactivity using mplcursors
cursor = mplcursors.cursor(bars, hover=True)

# Define what to display when hovering over a bar
@cursor.connect("add")
def on_hover(sel):
    year = yearly_data['year'][sel.index]
    frequency = yearly_data['frequency'][sel.index]
    names = yearly_data['names'][sel.index]
    
    # Wrap names into multiple lines (e.g., 20 characters per line)
    wrapped_names = textwrap.fill(', '.join(names), width=20)
    
    # Set the annotation text with wrapped names
    sel.annotation.set_text(f"Year: {year}\nFrequency: {frequency}\nNames:\n{wrapped_names}")
    
    # Adjust annotation box properties
    sel.annotation.get_bbox_patch().set_boxstyle("round,pad=0.3")
    sel.annotation.get_bbox_patch().set_facecolor("white")
    sel.annotation.get_bbox_patch().set_edgecolor("black")
    sel.annotation.get_bbox_patch().set_alpha(0.9)
    
    # Ensure the annotation stays within the plot area
    #sel.annotation.set_animated(True)
    sel.annotation.set_clip_on(True)

# Show the plot
plt.tight_layout()  # Adjust layout to prevent text from being cut off
plt.show()
