

def find_person(dict_users, strU):
    if strU in dict_users:
        return dict_users[strU]
    else:
        return 'Not Found'


if __name__ == "__main__":
    names = ['xiaoyun','xiaohong','xiaoteng','xiaoyi','xiaoyang']
    QQ = ['88888','5555555','11111','12341234','1212121']
    dict_users = dict(zip(names, QQ))
    strU = input()
    print(find_person(dict_users, strU))