# pip install openai==0.28
# Tis script is used to categorise each sparql Query based on its topic.
import openai 
import json
import time

# Set your OpenAI API key
openai.api_key = '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'

def categorize_objects(data, output_file):
    categorized_data = []
    for key, obj in data.items():
        print("loop")
        query = obj["translated_query"] 
        answer = obj["generated_response"]
        
        # Call OpenAI API to categorize based on the question
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-1106",  
            messages=[{"role": "user", "content": f"Write this question {query} and write this answer {answer} and assign to them a general category(eg. history , mathematics, geography etc) about the topic they refer to(dont write sparql queries or data retrieval). The format should be question:example\n answer:example\n Category: example\n"}],
            max_tokens=1000  # Adjust based on your requirements
        )
        # Save the categorized data to output file (JSON)
        categorised_answer = response['choices'][0]['message']['content']
        lines = [line for line in categorised_answer.split('\n') if line.strip()] # split lines and remove the empty ones.
    
    
        categorized_data.append(lines)
        
        #write the content of the response to the output file
        with open(output_file, 'w') as outfile:
            json.dump(categorized_data, outfile, indent=4 )
            
        
        time.sleep(60)
        
            
            
    
if __name__ == "__main__":    
    with open("C:/Users/Eleutheria/Desktop/SEMANTIC/input_results.json", 'r', encoding="utf-8" ) as file:
        data = json.load(file)
    output_file = 'output.json'
    # Example: Ask OpenAI to categorize based on a specific question

    categorize_objects(data, output_file)