import pandas as pd
import random

def generate_csv(file_path="data/cyber_logs.csv", row_count=50):
    data = []
    # Örnek IP havuzu
    ips = [f"192.168.1.{random.randint(10, 50)}" for _ in range(10)]
    
    for _ in range(row_count):
        # Normal veri üretimi
        ip = random.choice(ips)
        islem_sayisi = random.randint(1, 20)
        veri_boyutu = random.randint(100, 1500)
        
        # Arada bir 'Saldırı/Anomali' verisi ekleyelim (Modelin yakalaması için)
        if random.random() < 0.1: # %10 ihtimalle anomali
            islem_sayisi = random.randint(80, 200) # Çok yüksek işlem
            veri_boyutu = random.randint(5000, 10000) # Çok büyük veri transferi
            
        data.append([ip, islem_sayisi, veri_boyutu])

    df = pd.DataFrame(data, columns=['ip', 'islem_sayisi', 'veri_boyutu'])
    df.to_csv(file_path, index=False)
    print(f"✅ {file_path} başarıyla oluşturuldu!")

if __name__ == "__main__":
    import os
    if not os.path.exists('data'): os.makedirs('data')
    generate_csv()