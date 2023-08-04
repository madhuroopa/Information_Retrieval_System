# Information_Retrieval_System 

## Problem Statement

The central aim of this project is to engineer a sophisticated yet user-friendly search application that capitalizes on the TF-IDF (Term Frequency-Inverse Document Frequency) algorithm's potential. This algorithm serves as the bedrock for measuring the relevance of documents in response to user-entered search queries.

## Pipeline Architecture
<img width="812" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/e829bfb5-d1b3-4d12-a456-a1ec434fb981">

<img width="812" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/3b1cb2bc-b281-47bd-8dff-7e604da65948">

## Tools

- AWS Services: Leveraged Amazon S3 for data storage, AWS EMR for distributed data processing, and DynamoDB for efficient data retrieval.
- Apache Spark: Utilized Spark RDDs to perform TF-IDF calculations, resulting in a significant reduction in processing time.
- TF-IDF (Term Frequency-Inverse Document Frequency): Calculated and analyzed TF-IDF scores to quantify the relevance of documents to search queries.
- S3- For intermediate storage of tf-idf calculations and title of the documents.
- DynamoDB Tables: Created two DynamoDB tables, 'tfidf' and 'doctitle,' to store processed data efficiently, with careful consideration of partition and sort keys.
- AWS Lambda: Orchestrated the system's functionality into an AWS Lambda function, ensuring seamless execution and scalability.
- HTML and CSS: Developed an HTML-based user interface, 'search.html,' which communicates with the Lambda function to display search results.


### Data Collection and Preprocessing:

- Curate a diverse collection of text files from different authors along with a file containing their titles.
- Perform initial data cleaning and transformation to ensure uniformity and consistency.
-  TF-IDF Calculation with Spark:
   - TF- IDF calculation steps :
   - 
<img width="635" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/30e096f4-4e78-49db-a0d2-e4142f17c9c0">

- Leverage the distributed computing capabilities of Apache Spark running on AWS EMR (Elastic MapReduce) to calculate TF-IDF scores.
- Utilize Spark RDDs to efficiently process and analyze the text data, resulting in accurate TF-IDF values for each term-document pair.

### DynamoDB Table Design:

- Create two DynamoDB tables: 'tfidf' and 'doctitle,' with careful consideration of partition keys and sort keys.
- Efficiently store the processed TF-IDF data and document titles for seamless data retrieval.

### Relevance Ranking and Search:

- Develop Python code that implements the TF-IDF algorithm to assess the relevance of documents to a given search query.
- Formulate a scoring mechanism, the relevance is just the sum of the TF-IDF values for each term in the query, normalized for the length of the query terms.
  If Q is a set of terms, then relevance is defined as follows:

<img width="288" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/e4e0892e-bcf9-4fa5-b1ae-a13eb60771fc">

### Lambda Function Integration:

- Design and configure an AWS Lambda function that encapsulates the relevance ranking logic.
- Set up the Lambda function to accept user input (search queries) and return the search results.

### User-Friendly Interface:

- Create an interactive HTML-based user interface ('search.html') that allows users to enter search queries.
- Connect the HTML interface to the Lambda function for querying and result retrieval.


## Output screenshot

## Search Page


<img width="580" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/2b4d05ba-2200-494f-887a-89060600d35e">

### Search for a relevant documents

<img width="478" alt="image" src="https://github.com/madhuroopa/Information_Retrieval_System/assets/22576343/23ec47bb-5587-4712-9ed2-f702d2029b84">




