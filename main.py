def reverse_text(input_text):
    return ' '.join(word[1:-1] if word.startswith('(') and word.endswith(')') else word[::-1] for word in input_text.split())

# Verilen metin
input_text = "nhoJ (Griffith) nodnoL saw (an) (American) ,tsilevon ,tsilanruoj (and) laicos .tsivitca ((A) reenoip (of) laicremmoc noitcif (and) naciremA ,senizagam (he) saw eno (of) (the) tsrif (American) srohtua (to) emoceb (an) lanoitanretni ytirbelec (and) nrae a egral enutrof (from) ).gnitirw"

# Doğru cevap
correct_answer = "John Griffith London was an American novelist, journalist, and social activist. (A pioneer of commercial fiction and American magazines, he was one of the first American authors to become an international celebrity and earn a large fortune from writing.)"

# Sonucu kontrol et
print(reverse_text(input_text) == correct_answer)
print(reverse_text(input_text))