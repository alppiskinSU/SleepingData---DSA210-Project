# SleepingData---DSA210-Project

## Project Overview

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

In this section, three regression models were developed to explore how different sleep-related metrics affect study quality.

---

### Model 1: Sleep Quality → Study Quality

- **Objective:** To examine the impact of self-rated sleep quality on study quality.
- **Method:** Simple Linear Regression  
- **Features:**  
  - Independent Variable (X): Sleep Quality (scale 1–10)  
  - Dependent Variable (y): Study Quality (scale 1–10)
- **Results:**  
  - R²: 0.016
  - MAE: 1.602
- **Interpretation:** Sleep quality has a very weak relationship with study quality, as indicated by the low R² value. It may not be a reliable predictor on its own.

![Model 1 - Sleep Quality vs Study Quality](Model%201%20-%20ML.png)

---

### Model 2: Sleep Efficiency → Study Quality

- **Objective:** To test the effectiveness of sleep efficiency (quality/hours) in predicting study quality.
- **Method:** Simple Linear Regression  
- **Features:**  
  - Independent Variable (X): Sleep Efficiency (SleepQuality / SleepHours)  
  - Dependent Variable (y): Study Quality
- **Results:**  
  - R²: 0.006
  - MAE: 1.615
- **Interpretation:** Sleep efficiency also showed a negligible predictive power for study quality, suggesting that more complex or additional variables may be needed.


![Model 2 - Predict Study Quality](Model%202%20-%20ML.png)

---

### Model 3: Decision Tree Regressor

- **Objective:** To model study quality using multiple features and assess feature importance.
- **Method:** Decision Tree Regression  
- **Features:**  
  - Sleep Hours  
  - Sleep Quality  
- **Results:**  
  - R²: -0.240  
  - MAE: 2.375
- **Feature Importance Results:**  
  - Sleep Hours: Most impactful  
  - Sleep Quality: Moderately impactful

- **Interpretation:** The Decision Tree model highlights feature importance but showed weak generalization due to dataset size.

![Model 3: Decision Tree](Model%203%20-%20ML.png)  
![Model 3: Feature Importance](Model%203%20-%20ML2.png)


---

### Comparison of Models

| Model                             | R²     | MAE     |
|----------------------------------|--------|---------|
| Sleep Quality → Study Quality    | 0.016  | 1.602   |
| Sleep Efficiency → Study Quality | 0.006  | 1.615   |
| Decision Tree (Multi-feature)    | -0.240 | 2.375   |

**Note:** None of the models achieved strong predictive performance. The R² values are close to zero or even negative, which suggests that the input features may not have strong linear or nonlinear relationships with the target variable (Study Quality). This outcome is likely due to a small dataset and high variability in subjective ratings.

---

## Limitations and Future Work

### Limitations

- Data is collected from a single individual, limiting the generalizability of the findings.
- Self-reported measures may introduce bias.
- Small dataset affects the robustness of machine learning models.
- Decision Tree feature importances may vary with small data.

### Future Work

- Collect larger datasets across multiple participants.
- Include additional contextual variables (e.g., stress, diet, distractions).
- Apply more robust models such as Random Forest or KNN with more data.
- Implement cross-validation to improve model generalization.
- Automate data collection to reduce self-report bias.

---

## Conclusion

This project explored the potential impact of sleep-related factors on self-rated academic performance. Although the machine learning models yielded low predictive accuracy, several insights were drawn:

- **Sleep Quality** and **Sleep Efficiency** exhibited weak positive trends with Study Quality.
- **Decision Tree analysis** emphasized that Sleep Hours may have slightly more influence than other features, though overall predictability remained low.
- The limited model performance emphasizes the challenges of working with small, subjective datasets and the complexity of factors influencing study effectiveness.

Despite its statistical limitations, this project provided an excellent opportunity to practice data analysis, visualization, hypothesis testing, and machine learning in a real-life context. In future work, larger and more diverse datasets—combined with richer features—could help build models that better reflect the intricate relationship between lifestyle habits and academic productivity.


