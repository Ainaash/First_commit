def show(первый, второй="Python", третий="Java"):
    print(f"[1] — {первый}")
    print(f"[2] — {второй}")
    print(f"[3] — {третий}")
    print("-"*13)

show("Alpha")
show("A","B","C")
show(10,20)
show(100, третий=300)

