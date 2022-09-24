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
        "len_caractere": [{l},{randint(l+1,10)}],
        "len_carac_special": [3,{l-1}],
        "nombre_cle": {randint(100,1500)},
        "mini": {mi},
        "maxi": {randint(mi+100,900)},
        "confusion": {choice(["true","false"])}
    """

    return "{\n"+text+"\n}"


def creat_():
    f = open("setting.json", "w")
    f.write(gen(5,100))
    f.close()

creat_()


