# -*- coding: utf-8 -*-
"""visualize1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15AO84STuqN3BczlbNPEEdrhHY_oFUu3r
"""

import matplotlib.pyplot as plt

# Sample test scores data
tests = ['Test 1', 'Test 2', 'Test 3', 'Test 4']
scores = [85, 92, 78, 88]

# Create a bar plot
plt.bar(tests, scores, color='skyblue')
plt.xlabel('Cycle Tests')
plt.ylabel('Scores (out of 100)')
plt.title('Cycle Test Scores')

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(scores, labels=tests, autopct='%1.1f%%', startangle=140)
plt.title('Cycle Test Scores Distribution')

# Create a histogram
plt.hist(scores, bins=10, edgecolor='black', color='skyblue')
plt.xlabel('Test Scores (out of 100)')
plt.ylabel('Frequency')
plt.title('Distribution of Test Scores')

# Create a line plot
plt.plot(tests, scores, marker='o', linestyle='-')
plt.title('Cycle Test Marks')
plt.xlabel('Cycle Test Number')
plt.ylabel('Marks')
plt.grid(True)

# Show the plot
plt.show()

