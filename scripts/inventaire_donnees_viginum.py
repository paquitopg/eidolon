"""Inventaire des données publiées par VIGINUM dans le dépôt Rapports-Techniques.

Usage :
    git clone https://github.com/VIGINUM-FR/Rapports-Techniques.git data/viginum
    python scripts/inventaire_donnees_viginum.py data/viginum

Affiche, pour chaque campagne :
- les listes de domaines (CSV) : volume, répartition par année de création ;
- les bundles STIX 2.1 : types d'objets, comptes et chaînes par plateforme,
  techniques DISARM référencées.

Aucune dépendance hors bibliothèque standard.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path


def defang(domain: str) -> str:
    """'spiegel[.]ltd' -> 'spiegel.ltd'"""
    return domain.replace("[.]", ".").strip().lower()


def inventaire_csv(path: Path) -> None:
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("  (vide)")
        return
    cols = list(rows[0].keys())
    domain_col = cols[0]
    date_col = next((c for c in cols if "creat" in c.lower()), None)
    print(f"  {len(rows)} entrées, colonnes : {cols}")
    if date_col:
        years = Counter(
            (r[date_col] or "").strip()[-4:] or "inconnue" for r in rows
        )
        print(f"  année de création : {dict(sorted(years.items()))}")
    if "type" in cols:
        print(f"  types : {dict(Counter(r['type'] for r in rows))}")
    exemples = [defang(r[domain_col]) for r in rows[:5]]
    print(f"  exemples : {exemples}")


def plateforme(obj: dict) -> str:
    if obj.get("account_type"):
        return obj["account_type"].lower()
    if obj.get("channel_types"):
        return obj["channel_types"][0].lower()
    name = obj.get("name", "")
    m = re.match(r"(?:https?://)?([^/\s]+\.[a-z]{2,})(?:/|$)", name.lower())
    return m.group(1) if m else "inconnue"


def inventaire_stix(path: Path) -> None:
    bundle = json.loads(path.read_text(encoding="utf-8"))
    objs = bundle.get("objects", [])
    types = Counter(o.get("type") for o in objs)
    print(f"  {len(objs)} objets STIX : {dict(types.most_common(8))}")

    comptes = [o for o in objs if o.get("type") in ("user-account", "channel")]
    if comptes:
        print(
            f"  comptes / chaînes ({len(comptes)}) par plateforme : "
            f"{dict(Counter(plateforme(o) for o in comptes).most_common(6))}"
        )

    techniques = sorted(
        {
            (ref["external_id"], o["name"])
            for o in objs
            if o.get("type") == "attack-pattern"
            for ref in o.get("external_references", [])
            if ref.get("external_id")
        }
    )
    if techniques:
        print(f"  {len(techniques)} techniques DISARM, dont :")
        for tid, name in techniques[:8]:
            print(f"    {tid:<10} {name}")
        if len(techniques) > 8:
            print(f"    … (+{len(techniques) - 8})")


def main(root: str) -> None:
    base = Path(root)
    if not base.is_dir():
        sys.exit(f"Dossier introuvable : {base}")
    for dossier in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")):
        print(f"\n=== {dossier.name}")
        for f in sorted(dossier.iterdir()):
            if f.suffix.lower() == ".csv":
                print(f"- {f.name}")
                inventaire_csv(f)
            elif f.suffix.lower() == ".json":
                print(f"- {f.name}")
                inventaire_stix(f)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "data/viginum")
