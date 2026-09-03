# Sire AI — marketing site

A five-page marketing site for "Sire AI", a fictional foundation-model
company. Built with Flask, using one blueprint per page for easy expansion
(each page can grow its own routes/logic later without touching the others).

## Structure

```
sire-ai/
├── app.py                  # app factory, registers all blueprints
├── blueprints/
│   ├── home/routes.py
│   ├── about/routes.py
│   ├── products/routes.py
│   ├── careers/routes.py   # open roles list lives here (OPEN_ROLES)
│   └── contact/routes.py   # handles the contact form POST
├── templates/
│   ├── base.html           # shared nav + footer
│   └── <page>/index.html
└── static/
    ├── css/style.css       # design tokens + all styling
    └── js/main.js          # mobile nav + scroll reveal
```

## Run it

```bash
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Visit http://localhost:5000

## Design concept

The name "Sire" (to father / originate) drives the whole visual identity:
the signature element is a **lineage chart** — a pedigree-style diagram of
the model family (Sire‑1 → Sire‑2 → Sire‑3, branching into Vision / Code /
Voice) — used on the homepage hero and echoed as a timeline on the About
page. Palette is ink-black with an aged-brass accent, like an engraved
plaque; type pairs Fraunces (display serif) with Inter (body) and IBM Plex
Mono (data/labels).

## Notes for extending

- The contact form currently just flashes a confirmation — wire
  `blueprints/contact/routes.py` up to an email service or CRM.
- Careers roles are hardcoded in `blueprints/careers/routes.py` — swap
  `OPEN_ROLES` for a database query or ATS API when ready.
- Team bios on the About page are placeholders — replace names/photos.
