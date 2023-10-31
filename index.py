import requests 
import csv




def insert_new(name, description,category,effect,visual_description, card_class):
    body={}
    body["name"] = name
    body["description"] = description
    body["category"] = category
    body["effect"] = effect
    body["visual_description"] = visual_description
    body["card_class"] = card_class
    
    print("Body here", body)
    url = "http://127.0.0.1:8080/new"
    response = requests.post(url, json=body)
    print(f"Response for {url}: {response.status_code}")
    
    
def insert_by_table(): 

    csv_file_path = "cards.csv"
    # Open the CSV file
    with open(csv_file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:  
            # print(row)
            #name 
            name = row['NAME']
            #description
            description = row['DESCRIPTION']
            #category
            category = row['CATEGORY']
            #effect
            effect = row['EFFECT']
            #visual_description
            visual_description = row['VISUAL_DESCRIPTION']
            
            card_class = row['CLASS']
            print("\n \n ")
            insert_new(name, description, category, effect, visual_description,card_class)
            
            
            
insert_by_table()