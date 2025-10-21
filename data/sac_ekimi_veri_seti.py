"""
Saç Ekimi Chatbot - Veri Seti Hazırlama
Bu dosya siteden alınan soru-cevapları düzenlenmiş formatta saklar
"""

from haystack import Document
from typing import List

def create_hair_transplant_dataset() -> List[Document]:
    """
    Saç ekimi hakkında soru-cevap veri setini oluşturur
    Kaynak: https://estefavor.com/sac-ekimi-soru-cevap/
    """
    
    documents = [
        # TEMEL BİLGİLER
        Document(
            content="""
            Soru: Saç ekimi nedir?
            Cevap: Saç ekimi, saç dökülmesi nedeniyle saçları seyrekleşen ve kellik 
            problemi yaşayan kişilerin enselerinden alınan saç köklerinin saç yokluğu 
            meydana gelen yere nakledilmesini sağlayan operasyondur. Saç ekim işleminde 
            kök seçimi, sağlıklı ve güçlü kökler arasından tercih yapılmaktadır. 
            Bu sayede saç ekimi yapılan kişilerin sağlıklı ve gür saçlara ulaşılması 
            mümkün olmaktadır.
            """,
            meta={"kategori": "temel_bilgi", "source": "estefavor.com", "tags": ["genel", "tanım"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi kimlere yapılabilir?
            Cevap: Saç ekimi, cinsiyet fark etmeksizin 24 yaşından büyük herkese 
            yapılabilecek bir işlemdir. Genetik faktörler, yaş ilerlemesi, hastalık 
            ve kaza gibi nedenlerle saç kaybı veya saç seyrekliği olan herkes saç 
            ekim işlemi gerçekleştirebilir.
            """,
            meta={"kategori": "uygunluk", "source": "estefavor.com", "tags": ["yaş", "cinsiyet", "uygunluk"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi kimlere yapılamaz?
            Cevap: Saç ekimi uygulanamayacak kişiler şunlardır:
            - Doğuştan saçı olmayan kişiler
            - Kalp, karaciğer yetmezliği gibi rahatsızlıkları olan kişiler
            - Tansiyon ve şeker hastalıkları olan kişiler (dikkatli yaklaşılmalı)
            - Kan yolu ile bulaşan hastalıkları olan kişiler
            """,
            meta={"kategori": "uygunluk", "source": "estefavor.com", "tags": ["kontraendikasyon", "risk"]}
        ),
        
        # YÖNTEMLER
        Document(
            content="""
            Soru: FUE yöntemi nedir?
            Cevap: FUE yöntemi, özel uçlu mikro motorlar kullanılarak greftlerin 
            tek tek alınması ve saçsız bölgeye tek tek ekilmesi şeklinde gerçekleştirilen 
            saç ekimi yöntemidir. Deri üzerinde kesi yapılmayan bir yöntemdir. 
            Çok daha doğal bir görünüm ve kalıcılık sağladığı için en sık tercih 
            edilen yöntemdir.
            """,
            meta={"kategori": "yontem", "source": "estefavor.com", "tags": ["FUE", "teknik", "yöntem"]}
        ),
        
        Document(
            content="""
            Soru: FUE yönteminin avantajları nelerdir?
            Cevap: FUE saç ekiminin avantajları:
            - Sadece saç kökleri kullanılır, donör bölgeden doku alınmaz
            - Donör bölgede kesi veya dikiş yapılmaz
            - Seanslar arasındaki süre kısadır
            - Her santimetrekareye 55 adetten fazla saç ekilebilir
            - Operasyon sonrası ağrı veya his kaybı meydana gelmez
            """,
            meta={"kategori": "yontem", "source": "estefavor.com", "tags": ["FUE", "avantaj"]}
        ),
        
        Document(
            content="""
            Soru: DHI yöntemi nedir?
            Cevap: DHI işleminde ekim işlemi tek tek gerçekleştirilir. Donör bölgeden 
            alınan saç kökleri, özel kalemler kullanılarak ekim alanına yerleştirilir. 
            Bu yöntemde kanal açma ve kök yerleştirme işlemleri aynı anda gerçekleştirilebilir. 
            Lokal anestezi altında yapılan bir işlemdir. DHI yönteminde saçları tıraş 
            etmeden işlem yapılabilir.
            """,
            meta={"kategori": "yontem", "source": "estefavor.com", "tags": ["DHI", "teknik", "tıraşsız"]}
        ),
        
        Document(
            content="""
            Soru: DHI yönteminin avantajları nelerdir?
            Cevap: DHI yönteminin avantajları:
            - Daha sık ekilme imkanı vardır, daha doğal görünüm
            - Operasyonun verdiği hasar minimumdur
            - İyileşme süreci diğer yöntemlere kıyasla daha hızlıdır
            - Gerekli bölgeye doğrudan ekim imkanı tanır
            - Saç tıraşı gerekmeden işlem yapılabilir
            """,
            meta={"kategori": "yontem", "source": "estefavor.com", "tags": ["DHI", "avantaj"]}
        ),
        
        # OPERASYON SÜRECİ
        Document(
            content="""
            Soru: Saç ekimi operasyonu ne kadar sürer?
            Cevap: Ortalama bir saç ekimi operasyonu 5-6 saat arasında sürmektedir. 
            Ancak kullanılan teknik, ekilecek greft sayısı gibi etkenler operasyon 
            saatini değiştirebilir.
            """,
            meta={"kategori": "operasyon", "source": "estefavor.com", "tags": ["süre", "işlem"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi hangi mevsimlerde yapılabilir?
            Cevap: Saç ekimi dört mevsim gerçekleştirilebilen bir işlemdir. Ancak 
            yaz aylarında ultraviyole ışınların zararlı etkileri ve saç derisinin 
            devamlı olarak terlemesi nedeniyle çok tavsiye edilmez. Yine de dikkatli 
            olmak şartıyla yaz ayında da gerçekleştirilebilir.
            """,
            meta={"kategori": "operasyon", "source": "estefavor.com", "tags": ["mevsim", "zamanlama"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminde anestezi nasıl uygulanır?
            Cevap: Saç ekiminde iki farklı bölgeye lokal anestezi gerçekleştirilir: 
            Donör bölgeye ve saç ekim bölgesine. Lokal anestezi nedeniyle hasta 
            ağrı veya acı hissetmez.
            """,
            meta={"kategori": "operasyon", "source": "estefavor.com", "tags": ["anestezi", "ağrı", "lokal"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminde saçlar neden tıraşlanır?
            Cevap: Saçlar donör bölgedeki saç kökleri arasından en güçlü ve en 
            sağlıklı olanlarının seçilebilmesi için tıraş edilir. Ancak DHI yöntemiyle 
            tıraşsız bir şekilde saç ekimi operasyonu gerçekleştirilebilir.
            """,
            meta={"kategori": "operasyon", "source": "estefavor.com", "tags": ["tıraş", "hazırlık"]}
        ),
        
        # OPERASYON SONRASI
        Document(
            content="""
            Soru: Saç ekiminden sonra ilk yıkama ne zaman yapılır?
            Cevap: İlk yıkama işlemi, saç ekiminden sonraki 3. gün gerçekleştirilir. 
            İlk yıkama işlemi genellikle klinikte uzman gözetiminde gerçekleştirilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["yıkama", "hijyen"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra sigara içilebilir mi?
            Cevap: Saç ekiminin iyileşme sürecinin başarı ile geçirilebilmesi için 
            ilk 10 gün sigara kullanılmaması tavsiye edilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["sigara", "yasak"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra alkol kullanılabilir mi?
            Cevap: Saç ekiminden sonraki ilk ay iyileşme sürecinin başarı ile 
            geçirilebilmesi için alkol kullanılmamalıdır.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["alkol", "yasak"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra ne zaman işe dönülebilir?
            Cevap: 3. günden itibaren işe dönülebilir. Ancak 10. günden sonra 
            dönülmesi tavsiye edilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["iş", "dinlenme"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra spora ne zaman başlanabilir?
            Cevap: Saç ekiminden sonra ilk 3 ay ağır sporlar yasaktır. 1. aydan 
            sonra hafif sporlar, 3. aydan sonra ağır sporlar yapılabilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["spor", "egzersiz"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra denize ne zaman girilebilir?
            Cevap: Saç ekimi operasyonundan 3-4 hafta sonra denize ve havuza girilebilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["deniz", "havuz", "yüzme"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra şapka ne zaman takılabilir?
            Cevap: Saç ekiminden sonraki ilk 1 ay şapka takılmaması tavsiye edilir. 
            1 ay geçtikten sonra standart kumaş şapkalar kullanılabilir. Yün bere 
            kullanmak içinse operasyonun üzerinden iki ay geçmesi gerekir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["şapka", "bere", "koruma"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra nasıl uyunmalı?
            Cevap: İlk 14 gün boyunca saç köklerinin zarar görmemesi ve deriye tam 
            olarak tutunabilmesi için arkanıza iki adet yastık koyarak hafif dik 
            pozisyonda uyumanız tavsiye edilir. İlk 14 gün ense üzerine yatılması 
            donör bölgede ağrıya neden olabilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["uyku", "pozisyon"]}
        ),
        
        # İYİLEŞME SÜRECİ
        Document(
            content="""
            Soru: Saç ekiminden sonra iyileşme süreci ne kadar sürer?
            Cevap: Donör bölgenin iyileşmesi için gereken süre yaklaşık iki haftadır. 
            Kızarıklık, şişlik gibi problemler ise bir hafta içerisinde iyileşir. 
            Ancak tam olarak istenen sonucun yakalanabilmesi, altı ayın sonunda 
            mümkündür.
            """,
            meta={"kategori": "iyileşme", "source": "estefavor.com", "tags": ["süreç", "zaman"]}
        ),
        
        Document(
            content="""
            Soru: Saçlar ne zaman çıkmaya başlar?
            Cevap: İlk 3 ay çıkan saç telleri uzayıp tekrar dökülür. Üçüncü aydan 
            itibaren saçlar kalıcı olarak çıkmaya başlar. Altıncı ay %75'i, 
            on ikinci ayın sonunda ise %95'i çıkmış olur.
            """,
            meta={"kategori": "iyileşme", "source": "estefavor.com", "tags": ["saç_çıkma", "sonuç", "zaman"]}
        ),
        
        Document(
            content="""
            Soru: Şok dökülme nedir?
            Cevap: Şok dökülme ekim yapılan bölgedeki saçların geçici olarak 
            dökülmesidir. 1-3 ay arasında gözlemlenen olağan bir durumdur. 
            İki hafta gibi bir süreç içerisinde sona erer ve saçlar tekrar çıkar.
            """,
            meta={"kategori": "iyileşme", "source": "estefavor.com", "tags": ["şok_dökülme", "geçici"]}
        ),
        
        # İLAÇLAR VE BAKIM
        Document(
            content="""
            Soru: Saç ekiminden sonra hangi ilaçlar kullanılır?
            Cevap: İlk 10-15 gün içerisinde kullanılması gereken ilaçlar:
            - Antibiyotik: Enfeksiyon oluşumunu engellemek için
            - Aspirin: Kan dolaşımının kolaylaşması için
            - Ağrı kesici: Ağrıları kesmek için
            - Kortizon ilacı: Şişlik ve morluk problemlerinin önlenmesi için
            - Mide koruyucu: Diğer ilaçların mideye zarar vermesini engellemek için
            - Okyanus suyu: Kaşıntının giderilmesi için (gerekirse)
            """,
            meta={"kategori": "ilaç", "source": "estefavor.com", "tags": ["antibiyotik", "ağrı_kesici", "tedavi"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra hangi şampuan kullanılmalı?
            Cevap: İlk 14 gün kimyasal içermeyen şampuan kullanılmalıdır. 
            İşlemi gerçekleştiren doktor, kullanılması gereken şampuan hakkında 
            ayrıntılı bilgi verecektir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["şampuan", "temizlik"]}
        ),
        
        # SAÇ KESİMİ VE ŞEKİLLENDİRME
        Document(
            content="""
            Soru: Saç ekiminden sonra ne zaman saç kesilebilir?
            Cevap: İlk 2 ay kesim yapılması önerilmez. İlk kesim işleminin yeni 
            köklerin zarar görmemesi için makas ile yapılması önerilir. 3. aydan 
            itibaren tıraş makinesiyle tıraş olunabilir. 6. aydan itibaren usturalı 
            kesim yapılabilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["kesim", "tıraş", "berber"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra ne zaman boya yapılabilir?
            Cevap: Saçların tam olarak uzaması 6. ayı bulabilir. İlk 3 ay herhangi 
            bir komplikasyon oluşmaması için boya yapılmaması önerilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["boya", "kimyasal"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra jöle kullanılabilir mi?
            Cevap: Saç ekiminden sonraki ilk 3 ay kullanılmaması tavsiye edilir. 
            Ancak sonraki süreçte rahatlıkla kullanılabilir.
            """,
            meta={"kategori": "bakım", "source": "estefavor.com", "tags": ["jöle", "şekillendirme"]}
        ),
        
        # KALICILIK VE SONUÇLAR
        Document(
            content="""
            Soru: Saç ekimi kalıcı mıdır?
            Cevap: Saç ekimi işleminde kullanılan saç kökleri, ense bölgesinden 
            alınır. Bu bölgedeki kıllar genetik olarak dökülmez. Bu nedenle kalıcı 
            bir operasyon olduğu söylenebilir.
            """,
            meta={"kategori": "sonuç", "source": "estefavor.com", "tags": ["kalıcılık", "ömür boyu"]}
        ),
        
        Document(
            content="""
            Soru: Ekilen saçlar doğal saçtan farklı mıdır?
            Cevap: Yeni ekilen saçlar sizin kendi saçlarınızdır. Bu nedenle normal 
            saçtan hiçbir farkı yoktur. İstenilen uzunluğa kadar uzatılabilir.
            """,
            meta={"kategori": "sonuç", "source": "estefavor.com", "tags": ["doğallık", "görünüm"]}
        ),
        
        # FİYAT VE EKONOMİK
        Document(
            content="""
            Soru: Saç ekimi fiyatlarını ne belirler?
            Cevap: Saç ekimi fiyatlarını belirleyen hususlar:
            - Uygulanacak yöntem (FUE, DHI vb.)
            - Greft sayısı
            - Saçsız bölgenin genişliği
            - Tedavi merkezinin kalitesi
            - Teknik ekibin uzmanlık seviyesi
            """,
            meta={"kategori": "fiyat", "source": "estefavor.com", "tags": ["maliyet", "ücret"]}
        ),
        
        Document(
            content="""
            Soru: Greft nedir?
            Cevap: Greft, saçsız bölgeye ekilecek doku parçasıdır. Greft sayısı 
            ise saç ekim operasyonunda kullanılacak saç kökü sayısını ifade eder.
            """,
            meta={"kategori": "temel_bilgi", "source": "estefavor.com", "tags": ["greft", "terim"]}
        ),
        
        # YAN ETKİLER VE RİSKLER
        Document(
            content="""
            Soru: Saç ekiminin yan etkileri var mıdır?
            Cevap: Saç ekiminin sağlığa zararlı olduğuna dair bir bulgu yoktur. 
            Ancak lokal anestezi nedeniyle alerji oluşması riski bulunur. 
            Operasyondan önce yapılacak testler ile bu risk sıfıra indirilir.
            """,
            meta={"kategori": "risk", "source": "estefavor.com", "tags": ["yan_etki", "alerji"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra enfeksiyon olur mu?
            Cevap: Saç ekimi cilt altında gerçekleştirilen bir uygulamadır. İşlem 
            sonrası antibiyotik kullanılır. Bu nedenle büyük çapta enfeksiyonlar 
            gelişmez. %2 ihtimalle küçük enfeksiyonlar oluşabilir.
            """,
            meta={"kategori": "risk", "source": "estefavor.com", "tags": ["enfeksiyon", "komplikasyon"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra kaşıntı neden olur?
            Cevap: Saç ekiminde açılan küçük delikler, tıbbi olarak yaralanma 
            olarak nitelendirilir. Kaşıntı, yaraların iyileşme aşamasında meydana 
            gelen doğal bir süreçtir. Yaranın kabuklanması, saç diplerinin 
            nemlenmesini ve hava almasını yavaşlatarak kaşıntıya neden olabilir.
            """,
            meta={"kategori": "yan_etki", "source": "estefavor.com", "tags": ["kaşıntı", "iyileşme"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra sivilce çıkar mı?
            Cevap: Saç ekiminden sonra sivilce çıkması yan etkilerden birisidir. 
            Kalıcı bir durum değildir. İçerideki saç köklerinin dışarıya çıkmaya 
            çalışması nedeniyle meydana gelir. Donör bölgede veya saç ekimi yapılan 
            bölgede sivilce problemi ortaya çıkabilir.
            """,
            meta={"kategori": "yan_etki", "source": "estefavor.com", "tags": ["sivilce", "geçici"]}
        ),
        
        # DİNİ VE ETİK
        Document(
            content="""
            Soru: Saç ekimi dinen haram mıdır?
            Cevap: Saç ekimi insanın kendi saçıyla gerçekleştirilen, kalıcı olan 
            ve tedavi olarak görülen bir operasyondur. Bu nedene dinen haram 
            olduğu söylenmemektedir.
            """,
            meta={"kategori": "dini", "source": "estefavor.com", "tags": ["din", "helal", "haram"]}
        ),
        
        # KADINA ÖZEL
        Document(
            content="""
            Soru: Kadınlar saç ekimi yaptırabilir mi?
            Cevap: Kadınların da saç ekimi yaptırabilmesi mümkündür. Ancak bazı 
            tetkik işlemlerinin gerçekleştirilmesi ve engel bir durum olup olmadığının 
            araştırılması gerekmektedir. Özellikle hormonal problemlerin, tiroid 
            bezlerinin az ya da fazla çalışıp çalışmadığına bakılmalıdır.
            """,
            meta={"kategori": "uygunluk", "source": "vitasacekim.com", "tags": ["kadın", "cinsiyet", "hormon"]}
        ),
        
        # YENİ EKLENENLER - VİTASACEKIM.COM
        
        Document(
            content="""
            Soru: Şok dökülme nedir ve ne zaman olur?
            Cevap: Saç ekimi işleminden yaklaşık 2 ile 4 hafta sonra genellikle geçici 
            bir saç dökülmesi yaşanır. Bu duruma şok dökülme denir. FUE saç ekimi 
            işleminden sonra yaşanan geçici saç dökülmesi, iyileşme sürecinin doğal 
            bir döngüsüdür. Saç kökleri büyüme döngüsüne başlamadan önce uyku 
            dönemine girer ve ardından da dökülür. Şok dökülme süreci geçtikten 
            sonra ekilen saçlar tekrar çıkmaya ve uzamaya başlar.
            """,
            meta={"kategori": "iyileşme", "source": "vitasacekim.com", "tags": ["şok_dökülme", "geçici", "normal"]}
        ),
        
        Document(
            content="""
            Soru: Başarılı bir saç ekiminden sonra tekrar saç dökülmesi olur mu?
            Cevap: Başarılı bir saç ekimi yaptırdıktan seneler sonra gözle görülür 
            biçimde saç kaybı yaşanmasının nedenlerinden bir tanesi Telogen Effluvium'dur. 
            Bu durumda çok fazla oranda saç folikülü telogen (dinlenme) faza girer ve 
            dökülmeye başlar. Saç folikülleri dinlenme fazından çıktıktan sonra tekrar 
            büyüme fazına hazırlanır, böylece dökülen eski saçların yerine yenileri 
            çıkmaya başlar. Bu geçici bir durumdur.
            """,
            meta={"kategori": "iyileşme", "source": "vitasacekim.com", "tags": ["telogen_effluvium", "geçici_dökülme"]}
        ),
        
        Document(
            content="""
            Soru: Hangi sağlık durumları saç dökülmesine sebep olabilir?
            Cevap: Ender de olsa bir sağlık durumu, saç köklerine zarar verebilir ve 
            dökülmeye neden olabilir. Diffüz Alopecia Areata formları ve Liken Planopilaris 
            hastalığı saç dökülmesinin yeniden yaşanmasına neden olabilmektedir.
            """,
            meta={"kategori": "risk", "source": "vitasacekim.com", "tags": ["hastalık", "alopecia"]}
        ),
        
        Document(
            content="""
            Soru: Hayat tarzı saç dökülmesini etkiler mi?
            Cevap: Evet, belirli ilaçların kullanımı saç dökülmesine neden olabilmektedir. 
            Beslenme alışkanlıkları, sigara kullanımı ve stres gibi yaşam tarzı faktörlerine 
            bağlı olarak da saç dökülmesi yaşanabilmektedir. Sağlıklı bir yaşam tarzı 
            benimsemek, başarılı bir saç ekimi işleminden sonra tekrarlanabilecek bir 
            saç dökülmesi riskini minimal düzeye çekecektir.
            """,
            meta={"kategori": "bakım", "source": "vitasacekim.com", "tags": ["yaşam_tarzı", "beslenme", "sigara"]}
        ),
        
        Document(
            content="""
            Soru: FUE tekniğinde acı hissediliyor mu?
            Cevap: Operasyon esnasında saç köklerinin alınacağı alan ve sonrasında da 
            ekimin yapılacağı bölge lokal anestezi ile uyuşturulur. Operasyona başlamadan 
            önce enjekte edilen lokal anestezi biraz rahatsızlık verebilir ama bu durum 
            geçicidir. Anestezi etkisini göstermeye başladıktan sonra ağrı ve acı hissetmez. 
            Operasyon sonrası anestezi etkisini göstermeye devam edeceği için hasta bir 
            süre daha acı duymaz. Biraz rahatsızlık ve hassasiyet hissedilebilir ama 
            genellikle kısa ve hafif süreli olacaktır.
            """,
            meta={"kategori": "operasyon", "source": "vitasacekim.com", "tags": ["ağrı", "anestezi", "acı"]}
        ),
        
        Document(
            content="""
            Soru: Türkiye'de FUE ile saç ekimi iyileşme süresi ne kadar?
            Cevap: İyileşme süresi kişiden kişiye değişkenlik gösterir. Çoğu kişide 
            operasyondan 10-14 gün sonra gözle görülür bir iyileşme başlar. Bazı durumlarda 
            ekim yapılan bölgede oluşan kızarıklık, operasyonun ikinci haftasından sonra 
            devamlılığını koruyabilir.
            """,
            meta={"kategori": "iyileşme", "source": "vitasacekim.com", "tags": ["süre", "kızarıklık"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi operasyonundan önce nelere dikkat etmeliyim?
            Cevap: Operasyondan bir hafta önce aspirin, coraspin, alkol, vitamin E gibi 
            kan sulandırıcı maddelerden uzak durulmalıdır. Sigara ve kahve ürünlerin 
            tüketimi en aza indirgenmeli ve hatta içilmemesi tavsiye edilir. Sağlıklı 
            bir verim ve hızlı iyileşme için bu çok önemlidir. Operasyon günü iyi bir 
            kahvaltı yapmak gerekir.
            """,
            meta={"kategori": "hazırlık", "source": "vitasacekim.com", "tags": ["öncesi", "hazırlık", "aspirin"]}
        ),
        
        Document(
            content="""
            Soru: Ekilen saçlar ne zaman ve nasıl çıkar?
            Cevap: Saçlar ekim işleminden yaklaşık 15-20 gün sonra dökülebilir (şok dökülme). 
            İlk saçlar ekim işleminden ortalama 3 ay sonra çıkmaya başlar. 6. ayda ekilen 
            saçların %70'inin çıkmış olması beklenir. Saçlar ayda yaklaşık 1 cm uzar. 
            Ortalama 1 yıl sonra ekilen saçların tamamı çıkmış olacaktır. Zamanla saç 
            gerçek formuna kavuşacaktır.
            """,
            meta={"kategori": "iyileşme", "source": "vitasacekim.com", "tags": ["saç_çıkma", "zaman", "süreç"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi için yaş sınırı var mıdır?
            Cevap: Saç ekimi 20 yaşından itibaren erkek tipi saç dökülmesi olan herkese 
            uygulanabilir. Önemli bir rahatsızlık, alerji, yüksek tansiyon veya şeker 
            hastalığı varsa özellikle belirtilmelidir. Saç ekimi operasyonu için dökülmenin 
            şekli önemlidir ve saç dökülmesinin bitip bitmemiş olmasında yaş önemli 
            belirleyicidir.
            """,
            meta={"kategori": "uygunluk", "source": "vitasacekim.com", "tags": ["yaş", "20_yaş"]}
        ),
        
        Document(
            content="""
            Soru: Ekilen saçlar dökülür mü?
            Cevap: Saç ekiminde ekilen saçlar dökülmez. Çünkü ekilen kökler genetik 
            olarak dökülme özelliği olmayan iki kulak arasındaki ense bölgesinden 
            alınmaktadır. Bu nedenle saçların tutmama ihtimali yoktur. Enseden alınan 
            saçlar genetik olarak dökülmediği için bu bölgeden alınarak ekilen saçlar 
            kalıcıdır.
            """,
            meta={"kategori": "sonuç", "source": "vitasacekim.com", "tags": ["kalıcılık", "ense", "genetik"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi operasyonu için uygun olmayan durumlar nelerdir?
            Cevap: Saç nakli her yaşta uygulanabilir ancak tansiyon hastalığı, şeker 
            hastalığı, karaciğer ya da kalp hastalığı olan kişilere ön kontrolleri 
            yapıldıktan sonra uygulanabilir. Lokal anestezi altında yapılacak bir 
            operasyonda kontraendikasyon oluşturacak herhangi bir sistemik hastalık 
            varsa bu hastalık tedavi edildikten sonra yapılmalıdır.
            """,
            meta={"kategori": "uygunluk", "source": "vitasacekim.com", "tags": ["kontraendikasyon", "hastalık"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi sağlık açısından problem teşkil eder mi?
            Cevap: Saç ekiminin kişiye rahatsızlık verecek veya ileride oluşabilecek 
            hiçbir yan etkisi yoktur. Ehil ellerde, uygun ameliyathane koşullarında, 
            uygun cerrahi aletlerle yapılan operasyonun bilinen bir zararı yoktur.
            """,
            meta={"kategori": "risk", "source": "vitasacekim.com", "tags": ["güvenlik", "yan_etki"]}
        ),
        
        Document(
            content="""
            Soru: Ekilen saça özel bakım gerekiyor mu?
            Cevap: Ekilen saçlara uygulanacak ilk yıkama Uzman Doktor tarafından 
            yapılmalıdır. Sonrasında kullanılacak solüsyonların seçimini de Uzman 
            Doktor belirlemelidir. 3 aydan sonra Saç Mezoterapisi yapılması tavsiye edilir.
            """,
            meta={"kategori": "bakım", "source": "vitasacekim.com", "tags": ["bakım", "mezoterapi", "yıkama"]}
        ),
        
        Document(
            content="""
            Soru: Saç muayenesi nasıl yapılır?
            Cevap: Saç ekimi yaptıracak kişinin muayenesinde tüm sağlık sorunları 
            sorgulandıktan sonra saç rengi, saç kalınlığı, saç köklerinin alınacağı 
            bölgenin sıklığı ve ekim yapılacak bölgenin genişliği belirlenir. Hasta 
            bilgilendirilir. Fiziki muayene, saç analizi ve dermatolojik testlerin 
            sonucu değerlendirilir.
            """,
            meta={"kategori": "hazırlık", "source": "vitasacekim.com", "tags": ["muayene", "analiz"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi komplikasyonları ve yan etkileri nelerdir?
            Cevap: Saç ekimi komplikasyonları oldukça az görülür:
            - Pembelik 2-8 hafta sürebilir
            - Mevcut saçlarda geçici incelme olabilir
            - Hafif sızıntı ve kabuklanma 7-10 gün içinde temizlenir
            - Ense bölgesinde hafif ağrı (FUE'de 3-4 gün, FUT'ta 1-2 hafta)
            - Hissizlik ve uyuşukluk (FUE'de birkaç hafta, FUT'ta aylarca)
            - Hafif kaşıntı (ilaçlarla giderilebilir)
            - Hafif şişlik/ödem (3-5 gün içinde)
            - Kist oluşumu (2 ay sonra, kendiliğinden düzelebilir)
            - Enfeksiyon (çok nadir)
            """,
            meta={"kategori": "risk", "source": "vitasacekim.com", "tags": ["komplikasyon", "yan_etki", "şişlik"]}
        ),
        
        Document(
            content="""
            Soru: Hangi durumlar saç ekimini riskli hale getirir?
            Cevap: Kanama riskini artıran, geç iyileşme ve enfeksiyon gibi komplikasyonlara 
            yol açabilecek durumlar: kronik metabolik hastalıklar, saçlı deride oluşan 
            yineleyen enfeksiyonlar, diabet hastalığı, sigara ve alkol tüketimi, obezite, 
            beslenme problemleri, kemoterapi ilaçları gibi immunsupresif ilaçların ve 
            kan sulandırıcı ilaçların kullanılması. Hasta mutlaka bunlar hakkında 
            cerraha bilgi vermeli ve uyarılmalıdır.
            """,
            meta={"kategori": "risk", "source": "vitasacekim.com", "tags": ["risk_faktörü", "diabet", "sigara"]}
        ),
        
        Document(
            content="""
            Soru: Ekilen saçların tamamı çıkar mı, büyüme oranı nedir?
            Cevap: Ön kısımda ekimden sonra uzayan saç miktarı yaklaşık %80-90 oranlarında 
            iken tepe (vertex) bölgesinde bu oran %60-70'lere düşmektedir. Saçlar çıktıktan 
            sonra hangi saçların ekim sonucu çıkan, hangilerinin daha önce var olan saçlar 
            olduğunu söylemek zor olduğu için kesin bir oran vermek mümkün değildir.
            """,
            meta={"kategori": "sonuç", "source": "vitasacekim.com", "tags": ["başarı_oranı", "büyüme"]}
        ),
        
        Document(
            content="""
            Soru: Genç yaşta başlayan saç dökülmelerinde nasıl yol izlenmeli?
            Cevap: 21 yaş altında, eğer hastada dökülme çok şiddetli değilse saç ekiminden 
            kaçınmak gerekli. Çok erken yaşlarda saç restorasyon cerrahisi ilk seçenek 
            olarak düşünülmemeli, daha çok medikal tedavilerle hasta izlenmeli ve kontrol 
            altında tutularak dökülme paternine göre tedavi değişikliklerine gidilmeli. 
            Tecrübeli ve etik ilkelere uygun olarak hastalarını değerlendiren doktorlara 
            gidilmeli ve ne tür bir yol haritası izleneceği konusunda fikir alınmalı.
            """,
            meta={"kategori": "uygunluk", "source": "vitasacekim.com", "tags": ["genç", "21_yaş", "erken_yaş"]}
        ),
        
        Document(
            content="""
            Soru: FUE saç ekimi nedir ve nasıl yapılır?
            Cevap: FUE, saç ekiminde en bilinen ve en sık tercih edilen tekniklerden 
            biridir. Hastanın tüm saçları 3mm uzunluğunda olacak şekilde kısaltıldıktan 
            sonra donör bölge lokal anestezi ile uyuşturulur. Mikro motor ile gevşetilen 
            greftler cımbıza benzer bir aletle toplanır. Ekim yapılacak bölge uyuşturularak, 
            bladeler kullanılarak köklerin yerleştirileceği kanallar açılır. Toplandığında 
            üzerinde bir miktar doku parçası bulunan greftler doku parçalarından ayrıştırılarak 
            kalan saç kökleri kanallara yerleştirilir. En son aşamada donör bölge pansuman 
            yapılarak kapatılır.
            """,
            meta={"kategori": "yontem", "source": "vitasacekim.com", "tags": ["FUE", "teknik", "mikro_motor"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi yaptıran ünlüler kimlerdir?
            Cevap: Ülkemizde ve yurt dışında pek çok ünlü ismin saç ekimi yaptığı 
            bilinmektedir. Yalın, Mustafa Ceceli, Oktay Kaynarca, Yılmaz Erdoğan, 
            Tamer Karadağlı, Fikret Kuşkan, Murat Boz, Kenan İmirzalıoğlu, George Clooney, 
            Mel Gibson, Tom Hanks, John Travolta, Jude Law ve Robbie Williams saç ekimi 
            yaptıran yıldızlar arasında yer almaktadır.
            """,
            meta={"kategori": "genel", "source": "vitasacekim.com", "tags": ["ünlüler", "celebrities"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminde kullanılan son teknolojiler nelerdir?
            Cevap: Her gün gelişen teknoloji, saç ekimi prosedürlerini de olumlu yönlerde 
            etkilemektedir. Son gelişmeler arasında Sapphire Blade ve ağrısız anestezi 
            alternatifleri yer almaktadır. Özellikle iğne korkusu yaşayan kişiler tarafından 
            tercih edilen ağrısız anestezi alternatifi, iğne kullanılmadan lokal anestezi 
            yapılmasını sağlar. Sapphire Blade ise kanal açma aşamasında çelik uçlu 
            bladeler yerine safirden elde edilmiş bladeler kullanılmasıdır.
            """,
            meta={"kategori": "teknoloji", "source": "vitasacekim.com", "tags": ["safir", "sapphire", "ağrısız_anestezi"]}
        ),
        
        Document(
            content="""
            Soru: Zayıflayan (incelen) saç üzerine ekim yapılabilir mi?
            Cevap: Saç ekimi yapılabilmesi için saç dökülmesinin neredeyse durmuş olması 
            gereklidir. Bazı kişilerde saç dökülmesi neredeyse durmuş olduğunda belli 
            bir bölgede tamamen saç kaybı yerine seyrelen ve zayıflayan saçların kalmış 
            olduğu gözlenebilir. Böyle bir durumda kalan zayıf saçlar, saç ekimi operasyonu 
            ile sıklaştırılıp, daha gür görünmeleri sağlanabilir.
            """,
            meta={"kategori": "uygunluk", "source": "vitasacekim.com", "tags": ["seyrelme", "sıklaştırma"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminde donör başkası olabilir mi?
            Cevap: Hayır olamaz. Saç ekiminde kendi saç köklerinizin kullanılması esastır. 
            Bir başkasına ait olan saç kökleri veya sentetik maddeler kullanılamaz. 
            Saç ekiminde başkasının donör olması mümkün değildir.
            """,
            meta={"kategori": "genel", "source": "vitasacekim.com", "tags": ["donör", "kendi_saç"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi için kaç gün ayırmam gerekir?
            Cevap: Ekim işlemi aynı gün tamamlanır. 3. gün ise ilk yıkama için 
            merkezimize gelmeniz gerektiğinden toplamda 3 gün yeterli olacaktır.
            """,
            meta={"kategori": "operasyon", "source": "vitasacekim.com", "tags": ["süre", "gün", "planlama"]}
        ),
        
        # ANKARA INTERNATIONAL SAÇ EKİMİ
        
        Document(
            content="""
            Soru: Saç ekiminden önce deri bakımında nelere dikkat edilmelidir?
            Cevap: Eğer aktif bir saçlı deri hastalığı var ise operasyondan önce tedavi 
            edilmeli, aktif sivilce varlığında antibiyotik kullanılmalı, aşırı kepeklenme 
            varsa tedavi edilmeli, prekanseröz olabilecek deri lezyonları var ise operasyon 
            öncesi alınmalı ve patolojiye gönderilmelidir. Peruk kullanılıyorsa 1-2 hafta 
            önceden kullanımı kısıtlanmalı, yapıştırıcı yıkanmalıdır. Jöle, topik gibi 
            kozmetik ürünler kullanılmamalıdır. Minoksil gibi saçların dökülmesini önleyen 
            spreyler kullanılıyorsa kullanımları 1 hafta önceden kesilmelidir.
            """,
            meta={"kategori": "hazırlık", "source": "ankarainternational.com", "tags": ["deri_bakımı", "öncesi", "peruk"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimini yaptırmak için bütün saçların dökülmesi beklenmeli midir?
            Cevap: Hayır. Ön saçların çizgisi ya da arka taç bölgesi dökülmüş, diğer 
            bölgeleri dökülmemiş hastalarda diğer saçların dökülmesi beklenmeden yapılabilir. 
            FUE yöntemini ilerleyen dönemlerde işlemi tekrarlamak mümkündür. Yani diğer 
            saçları da döküldüğünde doğal olmayan bir görünüm oluşmadan önce ikinci bir 
            operasyon yapılabilir. Yıllar içerisinde yapılabilecek bu operasyonlarla hiç 
            kel kalmadan kellik sorunu çözülmüş olur.
            """,
            meta={"kategori": "uygunluk", "source": "ankarainternational.com", "tags": ["zamanlama", "erken_ekim"]}
        ),
        
        Document(
            content="""
            Soru: Uygulamadan sonra hastanede kalmak gerekir mi?
            Cevap: Saç ekimi sonrası hastanede kalmaya gerek yoktur, hasta işlemden 
            hemen sonra evine gidebilir. Operasyon günü değil olmak üzere normal 
            aktivitelerine dönebilir.
            """,
            meta={"kategori": "operasyon", "source": "ankarainternational.com", "tags": ["hastane", "yatış"]}
        ),
        
        Document(
            content="""
            Soru: Operasyon sonrasında nelere dikkat edilmelidir?
            Cevap: İşlem yapılan bölge her türlü travmadan korunmalıdır. Oluşabilecek 
            ödemin önlenmesi hastanın sırt üstü uzanması ile engellenebilir. Operasyona 
            bağlı ödem nedeni ile saçların çizgisi asimetrik ya da çok geride görülebilir, 
            bu değerlendirmelerin yapılabilmesi ancak 8 ay sonra mümkün olacaktır. Eve 
            giderken hastanın araç kullanması önerilmez. Operasyon sonrası hafif yemekler 
            yenmesi önerilir. Operasyon sonrası ortalama 10 gün sigara ve alkol kullanımı 
            önerilmez.
            """,
            meta={"kategori": "bakım", "source": "ankarainternational.com", "tags": ["sonrası", "ödem", "dikkat"]}
        ),
        
        Document(
            content="""
            Soru: Sonrasında pansuman gerekecek mi?
            Cevap: Evet, özellikle donör alan kapatılır, alıcı alan açık bırakılır. 
            Bu pansuman ortalama 2-3 gün sonra saçlar yıkanırken çıkartılır.
            """,
            meta={"kategori": "bakım", "source": "ankarainternational.com", "tags": ["pansuman", "donör_alan"]}
        ),
        
        # YENİ EKLENENLER - SMILE HAIR CLINIC
        
        Document(
            content="""
            Soru: Saç ekiminden sonra ne kadar süre şapka kullanmalıyım?
            Cevap: Saç ekiminden sonra size verilen şapkayı 10 gün boyunca kullanmanız 
            önerilir. Mecbur kalmadıkça ekim işleminden bir ay öncesinde şapka kullanımı 
            uygun değildir. Güneşe çıkarken mutlaka şapka ya da yüksek faktörlü güneş 
            kremi kullanılmalıdır.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["şapka", "koruma", "güneş"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra ne zaman egzersiz yapabilirim?
            Cevap: Operasyondan sonra egzersiz yapmaya başlamak için en az 1 ay 
            beklemelisiniz. İlk 3 ay ağır sporlar yasaktır. 1. aydan sonra hafif 
            sporlar yapılabilir.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["spor", "egzersiz", "1_ay"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra başımı her gün yıkamalı mıyım?
            Cevap: Evet, saç ekiminden sonra 1 ay boyunca her gün başınızı yıkamalısınız. 
            İlk yıkama operasyondan sonraki ikinci gün yapılır. Yaklaşık 15 gün boyunca, 
            kabuklar deriden tamamen atılana kadar özel şampuan kullanılmalıdır. 
            Yaklaşık 15 gün sonra saçlarınızı parmak uçlarınızla hafifçe masaj yaparak, 
            1 ay sonra ise tam olarak eskiden olduğu şekilde yıkamaya başlayabilirsiniz.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["yıkama", "günlük", "şampuan"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi sonrasında bandajımı ne zaman çıkarabilirim?
            Cevap: Operasyondan sonraki ikinci gün başınızı yıkamanız gerekir. Başınızı 
            yıkamadan önce bandaj çıkartılır ve sonrasında tekrar kullanılması gerekmez. 
            Donör bölge özellikle kapatılır, pansuman ortalama 2-3 gün sonra saçlar 
            yıkanırken çıkartılır.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["bandaj", "pansuman"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi sonrası ne zaman cinsel ilişkiye girebilirim?
            Cevap: Operasyon sonrası cinsel ilişki konusunda kısıtlama getirilmez, 
            çok efor harcamamanız önerilir. İlk birkaç gün dikkatli olunması tavsiye edilir.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["cinsel_ilişki", "aktivite"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra şişlik normal midir?
            Cevap: Şişlik görülmesi normaldir, endişelenmeyin. Her iki saatte bir 
            10 dakika buz uygulayabilir, başınıza hafifçe masaj yapabilirsiniz. 
            Şişlikler birkaç gün içinde yok olacaktır. Oluşabilecek ödemin önlenmesi 
            hastanın sırt üstü uzanması ile engellenebilir.
            """,
            meta={"kategori": "yan_etki", "source": "smilehairclinic.com", "tags": ["şişlik", "ödem", "normal"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi sonrası kullanılan ilaçlar uçakta el bagajına alınır mı?
            Cevap: Hayır alınmaz, bu nedenle ilaçlarınızı kontrol etmelisiniz. Yanınızda 
            4 x 100 ml boş şişeler getirerek verilen ürünleri bu şişelere doldurabilirsiniz.
            """,
            meta={"kategori": "seyahat", "source": "smilehairclinic.com", "tags": ["uçak", "ilaç", "bagaj"]}
        ),
        
        Document(
            content="""
            Soru: Nakledilen saçlar döküldü, endişelenmeli miyim?
            Cevap: Nakledilen saçların dökülmesi normaldir. Saçlar dökülse dahi nakledilen 
            saç kökleri sağlamlığını korumaktadır. Bu şok dökülme (shock loss) dediğimiz 
            doğal bir süreçtir. Saç ekiminin sabır isteyen bir süreç olduğu unutulmamalıdır. 
            Operasyondan ortalama 2-4 hafta sonra saçlar dökülür, ancak kökler derinin 
            altında kalır ve 3 ay sonra tekrar çıkmaya başlar.
            """,
            meta={"kategori": "iyileşme", "source": "smilehairclinic.com", "tags": ["şok_dökülme", "normal", "endişe"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminin sonuçları ne zaman görünür olur?
            Cevap: Saç ekimi operasyonundan sonra ilk 6 ay içinde sonuç %70 oranında 
            görünür olur. Tam sonuç alınması ise 12 ila 18 ay aralığında sürer. 
            6.-9. ay arasında sonucun %60-70'i görülür. 9.-12. ay arasında ekilen 
            saçların yoğunluğunda artış görülür. 12. ayın bitiminde yoğunluğun %80-90'ına 
            ulaşılmış olur. 12-24. aylar arasında kalınlaşma tamamlanır ve operasyonun 
            sonucu tamamen görülür.
            """,
            meta={"kategori": "sonuç", "source": "smilehairclinic.com", "tags": ["zaman", "12_ay", "18_ay", "sonuç"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra ne kadar süre dikkatli uyumam gerekir?
            Cevap: Bir hafta boyunca dikkatli uyumanız önerilir. İlk 14 gün boyunca 
            saç köklerinin zarar görmemesi için arkanıza iki adet yastık koyarak hafif 
            dik pozisyonda uyumanız tavsiye edilir.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["uyku", "pozisyon", "1_hafta"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden sonra evden çıkabilir miyim?
            Cevap: Evet, doktor tarafından önerilen dinlenme süresinin ardından evinizden 
            ayrılabilir, şehri keşfedebilirsiniz. Aynı gün evinize ya da otelinize 
            dönebilirsiniz. Ancak ilk birkaç gün dikkatli olunması önerilir.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["günlük_yaşam", "aktivite"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden önce saçlarımı tıraş etmeli miyim?
            Cevap: Hayır, yapılacak saç ekim işlemine bağlı olarak saçlarınızı tıraş 
            etmek iyi bir fikir olmayabilir. İşlem öncesi saç planlamanızı yapmak ve 
            cerrahi düzeltme gerektiren bölgeleri işaretlemek için saçlarınızı tıraş 
            etmemeniz önerilir. Planlama sonrası klinik saçlarınızı tıraş edecektir.
            """,
            meta={"kategori": "hazırlık", "source": "smilehairclinic.com", "tags": ["tıraş", "hazırlık"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekiminden önce nelere dikkat etmeliyim?
            Cevap: İşlem öncesi hafif bir kahvaltı yapılmalı, yağlı ve ağır yiyeceklerden 
            kaçınılmalıdır. Kullandığınız ilaçlar ve sağlık durumunuz hakkında doktoru 
            bilgilendirmelisiniz. Ameliyattan bir hafta önce Minoxidil veya Rogaine'den 
            kaçınılmalı ve iki hafta sonra tekrar başlanmalıdır. Alkol kullanımından 
            operasyon gününden 12 saat önce kaçınılmalıdır. Operasyondan 2 gün önce 
            sigara kullanımı bırakılmalıdır. Saç bakım yağları, jel, krem gibi ürünler 
            kullanılmamalıdır.
            """,
            meta={"kategori": "hazırlık", "source": "smilehairclinic.com", "tags": ["öncesi", "hazırlık", "beslenme"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi operasyonunda ağrı hissedilir mi?
            Cevap: Saç ekimi sırasında hissedilen acı kişiden kişiye göre değişmektedir 
            ancak operasyon lokal anestezi altında yapıldığından yoğun bir acı 
            hissedilmemektedir. Operasyon öncesi enjekte edilen lokal anestezi biraz 
            rahatsızlık verebilir ama bu durum geçicidir.
            """,
            meta={"kategori": "operasyon", "source": "smilehairclinic.com", "tags": ["ağrı", "anestezi"]}
        ),
        
        Document(
            content="""
            Soru: Operasyondan sonra yeni çıkan saçlarım doğal görünecek mi?
            Cevap: Operasyonlar profesyonel ve alanında deneyimli hekimler tarafından 
            yapıldığında kişi doğal görünümlü saçlara sahip olur. Saç ekimi yaptırdığınız 
            belli olmaz. Kanal açma işlemi doğru yapıldığında ve saçların çıkış yönü 
            dikkate alındığında tamamen doğal bir görünüm elde edilir.
            """,
            meta={"kategori": "sonuç", "source": "smilehairclinic.com", "tags": ["doğallık", "görünüm"]}
        ),
        
        Document(
            content="""
            Soru: Vücut kılı saç ekiminde kullanılabilir mi?
            Cevap: Evet, Vücut kılı saç ekimi yöntemi ile vücudun sırt ve göğüs gibi 
            farklı bölgelerinden alınan kökler baş bölgesine nakledilebilir. Ense 
            bölgesinde yeterli saç olmaması durumunda vücudun farklı bölgelerinden 
            de kıl kökleri alınarak işlem gerçekleştirilebilir.
            """,
            meta={"kategori": "yontem", "source": "smilehairclinic.com", "tags": ["vücut_kılı", "alternatif_donör"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi düzeltme cerrahisi nedir?
            Cevap: Saç ekimi düzeltme cerrahisi (revizyon cerrahisi), başarısız olan 
            saç ekimi işlemlerini düzeltme işlemidir. Yanlış açı ile ekilmiş, yapay 
            görünümlü saç çizgileri, fırça gibi görünen saçlar düzeltilebilir. Bunun 
            için yeterli donör bölgenin kalmış olması gereklidir. İki yol vardır: 
            ya saç çizgisi biraz aşağıya alınarak yeni ve doğal bir saç çizgisi 
            oluşturulur, ya da problemli saç kökleri elektroliz cihazı ile alınır.
            """,
            meta={"kategori": "düzeltme", "source": "smilehairclinic.com", "tags": ["revizyon", "düzeltme", "başarısız"]}
        ),
        
        Document(
            content="""
            Soru: Saç ekimi operasyonunun aşamaları nelerdir?
            Cevap: Saç ekimi operasyonunun üç safhası vardır: 
            1. Köklerin (greftlerin) donör alandan alınması/toplanması
            2. İnsizyonların/kanalların açılması  
            3. Ekim işlemi
            Hastanın ihtiyacına göre greft toplama ve insizyonların sırası değişebilir. 
            Operasyon toplam olarak 6-8 saat sürmektedir. En önemli aşama kanal açılma 
            noktasıdır çünkü bu doğal görünümü yaratır.
            """,
            meta={"kategori": "operasyon", "source": "smilehairclinic.com", "tags": ["aşamalar", "süreç", "kanal_açma"]}
        ),
        
        Document(
            content="""
            Soru: Masaj saç çıkışını hızlandırır mı?
            Cevap: Evet, 2-6 ay arası masaj yaparak kan akımının hızlandırılması 
            saç ekiminden sonra yeni saçların uzamasına ve donör alanın kendisini 
            daha çabuk toparlamasına pozitif etkisi olmaktadır. Başa hafifçe masaj 
            yapılması önerilir.
            """,
            meta={"kategori": "bakım", "source": "smilehairclinic.com", "tags": ["masaj", "kan_akımı", "hızlandırma"]}
        ),
        
        Document(
            content="""
            Soru: Farklı bölgelerde saç çıkışı farklı mı olur?
            Cevap: Evet, saç ekimi yapılan bölgeye göre saçların uzamasında farklılıklar 
            görülür. Ön bölgelere yapılan ekimlerde sonuçlar tepe bölgesine yapılan 
            ekimlere göre daha erken sonuç vermektedir. Ön kısımda ekimden sonra uzayan 
            saç miktarı yaklaşık %80-90 iken tepe (vertex) bölgesinde bu oran %60-70'lere 
            düşmektedir.
            """,
            meta={"kategori": "sonuç", "source": "smilehairclinic.com", "tags": ["bölgesel_fark", "ön_bölge", "tepe"]}
        ),
    ]
    
    return documents

# Test için
if __name__ == "__main__":
    docs = create_hair_transplant_dataset()
    print(f"✅ Toplam {len(docs)} doküman oluşturuldu")
    print(f"\nİlk doküman örneği:")
    print(docs[0].content[:200] + "...")