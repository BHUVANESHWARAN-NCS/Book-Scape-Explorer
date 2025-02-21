import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Book Scape Explorer")
st.subheader("Book Scape Explorer Analysis.")
st.sidebar.write("Select the questions on given box.")
query= st.sidebar.radio(
    "SELECT_QUERY:",
    [
        "1.Check Availability of eBooks vs Physical Books",
        "2.Find the Publisher with the Most Books Published",
        "3.Identify the Publisher with the Highest Average Rating",
        "4.Get the Top 5 Most Expensive Books by Retail Price",
        "5.Find Books Published After 2010 with at Least 500 Pages",
        "6.List Books with Discounts Greater than 20%",
        "7.Find the Average Page Count for eBooks vs Physical Books",
        "8.Find the Top 3 Authors with the Most Books",
        "9.List Publishers with More than 10 Books",
        "10.Find the Average Page Count for Each Category",
        "11.Retrieve Books with More than 3 Authors",
        "12.Books with Ratings Count Greater Than the Average",
        "13.Books with the Same Author Published in the Same Year",
        "14.Books with a Specific Keyword in the Title",
        "15.Year with the Highest Average Book Price",
        "16.Count Authors Who Published 3 Consecutive Years",
        "17.Authors Who Published in the Same Year but Different Publishers.",
        "18.Average Retail Price of eBooks vs Physical Books.",
        "19.Identify Outlier Books Based on Average Rating.",
        "20.Publisher with Highest Average Rating (More than 10 Books)."
    ]
 
 )
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="nbhuvanesh385",
        database="Books_Scape"
    )
def run_query(query):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return pd.DataFrame(result)

if query == "1.Check Availability of eBooks vs Physical Books":
    with st.expander("Check Availability of eBooks vs Physical Books"):
        st.write("The Availability of eBooks vs Physical Books.")
    sql ="""
    SELECT isEbook, COUNT(*) AS book_count
    FROM bookscape
    GROUP BY isEbook;
    """
    df = run_query(sql)
    st.write(df)
    fig, ax = plt.subplots()
    ax.bar(df['isEbook'].astype(str), df['book_count'], color=['blue', 'orange'])
    ax.set_xlabel("Type of Book (0 = Physical, 1 = eBook)")
    ax.set_ylabel("Count")
    ax.set_title("Availability of eBooks vs Physical Books")
    st.pyplot(fig)
elif query == "2.Find the Publisher with the Most Books Published":
    with st.expander("Find the Publisher with the Most Books Published"):
        st.write("Finding the publisher with the most books published.")
    sql="""
    SELECT book_publisher, COUNT(*) AS book_count
    FROM bookscape
    GROUP BY book_publisher
    ORDER BY book_count DESC LIMIT 1;
   """
    df = run_query(sql)
    st.write(df)
elif query == "3.Identify the Publisher with the Highest Average Rating":
    with st.expander("Identify the Publisher with the Highest Average Rating"):
        st.write("Identifying the publisher with the highest average rating.")
    sql = """
    SELECT book_publisher, AVG(averageRating) AS avg_rating 
    FROM bookscape WHERE averageRating IS NOT NULL 
    GROUP BY book_publisher
    ORDER BY avg_rating DESC LIMIT 1;
    """
    df = run_query(sql)
    st.write(df)
    st.bar_chart(df.set_index("book_publisher"))
elif query == "4.Get the Top 5 Most Expensive Books by Retail Price":
    with st.expander("Get the Top 5 Most Expensive Books by Retail Price"):
        st.write("Retrieving the top 5 most expensive books by retail price.")
    sql = """
    SELECT book_title, amount_retailPrice
    FROM bookscape WHERE amount_retailPrice IS NOT NULL
    ORDER BY amount_retailPrice DESC LIMIT 5;
    """
    df = run_query(sql)
    st.write(df)
elif query == "5.Find Books Published After 2010 with at Least 500 Pages":
    with st.expander("Find Books Published After 2010 with at Least 500 Pages"):
        st.write("Finding books published after 2010 with at least 500 pages.")
    sql = """
    SELECT book_title, pageCount, year
    FROM bookscape WHERE year > 2010 AND pageCount >= 500;
    """
    df = run_query(sql)
    st.write(df)
elif query == "6.List Books with Discounts Greater than 20%":
    with st.expander("List Books with Discounts Greater than 20%"):
        st.write("Listing books with discounts greater than 20%.")             
    sql = """ 
    SELECT book_title, amount_listPrice, amount_retailPrice
    FROM bookscape WHERE amount_listPrice IS NOT NULL AND amount_retailPrice IS NOT NULL AND (amount_listPrice - amount_retailPrice) / amount_listPrice > 0.2;
    """
    df = run_query(sql)
    st.write(df)
elif query == "7.Find the Average Page Count for eBooks vs Physical Books":
    with st.expander("Find the Average Page Count for eBooks vs Physical Books"):
        st.write("Finding the average page count for eBooks vs Physical Books.")
    sql = """
    SELECT isEbook, AVG(pageCount) AS avg_page_count
    FROM bookscape WHERE pageCount IS NOT NULL
    GROUP BY isEbook;
    """
    df = run_query(sql)
    st.write(df)
elif query == "8.Find the Top 3 Authors with the Most Books":
    with st.expander("Find the Top 3 Authors with the Most Books"):
        st.write("Finding the top 3 authors with the most books.")
    sql = """
    SELECT book_authors, COUNT(*) AS book_count
    FROM bookscape GROUP BY book_authors ORDER BY book_count DESC LIMIT 3;
    """
    df = run_query(sql)
    st.write(df)
