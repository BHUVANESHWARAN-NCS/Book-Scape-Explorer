SELECT * FROM books_scape.bookscape;
# 1. Check Availability of eBooks vs Physical Books
SELECT isEbook, COUNT(*) AS book_count
 FROM bookscape
 GROUP BY isEbook;

# 2. Find the Publisher with the Most Books Published
SELECT book_publisher, COUNT(*) AS book_count
 FROM bookscape
 GROUP BY book_publisher
 ORDER BY book_count DESC LIMIT 1;
 
# 3. Identify the Publisher with the Highest Average Rating
SELECT book_publisher, AVG(averageRating) AS avg_rating
 FROM bookscape WHERE averageRating IS NOT NULL 
 GROUP BY book_publisher
 ORDER BY avg_rating DESC LIMIT 1;

# 4. Get the Top 5 Most Expensive Books by Retail Price
SELECT book_title, amount_retailPrice
 FROM bookscape WHERE amount_retailPrice IS NOT NULL
 ORDER BY amount_retailPrice DESC LIMIT 5;

# 5. Find Books Published After 2010 with at Least 500 Pages
SELECT book_title, pageCount, year
 FROM bookscape WHERE year > 2010 AND pageCount >= 500;

# 6. List Books with Discounts Greater than 20%
SELECT book_title, amount_listPrice, amount_retailPrice
 FROM bookscape WHERE amount_listPrice IS NOT NULL AND amount_retailPrice IS NOT NULL AND (amount_listPrice - amount_retailPrice) / amount_listPrice > 0.2;

# 7. Find the Average Page Count for eBooks vs Physical Books
SELECT isEbook, AVG(pageCount) AS avg_page_count
 FROM bookscape WHERE pageCount IS NOT NULL
 GROUP BY isEbook;

# 8. Find the Top 3 Authors with the Most Books
SELECT book_authors, COUNT(*) AS book_count
 FROM bookscape GROUP BY book_authors ORDER BY book_count DESC LIMIT 3;

# 9. List Publishers with More than 10 Books
SELECT book_publisher, COUNT(*) AS book_count
 FROM bookscape
 GROUP BY book_publisher HAVING book_count > 10;

# 10. Find the Average Page Count for Each Category
SELECT categories, AVG(pageCount) AS avg_page_count 
 FROM bookscape WHERE pageCount IS NOT NULL
 GROUP BY categories;

# 11. Retrieve Books with More than 3 Authors
SELECT book_title, book_authors
 FROM bookscape WHERE LENGTH(book_authors) - LENGTH(REPLACE(book_authors, ',', '')) + 1 > 3;

# 12. Books with Ratings Count Greater Than the Average
SELECT book_title, ratingsCount
 FROM bookscape WHERE ratingsCount > (SELECT AVG(ratingsCount) 
 FROM bookscape WHERE ratingsCount IS NOT NULL);

# 13. Books with the Same Author Published in the Same Year
SELECT book_authors, year, COUNT(*)
 FROM bookscape
 GROUP BY book_authors, year HAVING COUNT(*) > 1;

# 14. Books with a Specific Keyword in the Title
SELECT book_title
 FROM bookscape WHERE book_title LIKE 'Programming and Problem Solving using Python';

# 15. Year with the Highest Average Book Price
SELECT year, AVG(amount_retailPrice) AS avg_price
 FROM bookscape WHERE amount_retailPrice IS NOT NULL
 GROUP BY year
 ORDER BY avg_price DESC LIMIT 1;

# 16. Count Authors Who Published 3 Consecutive Years
SELECT book_authors, COUNT(DISTINCT year) AS years_count
 FROM bookscape
 GROUP BY book_authors HAVING MAX(year) - MIN(year) >= 2;

# 17. Authors Who Published in the Same Year but Different Publishers
SELECT book_authors, year, COUNT(DISTINCT book_publisher)
 FROM bookscape
 GROUP BY book_authors, year HAVING COUNT(DISTINCT book_publisher) > 1;

# 18. Average Retail Price of eBooks vs Physical Books
SELECT isEbook, AVG(amount_retailPrice) AS avg_price
 FROM bookscape WHERE amount_retailPrice IS NOT NULL
 GROUP BY isEbook;

# 19. Identify Outlier Books Based on Average Rating
SELECT book_title, averageRating, ratingsCount
 FROM bookscape WHERE averageRating > (SELECT AVG(averageRating) + 2 * STDDEV(averageRating) 
 FROM bookscape WHERE averageRating IS NOT NULL) OR averageRating < (SELECT AVG(averageRating) - 2 * STDDEV(averageRating) FROM bookscape WHERE averageRating IS NOT NULL);

# 20. Publisher with Highest Average Rating (More than 10 Books)
SELECT book_publisher, AVG(averageRating) AS avg_rating, COUNT(*) AS book_count
 FROM bookscape WHERE averageRating IS NOT NULL
 GROUP BY book_publisher HAVING book_count > 10
 ORDER BY avg_rating DESC LIMIT 1;
