import pandas as pd
import os


path = r'F:\Edin\1_2\Design with Data\Data'
file = path + "\\" + "new_inventory.csv"
output_dir = r'F:\Edin\1_2\Design with Data\Project\word_count\per_subject_combined\text'

def text_create(name, msg):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    full_path = output_dir + "\\" + name + '.txt'  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w', encoding='UTF-8')
    file.write(msg)  # msg也就是下面的Hello world!
    # file.close()

def classify():
    data = pd.read_csv(file)
    subject_list = data['subject'].tolist()
    key_list = data['key'].tolist()
    text_list = []
    for key in key_list:
        file_text = r"F:\Edin\1_2\Design with Data\Data\nls-text-broadsides\nls-text-broadsides" + "\\" + str(key) + ".txt"
        with open(file_text, "r", encoding='UTF-8') as f:  # 设置对象
            text = f.read()  # 读取文件内容
        text_list.append(text)


    different_subject_list = []
    different_subject_with_text_dict_list = []
    for k in range(len(subject_list)):
        if subject_list[k] not in different_subject_list:
            different_subject_list.append(subject_list[k])
            if subject_list[k] == "":
                different_subject_with_text_dict = {'Subject': "Unknown", 'Text': text_list[k]}
                different_subject_with_text_dict_list.append(different_subject_with_text_dict)
            else:
                different_subject_with_text_dict = {'Subject': subject_list[k], 'Text': text_list[k]}
                different_subject_with_text_dict_list.append(different_subject_with_text_dict)
        else:
            for j in range(len(different_subject_list)):
                if different_subject_with_text_dict_list[j]['Subject'] == subject_list[k] or "" == subject_list[k]:
                    different_subject_with_text_dict_list[j]['Text'] = different_subject_with_text_dict_list[j]['Text']+(text_list[k])


    name = ['Subject', 'Text']
    df = pd.DataFrame(columns=name, data=different_subject_with_text_dict_list)  # 数据有三列，列名分别为one,two,three
    for row in df.itertuples():
        subject = str(getattr(row, 'Subject'))
        text = str(getattr(row, 'Text'))
        text_create(subject, text)


classify()