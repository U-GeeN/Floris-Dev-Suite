# Troop Skill Distribution Guidelines

Source: `Source/Source - Floris Expanded Mod Pack/Module/module_troops_part1.py` (the marked skills-distribution section).

These are balancing guidelines, not hard rules. Make exceptions where needed for balance; Nord troops are an existing example.

## Tier by level

| Tier | Unit level |
| :--: | :--------: |
|  T1  |   1–6    |
|  T2  |   7–12   |
|  T3  |  13–18   |
|  T4  |  19–24   |
|  T5  |  25–30   |
|  T6  |  31–36   |
|  T7  |  37–42   |

## Proficiencies

- Each level grants 15 proficiency points, distributed for the troop's role.
- Troops retain proficiencies and skills as they advance through their upgrade tree.
- All basic T1 troops start at level 4 with 40 points in every proficiency.
- Apply the faction baseline below, then add progression for levels gained. Cap the weapon increase at 8 points per level.

|    Faction    | 1H  | 2H  | Polearm | Bow | Crossbow | Throwing |
| :-----------: | :-: | :-: | :-----: | :-: | :------: | :------: |
|    Swadia     | +20 |     |   +30   | +10 |          |          |
|    Vaegir     | +10 |     |   +20   | +30 |          |          |
|    Khergit    | +20 | +10 |         | +30 |          |          |
|     Nord      | +10 | +30 |         |     |          |   +20    |
|    Rhodok     | +20 |     |   +10   |     |   +30    |          |
|   Sarranid    | +30 | +20 |   +10   |     |          |          |
|  Mercenaries  | +10 |     |   +30   |     |   +20    |          |
| Sword Sisters | +30 | +10 |         | +20 |          |          |

## Starting skills

Skill abbreviations: IF = Ironflesh, PS = Power Strike, PT = Power Throw, PD = Power Draw, SH = Shield, AL = Athletics, RD = Riding, HA = Horse Archery.

|    Faction    | IF | PS | PT | PD | SH | AL | RD | HA |
| :-----------: | -- | -- | -- | -- | -- | -- | -- | -- |
|    Swadia     |    | 2  | 1  |    | 1  |    |    |    |
|    Vaegir     |    | 1  |    | 2  |    |    |    | 1  |
|    Khergit    |    |    |    | 1  |    |    | 1  | 2  |
|     Nord      | 1  |    | 2  |    |    | 1  |    |    |
|    Rhodok     | 1  | 1  |    |    |    | 2  |    |    |
|   Sarranid    |    |    |    | 1  |    |    | 2  | 1  |
|  Mercenaries  | 2  |    |    |    | 1  | 1  |    |    |
| Sword Sisters |    |    |    | 1  | 2  |    | 1  |    |

## Skill increases by tier

At each tier, add all applicable bonuses from weapon, movement, and troop-type columns. T1 has no standard increase. Nord troops receive a T1 faction bonus of +1 Athletics and +1 Ironflesh.

| Tier 	| Melee |  Bow  | Crossbow | Throwing | Shield | No horse | Horse |       Cavalry       |   Infantry   | Archer | Horse archer | Nord
| :--:	| :---: | :---: | :------: | :------: | :----: | :------: | :---: | :-----------------: | :----------: | :----: | :----------: |
|  T1	|															       | +1 AL, +1 IF
|  T2  	| +1 PS | +1 PD |  +1 SH   |  +1 PT   | +1 IF  |  +1 AL   | +1 RD |    +1 AL, +1 SH     |    +1 PS     |  —     | +1 HA, +1 RD |
|  T3  	| +1 IF | +1 PD |  +1 IF   |  +1 PT   | +1 SH  |  +1 AL   | +1 RD | +1 RD, +1 IF, +1 PS | +1 IF, +1 SH |  —     | +1 HA, +1 AL |
|  T4  	| +1 PS | +1 PD |  +1 SH   |  +1 PT   | +1 IF  |  +1 AL   | +1 RD |    +1 AL, +1 SH     |    +1 PS     |  —     | +1 HA, +1 RD |
|  T5	| +1 IF | +1 PD |  +1 IF   |  +1 PT   | +1 SH  |  +1 AL   | +1 RD | +1 RD, +1 IF, +1 PS | +1 IF, +1 SH |  —     | +1 HA, +1 AL |
|  T6	| +1 PS | +1 PD |  +1 SH   |  +1 PT   | +1 IF  |  +1 AL   | +1 RD |    +1 AL, +1 SH     |    +1 PS     |  —     | +1 HA, +1 RD |
|  T7	| +1 IF | +1 PD |  +1 IF   |  +1 PT   | +1 SH  |  +1 AL   | +1 RD | +1 RD, +1 IF, +1 PS | +1 IF, +1 SH |  —     | +1 HA, +1 AL |

## Final-upgrade bonus

Apply the relevant final bonus in addition to the normal tier progression.

|    Condition    | Bonus |
| :-------------: | :---: |
|  Melee weapon   | +1 PS |
|       Bow       | +1 PD |
|    Crossbow     | +1 IF |
| Throwing weapon | +1 PT |
|     Shield      | +1 SH |
|    No horse     | +1 AL |
|      Horse      | +1 RD |
|     Cavalry     | +1 PS |
|    Infantry     | +1 PS |
|     Archer      | +1 HA |
|     Swadia      | +1 PD |
|     Vaegir      | +1 PD |
|     Khergit     | +1 HA |
|     Rhodok      | +1 SH |
|    Sarranid     | +1 PS |
|   Mercenaries   | +1 AL |
|  Sword Sisters  | +1 RD |

Nord troops have no listed final faction bonus.
