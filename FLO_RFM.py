###############################################################
# RFM ile Müşteri Segmentasyonu (Customer Segmentation with RFM)
###############################################################

###############################################################
# İş Problemi (Business Problem)
###############################################################
# FLO müşterilerini segmentlere ayırıp bu segmentlere göre pazarlama stratejileri belirlemek istiyor.
# Buna yönelik olarak müşterilerin davranışları tanımlanacak ve bu davranış öbeklenmelerine göre gruplar oluşturulacak..

###############################################################
# Veri Seti Hikayesi
###############################################################

# Veri seti son alışverişlerini 2020 - 2021 yıllarında OmniChannel(hem online hem offline alışveriş yapan) olarak yapan müşterilerin geçmiş alışveriş davranışlarından
# elde edilen bilgilerden oluşmaktadır.

# master_id: Eşsiz müşteri numarası
# order_channel : Alışveriş yapılan platforma ait hangi kanalın kullanıldığı (Android, ios, Desktop, Mobile, Offline)
# last_order_channel : En son alışverişin yapıldığı kanal
# first_order_date : Müşterinin yaptığı ilk alışveriş tarihi
# last_order_date : Müşterinin yaptığı son alışveriş tarihi
# last_order_date_online : Muşterinin online platformda yaptığı son alışveriş tarihi
# last_order_date_offline : Muşterinin offline platformda yaptığı son alışveriş tarihi
# order_num_total_ever_online : Müşterinin online platformda yaptığı toplam alışveriş sayısı
# order_num_total_ever_offline : Müşterinin offline'da yaptığı toplam alışveriş sayısı
# customer_value_total_ever_offline : Müşterinin offline alışverişlerinde ödediği toplam ücret
# customer_value_total_ever_online : Müşterinin online alışverişlerinde ödediği toplam ücret
# interested_in_categories_12 : Müşterinin son 12 ayda alışveriş yaptığı kategorilerin listesi

###############################################################
# GÖREVLER
###############################################################

# GÖREV 1: Veriyi Anlama (Data Understanding) ve Hazırlama
           # 1. flo_data_20K.csv verisini okuyunuz.
import datetime as dt
from datetime import timedelta
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
df_ = pd.read_csv("/Users/sinemdokmeci/PycharmProjects/CRM_Analitigi/case/case_study_1/flo_data_20k.csv")
df = df_.copy()
df.head()
df.shape

           # 2. Veri setinde
                     # a. İlk 10 gözlem,
df.head(10)
                     # b. Değişken isimleri,
print(df.columns)
                     # c. Betimsel istatistik,
df.describe()
                     # d. Boş değer,
df.isnull().sum()
                     # e. Değişken tipleri, incelemesi yapınız
print(df.dtypes)



           # 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir. Herbir müşterinin toplam
           # alışveriş sayısı ve harcaması için yeni değişkenler oluşturun.
df['total_orders'] = df['order_num_total_ever_online'] + df['order_num_total_ever_offline']
df['total_spent'] = df['customer_value_total_ever_online'] + df['customer_value_total_ever_offline']
           # 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.
print(df.dtypes)
date_columns = [
    'first_order_date',
    'last_order_date',
    'last_order_date_online',
    'last_order_date_offline'
]

for col in date_columns:
    df[col] = pd.to_datetime(df[col])
           # 5. Alışveriş kanallarındaki müşteri sayısının, ortalama alınan ürün sayısının ve ortalama harcamaların dağılımına bakınız.
df.groupby("order_channel").agg({"master_id": "nunique",
                                 "order_num_total_ever_online": "mean",
                                 "customer_value_total_ever_online": "mean"
                                 })
           # 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.
df.sort_values(by='total_spent', ascending=False).head(10)
           # 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.
df.sort_values(by='total_orders', ascending=False).head(10)
           # 8. Veri ön hazırlık sürecini fonksiyonlaştırınız
