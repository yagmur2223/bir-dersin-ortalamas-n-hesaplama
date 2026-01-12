not1=int(input("birinci notu girin="))
not2=int(input("ikinci notu girin="))
performans1=int(input("birinici performasnı girin="))
performans2=int(input("ikinci performansı girin="))
sozlu1=int(input("birinci sözlüyü girin="))
sozlu2=int(input("ikinci sözlüyü girin="))
sozlu_ort=(sozlu1+sozlu2)/2
performans_ort=(performans1+performans2)/2
not_ort=(not1+not2)/2
genel_ortalama=(not_ort+performans_ort+sozlu_ort)/3
print("genel_ortalama=",genel_ortalama)
if genel_ortalama<=50:
    print("sonuç=kaldınız")
else:
    print("sonuç=geçtiniz")