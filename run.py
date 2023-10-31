import os 
import csv
import time


def write_line_to_file(line, filename):
    with open(filename, "a") as file:
        file.write(line + "\n")


def line_exists_in_file(line, filename):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            print("Lines:", lines)  # Debugging: Print the lines to see what's read from the file
            for existing_line in lines:
                if existing_line.strip() == line:
                    return True
        return False
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {str(e)}")
        return False



def run_bing_image_creator(file_path, prompt, output, id):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            run_on_site = f"python3 -m BingImageCreator -U {file_content} --prompt {prompt} --output-dir {output}"
            os.system(run_on_site)
    
    except FileNotFoundError:
        # print(f"The file {file_path} was not found.")
        return False
    except Exception as e:
        # print(f"An error occurred: {str(e)}")
        print(" \n \n \n TRavou aqui ")
        return False
    finally:
        # Code to be executed in the 'finally' block (regardless of exceptions)
        # You can add any cleanup or finalization code here
            # time.sleep(60)
            if os.path.exists(output):
                write_line_to_file(id,"visited.txt")
                return True
            else: return False
    pass
    

# Example usage:


def insert_by_table(): 

    csv_file_path = "cards.csv"
    # Open the CSV file
    with open(csv_file_path, mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV file
        for row in csv_reader:  
            #visual_description
            visual_description = row['VISUAL_DESCRIPTION']
            id = row['id']
            output= f"image_[{id}]"
        
            # print("\n \n \n ", visual_description)   
            # print("output \n \n \n", output)  
            file_path = "cookie.txt"  # Replace with the actual file path
            prompt = f' " minimalist and without background image with this description: {visual_description}" '
            # print("prompt \n ",prompt)
            line_exists_in_file(id,"visited.txt")
            if(line_exists_in_file(id,"visited.txt") == False):
                print(f"id {id} not visited")
                run_bing_image_creator(file_path,prompt,output,id)
                time.sleep(120)
                # print(f"Imagem do id [{id}] criada com sucesso")
                # write_line_to_file(id,"visited.txt")
                # else: print(f"Id {id} já criado")

    
insert_by_table()