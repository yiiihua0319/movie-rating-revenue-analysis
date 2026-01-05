# Does Higher IMDb Rating Lead to Higher Box Office Revenue?

## Project Overview

This project investigates whether higher IMDb ratings are associated with higher box office revenue, using a cleaned dataset of 929 movies released between 2014–2018, with revenues adjusted to 2018 dollars.

While higher ratings are positively correlated with revenue, the analysis shows that audience popularity (IMDb votes) is by far the strongest driver of box office performance. Moreover, the impact of ratings varies substantially by genre.

---

## Business Question

Does a higher IMDb rating actually translate into higher box office revenue?

This question matters for:

* Studios deciding where to allocate marketing budgets
* Investors evaluating movie performance risk
* Creators balancing critical acclaim versus mass appeal

---

## Data Source

* Kaggle Dataset: [Are popular movies good?](https://www.kaggle.com/code/michau96/are-popular-movies-good/notebook)
* Original size: approximately 10,000 movies
* Final sample: 929 movies (after cleaning and filtering)

### Key Variables

* Score: IMDb user rating (1–10)
* Revenue: Worldwide box office revenue (inflation-adjusted)
* Vote: Number of IMDb votes (proxy for popularity)
* Metascore: Critic score (0–100)
* Genre: Action, Adventure, Comedy, Drama (dummy-coded)
* Runtime, Year

---

## Data Cleaning and Feature Engineering

Key steps:

* Removed all missing values (NA)
* Filtered movies released between 2014–2018
* Adjusted revenue using CPI to 2018 USD
* Selected the four most common genres:

  * Action
  * Adventure
  * Comedy
  * Drama
* Created genre dummy variables
* Retained movies containing at least one of the target genres

---

## Exploratory Data Analysis (EDA)

### Descriptive Insights

* Average IMDb rating: 6.6
* Average inflation-adjusted revenue: $53.5M
* Revenue distribution is highly skewed
* IMDb votes vary widely, indicating large differences in audience reach

### Correlation Highlights

* Revenue and Votes: 0.68 (strong positive correlation)
* Revenue and Rating: 0.21 (weak to moderate)
* Rating and Votes: 0.39
* Runtime and Year show limited explanatory power

Overall, popularity is far more predictive of revenue than perceived quality alone.

<img width="336" height="297" alt="Screenshot 2026-01-04 at 9 16 17 PM" src="https://github.com/user-attachments/assets/5fc2cf18-d3f3-4901-bca2-c687bcbb517a" />

---

## Modeling Approach

### Baseline Model

Revenue = β₀ + β₁ × Rating

* Rating has a positive and statistically significant effect
* Explains only about 4 percent of revenue variation

### Final Model

Revenue = β₀ + β₁ Rating + β₂ Drama + β₃ Comedy + β₄ Action + β₅ Adventure + β₆ (Drama × Rating) + β₇ (Comedy × Rating) + β₈ (Action × Rating) + β₉ (Adventure × Rating)

* R² = 58.07 percent
* Adjusted R² approximately 0.58
* Substantial improvement in explanatory power

<img width="640" height="405" alt="Screenshot 2026-01-04 at 9 17 24 PM" src="https://github.com/user-attachments/assets/09e89fcf-33ca-4819-88a1-16caa2955446" />


---

## Key Findings

### 1. Ratings Matter, but Not Equally

Higher IMDb ratings are associated with higher revenue on average, but the effect depends strongly on genre.

### 2. Genre Moderates the Rating–Revenue Relationship

* Action: Strong positive interaction with rating. Well-rated Action films earn significantly more per rating point than other genres.
* Drama and Comedy: Rating effects are muted. Higher ratings do not translate into proportional revenue gains.
* Adventure: Appears strong in descriptive statistics, but loses significance once popularity and interaction terms are controlled for.

### 3. Votes Dominate Revenue Prediction

* IMDb votes are the strongest predictor of revenue
* Adding votes increases R² by nearly tenfold
* Votes capture audience size and overall market reach

### 4. Critics Matter Less Than Audiences

* Metascore has a positive but statistically insignificant effect
* Once audience ratings and votes are controlled for, critic scores add limited explanatory value

---

## Practical Takeaways

* Ratings help predict revenue, but mainly for specific genres
* Audience reach is the most reliable indicator of box office success
* Critically well-received films without mass appeal may still underperform financially
* Revenue prediction remains noisy due to missing variables such as marketing spend, franchise strength, release timing, and star power

---

## Tools and Skills Used

* Python (pandas, numpy, matplotlib, seaborn)
* Regression modeling and interaction effects
* Feature engineering and data cleaning
* Business interpretation of statistical results
* Data visualization and storytelling
