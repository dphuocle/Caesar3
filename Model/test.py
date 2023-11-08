def recurl(tab):
    print(tab)
    if len(tab) > 6:
        return
    tab.append(1)
    recurl(tab)


recurl([])
