---
name: troop-tree-layout
description: Use this skill when generating, aligning, or debugging Mount & Blade Floris Expanded troop tree UI presentations, calculating X/Y troop coordinates, positioning upgrade cost labels, or drawing horizontal and vertical bridge lines.
---

This document defines the geometric and structural standards for generating and aligning troop tree presentations in the Floris Expanded Mod Pack.

## 1. Coordinate Constants (7-Tier Distribution)
To ensure even distribution across the screen, use a uniform **140-pixel gap** between tiers:
- **Tier 1**: 60
- **Tier 2**: 200
- **Tier 3**: 340
- **Tier 4**: 480
- **Tier 5**: 620
- **Tier 6**: 760
- **Tier 7**: 900

## 2. Alignment & Offsets
- **Portrait/Name**: Centered at (X, Y).
- **Standard Horizontal Rows (Y-Coordinates)**:
  The layout grid is comprised of exactly **7 standard rows** spaced at a uniform **89-pixel interval** around the central Row 4 origin:
  * **Row 7 (Max Upper)**: `Y = 609` (Only used in full 7-row trees)
  * **Row 6 (Upper)**: `Y = 520` (Max height for compact 5-row trees)
  * **Row 5 (Mid-Upper)**: `Y = 431`
  * **Row 4 (Center / Origin)**: `Y = 342` (Anchor point for Tier 1)
  * **Row 3 (Mid-Lower)**: `Y = 253`
  * **Row 2 (Lower)**: `Y = 164` (Standard noble baseline for compact 5-row trees)
  * **Row 1 (Min Lower)**: `Y = 75` (Noble baseline for full 7-row trees)
- **Row Selection & Layout Compactness**:
  * **Full 7-Row Trees** (e.g., Vaegirs, Rhodoks): Use all 7 rows from Row 1 (`75`) to Row 7 (`609`) to distribute complex vertical specialization lanes.
  * **Compact 5-Row Trees** (e.g., Nords): Restrict the entire layout strictly to **Row 2 (`164`) through Row 6 (`520`)**. Do NOT use Row 7 (`609`) or Row 1 (`75`) to ensure a compact, visually pleasing, and vertically symmetrical tree centered on Row 4 (`342`).
- **Upgrade Path**: All horizontal lines must be at **`Y + 40`** relative to the unit's center.
- **Upgrade Costs**: Positioned at **`Troop_X + 55, Troop_Y + 55`**. This places the cost exactly **15px above** the standard upgrade path.
  * **Dead End Rule**: Do **not** include upgrade costs for units that have no further upgrades.

## 3. Geometric Rules
- **Line Thickness**: 4.
- **Unit Exit**: Horizontal lines start at **`X + 23`**.
- **Unit Entry**: Horizontal lines end at **`X - 7`**.
- **Bridge Lengths**:
    - **Full Straight Bridge**: 108px.
    - **Split Exit (to midpoint)**: 54px (reaches X+77).
    - **Split Entry (from midpoint)**: 54px (reaches X2-7).

## 4. Path Ambiguity & Parallel Offsets
When paths converge or cross, use parallel entries to maintain visual separation. This rule is required whenever two upgrade statements have the same destination troop as a parameter, for example `upgrade(troops, "source_a", "target")` and `upgrade2(troops, "source_b", "other", "target")`.
- **Case A: Dual Half-Segment Entry** (e.g., Scout):
    - Position entries symmetrically at **`Y + 36`** and **`Y + 44`**.
- **Case B: Straight + Half-Segment Entry** (e.g., Vikingr):
    - Straight path remains at **`Y + 40`**.
    - Split path uses an **8px offset** based on source direction:
        - Source from **Above**: **`Y + 48`**.
        - Source from **Below (Noble)**: **`Y + 32`** (Negated Offset Rule to prevent crossing center line).

## 5. Branch Logic
- **Origin**: Build the commoner trunk from Row 4 (`342`) unless the tree needs a different center for symmetry.
- **Double Upgrades**: Each `upgrade2` creates a branch from its source row. Keep the first/common continuation on the source row when possible, then add the second branch one standard row away (`+89` or `-89`) in the direction that keeps the tree readable.
- **Branch Expansion**: Additional branch depth continues by adding standard rows from the origin or current branch row. Do not jump to arbitrary Y values.
- **Noble Branches**: Noble branches do not have fixed baselines. Place them under the lowest commoner branch currently used by that tree, then continue building them by the same standard-row rules.

## 6. Code Structure
1. Portrait/Name script.
2. Cost script (only if not a dead end).
3. Horizontal Line block (`##### - lines`).
4. Vertical Line block (`##### | lines`).
