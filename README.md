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
<b>
<br> You can use the script in this folder, to query the SPARQL ENDPOINT, with the most frequent SPARQL queries from the log provided in the data folder.
</b>

The script parse_tsv_file.py  will USE THE SPARQL QUERY LOG (FROM DATA FOLDER) to query the Endpoint, and collect the answers/results
<br>
 Will create:

 <ul>
<li> A Folder containing json files with the responses returned from querying DBpedia endpoint with the script (response_folder) </li>
<li> An Excel file created by the script containing the saved DataFrames and the counts from the execution of the 
queries in the DBpedia endpoint(db.xlsx) - (contains the most frequent queries , which will be used for FAQ creation)</li>

  </ul>
<br><b> BOTHto be given as input to the LLM query scrript
<br>
</b>b>


<br> <br>
## ULYSSES LLM Query
</b>
You can use the python script in this folder, to send to ChatGPT the most frequent queries, along with their output (fromt the Endpoint) as collected from the previous (parser) script, to create the 
plain English question/answer pairs.
</b>
<br>
<br>
<UL>

<Li> main.py : reads the sparql queries in Results.xlsx and their responds in response_folder (contains json style replies of the SPARQL queries from Endpoint-done by Parser)
           and via the OPENAI API, translates the queries/responses to plain English questions/answers pairs </Li>
   INPUTS:
   <UL>
<li>input_results.json: The ENDPOINT's response to the queries  created by parser</Li>
<li>Results.xlsx: The actual SPARQL queries (most frequent used), created by parser</li>

   </UL>
   </UL>


<br>

