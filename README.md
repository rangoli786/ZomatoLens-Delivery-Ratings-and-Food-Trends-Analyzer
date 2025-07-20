#  ZomatoLens: Delivery, Rating & Food Trend Analyzer

A data-driven project that explores food delivery patterns, restaurant ratings, and trending cuisines using Python. This project aims to extract valuable insights from food platform data — inspired by platforms like *Zomato*.

---

##  Table of Contents

- [Overview]
- [Objectives]
- [Tech Stack]
- [Dataset]
- [Key Insights]
- [Business Value]
- [Project Structure]
- [Future Improvements]
- [Getting Started]
- [Author]

---

##  Overview

**ZomatoLens** is a food analytics project focused on understanding customer preferences, delivery performance, and cuisine popularity. Through exploratory data analysis and visualization, it uncovers actionable insights for food delivery platforms.

---

##  Objectives

- Analyze delivery time patterns  
- Explore cuisine popularity and trends  
- Understand rating and cost relationships  
- Visualize voting behavior and booking options  
- Present insights that can inform business decisions  

---

##  Tech Stack

| Tool/Library        | Purpose                 |
|---------------------|-------------------------|
| Python              | Programming language    |
| Pandas, NumPy       | Data manipulation       |
| Matplotlib, Seaborn | Data visualization      |
| VS-Code             | Development environment |

---

##  Dataset

- **Filename:** `zomato_data_cleaned.csv`  
- **Size:** ~700 rows  
- **Features include:**  
  - Restaurant name and type  
  - Location, Cuisines  
  - Online/Table booking availability  
  - Cost for two, Delivery time  
  - Ratings and votes

---

##  Key Insights

- North Indian and Chinese cuisines dominate the food landscape  
- Costlier restaurants generally receive higher ratings  
- Delivery time clusters between 30–50 minutes for most restaurants  
- Table booking is more popular in fine-dining formats  
- Higher-rated restaurants receive more user votes

---

##  Business Value

Platforms like *Zomato* can use these insights to:

- Recommend trending cuisines by area  
- Improve ETA prediction and delivery logistics  
- Recognize top-performing restaurants by rating and vote count  
- Target specific restaurant types for promotions  

---


## Project Structure


 -<pre> ```  ZomatoLens-Delivery-Ratings-and-Food-Trends-Analyzer ├── data/ │ └── zomato_data_cleaned.csv ├──  images/ │ ├── cuisine_popularity.png │ ├── cost_vs_rating.png │ ├── delivery_time_histogram.png │ ├── votes_vs_rating.png
 │ └── restaurant_types_distribution.png ├──  notebook/ │ └── Zomato_Analyzer.ipynb ├── README.md ├── requirements.txt ├── .gitignore └── LICENSE ``` </pre>


 ---
 >  **Note:** The cleaned dataset (`zomato_data_cleaned.csv`) is too large to display on GitHub.  
> You can still access and use it after cloning this repo locally.

---
##  Visualizations

###  Cuisine Popularity
![Cuisine Popularity](plots/cuisine_popularity.png)

###  Cost vs. Rating
![Cost vs Rating](plots/cost_vs_rating.png)

###  Delivery Time Distribution
![Delivery Time](plots/delivery_time_hist.png)

###  Votes vs. Rating
![Votes vs Rating](plots/votes_vs_rating.png)

###  Restaurant Types
![Restaurant Types](plots/restaurant_types.png)



---
 Author
Rangoli Bakshi
📧 Email: rangolibakshi59@gmail.com
📞 Phone: +91-7988407651
🔗 LinkedIn
💻 GitHub




