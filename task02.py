def yosh_hisobla(t_yil):
    hozirgi_yil = 2026
    yosh = hozirgi_yil - t_yil
    return yosh

til_yil = int(input("tug'ilgan yilingizni kiriting: "))
print("sizning yoshingiz: ", yosh_hisobla(til_yil))
