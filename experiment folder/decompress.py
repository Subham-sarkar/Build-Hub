def decompress(compressed_in):
    new_word = True
    char_holder = ""
    decompressed_out = ""
    for char in compressed_in:
        if char.isalpha and new_word:
            char_holder += char
            new_word = False
        elif char.isalnum:
            decompressed_out += char * char_holder
            new_word = True
    return decompressed_out