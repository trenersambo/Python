def add_cont(database: list, user_dict: dict):  
    # print(user_dict.values())
    database.append(user_dict.values())
    return database
    
def del_cont(database: list, num_str: int):
    database.pop(num_str)
    return database

def edit_cont(database: str, user_dict: dict, num_str: int):
    database[num_str] = user_dict
    return database