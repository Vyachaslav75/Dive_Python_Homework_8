import os
import json
import csv
import pickle


def main():
    check_path=os.getcwd()
    res=my_walk(check_path)
    write_json(res)
    write_csv(res)
    write_pickle(res)


def my_walk(my_path=os.getcwd()):
    #fl = os.path.walk(my_path)
    fs=os.walk(my_path)
    folder_info=[[], [], [], []]
    for f in fs:
        #print(f)
        files_size=0
        if len(f[1])>0:
            for i in f[1]:
                folder_info[0].append(f[0])
                folder_info[1].append(i)
                folder_info[2].append('folder')
                folder_info[3].append(0)
        if len(f[2])>0:
            for i in f[2]:
                temp=os.path.getsize(os.path.join(f[0], i))
                folder_info[0].append(f[0])
                folder_info[1].append(i)
                folder_info[2].append('file')
                folder_info[3].append(temp)
                files_size+=temp
        #if files_size>0:
            #print(files_size)
    for i in range(len(folder_info[0])):
        if folder_info[2][i]=='folder':
            folder_size=0
            fl_name=os.path.join(folder_info[0][i], folder_info[1][i])
            for j in range(len(folder_info[0])):
                if fl_name in folder_info[0][j]:
                    folder_size+=folder_info[3][j]
            folder_info[3][i]=folder_size
    # for i in range(len(folder_info[0])):
    #     print(f'{folder_info[0][i]}, {folder_info[1][i]}, {folder_info[2][i]}, {folder_info[3][i]}')
    return folder_info

def write_json(write_data):
    with open('res_json.json', 'w', encoding='utf-8') as f:
        json.dump(write_data, f, ensure_ascii=False)

def write_csv(write_data):
    with open('res_csv.csv', 'w', newline='', encoding='utf-8') as f:
        csv_writer=csv.writer(f, dialect='excel')
        csv_writer.writerows(write_data)


def write_pickle(write_data):
    with open('res_pickle.pickle', 'wb') as f:
            pickle.dump(write_data, f)

if __name__ == "__main__":
    main()