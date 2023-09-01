# Vizyoner Genç Web Projesi
## Projeyi çalıştırmak
Projeyi çalıştırmak için projenin dosyalarını indirmek gerekmektedir.  
+ [Proje Backend](https://github.com/DogukanEsen/Vizyoner_Backend)
+ [Proje Frontend](https://github.com/DogukanEsen/Vizyoner_Frontend)
+ [Proje Yapay Zeka](https://github.com/emineygt/Vizyoner_ai)  
Bu dosyaları indirdikten sonra postgresql' de vg_db isimli bir veritabanı oluşturulması gerekmektedir. Bu sayede veritabanına migration ile tablolar eklenecektir. Ardından dosyalar çalıştırılarak proje çalışmaktadır. Proje ilk çalıştırıldığında örnek veriler eklenecektir. 
## Proje Özellikleri
Projede 2 tip kullanıcı bulunmaktadır. Normal kullanıcılar ilgili ilanlara başvurabilir, profillerini güncelleyebilir. Kurumsal kullanıcılar ise firma bilgilerini güncelleyebilir ve ilan oluşturabilir. Dışarıdan gelen kişiler her iki tarafa da kayıt olabilir. Dışarıdan gelen kullanıcılar giriş yapmadan firmaları ve ilanları görüntüleyebilir. Projenin bir diğer özelliği ise normal kullanıcıların başvurduğu ilanların türüne ve o ilana başvuran kişilerin başvurdukları ilanlara göre ilan öneri sistemidir. 

## AI
AI geliştirmesi için Python ve Django Rest Framework kullanıldı. İlan öneri sistemi için Collaborative Filtering ve Content-Based Filtering tekniklerini birleştiren bir hibrit model geliştirildi. Bu model üç farklı algoritmayı kullanıyor:
İçerik tabanlı öneri: Bu algoritma, kullanıcının profil bilgileri ve yetenekleri üzerinden ilanlarını önerir. Kullanıcının ilgi alanlarına dayalı olarak TF-IDF (Term Frequency-Inverse Document Frequency) kullanılır.
Geçmiş Başvurulara Dayalı Öneri: Bu algoritma, kullanıcının geçmiş başvurularına benzeyen ilanları önerir. 
Benzer Profillere Dayalı Öneri: Bu algoritma, kullanıcıya benzer profil sahibi diğer kullanıcıların başvurduğu ilanları önerir. Kullanıcının profil bilgileri benzer kullanıcı profillerini belirlemek için kullanılır.

