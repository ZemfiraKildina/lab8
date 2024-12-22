def hp():
    hp =100

    def changes_hp(sum):
        nonlocal hp
        hp +=sum
        if hp>100:
            hp = 100 #max
        if hp<0:
            hp = 0 #min
        return hp
    return changes_hp

track_hp = hp()
print(track_hp(-50))