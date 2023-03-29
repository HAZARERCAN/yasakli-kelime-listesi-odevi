yasakli_kelime_liste= ["karpuz", "kavun"]
paragraf: str = input("paragraf yazınız: ").lower()

for i in yasakli_kelime_liste:
    if i in paragraf:
        paragraf = paragraf.replace(i, len(i) * "*")

print(paragraf)









