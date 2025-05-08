# SleepingData---DSA210-Project

## Project Overwiev

This project explores how sleep duration and quality impact academic performance. Sleep is a critical factor in cognitive function, study time, and study quality. The goal is to analyze whether better sleep habits lead to improved academic success.

---

## Motivation

### Personal Growth

- Sleep is an essential part of overall well-being.
- By understanding how my sleep patterns influence my academic performance, I can develop healthier and more efficient habits to improve my efficiency in studying.

### Long-Term Impact

- The findings of this project will not only help me enhance my academic performance, but they also contribute to developing better sleep habits for increased productivity, focus, and mental and physical well-being.

---

## Objectives

- Investigate the correlation between sleep duration and studying time and quality.
- Identify the optimal sleep schedule for better learning efficiency.
- Examine how sleep quality affects focus and productivity during study sessions.

---

## Data Sources

To conduct this analysis, data will be collected through the following sources:

- **Sleep Duration:** Total sleep duration (hours).
- **Sleep Quality:** Self-rated sleep quality (scale of 1-10).
- **Study Time:** Tracked manually with using chronometer.
- **Study Quality:** Self-rated study quality ( scale of 1-10).
- **Academic Performance:** Although academic performance (grades) was initially considered as a potential variable, it was excluded from the analysis because I believe that exam scores are influenced by various external factors unrelated to sleep habits and thus would not provide meaningful insights in this specific context.

---

## Analysis Plan

- **Correlation Analysis:** Determining whether there is strong link between sleep patterns and academic performance.
- **Sleep-Wake Pattern Evaluation:** Finding the best time to sleep and wake up for improved learning.
- **Data Visualization:** Using scatter plots, time-series graphs to present findings effectively.

---

## Expected Outcomes

By the end of the study, this project aims to answer the following questions:

- Does getting more sleep lead to better academic performance?
- Is there an ideal sleep schedule for increased focus and learning efficiency?
- How does poor sleep impact productivity and retention of information?
- Are there any meaningful trends or fluctuations in my personal study performance based on different sleep patterns?

---

## Findings

### 1. Correlation Matrix

The heatmap below visualizes correlations between four key variables: Sleep Duration (SleepHours), Sleep Quality, Study Duration (StudyHours), and Study Quality. The color gradient from blue (negative correlation) to red (positive correlation) highlights the strength and direction of these relationships.

- **SleepHours** and **SleepQuality** show a high positive correlation (0.84), suggesting that longer sleep often coincides with better perceived quality.
- **StudyHours** has a weak negative correlation with sleep metrics but a moderate positive correlation with **StudyQuality** (0.36).

![Correlation Matrix](Correlation%20Matrix.png)

*Figure 1: Correlation between sleep and study metrics.*

**Insight:** Good sleep tends to align with higher sleep quality ratings, but doesn't significantly impact study duration directly.

---

### 2. Distribution of Sleep Hours

![Sleep Duration Histogram](Sleep%20Duration%20-%20Histogram.png)

*Figure 2: Distribution of sleep hours.*

**Insight:** Typical sleep patterns appear healthy, but occasional deviations may impact productivity.

---

### 3. Distribution of Study Hours

![Study Duration Histogram](Study%20Duration%20-%20Histogram.png)

*Figure 3: Distribution of study hours.*

**Insight:** Most study sessions are moderate in length, possibly indicating optimal attention spans.

---

### 4. Relationship Between Sleep Duration and Study Duration

![Scatter: Sleep vs Study Hours](Study%20Duration%20-%20Sleep%20Duration.png)

*Figure 4: Sleep duration versus study hours.*

**Insight:** Sleep duration alone is insufficient to explain study habits.

---

### 5. Sleep Quality vs Study Hours

![Boxplot: Sleep Quality vs Study Hours](Study%20Duration%20-%20Sleep%20Quality.png)

*Figure 5: Boxplot of sleep quality versus study hours.*

**Insight:** Better sleep quality does not consistently translate into increased study hours.

