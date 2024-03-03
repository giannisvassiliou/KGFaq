# pip install openai==0.28
# This script is used to sort the data Openai API produced.

import openai 
import json

# Set your OpenAI API key
openai.api_key = 'use your OWN '


def categorize_objects(data):
        
        # Call OpenAI API to categorize based on the question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  
             messages=[{"role": "user", "content": f"sort these by category {data} "}],
            max_tokens=3900  # Adjust based on your requirements
        )
        
        #write the output to a txt file
        with open('sorted_output.txt', 'w') as outfile:
            json.dump(response['choices'][0]['message']['content'], outfile, indent=4 )
        
            
            
    
if __name__ == "__main__":    
    with open("C:/Users/Eleutheria/Desktop/SEMANTIC/deleteme.json", 'r', encoding="utf-8" ) as file:
        data = json.load(file)
    categorize_objects(data)
