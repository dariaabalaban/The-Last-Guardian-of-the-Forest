import functools

battle_count =0
def battle_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        global battle_count
        battle_count+=1
        print("\n ------ BATTLE STARTED ------")
        result = func(*args, **kwargs)
        print("\n ------ BATTLE ENDED ------")
        return result
    return wrapper
