def solution(attack, recovery, hp):
    
    if recovery >= attack:
        print("attack value have to be larger than recovery value")
        return None
    
    monster_hp = hp
    attk_cnt = 0
    while True:
        if monster_hp <= 0: break
        monster_hp -= attack
        monster_hp += recovery
        attk_cnt += 1
        
    return attk_cnt

#TestCase Code
attack = 40
recovery = 20
hp = 60
ret = solution(attack,recovery,hp)

print("solution is ", ret,".")