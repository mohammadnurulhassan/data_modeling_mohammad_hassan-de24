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
  
**Initial  naive conceptual ERD**


<img src= ".. /assets/initial_conceptual_model_ex1.png" width=400>



**Initial tabels**

Hospital



