#!/usr/bin/env python3
"""Ontario public corridor fire separation checker (OBC 2024, 3.3.1.4) + exit enclosure rating (3.4.4.1).
Usage:
  python3 corridor_checker.py --sprinklered no
  python3 corridor_checker.py --sprinklered yes --serves residential --travel-distance 30
  python3 corridor_checker.py --exit --floor-rating 60
--serves: protected = care / care and treatment / detention / residential (B-1, B-2, B-3, C);
          other = assembly, business, mercantile, industrial (A, D, E, F)
"""
import argparse
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sprinklered", choices=["yes", "no"], default="no")
    ap.add_argument("--serves", choices=["protected", "other"], default="other")
    ap.add_argument("--travel-distance", type=float, default=None, help="max travel distance to an exit, m")
    ap.add_argument("--exit", action="store_true", help="report the exit enclosure rule instead")
    ap.add_argument("--floor-rating", type=float, default=None, help="FRR required for the floor assembly above, minutes (for --exit)")
    a = ap.parse_args()
    if a.exit:
        if a.floor_rating is None:
            print("3.4.4.1: exit FRR = the FRR required by 3.2.2 for the floor assembly above the storey (or below if none), min 45 min, max 2 h.")
        else:
            r = min(max(a.floor_rating, 45), 120)
            print(f"Exit enclosure fire separation: {r:g} min FRR (floor assembly {a.floor_rating:g} min, clamped to the 45 min floor / 2 h cap of 3.4.4.1).")
        return
    if a.sprinklered == "no":
        print("Corridor: fire separation with FRR >= 45 min from the remainder of the storey. [3.3.1.4.(1), (2)]")
        return
    if a.serves == "protected":
        print("Corridor: fire separation with FRR >= 45 min. Sentence (3) no-rating relief does not apply to care / care and treatment / detention / residential occupancies. [3.3.1.4.(2), (3)]")
    else:
        print("Corridor: fire separation required, but NO fire-resistance rating required. [3.3.1.4.(3)]")
    if a.travel_distance is not None and a.travel_distance <= 45:
        print("Also: sprinklered floor area with travel distance <= 45 m - no corridor separation from the remainder of the storey is required at all. [3.3.1.4.(4)(a); exceptions 3.3.3.5.(9), 3.3.4.2.(1)]")
if __name__ == "__main__":
    main()
