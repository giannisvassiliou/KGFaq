import pandas as pd
import requests
import re
import json
import os
# Define the number of queries to send to the endpoint
number_of_queries =30
DBPEDIA_ENDPOINT = "https://dbpedia.org/sparql"
response_folder_path = 'response_folder'
file_path = 'db.tsv'
#Create folder to save responses from DBpedia if it doesn't exist 
os.makedirs(response_folder_path, exist_ok=True)
#Initialize counters 
valid_query_count=error_count = no_data_count=0
# Initialize a list to store valid responses
valid_responses=[]
#Read db.tsv and produce a DataFrame
all_queries_df = pd.read_csv(file_path, sep='\0', encoding='unicode_escape', on_bad_lines='warn', header=None)
all_queries_df.rename(columns={0:'Query'}, inplace=True)
#Calculate the number of times that each query appears in the initial dataframe and create a new dataframe to hold dthe values
frequent_df = all_queries_df['Query'].value_counts().reset_index()
frequent_df['Query'] = frequent_df['Query'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii').replace('\x0b', '\n').replace('\x14', '\n'))
frequent_df.rename(columns={ 'count': 'Frequency'}, inplace=True)
frequent_df.index = range(1, len(frequent_df) + 1)

# Exclude queries with 'DESCRIBE','CONSTRUCT' or 'ASK' and the generic query "select distinct ?Concept from <http://dbpedia3\.8> where {[] a ?Concept}" 
excluded_keywords = ['DESCRIBE', 'CONSTRUCT','ASK','/psh']
exclude_pattern = r"select distinct \?Concept from <http://dbpedia3\.8> where \{\[\] a \?Concept\}"
# Create a new dataframe (frequent_df_clean) that  holds the list of the queries and their respective frequencies in the original file
frequent_df_clean = frequent_df[~frequent_df['Query'].str.contains('|'.join(excluded_keywords), flags=re.IGNORECASE)]
frequent_df_clean = frequent_df_clean[~frequent_df['Query'].str.contains(exclude_pattern, case=True, na=False)]
#Set the index of the dataframe to start at 1
frequent_df_clean.index = range(1, len(frequent_df_clean) + 1)
#Function to send the selected queries to the DBpedia endpoint and return the results in json format
def get_sparql_results(query):
    query=query.strip()
    headers = {"Accept": "application/sparql-results+json"}
    response = requests.get(DBPEDIA_ENDPOINT, params={"query": query,"format":"application/sparql-results+json","default-graph-uri": "http://dbpedia.org"}, headers=headers)
    if response.ok:
        return response.json()
    else:
        print(f"Error in query {index} execution: {response.status_code},{response.text}")  # Detailed error info
        return None
# Iterate over the top N queries in frequent_df_clean and process responses
for index, row in frequent_df_clean.head(number_of_queries).iterrows():
    query = row['Query']
    response_json = get_sparql_results(query)
    #Select responses that are not empty
    if  response_json:
        if response_json['results'] and 'bindings' in response_json['results'] and response_json['results']['bindings']:
            print(f'Response of query {index} not empty')
            valid_responses.append(query)
            valid_query_count+=1
            # Save each response to a separate JSON file in the response folder
            file_name =os.path.join(response_folder_path,f"query_response_{valid_query_count}.json")  # Index for filename starting from 1
            with open(file_name, 'w') as file:
                json.dump(response_json, file, indent=4)
                print(f"Saved response of query {index} to '{file_name}'\n")
        else:
            #Counter for responses that yield no data
             no_data_count+=1
             print(f'Response {index} has no data')    
    else:
        #Counter for responses that are not executed due to an error
        error_count+=1
        print(f'Response of query {index} has returned an error')
#Create dataframe with all the valid queries (Queries that return responses with results from the DBpedia endpoint)
final_querylist_df=pd.DataFrame(valid_responses,columns=['Query'])
# Merge to include frequency information
final_querylist_df = pd.merge(final_querylist_df, frequent_df_clean[['Query', 'Frequency']], on='Query', how='left')
final_querylist_df.index=range(1, len(final_querylist_df) + 1)

with pd.ExcelWriter('db.xlsx', engine='openpyxl') as writer:
     # Write the first DataFrame to the first sheet
    frequent_df.to_excel(writer, index=True, sheet_name='frequent queries')
    # Write the second DataFrame to the second sheet
    frequent_df_clean.to_excel(writer, index=True, sheet_name='frequent cleaned')
    #Write the Final DataFrame of queries with valid responses to a new sheet
    final_querylist_df.to_excel(writer, index=True, sheet_name='valid_responses')

                # Statistics
# Calculate the initial number of queries
initial_query_count = len(all_queries_df)
# Calculate the number of unique queries
unique_query_count = len(frequent_df)
# Calculate the number of cleaned unique queries
unique_clean_query_count = len(frequent_df_clean)
# Prepare counts for excluded queries
describe_count = construct_count = ask_count = pattern_count = psh_count= 0 
# Counting excluded queries
for query in frequent_df['Query'].unique():  # Iterate over unique queries

    if re.search(r'describe', query, re.IGNORECASE):
        describe_count += 1
    if re.search(r'construct', query, re.IGNORECASE):
        construct_count += 1
    if re.search(r'ask', query, re.IGNORECASE):
        ask_count += 1
    if re.search(r'/psh', query, re.IGNORECASE):
        psh_count += 1
    if re.search(exclude_pattern, query):
        pattern_count += 1

# Number of queries sent to the endpoint
queries_sent_count =number_of_queries
# Calculate percentages
valid_query_percentage = (valid_query_count / queries_sent_count) * 100 if queries_sent_count > 0 else 0
# Create a DataFrame for statistics
stats_df = pd.DataFrame({
    'Statistic': ['Initial Queries', 'Unique Queries','Unique cleaned queries','Total Queries Excluded', 'Excluded by Keywords','DESCRIBE', 'CONSTRUCT','ASK','/psh','Excluded by Pattern', 'Sent to Endpoint', 'Errors', 'Queries that returned no data', 'Valid Queries', 'Valid Query Percentage'],
    'Count': [initial_query_count, unique_query_count,unique_clean_query_count, describe_count + construct_count + ask_count + psh_count + pattern_count, describe_count + construct_count + ask_count + psh_count,describe_count,construct_count,ask_count,psh_count, pattern_count, queries_sent_count, error_count, no_data_count, valid_query_count, valid_query_percentage]
})
# Write the Statistics DataFrame to a new sheet in the Excel file
with pd.ExcelWriter('db.xlsx',engine='openpyxl', mode='a') as writer:
    stats_df.to_excel(writer, index=False, sheet_name='Statistics')