def solution(bandage, health, attacks):
    time=0
    current_health=health
    for att in attacks:
        heal_time=att[0]-time-1
        if heal_time%bandage[0]==0:
            heal=heal_time/bandage[0]*bandage[2]+heal_time*bandage[1]
        else:
            heal=int(heal_time/bandage[0])*bandage[2]+heal_time*bandage[1]
        if current_health+heal<health:
            current_health+=heal
        else:
            current_health=health
        current_health-=att[1]
        time=att[0]
        if current_health<=0:
            return -1
    return current_health