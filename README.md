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

<br> You can use the script in this folder, to query the SPARQL ENDPOINT, with the questions from the log
<br><b> An Excel file will be created with various statistics and the most frequent queries. A folder "response_json" will be also created, containing the results of the most frequent queries.
<br>
<br>
<b>
Where
</b>
<li>
queryfile : The name of the original query log (see data folder, choose e.g YAGO_orig_quer.txt) 
</li>
<li>
flag : 0 or 1  whether we need most frequent results 1 (yes) or  0 (no)
</li>
<li>
basefilename: a string to base the output file names {e.g yago}
</li>



<li>
limit: a SPARQL limit {e.g. 500}
</li>
<li>
urlendpoint: a valid url endpoint ( e.g.  https://yago-knowledge.org/sparql/query )
</li>
<br>
<b> We have stored in data folder results-examples for the 3 datasets we used (DBpedia, YAGO, Wikidata) </b>
<br> These files can be used directly from the LFS Evaluator

<br> <br>
## ULYSSES LLM Query

You need to provide two INPUT files (<b> orig_summary_filename</b> and <b> queries_for_summary</b> ) and one filename for OUTPUT (the actual <b> .nt LFS Summary </b>) ,  finally  the <b> address_of_endpoint </b>{OPTIONAL}
<br><b> <br>
USAGE:  lfs orig_summary_filename queries_for_summary LFS_summary_output {url of endpoint - optional} </b>
<br>
<br>
<b>
Where
</b>
<li>
 orig_summary_filename: The filename of the summary that parserIT produced
 </li>
 <li>
 queries_for_summary: The filename of the previous summary, corresponding queries
 
</li>
<li>
 LFS_summary_output: The final .nt file of the actual LFS summary
</li>

<li> address_of_endpoint: if given, the system will try to evaluate the queries cannot be answered by the LFS Summary, from the endpoint
</li>

<br>

<b>The previous script, will:</b>
<br>
<li> Create the train/test portions from the orig_summary_filename </li>
<li> Create the lfs .nt summary (from the train portion)</li>
<li> Query the .nt summary created with the test queries</li>
<li> Present the % of the first-sight queries replied, and the time consumed</li>

 ## Used Python v3.9 - Required Python libraries
<br>
<li>rdflib</li>
<li>pandas</li>
<li>SPARQLWrapper</li>
<li>numpy</li>
<li>sys</li>
<li>JSON</li>