def preprocess_data(dataframe):

    dataframe.head()
    dataframe.head(10)
    dataframe.shape
    print(dataframe.columns)
    dataframe.describe()
    dataframe.isnull().sum()
    print(dataframe.dtypes)
    dataframe['total_orders'] = dataframe['order_num_total_ever_online'] + dataframe['order_num_total_ever_offline']
    dataframe['total_spent'] = dataframe['customer_value_total_ever_online'] + dataframe['customer_value_total_ever_offline']
    print(dataframe.dtypes)
    date_columns = [
        'first_order_date',
        'last_order_date',
        'last_order_date_online',
        'last_order_date_offline'
    ]
    for col in date_columns:
        dataframe[col] = pd.to_datetime(dataframe[col])
    dataframe.groupby("order_channel").agg({"master_id": "nunique",
                                     "order_num_total_ever_online": "mean",
                                     "customer_value_total_ever_online": "mean"
                                     })
    dataframe.sort_values(by='total_spent', ascending=False).head(10)
    dataframe.sort_values(by='total_orders', ascending=False).head(10)
    return dataframe
df_new = preprocess_data(df)
# GÖREV 2: RFM Metriklerinin Hesaplanması
df.head()
# günü yazma
today_date = df["last_order_date"].max() + timedelta(days=2)
type(today_date)
# Recency, Frequency, Monetary bulma
rfm = df.groupby('master_id').agg({'last_order_date': lambda last_order_date: (today_date - last_order_date.max()).days,
                                     'total_orders': 'sum',
                                     'total_spent': 'sum'})
#2.çözüm
rfm["recency"] = (today_date - df["last_order_date"]).astype('timedelta64[ns]').dt.days
rfm["frequency"] = df["order_num_total"]
rfm["monetary"] = df["customer_value_total"]
rfm.head()
rfm.columns = ['recency', 'frequency', 'monetary'] #isimleri değiştir
rfm.describe().T #betimleme
rfm = rfm[rfm["monetary"] > 0] #monatary değişken 0 olduğu için bunu değiştiriyoruz
rfm.shape

# GÖREV 3: RF ve RFM Skorlarının Hesaplanması
rfm["recency_score"] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
rfm["frequency_score"] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
rfm["monetary_score"] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])
#RFM Skore değişkeni hesaaplarız R ve F ile yapılır
rfm["RFM_SCORE"] = (rfm['recency_score'].astype(str) +
                    rfm['frequency_score'].astype(str))
rfm.describe().T
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
seg_map = {
    r'[1-2][1-2]': 'hibernating', #Uyuyan Müşteriler
    r'[1-2][3-4]': 'at_Risk', #Risk Altındaki Müşteriler
    r'[1-2]5': 'cant_loose', #Kaybedilmemesi Gereken Müşteriler
    r'3[1-2]': 'about_to_sleep', #Uyumaya Yakın Müşteriler
    r'33': 'need_attention', #İlgiye İhtiyacı Olan Müşteriler
    r'[3-4][4-5]': 'loyal_customers', #Sadık Müşteriler
    r'41': 'promising', #Gelecek Vaadeden Müşteriler
    r'51': 'new_customers', #Yeni Müşteriler
    r'[4-5][2-3]': 'potential_loyalists', #Potansiyel Sadık Müşteriler
    r'5[4-5]': 'champions' #Şampiyon Müşteriler
}
#skorları birleştirme isimlendirme
rfm['segment'] = rfm['RFM_SCORE'].replace(seg_map, regex=True)
#sınıfları yani segmentleri incelemek için
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean", "count"])
#kaybedilmemesi gereken müşteri segmentini görüntüleme
rfm[rfm["segment"] == "cant_loose"].head()
# Bu kişilerin index bilgisi yani ıd bilgisi
rfm[rfm["segment"] == "cant_loose"].index
# belirli bir segmenti ilgili formata çevirerek atmak için
new_df = pd.DataFrame()
new_df["new_customer_id"] = rfm[rfm["segment"] == "new_customers"].index
new_df["new_customer_id"] = new_df["new_customer_id"].astype(int)
new_df.to_csv("new_customers.csv")
rfm.to_csv("rfm.csv")

# GÖREV 5: Aksiyon zamanı!
           # 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.
rfm[["segment", "recency", "frequency", "monetary"]].groupby("segment").agg(["mean"])
           # 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulun ve müşteri id'lerini csv ye kaydediniz.
                   # a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
                   # tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Sadık müşterilerinden(champions,loyal_customers),
                   # ortalama 250 TL üzeri ve kadın kategorisinden alışveriş yapan kişiler özel olarak iletişim kuralacak müşteriler. Bu müşterilerin id numaralarını csv dosyasına
                   # yeni_marka_hedef_müşteri_id.cvs olarak kaydediniz.