elif query=="9.List Publishers with More than 10 Books":
    with st.expander("List Publishers with More than 10 Books"):
        st.write("Listing publishers with more than 10 books.")
    sql ="""
    SELECT book_publisher, COUNT(*) AS book_count
    FROM bookscape
    GROUP BY book_publisher HAVING book_count > 10;
    """
    df = run_query(sql)
    st.write(df)
elif query =="10.Find the Average Page Count for Each Category":
    with st.expander("Find the Average Page Count for Each Category"):
        st.write("Finding the average page count for each category.")
    sql = """
    SELECT categories, AVG(pageCount) AS avg_page_count 
    FROM bookscape WHERE pageCount IS NOT NULL
    GROUP BY categories;
    """
    df = run_query(sql)
    st.write(df)
elif query =="11.Retrieve Books with More than 3 Authors":
    with st.expander("Retrieve Books with More than 3 Authors"):
        st.write("Retrieving books with more than 3 authors.")
    sql = """
    SELECT book_title, book_authors
    FROM bookscape WHERE LENGTH(book_authors) - LENGTH(REPLACE(book_authors, ',', '')) + 1 > 3;
    """
    df = run_query(sql)
    st.write(df)
elif query=="12.Books with Ratings Count Greater Than the Average":
    with st.expander("Books with Ratings Count Greater Than the Average"):
        st.write("Finding books with ratings count greater than the average.")
    sql ="""
    SELECT book_title, ratingsCount
    FROM bookscape WHERE ratingsCount > (SELECT AVG(ratingsCount) 
    FROM bookscape WHERE ratingsCount IS NOT NULL);
    """
    df = run_query(sql)
    st.write(df)
elif query== "13.Books with the Same Author Published in the Same Year":
    with st.expander("Books with the Same Author Published in the Same Year"):
         st.write("Finding books with the same author published in the same year.")
    sql = """
    SELECT book_authors, year, COUNT(*)
    FROM bookscape
    GROUP BY book_authors, year HAVING COUNT(*) > 1;
    """
    df = run_query(sql)
    st.write(df)
elif query =="14.Books with a Specific Keyword in the Title":
    with st.expander("Books with a Specific Keyword in the Title"):
        st.write("Finding books with a specific keyword in the title.")
    sql = """
    SELECT book_title
    FROM bookscape WHERE book_title LIKE 'Programming and Problem Solving using Python';
    """
    df = run_query(sql)
    st.write(df)
elif query == "15.Year with the Highest Average Book Price":
    with st.expander("Year with the Highest Average Book Price"):
        st.write("Finding the year with the highest average book price.")
    sql = """
    SELECT year, AVG(amount_retailPrice) AS avg_price
    FROM bookscape WHERE amount_retailPrice IS NOT NULL
    GROUP BY year
    ORDER BY avg_price DESC LIMIT 1;
    """
    df = run_query(sql)
    st.write(df)
    fig, ax = plt.subplots()
    sns.lineplot(data=df, x="year", y="avg_price", marker="o", ax=ax)
    ax.set_title("Average Book Price Per Year")
    ax.set_xlabel("Year")
    ax.set_ylabel("Avg Price")
    st.pyplot(fig)
elif query=="16.Count Authors Who Published 3 Consecutive Years":
    with st.expander("Count Authors Who Published 3 Consecutive Years"):
        st.write("Counting authors who published in 3 consecutive years.")
    sql = """
    SELECT book_authors, COUNT(DISTINCT year) AS years_count
    FROM bookscape
    GROUP BY book_authors HAVING MAX(year) - MIN(year) >= 2;
    """
    df = run_query(sql)
    st.write(df)
elif query =="17.Authors Who Published in the Same Year but Different Publishers.":
    with st.expander("Authors Who Published in the Same Year but Different Publishers."):
        st.write("Finding authors who published in the same year but with different publishers.")
    sql = """
    SELECT book_authors, year, COUNT(DISTINCT book_publisher)
    FROM bookscape
    GROUP BY book_authors, year HAVING COUNT(DISTINCT book_publisher) > 1;
    """
    df = run_query(sql)
    st.write(df)
elif query =="18.Average Retail Price of eBooks vs Physical Books.":
    with st.expander("Average Retail Price of eBooks vs Physical Books."):
        st.write("Finding the average retail price of eBooks vs Physical Books.")
    sql = """
    SELECT isEbook, AVG(amount_retailPrice) AS avg_price
    FROM bookscape WHERE amount_retailPrice IS NOT NULL
    GROUP BY isEbook;
    """
    df = run_query(sql)
    st.write(df)
elif query =="19.Identify Outlier Books Based on Average Rating.":
    with st.expander("Identify Outlier Books Based on Average Rating."):
        st.write("Identifying outlier books based on average rating.")
    sql="""
    SELECT book_title, averageRating, ratingsCount
    FROM bookscape WHERE averageRating > (SELECT AVG(averageRating) + 2 * STDDEV(averageRating) 
    FROM bookscape WHERE averageRating IS NOT NULL) OR averageRating < (SELECT AVG(averageRating) - 2 * STDDEV(averageRating) FROM bookscape WHERE averageRating IS NOT NULL);
    """
    df = run_query(sql)
    st.write(df)
elif query== "20.Publisher with Highest Average Rating (More than 10 Books).":
    with st.expander("Publisher with Highest Average Rating (More than 10 Books)."):
        st.write("Finding the publisher with the highest average rating (more than 10 books).")
    sql="""
    SELECT book_publisher, AVG(averageRating) AS avg_rating, COUNT(*) AS book_count
    FROM bookscape WHERE averageRating IS NOT NULL
    GROUP BY book_publisher HAVING book_count > 10
    ORDER BY avg_rating DESC LIMIT 1;
    """
    df = run_query(sql)
    st.write(df)