---
name: floris-troop-balancer
description: Calculates weapon proficiencies and skill distributions for Mount & Blade: Warband (Floris Expanded) troops and outputs Module System tuple syntax.
---

# Skill: Floris Troop Stat & Skill Balancer

## Context & Scope
Use this skill whenever creating, modifying, or auditing troop entries in `module_troops_part1.py` (or related Module System troop files) for the Floris Expanded Mod Pack. 
*Note: These are balancing guidelines, not hard rules. Make minor exceptions where needed for gameplay balance (e.g., Nord troops).*

## Step-by-Step Calculation Rules

### Step 1: Determine Tier from Level
* **T1:** 1–6 | **T2:** 7–12 | **T3:** 13–18 | **T4:** 19–24 | **T5:** 25–30 | **T6:** 31–36 | **T7:** 37–42

### Step 2: Calculate Weapon Proficiencies
1. **Base:** Every troop starts at **Level 4** with **40** in all 6 proficiencies (`1H`, `2H`, `Polearm`, `Bow`, `Crossbow`, `Throwing`).
2. **Faction Baseline:** Add the faction's starting modifiers from Table A.
3. **Level Progression:** Calculate `(Target_Level - 4) * 15` to find total distributable points.
4. **Distribution Cap:** Assign points based on the troop's weapons/role. **Cap any single proficiency's level-up growth at +8 points per level gained** (`(Target_Level - 4) * 8`).
5. **Inheritance:** Troops must retain or exceed the proficiencies of the previous troop in their upgrade tree.

### Step 3: Calculate Skills
Start with the **Faction Starting Skills** (Table A), then cumulatively add every applicable bonus from **T1 up to the unit's current Tier** (Table B). If the troop is the final unit in its upgrade branch, add all matching **Final-Upgrade Bonuses** (Table C).

**Abbreviations:** `IF` = Ironflesh | `PS` = Power Strike | `PT` = Power Throw | `PD` = Power Draw | `SH` = Shield | `AL` = Athletics | `RD` = Riding | `HA` = Horse Archery

---

## Reference Tables

### Table A: Faction Baselines

| Faction | Proficiency Modifiers | Starting Skills |
| :--- | :--- | :--- |
| **Swadia** | 1H +20, Polearm +30, Bow +10 | PS 2, PT 1, SH 1 |
| **Vaegir** | 1H +10, Polearm +20, Bow +30 | PS 1, PD 2, HA 1 |
| **Khergit** | 1H +20, 2H +10, Bow +30 | PD 1, RD 1, HA 2 |
| **Nord** | 1H +10, 2H +30, Throwing +20 | IF 1, PT 2, AL 1 |
| **Rhodok** | 1H +20, Polearm +10, Crossbow +30 | IF 1, PS 1, AL 2 |
| **Sarranid** | 1H +30, 2H +20, Polearm +10 | PD 1, RD 2, HA 1 |
| **Mercenaries** | 1H +10, Polearm +30, Crossbow +20 | IF 2, SH 1, AL 1 |
| **Sword Sisters** | 1H +30, 2H +10, Bow +20 | PD 1, SH 2, RD 1 |

### Table B: Cumulative Tier Progression
*(Add every applicable tag from T1 up to the troop's Tier)*

| Tier | Weapon Tags | Mount Tags | Role Tags | Faction |
| :--- | :--- | :--- | :--- | :--- |
| **T1** | *None* | *None* | *None* | **Nord:** +1 AL, +1 IF |
| **T2, T4, T6** *(Even)* | **Melee:** +1 PS<br>**Bow:** +1 PD<br>**Crossbow:** +1 SH<br>**Throwing:** +1 PT<br>**Shield:** +1 IF | **No Horse:** +1 AL<br>**Horse:** +1 RD | **Cavalry:** +1 AL, +1 SH<br>**Infantry:** +1 PS<br>**Archer:** —<br>**Horse Archer:** +1 HA, +1 RD | *None* |
| **T3, T5, T7** *(Odd)* | **Melee:** +1 IF<br>**Bow:** +1 PD<br>**Crossbow:** +1 IF<br>**Throwing:** +1 PT<br>**Shield:** +1 SH | **No Horse:** +1 AL<br>**Horse:** +1 RD | **Cavalry:** +1 RD, +1 IF, +1 PS<br>**Infantry:** +1 IF, +1 SH<br>**Archer:** —<br>**Horse Archer:** +1 HA, +1 AL | *None* |

### Table C: Final-Upgrade Bonuses
*(Apply ONLY if the troop has no further upgrades. Stack all matching conditions)*
* **Weapon:** Melee (+1 PS) | Bow (+1 PD) | Crossbow (+1 IF) | Throwing (+1 PT) | Shield (+1 SH)
* **Mount:** No Horse (+1 AL) | Horse (+1 RD)
* **Role:** Cavalry (+1 PS) | Infantry (+1 PS) | Archer (+1 HA)
* **Faction:** Swadia (+1 PD) | Vaegir (+1 PD) | Khergit (+1 HA) | Rhodok (+1 SH) | Sarranid (+1 PS) | Mercenaries (+1 AL) | Sword Sisters (+1 RD) | Nord (*None*)

---

## Required Output Format
When generating or auditing a troop, provide:
1. **Calculation Breakdown:** Show Base + Progression for proficiencies and Starting + Tier + Final bonuses for skills.
2. **Module System Snippet:** Output valid Python syntax matching `module_troops_part1.py` conventions (e.g., `knows_power_strike_4 | knows_ironflesh_3...` and `wp_one_handed(...) | wp_polearm(...)`).