new_df = df.merge(rfm, left_on='master_id', right_index=True)
target_customers = new_df[
    (new_df["segment"].isin(["champions", "loyal_customers"])) &
    (new_df["total_spent"] > 250) &
    (new_df["interested_in_categories_12"] == "KADIN")
]
#df["segment"]str.contains("champions | loyal_customers")
print(target_customers.head())
target_customers_ids = target_customers[["master_id"]]
target_customers_ids.to_csv("yeni_marka_hedef_musteri_id.csv", index=False)

                   # b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşteri olan ama uzun süredir
                   # alışveriş yapmayan kaybedilmemesi gereken müşteriler, uykuda olanlar ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
                   # olarak kaydediniz.


# GÖREV 6: Tüm süreci fonksiyonlaştırınız.

###############################################################
# GÖREV 1: Veriyi  Hazırlama ve Anlama (Data Understanding)
###############################################################


# 2. Veri setinde
        # a. İlk 10 gözlem,
        # b. Değişken isimleri,
        # c. Boyut,
        # d. Betimsel istatistik,
        # e. Boş değer,
        # f. Değişken tipleri, incelemesi yapınız.



# 3. Omnichannel müşterilerin hem online'dan hemde offline platformlardan alışveriş yaptığını ifade etmektedir.
# Herbir müşterinin toplam alışveriş sayısı ve harcaması için yeni değişkenler oluşturunuz.



# 4. Değişken tiplerini inceleyiniz. Tarih ifade eden değişkenlerin tipini date'e çeviriniz.


# df["last_order_date"] = df["last_order_date"].apply(pd.to_datetime)



# 5. Alışveriş kanallarındaki müşteri sayısının, toplam alınan ürün sayısı ve toplam harcamaların dağılımına bakınız.



# 6. En fazla kazancı getiren ilk 10 müşteriyi sıralayınız.




# 7. En fazla siparişi veren ilk 10 müşteriyi sıralayınız.




# 8. Veri ön hazırlık sürecini fonksiyonlaştırınız.


###############################################################
# GÖREV 2: RFM Metriklerinin Hesaplanması
###############################################################

# Veri setindeki en son alışverişin yapıldığı tarihten 2 gün sonrasını analiz tarihi



# customer_id, recency, frequnecy ve monetary değerlerinin yer aldığı yeni bir rfm dataframe


###############################################################
# GÖREV 3: RF ve RFM Skorlarının Hesaplanması (Calculating RF and RFM Scores)
###############################################################

#  Recency, Frequency ve Monetary metriklerini qcut yardımı ile 1-5 arasında skorlara çevrilmesi ve
# Bu skorları recency_score, frequency_score ve monetary_score olarak kaydedilmesi




# recency_score ve frequency_score’u tek bir değişken olarak ifade edilmesi ve RF_SCORE olarak kaydedilmesi


###############################################################
# GÖREV 4: RF Skorlarının Segment Olarak Tanımlanması
###############################################################

# Oluşturulan RFM skorların daha açıklanabilir olması için segment tanımlama ve  tanımlanan seg_map yardımı ile RF_SCORE'u segmentlere çevirme


###############################################################
# GÖREV 5: Aksiyon zamanı!
###############################################################

# 1. Segmentlerin recency, frequnecy ve monetary ortalamalarını inceleyiniz.



# 2. RFM analizi yardımı ile 2 case için ilgili profildeki müşterileri bulunuz ve müşteri id'lerini csv ye kaydediniz.

# a. FLO bünyesine yeni bir kadın ayakkabı markası dahil ediyor. Dahil ettiği markanın ürün fiyatları genel müşteri tercihlerinin üstünde. Bu nedenle markanın
# tanıtımı ve ürün satışları için ilgilenecek profildeki müşterilerle özel olarak iletişime geçeilmek isteniliyor. Bu müşterilerin sadık  ve
# kadın kategorisinden alışveriş yapan kişiler olması planlandı. Müşterilerin id numaralarını csv dosyasına yeni_marka_hedef_müşteri_id.cvs
# olarak kaydediniz.



# b. Erkek ve Çoçuk ürünlerinde %40'a yakın indirim planlanmaktadır. Bu indirimle ilgili kategorilerle ilgilenen geçmişte iyi müşterilerden olan ama uzun süredir
# alışveriş yapmayan ve yeni gelen müşteriler özel olarak hedef alınmak isteniliyor. Uygun profildeki müşterilerin id'lerini csv dosyasına indirim_hedef_müşteri_ids.csv
# olarak kaydediniz.
