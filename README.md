## Uygulama ne yapar
- String formatında verilen text'e bakar tersten yazılmış kelimeleri düzeltir ve parantez içindeki düzgün kelimeleri parantezden çıkartır. Tüm text'i sıralı bir şekilde geri döndürür.
- En kısa yazılması şeklinde ekstra puan alınacağından tek satırlık bir kod yazılmıştır.

## Çalıştırma
- main.py'nin bulunduğu dizinde terminale "python3 main.py" komutu yazılarak çalıştırılır

## Örnek Kullanım
```python
# Verilen metin
input_text = "nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon ,tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif (American) srohtua (to) emoceb (an) lanoitanretni ytirbelec (and) nrae a egral enutrof (from) ).gnitirw"

# Doğru cevap
correct_answer = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

print(reverse_text(input_text) == correct_answer) # Çıktı True
print(reverse_text(input_text))