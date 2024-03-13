def lists_to_dictionary(keys, values):
    
    if len(keys) != len(values):
        print("Jumlah elemen dalam kedua list harus sama.")
        return None

    
    data_dict = {}
    for i in range(len(keys)):
        data_dict[keys[i]] = values[i]
    
    return data_dict


keys_list = ['nama', 'umur', 'status', 'alamat']


values_list = ['mega', 19, 'mahasiswas', 'kel Mangga dua']


result_dict = lists_to_dictionary(keys_list, values_list)

if result_dict:
    print("Data dictionary hasil konversi:")
    print(result_dict)

