# OYUN PROJESİ
## ARABA YARIŞI
Python programlama dili ve Pygame kütüphanesi kullanılarak geliştirilmiş bir 2
boyutlu sonsuz yarış oyunudur. Oyunun temel amacı, oyuncunun kontrol ettiği arabanın ekrandaki diğer araçlara çarpmadan mümkün
olduğunca uzun süre ilerlemesini sağlamaktır. Oyuncu ilerledikçe skor artar, oyun zorlaşır ve seviye ilerler.
### Hedefler ve Amaç
- Python ile temel oyun motoru mantığını kavratmak.
- Pygame kütüphanesini etkin şekilde kullanarak sahne yönetimi, kullanıcı girişi, nesne çarpışmaları ve
skor takibi gibi fonksiyonları entegre etmek.
- Görsel zenginlik ve kullanıcı dostu arayüz ile eğlenceli bir deneyim sunmak.
  
#### Oyuncu Aracı:
- Oyuncunun kontrol ettiği araba ekranın alt kısmında sabit bir başlangıç konumuna sahiptir.
- Yön tuşları (← ve →) kullanılarak sağa veya sola hareket ettirilir.
- Oyuncu sadece yatay eksende hareket edebilir.
  
 #### Rakip Araçlar:
- Üst kısımdan rastgele pozisyonlarda aşağı doğru hareket eden araçlardır.
- Her biri sabit hızla aşağı iner.
- Oyuncu bir rahip araca çarptığında bir can kaybeder.

#### Skor ve Seviye:
- Oyuncu her rakipten kaçtığında skor artar.
- Belirli skor aralıklarında (örneğin her 10 puan) seviye atlanır.
- Seviye arttıkça düşman araçların sayısı ve hızları artarak oyunun zorluk seviyesi yükselir.

#### Can Sistemi:
- Oyuncunun başlangıçta 3 canı bulunur.
- Her çarpışma bir can eksiltir.
- Canlar sıfırlandığında oyun sona erer ve oyun sonu ekranı görüntülenir.

#### Kullandığım Teknolojiler ve Kütüphaneler
Python - Projenin ana programlama dili olarak kullandım. 
Pygame - 2D grafikler, olay yönetimi, zamanlayıcı, ses ve kullanıcı girişi için
Sys - Uygulama çıkışı ve sistemle etkileşimler için
Random - Düşman araçların rastgele konumlandırılması
Pygame.time.Clock Oyun döngüsünün kare hızını (FPS) kontrol etmek için 

#### Yazılım Mimarisi
- Oyun Döngüsü: Sonsuz bir `while` döngüsü ile oluşturulmuştur. Her döngüde ekran temizlenir, nesneler
güncellenir ve yeniden çizilir.
- Sprite Yönetimi: Oyuncu ve düşman araçlar `pygame.Rect` yapılarıyla temsil edilmekte, her birinin
pozisyonu ve boyutu tanımlanmıştır.
- Çarpışma Algoritması: `colliderect()` fonksiyonu ile düşman araç ile oyuncu arasında temas kontrolü
sağlanır.
-Skor ve Seviye Yönetimi:Her kaçınılan düşman için skor artar, skor belirli değerlere ulaştığında seviye
artar ve düşmanlar hızlanır.
- Oyun Sonu: Canlar sıfırlandığında döngüden çıkılır ve final ekranı kullanıcıya gösterilir.

  HATİCE ÇEVİK
  23253060
