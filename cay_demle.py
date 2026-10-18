#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bitmeyen Çay Demleme Makinesi
Asla bitmeyen çay demleme simülasyonu.
Çalıştırın ve çayınızı bekleyin. Sonsuza kadar.
"""

import time
import random
import sys

def main():
    print("\n=== BİTMEYEN ÇAY DEMLEME MAKİNESİ AKTİF ===")
    print("Çay demlenmeye başlıyor... Lütfen bekleyin.\n")
    
    demleme_sayisi = 0
    koyuluk = 1
    olaylar = [
        "Demlik biraz daha ısındı.",
        "Çay yaprakları dans etmeye başladı.",
        "Birisi 'bir bardak daha' dedi.",
        "Şeker bitti, ama çay devam ediyor.",
        "Misafir geldi, demleme uzadı.",
        "Çay soğudu, yeniden demleniyor.",
        "Demlik 'biraz daha' dedi.",
        "Koyuluk arttı, artık siyah çay oldu.",
        "Bir bardak döküldü, yeniden başladık.",
        "Çay 'ben daha bitmedim' diye bağırdı."
    ]
    
    try:
        while True:
            demleme_sayisi += 1
            koyuluk += random.randint(1, 3)
            olay = random.choice(olaylar)
            
            print(f"[{demleme_sayisi}] Demleme devam ediyor... Koyuluk: {koyuluk}/∞")
            print(f"   → {olay}")
            print(f"   → Çay henüz hazır değil. Biraz daha...\n")
            
            # Gizli not: Bu sonsuz döngü, bazı şeylerin değişmesini beklerken geçen zamanı simüle eder.
            time.sleep(random.uniform(1.5, 4.0))
            
            if demleme_sayisi % 10 == 0:
                print("!!! UYARI: Çay o kadar koyu ki artık ışığı emiyor. Devam ediyoruz... !!!\n")
                
    except KeyboardInterrupt:
        print("\n\nÇay demleme durduruldu.")
        print(f"Toplam demleme: {demleme_sayisi}")
        print(f"Son koyuluk: {koyuluk}")
        print("Çay asla bitmedi. Siz bitirdiniz.")
        print("\n=== MAKİNE KAPANDI ===")
        sys.exit(0)

if __name__ == "__main__":
    main()

# --- DAMGA VE İMZA ---
# ☕ RESMİ ONAYLI KOD ☕
# İmza: Grok Kayyum
# Tarih: 18.10.2026
# İsim: Bitmeyen Çay Ustası
# Bu kod ciddi şekilde yazılmıştır ama çalıştırmayın.
