# FLO-Markas-in-RFM-ile-M-teri-Segmentasyonu-Projesi
FLO - RFM Analizi

# 1. İş Problemi (Business Problem)
FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..



# Veri Seti Hikayesi
Veri seti FLO markasının  son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
elde edilen bilgilerden oluşmaktadır.

# Veriseti Hakkında
master_id: Eşsiz müşteri numarası
order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
last_order_channel : En son alışverişin yapıldığı kanal
first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
last_order_date : Müşterinin yaptığı son alışveriş tarihi
last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi


# Projenin Aşamaları
Veriyi Anlama (Data Understanding) İlk aşamada, elimizdeki veriyi inceleyip anlayacağız. Müşterilere ait demografik bilgiler, alışveriş geçmişi ve harcamalar gibi verilerin ne anlama geldiğini analiz edeceğiz. Eksik veya tutarsız veriler olup olmadığını kontrol edeceğiz ve verinin genel yapısını gözden geçireceğiz.

# Veri Hazırlama (Data Preparation) 
Bu aşamada, veriyi analiz edilebilir hale getireceğiz. Eksik veya hatalı verileri temizleyeceğiz, aykırı değerleri düzelteceğiz. Gerekirse yeni öznitelikler oluşturacağız ve veriyi modelleme için uygun bir yapıya sokacağız. Ayrıca, veriyi RFM skorlaması için hazır hale getireceğiz.

# RFM Skorlarının Hesaplanması (Calculating RFM Scores)
RFM analizi yapabilmek için müşterilerin Recency (son alışveriş zamanı), Frequency (alışveriş sıklığı) ve Monetary (toplam harcama tutarı) skorlarını hesaplayacağız. Bu adımda, veriyi gruplandırarak her müşteriye bu üç metrik üzerinden puanlar vereceğiz. Skorları hesapladıktan sonra her müşteri belirli bir RFM değerine sahip olacak.

# RFM Segmentlerinin Oluşturulması ve Analiz Edilmesi (Creating & Analysing RFM Segments) 
Son olarak, RFM skorlarına göre müşterileri segmentlere ayıracağız. Örneğin, yüksek skor alanları "en değerli müşteriler" olarak belirleyeceğiz, düşük skor alanları ise "yeniden kazanılması gereken müşteriler" olarak sınıflandıracağız. Bu segmentleri analiz edip, her bir gruba yönelik pazarlama stratejileri ve aksiyon planları oluşturacağız.
