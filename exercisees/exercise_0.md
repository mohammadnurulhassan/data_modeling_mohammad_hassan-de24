# Exercise 0
## 1. Hospital task
You have this json data, convert it into three tables: Hospital, Department and Doctor. Fill these tables with data. Do this manually and not programmatically.

{
  "hospital": "Sjukhusstock",
  "address": "Drottninggatan 3, Stockholm",
  "departments": [
    {
      "name": "Kardiologi",
      "doctors": [
        { "id": 1, "name": "Dr. Abra Abrahamson" },
        { "id": 2, "name": "Dr. Erika Eriksson" }
      ]
    },
    {
      "name": "Neurologi",
      "doctors": [{ "id": 3, "name": "Dr. Sven Svensson" }]
    }
  ]
}

### Solution
Approach
- identify entities
- identify relationships and cardinalities
- identify conceptual ERD
- create tabels
  
**Initial naive conceptual ERD**

<img src="../assets/initial_conceptual_model_ex1.png" width="400">

**Initial tables**

Hospital

| hospital_id | name         | address                     |
| ----------- | ------------ | --------------------------- |
| 1           | Sjukhusstock | Drottninggatan 3, Stockholm |

Department

| department_id | name       |
| ------------- | ---------- |
| 1             | Kardiologi |
| 2             | Neurologi  |

Doctor

| doctor_id | name                |
| --------- | ------------------- |
| 1         | Dr. Abra Abrahamson |
| 2         | Dr. Erika Eriksson  |
| 3         | Dr. Sven Svensson   |

Refined with bridge tables to reflect many-to-many relationships

<img src="../assets/conceptual_hospital_ex0_1.png" width="500">
