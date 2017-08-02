def dictionary_tuple():
    # function input
    my_dict = {
        "Speros": "(555) 555-5555",
        "Michael": "(999) 999-9999",
        "Jay": "(777) 777-7777"
    }
    dict_tuple = ()
    for key, data in my_dict.iteritems():
        dict_tuple += (key, data)
    print dict_tuple

dictionary_tuple()