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
<br>
<br>
The script <b>parse_tsv_file.py </b> will USE THE SPARQL QUERY LOG (FROM DATA FOLDER) to query the Endpoint, and collect the answers/results
<br>
<br>
 Will create:
<br>
<br>
 <ul>
<li> A Folder containing json files with the responses returned from querying DBpedia Endpoint with the most 
 frequent queries (response_folder) </li>
<li> An Excel file created by the script containing the saved DataFrames and the counts from the execution of the 
queries in the DBpedia endpoint(db.xlsx) - (contains the most frequent queries , which will be used for FAQ creation)</li>

  </ul>
<br><b> BOTH to be given as input to the LLM query script
<br>
</b>


<br> <br>
## ULYSSES LLM Query
</b>
You can use the python script in this folder, to send to ChatGPT the most frequent queries, along with their output (fromt the Endpoint) as collected from the previous (parser) script, to create the 
plain English question/answer pairs.
</b>
<br>
<br>
<UL>

<Li> <b> main.py </b>: reads the SPARQL queries in Results.xlsx and their responses in response_folder (contains json style replies of the SPARQL queries from Endpoint-done by Parser)
           and via the OPENAI API, translates the queries/responses to plain English questions/answers pairs </Li>
           <br>
           
   INPUTS:
   <UL>
<li>Response_folder: The folder containing the ENDPOINT's response to the queries in json format, created by parser</Li>
<li>Results.xlsx: The actual SPARQL queries (most frequent used), created by parser</li>

   </UL>
   </UL>


<br>
<br>
<UL>
 <li>
 You have to use <b> YOUR OWN </b> OpenAI secret key, in the appropriate spots in the code  .</li>
<li> Same code with minor changes, was used for leveraging Google's GEMINI in the procedure .</li>
</UL>