---

### 6. Relationship Between Sleep Quality and Study Quality

![Scatter: Sleep Quality vs Study Quality](Study%20Quality%20-%20Sleep%20Quality.png)

*Figure 6: Sleep quality versus study quality.*

**Insight:** Improved sleep quality might modestly enhance subjective study quality.

---

### 7. Sleep and Study Hours Over Time

![Time Series: Sleep & Study Over Time](Study%20&%20Sleep%20Hours%20over%20Time.png)

*Figure 7: Sleep and study hours over time.*

**Insight:** Stable sleep doesn't always lead to stable study habits.

---

### 8. Correlation & Hypothesis Testing

**Research Question:**  
*Does sleep duration significantly correlate with study duration?*

**Hypotheses:**

- **Null Hypothesis (H₀):** There is **no significant linear relationship** between sleep duration and study duration.
- **Alternative Hypothesis (H₁):** There is a **significant linear relationship** between sleep duration and study duration.

**Test Results:**

- **Correlation coefficient (r):** `0.066`
- **P-value:** `> 0.05` *(Not statistically significant)*

**Interpretation:**

- The calculated Pearson correlation coefficient suggests only a negligible relationship.
- The resulting p-value means we **fail to reject** the null hypothesis.

**Conclusion:**

- Sleep duration does not significantly influence study duration.

---

## Machine Learning Models

In this section, two linear regression models were developed to explore whether sleep habits can predict study quality.

---

### Model 1: Sleep Quality → Study Quality

- **Objective:** To investigate whether self-rated sleep quality predicts self-rated study quality.
- **Method:** Simple Linear Regression
- **Features:**  
  - Independent Variable (X): Sleep Quality (scale 1–10)  
  - Dependent Variable (y): Study Quality (scale 1–10)
- **Results:**  
  - R²: 0.019  
  - MAE (Mean Absolute Error): 2.485
- **Interpretation:** Sleep quality explains only 1.9% of the variation in study quality.

![Model 1 - Sleep Quality vs Study Quality](Model%201%20-%20ML.png)

*Figure: Regression result of Sleep Quality vs Study Quality*

---

### Model 2: Sleep Hours → Study Quality

- **Objective:** To determine whether sleep duration can predict study quality.
- **Method:** Simple Linear Regression
- **Features:**  
  - Independent Variable (X): Sleep Hours (in hours)  
  - Dependent Variable (y): Study Quality (scale 1–10)
- **Results:**  
  - R²: 0.072  
  - MAE: 2.356
- **Interpretation:** Sleep hours explain approximately 7.2% of the variation in study quality.

![Model 2 - Sleep Hours vs Study Quality](Model%202%20-%20ML.png)

*Figure: Regression result of Sleep Hours vs Study Quality*

---

### Comparison of Models

| Model | R² | MAE |
|-------|----|-----|
| Sleep Quality → Study Quality | 0.019 | 2.485 |
| Sleep Hours → Study Quality   | 0.072 | 2.356 |

**Insight:** Neither model demonstrated strong predictive accuracy, although sleep duration performed slightly better.

---

## Limitations and Future Work

### Limitations

- Small sample size (single individual).
- Subjective self-reported data.
- Limited variables analyzed.
- Linear assumptions may oversimplify.
- Short-term dataset.

### Future Work

- Collect data from multiple participants.
- Include additional variables (stress, nutrition, etc).
- Try advanced ML models.
- Collect long-term data.
- Use automated tracking tools.

---

## Conclusion

This project used two linear regression models to explore the relationship between sleep and study performance. While neither sleep quality nor sleep duration proved to be strong predictors of study quality, the models still provide valuable insights.

Sleep duration had slightly more predictive power than sleep quality, but overall R² values were low, indicating that academic productivity is likely influenced by many other variables beyond sleep alone.

Despite these limitations, the project demonstrates how basic machine learning methods can be applied to personal data. Future studies with more variables and data can uncover deeper insights into effective studying habits.
