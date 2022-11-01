isim = input("İsminizi giriniz : ")
print("Hoşgeldin",isim)
print("Cevaplardan ilk seçeneği seçmek için 1 ikinci seçeneği seçmek için 2 yazman yeterli olacaktır. İyi eğlenceler :)")

cevap = input("Yolda ilerledin ve birden karşında harabe bir yapı belirdi. İçeriden anlamsız sesler geliyor ve girişte böcekler var. \n Seçimini yap \n İçeri gir ya da kaç : ").lower()

if cevap == "2":
    print("Hadi ama korkmuş olamazsın. \n Kaçtın ve maceradan eksik kaldın.")

elif cevap == "1":
    print("Vaay cesursun pekala o zaman hadi devam edelim",isim)
    print("İçeri girdin ve içeride hiç ışık yok her yer zifiri karanlık ama sen cesurca ilerlemeye devam ediyorsun")
    print("Belli bir süre ilerledikten sonra büyük bir taşın arkasında bir delik farkediyorsun ama girmek için taşı itmek zorundasın.")
    print("Taşı itip içeri girdin ve içerisinin kayanın diğer tarafıyla hiç ilgisi olmadığını gördün. Uçan arabalar,büyücüler,robot insanlar...")
    ri = input("Yakınındaki bir robot insan sana yaklaşıp ismini sordu. Ona cevap verecek misin. Cevap vermek için 1 konuşmadan gitmek için 2 yazman yeterli. : ")
    if ri == "1":
      print("Sen : Merhaba ismim",isim)
    elif ri == "2":
      print("Azıcık nezaket öğren be. Robot insan da olsalar onların da duyguları var. Püü gençlik bitmiş")




else:
  print("Geçersiz sayı. Lütfen oyunu baştan başlatıp geçerli bir sayı gir" ,isim)
