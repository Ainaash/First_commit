kun=["Ду","Ше","Ша","Жу","Иш","Же",]
apta={kun[s]: s for s in range (len(kun))}
apta1={d: kun.index(d) for d in kun}
print(apta)
print(apta1)
q={k:k**2 for k in range(1,11) if k%2!=0}
print(q)