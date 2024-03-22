import matplotlib.pyplot as plt

def waterfall_chart(categories, values, title):
    changes = [values[0]] # Initialize changes with the first value
    
    # Calculate the changes
    for i in range(1, len(values)):
        changes.append(values[i] - values[i-1])
    
    # Create the waterfall chart
    plt.figure(figsize=(10, 6))
    plt.bar(categories, values, color='b', alpha=0.5, align='center')
    plt.bar(categories, changes, color='r', alpha=0.5, align='center')
    
    # Add title and labels
    plt.title(title)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    
    # Show the chart
    plt.grid(True)
    plt.show()

# Example data
categories = ['Start', 'Step 1', 'Step 2', 'Step 3', 'End']
values = [100, 120, 90, 150, 140]
title = 'Waterfall Chart Example'

# Generate the waterfall chart
waterfall_chart(categories, values, title)
