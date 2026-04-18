hero_names = ["Layla", "Tigreal", "Gusion", "Kagura", "Chou"]
hero_roles = ["Marksman", "Tank", "Assassin", "Mage", "Fighter"]


ign = input("In-game name (IGN): ")
rank = input("Current rank: ")


print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")
for i in range(len(hero_names)):
    print(f" {i+1}. {hero_names[i]:<10} [{hero_roles[i]}]")
print("==========================================")

matches = []
wins = 0
losses = 0

for match_num in range(1, 5):
    print(f"\n--- MATCH {match_num} ---")
    
    hero_num = int(input("Hero number (0 to skip): "))
    
    if hero_num == 0:
        continue
    
    if 1 <= hero_num <= 5:
        kills = int(input("Kills: "))
        deaths = int(input("Deaths: "))
        assists = int(input("Assists: "))
        result = input("Result (W/L): ").upper()
        
        if deaths == 0:
            kda = (kills + assists) / 1
        else:
            kda = (kills + assists) / deaths
        
        if kda >= 5 and result == 'W':
            tag = "DOMINATION!"
        elif kda >= 5 and result == 'L':
            tag = "Carried Hard"
        elif kda < 5 and result == 'W':
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"
        
        if result == 'W':
            wins += 1
        elif result == 'L':
            losses += 1

        matches.append({
            "hero": hero_names[hero_num - 1],
            "kda": kda,
            "result": result,
            "tag": tag
        })

matches_played = len(matches)

if matches_played > 0:
    win_rate = int((wins / matches_played) * 100)
else:
    win_rate = 0

best_match_index = -1
highest_kda = -1

for i in range(len(matches)):
    if matches[i]["kda"] > highest_kda:
        highest_kda = matches[i]["kda"]
        best_match_index = i

print("\n=============================================")
print(f"     {ign} -- MATCH LOG ({rank})")
print("=============================================")

for i in range(len(matches)):
    hero = matches[i]["hero"]
    kda = matches[i]["kda"]
    result = "WIN" if matches[i]["result"] == 'W' else "LOSS"
    tag = matches[i]["tag"]
    
    print(f"[{i+1}] {hero:<11} | KDA: {kda:.2f} | {result:<4} | {tag}")

print("---------------------------------------------")
print(f"Matches Played : {matches_played}")
print(f"Wins : {wins}  |  Losses : {losses}")
print(f"Win Rate       : {win_rate}%")

if best_match_index != -1:
    best = matches[best_match_index]
    print(f"Best Match     : [{best_match_index+1}] {best['hero']}  (KDA: {best['kda']:.2f})")

print("=============================================")
