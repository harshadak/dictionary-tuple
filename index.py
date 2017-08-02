def dictionary_tuple():
    # function input
    my_dict = {
        "Speros": "(555) 555-5555",
        "Michael": "(999) 999-9999",
        "Jay": "(777) 777-7777"
    }
    list = []
    list.append(tuple(my_dict.items()))
    return list 

print dictionary_tuple()