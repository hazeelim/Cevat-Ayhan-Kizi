define z = Character("Patik", color="#ff6699") 
image bg metrobus = im.Scale("bg metrobus.jpg", 1920, 1080) 
image bg cevat = im.Scale("bg cevat.jpg", 1920, 1080) 
image bg gar = im.Scale("bg gar.jpg", 1920, 1080)



label start:

    scene bg metrobus
    with fade

    show duran at center
    with dissolve

    z "Metrobüsün o inanılmaz kalabalığında yine tam balık istifi ilerliyoruz..."
    z "Yine sen? Karşımda durmuş öylece bana bakıyorsun. Bakalım hangi okuldanmışın..."

    menu:
        "Cevat Ayhan Fen Lisesi'ndeyim.":
            jump cevat

        "Ben salcıyım...":
            jump metrobus1



label cevat:
    hide duran
    show el uzatan
    with dissolve
    z "Cevat Ayhan'da mı okuyorsun?! Dur bir dakika... Gerçekten mi?"
    z "Aynı okulun koridorlarını, o yoğun fizik ve matematik sınavlarını birlikte paylaşıyoruz demek ki..."

    menu:
        "Evet, aynı yollardan geçiyoruz. Birlikte inelim mi?":
            jump metrobus

        "Evet, ancak işim var...":
            jump metrobus1


label metrobus:
    hide el uzatan
    scene bg cevat
    with fade
    
    show bkonusan at center
    with dissolve

    z "Şey... Birlikte ayt matematik parçalayalım mı?"
    menu:
         "İşte beklediğim teklif!!":
              jump mutluson
         "Eee.. İşim var sonra ":
            jump kotuson

    return


label metrobus1:
    hide bkonusan
    scene bg metrobus
    with fade
    show sinirli konusan
    z "BENİM VAKTİMİ ÇALMA LÜTFEN!"
    z "Cevat Ayhan Fen Lisesi'nin efsanevi disiplinini ve gururunu bilmez misin sen?!"
    z "Nasıl vaktin olamaaz?!"

    menu:
        "Ş-şey, yanlış anladın!":
            jump dayak_sahnesi

        "SUS ARTIK BE":
            jump dayak_sahnesi1


label dayak_sahnesi1:
    hide bkonusan
    scene bg metrobus
    with fade
    show sinirli bakan
    z "Hâlâ konuşuyor musun?!"
    
    scene bg metrobus
    with fade
    hide sinirli bakan
    show sinirli konusan
    z "Bizim okulun adını lekeleyemezsin!"
    
 
    
    scene bg gar
    with fade
    
    "Metrobüsten dışarı, asfaltın orta yerine doğru dayak yiyerek fırlatılırsın."
    hide sinirli konusan
    show tehditkar
    z"Şimdi işin bitti."
    return

label dayak_sahnesi:

   scene bg metrobus
   with fade
   hide tehditkar
   show duran
   with dissolve
   z"Ne anlamışım o zaman!!"

   z"Seninle daha fazla uğraşamam"
   return

label kotuson:
   hide duran
   scene bg cevat
   show sinirli bakan
   with dissolve
   z"TAMAM O ZAMAN."
   return

label mutluson:
   hide sinirli bakan
   scene bg cevat
   show duran
   with dissolve
   z"Seninle beni harika bir gelecek bekliyor.."
   return