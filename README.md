# Decision Analytics for Business and Policy Final Project
### Authors
* Hiba Hassan, hibah@andrew.cmu.edu
* Niharika Patil, niharikp@andrew.cmu.edu 
* Genna Moellering, gmoeller@andrew.cmu.edu
---

### Project Description

Football, or soccer in the U.S. and Canida, is one of the most popular sports in the world, and its competitiveness transcends what the players do in a given match. Coaching staff, football operations, and general managers all do their part to maximize their teams’ advantages before the players even take the field. One of the primary ways they can do this is by acquiring the best players they can afford. The conventional process for finding and acquiring the players best suited to a team can be long and arduous, as various inputs like performance statistics, risk assessments, and team need analysis need to be factored in. This environment is ripe for data-driven decision making.


Our analysis draws inspiration from the problem made famous in Moneyball, the book by Micahel Lewis that narrates how a Major League Baseball team overcame the competitive gap between rich and poor teams by identifying undervalued players with underappreciated performance metrics that could significantly contribute to their team’s success. This report uses data from the European Football Transfer market to conduct a similar analysis for a hypothetical European football club, using an optimization model to help determine which players they should target as trade prospects under given constraints. 

**Question:**
As a General Manager of the FC Tartan Soccer club with a budget of 150 million Euros, which athletes should I focus on acquiring given my team’s budget, position needs, and the pool of available players?

---
### Data Collection

Our dataset from TransferMarkt.com, accessed through dataworld (https://data.world/dcereijo/player-scores), provides information on players, clubs, competitions, and valuations, which can inform decisions on what players are worth investing in.

---
### Assumptions and Modeling

Our dataset was sourced from TransferMarkt.com, this multidimensional dataset allows for an in-depth exploration of player performance, valuation trends, and strategic considerations across different playing positions in the realm of football. Some key assumptions integrated were budget availability, pool of players to transfer selected from 2023. Emphasizing a holistic approach to team formation our model puts importance on factors such as experience, current form, and overall performance metrics. In terms of our modeling, we first formulated a comprehensive performance metric.Then we opted for a Mixed Integer Problem, where the objective of the model is two-fold:maximizing the value added to the team through player transfers while simultaneously optimizing performance and minimizing the cost of transfers.

---
### Challenges and Constraints

Given data constraints and modeling assumptions, our key challenges were in the realm of how data-driven and realistic our model could be. Factors such as lack of transparency from clubs regarding budget and player needs, limited qualitative factors integration.In terms of OptiGuide, accessibility issues and limitations in OptiGuide's response, particularly when dealing with significant shifts in topics. Acknowledging and addressing these challenges is crucial for refining and enhancing the model's capabilities in future applications.

---
### Conclusions and Future Work

Overall, we were pleased with Optiguide and our model’s performance. It did fail to meet the demands of several of our questions, but, overall, OptiGuide responded decently to our diverse queries, addressing concerns about excluding specific players, and adjusted budget constraints. We noted how superior GPT-4 was to its GPT 3.5 counterpart in handling our queries, and moving forward, we would like to increase our model’s ability to handle prompts that are more vague and respond with important detail like player names and relevant data. In sports, both quantitative performance metrics and qualitative, intangible elements like player chemistry and star power are important. We see OptiGuide as a unique tool capable of bridging the gap between experts in each arena by making the optimization process more accessible with plain language. 

---
### How to Run the Project

Our raw data was too extensive to host on GitHub, but the final cleaned dataset `final_merged.csv ` is included here along with the jupyter notebook containing our data cleaning process - `data_cleaning.ipynb`. 

The `model_script.py` contains the code that is the input for our OptiGuide notebooks listed below - please read each notebook in the following order:
* `optiguide_pt1.ipynb`
* `optiguide_pt2.ipynb`

Our OptiGuide questions spanned two notebooks as both were used to iterate and test the consistencies of our answers.  The html versions of these files will serve as links to our Appendix 1, which contains the links to and transcripts of the chat.
