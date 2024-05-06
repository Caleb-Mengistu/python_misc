# Miscellaneous python project
This repository contains a collection of miscellaneous Python projects covering a range of topics and applications. Each project is designed to showcase different aspects of Python programming and can serve as examples or templates for similar projects.

**Project List:**

**FIFA 19 Player Data**
1. Loads FIFA 19 player data from a CSV file.
2. Cleans and preprocesses the data to extract relevant information.
3. Calculates the difference between player value and wage.
4. Visualizes player wage vs. value using scatter plots.

**Machine learning dataset**
1. Loading and exploring the Iris dataset.
2. Splitting the dataset into training and testing sets.
3. Training a K-Nearest Neighbors (KNN) classifier.
4. Evaluating the model's accuracy.
5. Saving and loading the trained model.
6. Making predictions with the loaded model.
7. Visualizing the dataset and model predictions using matplotlib.

**Password Checker**
1. Sends a hashed version of the password to the Have I Been Pwned API.
2. Retrieves a response containing hashes of leaked passwords that match the first 5 characters of the hashed password.
3. Checks if the full hashed password matches any of the leaked hashes to determine if the password has been compromised.
4. Prints a warning if the password has been found in data breaches.

**Email Sender**
1. Reads the HTML content from an index.html file.
2. Composes an email message with a customized subject, sender, recipient, and HTML content.
3. Sends the email using an SMTP server (e.g., Gmail)

**Hacker News Scraper**
This Python script scrapes news articles from Hacker News using the requests library to fetch web pages and BeautifulSoup for parsing HTML content.
1. Sends HTTP GET requests to Hacker News pages to fetch news articles.
2. Parses the HTML content of the pages using BeautifulSoup.
3. Extracts news article titles, links, and votes from the parsed HTML.
4. Filters articles based on vote count (excluding those with fewer than 100 votes).
5. Sorts the filtered articles based on votes in descending order.
6. Prints the sorted list of articles with titles, links, and votes.
