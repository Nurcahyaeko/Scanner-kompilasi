import re	

# Variabel
dict = {"main":"keyword_konstanta", "bool":"tipe_data_boolean", "char":"tipe_data_char", "float":"tipe_data_float",
        "int":"tipe_data_integer", "true":"boolean_true", "false":"boolean_false", "==":"operator_perbandingan_sama",
        "!=":"operator_tidak_sama_dengan", "<":"opeerator_lebih_kecil", "<=":"operator_lebih_kecil_sama_dengan",
        ">":"operator_lebih_besar", ">=":"operator_lebih_besar_sama_dengan", "=":"operator_sama_dengan",
        "if":"percabangan_if", "else":"percabangan_else", "while":"perulangan_while", "+":"operator_tambah",
        "-":"operator_kurang", "*":"operator_kali", "/":"operator_bagi", ";":"semicolon", "(":"kurung_buka",
        ")":"kurung_tutup", "{":"kurung_kurawal_buka", "}":"kurung_kurawal_tutup", "[":"kurung_siku_buka",
        "]":"kurung_siku_tutup", "return":"keyword_return","print":"print","printf":"printf",
		"%":"operator_modulus","&&":"operator_logika_and","!":"operator_logika_not",
		":":"delimiter",",":"delimiter","'":"delimiter","\"":"delimiter"}

nilai_var_integer = re.compile('\d+')
nilai_var_char = re.compile('\'\S|\s\'')
nilai_var_float = re.compile('\d+\.\d')
nilai_var_identifier = re.compile('[a-zA-z]\w*')

def main():
    """ #1 . Melakukan input nama file
        #2 . Membagi kode menjadi beberapa baris
    """


    filename = input("#Program Scanner untuk bahasa C \n#Please type in a filename: ")         #1
    infile = open(filename, "r")
    print("------------------------------------------")
    lines = infile.readlines()                              #2

    for line in lines:
        analyze(line, dict)

    print("------------------------------------------")


def analyze(line, dict):
    linee = re.split("(>=|<=|==|&&|!=|%d|\n|\t|//|\d+\.\d+|\'\S\'|\W)", line)

    lexemes = [x for x in linee if x != '' and x != ' ' and x != "\n"]

    for index in range(len(lexemes)):

        # Jika lexeme adalah comment
        if lexemes[index] == "//":
            print("comment", end = "\t")

            # print out whole comment
            for i in range(len(lexemes) - index):
                print(i, lexemes[i], end = " ")

            # disregard the rest of the line
            print()
            break

        #if the current lexeme is in the dictionary
        if (lexemes[index] in dict):
            # then just print the value of the key
            print(dict[lexemes[index]], end = "\t")

        # otherwise, look to see which literal the lexeme matches
        elif (nilai_var_float.match(lexemes[index]) != None):
            print("nilai_var_float", end = "\t")

        elif (nilai_var_integer.match(lexemes[index]) != None):
            print("nilai_var_integer", end = "\t")

        elif (nilai_var_char.match(lexemes[index]) != None):
            print("nilai_var_char", end = "\t")

            # check ids here because /w catches digits, so it would actually
        # recognize floatLiterals and intLiterals as ids
        elif(nilai_var_identifier.match(lexemes[index]) != None):
            print("nilai_var_identifier", end = "\t")

        print(lexemes[index])


main()

konfirmasi = input("\n \nTekan Enter untuk Keluar")