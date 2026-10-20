# Data Modeling — Coursework

Coursework from the **Data Modeling module** of the Data Engineering programme (DE24) at STI, Stockholm. Covers conceptual modelling (ER diagrams, normalisation) and document modelling with MongoDB.

**Tools:** ER modelling · PostgreSQL · MongoDB · Docker Compose · Python (PyMongo)

## Contents

| Folder | Topic |
|---|---|
| `exercisees/exercise_0.md` | Turning nested hospital JSON into normalised Hospital / Department / Doctor tables: entities, relationships, cardinalities, conceptual ERD |
| `assets/` | ER diagrams for the exercise |
| `08/` | MongoDB lab: Docker Compose stack (PostgreSQL, MongoDB, mongo-express), ingesting LinkedIn-style profile JSON with a unique index, querying with PyMongo |

## Run the MongoDB lab

```bash
cd 08
# create a .env with POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_PORT, MONGO_USER, MONGO_PASSWORD
docker compose up -d
pip install pymongo python-dotenv
python ingest_profiles.py
```
mongo-express UI: http://localhost:8081

---
**Mohammad Nurul Hassan** — Data Engineer, moving into ML / AI engineering.
