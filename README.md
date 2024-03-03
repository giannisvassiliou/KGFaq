# ULYSSES: FreqUentLY ASked QueStions for KnowlEdge GraphS

The exponential growth of knowledge graphs necessitates effective and efficient methods for their exploration and understanding.
Frequently Asked Questions (FAQ) is a list of questions and answers
related to a specific topic intended to help people understand a particular subject. In this paper, we present ULYSSES, the first system
for automatically constructing a FAQ for large Knowledge Graphs. Our
method consists of three key steps. First, we select the most frequent
questions by exploiting available query logs. In the sequel, we answer the
selected queries using the original graph and finally, we construct textual
descriptions of both the queries and the corresponding answers exploring state-of-the-art transformer models, i.e., ChatGTP and Gemini. We
evaluate the results of each model using a human-constructed FAQ, contributing a unique dataset to the domain and showing the benefits of our
approach
 <p align="center">

</p>
<p align="center">
  <img src="https://github.com/giannisvassiliou/KGFaq/blob/main/ulisses.png"/>
</p>

## ULYSSES Parser

<br> You can use the script in this folder, to query the SPARQL ENDPOINT, with the queries from the log provided in the data folder.
<br><b> An Excel file will be created with various statistics and the most frequent queries. A folder "response_json" will be also created, containing the results of the most frequent queries.
<br>to be given as input to the LLM query scrript
<br>
<b>


<br> <br>
## ULYSSES LLM Query

You can use the python script in this folder, to send to chatGPT the frequent queries, along with their output (fromt the endpoint) as collected from the previous (parser) script, to create the 
plain English question/answer.
<UL>

<Li> main.py : reads the sparql queries in Results.xlsx and its responds in response_folder (contains json style replies of the queries from endpoint)
           and via the OPENAI API, translates the queries/responses to plain English questions/answers</Li>
<li>input_resutls.json: The ENDPOINT's response to the queries (created by parser)</Li>
<li>Results.xlsx: The actual sparql queries (most frequent used), created by parser<li>
</UL>


<br>

