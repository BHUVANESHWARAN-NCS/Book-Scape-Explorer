# Book-Scape-Explorer
1. Book_Scape (Project-2) - Jupyter Notebook
•	Tool Used: Jupyter Notebook
•	Purpose:
o	Used for data extraction and cleaning.
o	The API link provided by the management was used to scrape book data in JSON format.
o	After extraction, the data was converted into a CSV file for further processing.
•	Key Steps in Jupyter Notebook:
1.	API request to fetch book data in JSON format.
2.	Parsing and structuring the JSON data.
3.	Data cleaning (handling missing values, duplicates, and formatting).
4.	Saving the cleaned data as book_scrape.csv.
________________________________________
2. book_scape (CSV File)
•	Tool Used: CSV File (Processed Data)
•	Purpose:
o	This is the cleaned dataset that was exported from Jupyter Notebook.
o	Used to store book details such as title, author, publisher, price, rating, pages, and availability.
•	Next Step:
o	Imported this dataset into MySQL Workbench for structured querying.
________________________________________
3. BOOK_SCAPE SQL Code - MySQL Workbench
•	Tool Used: MySQL Workbench
•	Purpose:
o	The book_scrape.csv data was imported into MySQL database (Books_Scape).
o	SQL queries were written to analyze the data based on management requirements.
•	Key Queries in SQL:
1.	Find the availability of eBooks vs Physical Books
2.	Retrieve the most expensive books
3.	Get the top publishers and authors
4.	Calculate the average rating and price trends
5.	Identify books with high discounts and outliers
•	Why MySQL?
o	Provides structured storage for large book data.
o	Enables efficient queries for analytics.
________________________________________
4. BOOK_SCAPE.py - Streamlit API Reference
•	Tool Used: VS Code & Streamlit
•	Purpose:
o	Developed an interactive API reference for clients using Streamlit.
o	Connected Streamlit with MySQL to display query results dynamically.
o	Used UI elements (radio buttons, charts, and tables) to enhance the user experience.
•	How It Works:
1.	User selects a query from the Streamlit sidebar (radio button).
2.	A SQL query is triggered to fetch relevant data.
3.	Data is displayed in a table (st.dataframe()) or chart (st.bar_chart(), st.pyplot()).
4.	Expandable sections (st.expander()) make the UI clean and interactive.
•	Key Features:
o	Bar charts for publisher ratings & book availability.
o	Line charts for average book price over time.
o	SQL-powered search for book details.
________________________________________
Final Summary (How Everything Connects)
1.	Extract Data: API scraping in Jupyter Notebook → Save as CSV.
2.	Store & Query: Import CSV into MySQL Workbench → Write SQL Queries.
3.	Develop UI: Use VS Code & Streamlit to build an interactive API reference.
4.	Present to Client: Final Streamlit app makes data exploration simple & visual.
