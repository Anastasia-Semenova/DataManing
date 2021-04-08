# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import vk_api
import re
import psycopg2
from nltk.corpus import stopwords


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/


def main():
    token = "7adb16fb7adb16fb7adb16fb4e7aad8d8377adb7adb16fb1aeccee5181096396ce74af7"
    vk_session = vk_api.VkApi(token=token)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    posts = get_posts(group_id="-35488145", api=vk)
    posts_strings = [post['text'] for post in posts]
    all_line = []
    for n in range(len(posts_strings)):
        line = str(posts_strings[n]).lower().split(" ")
        all_line += line
    s1 = re.sub("[^А-Яа-я ]", "", str(all_line)).split(" ")
    for words in s1:
        if words in stopwords.words('russian'):
            s1.remove(words)

    # print(s1)
    dict_sample = {}
    for i in range(len(s1)):
        prom = s1.count(s1[i])
        dict_sample[s1[i]] = prom
    # print(dict_sample)

    sorted_dict = {}
    sorted_keys = sorted(dict_sample, key=dict_sample.get)

    for w in sorted_keys:
        sorted_dict[w] = dict_sample[w]
    items = list(sorted_dict.items())
    right_sorted_dict = {k: v for k, v in reversed(items)}
    print(right_sorted_dict)
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="glotai)900",
        host="datamining.clmkmkowzuvm.us-east-1.rds.amazonaws.com",
        port="5432"
    )

    cur = con.cursor()

    for key in right_sorted_dict:
        cur.execute(
          "INSERT INTO VKAPI(WORD, COUNT) VALUES (%s, %s)", (str(key), int(right_sorted_dict[key]))
        )
    con.commit()
    con.close()


def get_posts(group_id, api):
    posts_0_100 = api.wall.get(owner_id=group_id, count=100).get('items')
    posts_101_200 = api.wall.get(owner_id=group_id, count=100, offset=100).get('items')
    return posts_0_100 + posts_101_200


if __name__ == '__main__':
    main()
