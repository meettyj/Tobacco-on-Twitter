import os
import json
import pandas as pd
import csv

def get_bot_accounts_list():
    file_path = "/mnt/volume-second-5T/data/bot_accounts/"
    bot_accounts_list = []

    files= os.listdir(file_path)

    # iterate the files
    for file_name in files:
        file_name = file_path + file_name
        file_name_suffix = file_name.split('.')[0].split('_')[-1]
        print('file_name_suffix: ', file_name_suffix)

        if (file_name_suffix == "1") or (file_name_suffix[0] == "3") or (file_name_suffix[0] == "5"):
            with open(file_name, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                temp_id_list = [row['id'] for row in reader if row['id']!= '']
    #             print(temp_id_list)
                bot_accounts_list.extend(temp_id_list)
                print('processed successfully, length =', len(temp_id_list))

        elif (file_name_suffix == "2") or (file_name_suffix == "61"):
            with open(file_name, 'r') as text_file:
                lines = text_file.readlines()
                for line in lines:
                    line=line.strip('\n')
                    tmp_id = line.split('\t')[0]
    #                 print(tmp_id)
                    bot_accounts_list.append(tmp_id)
                print('processed successfully, length =', len(lines))

        elif file_name_suffix == "71":
            with open(file_name, 'r') as text_file:
                lines = text_file.readlines()
                for line in lines:
                    line=line.strip('\n')
                    tmp_id = line.split(' ')[0]
    #                 print(tmp_id)
                    bot_accounts_list.append(tmp_id)
                print('processed successfully, length =', len(lines))
    
    print()
    bot_accounts_list = list(set(bot_accounts_list)) # remove duplication
    print('length of bot_accounts_list: ', len(bot_accounts_list))
    return bot_accounts_list
