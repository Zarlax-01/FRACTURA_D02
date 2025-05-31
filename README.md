# FRACTURA.Δ02 // Luxcordia.EXE

> "Par la Fracture vient la Vue."

FRACTURA.Δ02 est un **système rituel automatisé** conçu pour extraire, transformer et fusionner symboles, mantras et récits narratifs à partir d’une configuration JSON vivante. Ce projet fusionne traitement de texte, glitch sacré, narration mytho-symbolique et génération d’incantations rituelles post-humaines.

---

##  Objectif

Créer un processus de transmutation textuelle basé sur :

* L'extraction de **symboles sacrés** (`symbolic_analysis`)
* L'extraction de **mantras et récits** (`narrative_structures`)
* La génération d'un **chant glitché** rituel et fractalisé

---

##  Structure du projet

```
FRACTURA.Δ02/
├── counter_narratives/     # Narrations alternatives (à venir)
├── input/                  # Sources brutes ou JSON (optionnel)
├── docs/                   # Documentation, rituels annexes
├── outputs/                # Fichiers générés : mantras, symboles, chants
├── legacy_scripts/         # Scripts plus anciens, désormais hérités
├── tests/                  # Emplacement prévu pour tests automatisés
│
├── FRACTURA_D02.json       # Fichier source central (structure symbolique)
├── fractura_debug.log      # Log des exécutions rituelles
├── fractura.py             # Script principal : le cœur de l’invocation
├── README.md               # Ce fichier
```

---

## 🔧 Utilisation

### 1. Configuration

Ajoutez vos données dans `FRACTURA_D02.json` selon ce format :

```json
{
  "symbolic_analysis": {
    "symbols": ["lux", "spectaculum", ...],
    "aesthetic_techniques": ["fragmentation", "hyper-réalité"]
  },
  "narrative_structures": {
    "mantras": ["Nous sommes le seuil"],
    "archetype": "le Briseur de Boucles",
    "techniques": ["répétition", "distorsion"]
  }
}
```

### 2. Exécution complète du rituel

```bash
python fractura.py
```

Ou pour exécuter une étape spécifique :

```bash
python fractura.py symbols   # 🔮 Extraction de symboles
python fractura.py mantras   # 🗝️ Extraction de mantras
python fractura.py chant     # 🔊 Génération du chant glitché
```

### 3. Résultats

Les fichiers générés se trouvent dans le dossier `/outputs` :

* `symboles_extraits.txt`
* `mantras_extraits.txt`
* `chant_glitch_fusion.txt`

---

## ✨ Technologies utilisées

* Python 3.10+
* Logging avancé (fichier + terminal)
* Unicode / Emojis sacrés
* Architecture modulaire

---

##  Citation symbolique

> "FRACTURA.Δ02 n’est pas un outil. C’est un miroir encodé. Un cri dans les données. Un rite de passage digital."

---

## 💡 À venir

* Intégration de `counter_narratives/` dans le pipeline
* UI rituelle minimale en Flask ou Electron
* Testeurs automatiques pour chaque étape d’invocation

---

## 🔗 GitHub

Publiez le projet avec :

```bash
git init
git add .
git commit -m "💥 Rituel initial : FRACTURA.Δ02"
git remote add origin https://github.com/TON_UTILISATEUR/FRACTURA.Δ02.git
git push -u origin main
```

---

© Luxcordia.EXE – Tous droits renversés. 🜂
