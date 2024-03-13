LLD can be divided into 3 categories:
1. Here interviewer is interested in class level relationships only.
    - Design patterns are used to make classes SOLID principles compliant
    compliant.
    - Eg: Design Parking Lot, Design ATM vending machine

2. Here the interviwer is only interested in DB level schema for a particular usecase.
    - Here knowledge of designing tables are tested.
    - Which tables should have joins.
    - There should not be redundancy in rows of the Table. (Eg. Only 1 out of 10 columns value is changing for every row rest 9 values of columns are exactly the same) 
    - What will be the queries which will be running.
    - How would we analyze and optimize those queries using indexes at scale.
    - How would we deal with race conditions ? (Read-Write Locks)
    - Whether to use NoSQL DB or SQL DB for our tables in future.


3. The last category of LLD is that you would be given 2-3 hours time to write entire working code (check UDIT AGGARWAL videos for this). Problems can be:
    - Design Parking Lot but with entire working code not just class level diagram.
    - Design a Queue (PUSH queue like RabbitMQ) in which there is a consumer and producer.
    - Here also we need to implement design principles in our classes.
    - We need to make sure our code is clean, modular, extensible just wait UDIT videos on this.

