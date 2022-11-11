from random import choice, randint

cip = ["ascii_lowercase","ascii_uppercase","ascii_letters"]

lst_cara = ["all.carac",'asian.carac','emoji.carac',
'lang.carac','rand_carac.carac']

def gen(l,mi):
    """
    l: longeur minimume caractère
    mi: longeur minimume nombre de caractère du groupe b
    """

    text = f"""
        "cipher": "{choice(cip)}",
        "substitue with": "configs/{choice(lst_cara)}",
        "cipher punctuation": {choice(["true","false"])},
        "cipher space": true,
        "cipher accent": {choice(["true","false"])},
        "cipher digits": {choice(["true","false"])},
        "len_caractere": [{l},{randint(l+1,30)}],
        "len_carac_special": [3,{l-1}],
        "nombre_cle": [100,{randint(101,3000)}],
        "mini": {mi},
        "maxi": {randint(mi+100,20001)},
        "confusion": {choice(["true","false"])}
    """

    return "{\n"+text+"\n}"


def creat_():
    f = open("rand_"+ str(randint(1,9999)) +".json", "w")
    f.write(gen(5,100))
    f.close()

creat_()


