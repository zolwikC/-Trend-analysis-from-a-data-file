This program is a tool for generating charts based on user-input data and saving them in a selected format. It is written in Python using libraries such as tkinter for creating the graphical user interface, matplotlib for generating charts, and scikit-learn for performing linear regression.

Main Features of the Program:
User Interface (UI):

Loading Data: Users can load data from a text file using the "Load data from file" button. The data is then displayed in a table in the user interface.
Entering Data: The interface allows users to manually enter values and dates into up to 30 rows.
Chart Title: Users can enter a title for the chart, which will be displayed on the generated chart.
Save Format: Users can choose the save format for the chart from available options (PNG, PDF, SVG).
Generate and Save Chart: After entering the data and selecting the appropriate options, users can generate and save the chart using the "Generate chart and save data" button.
Functions:

Load Data from File: The load_data_from_file function opens a file dialog to select a file, loads the data from the selected file, and populates the corresponding fields in the table.
Save Chart: The save_chart function retrieves the data from the table, saves it to a text file, generates a chart from the entered data, adds a regression line and statistical analysis (mean, maximum, minimum, standard deviation), and saves the chart in the chosen format.
Data Analysis:

The program performs data analysis, calculating the mean, maximum, minimum value, and standard deviation.
Interactive labels are added to the chart, allowing users to view the value and date for each data point.
Linear Regression:

Linear regression is performed based on the entered data, and its result is displayed on the chart as a dashed line.
Used Libraries:
os: For file and path operations.
matplotlib.pyplot: For generating and displaying charts.
tkinter and ttk: For creating the graphical user interface.
datetime: For retrieving the current date and time.
numpy: For mathematical calculations.
sklearn.linear_model: For performing linear regression.
mplcursors: For adding interactive labels to the chart.
Summary:
The program is designed for users to input data, generate charts from that data, perform statistical analysis, and save charts in various formats. It functions as a graphical user interface application, allowing easy data entry and interaction with the resulting charts.
