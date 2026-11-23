---
name: item-allocation
description: Use when creating, auditing, or reworking Mount & Blade Floris Expanded faction troop trees; assigning armor, weapons, shields, helmets, boots, mounts, or gauntlets; or checking avatar uniqueness and noble/commoner branch rules.
---

# Master Guidelines for Troop Item Allocation
This document outlines the standardized protocols, visual constraints, and item distribution matrices used for faction troop tree reworks in the Floris Expanded Mod Pack. 

---

## 🎨 1. The Visual Tree Uniqueness Rule (Avatar Matching)

### Mechanic:
Mount & Blade's UI presentation engine renders a troop's visual card avatar in the Faction Troop Tree menu by scanning their inventory list and reading the **first item** matching the `itp_type_body_armor` classification.

### Visual Rules:
1. **Uniqueness:** No two troops within the same faction tree may share the same first-listed body armor in their inventory lists. This guarantees 100% visual distinctiveness in the UI.
2. **Expansion:** When expanding a troop's body armor pool, additional assets must always be appended **after** the first listed armor to protect their tree card presentation.
3. **Visual Progression:** Distribute distinct alternative armor variants (textures, colors, patterns) as the primary avatar across different sub-branches to present a clear hierarchy.

---

## 🏛️ 2. Social Tree Division: Noble vs. Commoners Branches

To preserve faction lore, upgrade progression, and visual clarity, all troop trees are strictly partitioned into a prestigious **Noble** branch and standard **Commoner** branches. Non-colored/neutral items can be used for any troop if they suffer from low item variety.

### A. The Noble Branch
* **Branch Mechanics:** Starts strictly at **Tier 3** and progresses linearly up to Tier 7. Critically, **no Tier 2 troop is upgradable to it**; noble recruits are acquired solely through unique faction recruitment or prisoner rescue.
* **Noble Visual Identity & Faction Colors:** Uses highly specific, unified armor/shield/helmet colors denoting high lineage and prestige. These specific colors must be used predominantly (aim for 2–3 variants of this color theme per troop):
  * **Nord:** Blue / Green
  * **Swadia:** Red / Black / Yellow
  * **Rhodok:** Green / Blue
  * **Khergit:** Purple / Red
  * **Vaegir:** White / Grey / Black
  * **Sarranid:** Orange / Yellow / Red

### B. The Commoner Branches
* **Branch Mechanics:** Covers the rest of the faction tree, beginning at **Tier 1** and scaling through various standard branches (Infantry, Archery, Light Cavalry) up to Tier 5 or Tier 6.
* **Color Guidelines:**
  * **Tier 1 & Tier 2:** Can use all colors (including noble ones) to allow early variety.
  * **Tier 3 and above:** Must use other colored items, avoiding the specific premium faction colors reserved for the Noble branch.

### C. Item Type Consistency
Maintain clear equipment class lines across different sub-branches of the same tier to give units instant battlefield readability.
* **Do Not Mix Armor Types:** Do not mix different types of armor (e.g., leather coats, mail shirts, lamellars, or plates) within a single troop's inventory pool.
* **Variety Exception:** Mixing different armor types is allowed only if there is a severe lack of visual variety otherwise.
* Keep shields, helmets, and boots within the same armor tier weight class where possible.

---

## 📦 3. Global Item & Weapon Distribution Guidelines

Standardized item tiers, gauntlets, and weapon valuations are calibrated directly from the global **Floris Balance & Distribution Guidelines**:

### A. Armor, Boots, Helmets, and Mounts
Armor and mount tiers are generally determined by the troop's tier and combat class:

| Troop Class | Armor Tier | Boots & Helmets | Mounts |
| :--- | :--- | :--- | :--- |
| **Cavalry** | Same as Troop Tier (e.g., T5 Cavalry = T5 Armor) | Same as Armor Tier | Same as Troop Tier (e.g., T5 Cavalry = T5 Mount) |
| **Infantry** | Troop Tier - 1 (e.g., T5 Infantry = T4 Armor) | Same as Armor Tier | None |
| **Archers** | Troop Tier - 2 (e.g., T5 Archer = T3 Armor) | Same as Armor Tier | None (Unless Horse Archer, then same as Cavalry) |

### B. Gauntlets Distribution
Normalized to Tier 5 units as the baseline for hand protection:

| Troop Class | T2 | T3 | T4 | T5 | T6+ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Cavalry** | T2 | T4 | T5 | T6 | T6+ |
| **Infantry** | None | T2 | T4 | T5 | T6 |
| **Horse Archers** | None | None | T2 | T4 | T5/T6 |
| **Archers** | None | None | None | T2 | T2 (T7 = T4) |

### C. Weapon & Ammo Progression
* **Bows:** 6 distinct bow types progressing linearly from T2 up to T7.
* **Arrows:** $+1$ damage bonus for T2–T4 archers, $+2$ damage bonus for T5–T7 archers.
* **Swords:** Value-based distribution calibrated by unit tier:
  * **T1:** 50
  * **T2:** 100–150
  * **T3:** 200
  * **T4:** 300
  * **T5:** 400
  * **T6:** 500
  * **T7:** 600

### D. Asset Auditing (Armor & Weapons)
When overhauling a tree, perform a full audit of both the faction's armor and weapon sets to look for:
1. **Underutilized Armor & Shield Variants:** Find colored or patterned armor/shields of the same tier that are unused or duplicated in the code. (Note: Exotic colors like gold and copper are regarded as simple ones, similar to yellow and orange).
2. **Underutilized Weapon Variants:** Ensure tier-appropriate sword models, axes, maces, or polearms are assigned to give each combat line unique tactical and visual flavors.
