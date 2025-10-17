import pandas as pd
import requests, keys
from IPython.display import display
from mistralai import Mistral


def main():

    user_input = ''
    files = []
    url = "https://api.mistral.ai/v1/chat/completions"
    query_string = 'I have several datasets for you to perform an exploratory data analysis on. List potential columns to join on but do not elaborate. Provide useful insights that could be gained from these datasets. Keep each insight to 1-3 sentences. \'nan\' represents a lack of data. The files are as described below.'


    print("Enter line by line the files you wish to analyze. Enter 'done' when done.")
    while user_input != "done":
        user_input = input("")

        if user_input != "done":
            files.append(user_input)

    # Generate metadata from each file
    for file in files:

        file_df = pd.read_csv(f'./{file}.csv')
        mode_df = file_df.mode()

        columns_list = list(mode_df.columns)
        values_list = [] # a list containing lists of each top value for each column

        for col in columns_list:
            val_list = list(mode_df[f'{col}'].transpose()) # mode may return >1 rows, so transpose is necessary
            values_list.append(val_list) 

        # Create query string
        query_string += '\nA file with the following columns:'
        for vals_list, columns in zip(values_list, columns_list):
            query_string += f"\n'{columns}', which has values such as "
            for vals in vals_list:
                query_string += f"'{vals}', "
            query_string += ""

    # Query Mistral API
    client = Mistral(keys.mistral_key)
    chat_response = client.chat.complete(
        model= "mistral-small",
        messages = [
            {
                "role": "user",
                "content": f"{query_string}",
            },
        ]
    )
    print(chat_response.choices[0].message.content)

if __name__ == "__main__":
    main()