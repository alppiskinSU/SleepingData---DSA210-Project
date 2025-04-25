# SleepingData---DSA210-Project

## Project Overwiev
This project explores how sleep duration and quality impact academic performance. Sleep is a critical factor in cognitive function, study time, and study quality. The goal is to analyze whether better sleep habits lead to improved academic success.

## Motivation

- **Personal Growth**

Sleep is an essential part of overall well-being. By understanding how my sleep patterns influence my academic performance, I can develop healthier and more efficient habits to improve my efficiency in studying.

- **Long-Term Impact**

The findings of this project will not only help me enhance my academic performance, but they also contribute to developing better sleep habits for increased productivity, focus, and mental and physical well-being. 

## Objectives
- Investigate the correlation between sleep duration and studying time and quality.
- Identify the optimal sleep schedule for better learning efficiency.
- Examine how sleep quality affects focus and productivity during study sessions.

## Data Sources
To conduct this analysis, data will be collected through the following sources:

- **Sleep Duration:** Total sleep duration (hours).
- **Sleep Quality:** Self-rated sleep quality (scale of 1-10).
- **Study Time:** Tracked manually with using chronometer.
- **Study Quality:** Self-rated study quality ( scale of 1-10).
- **Academic Performance:** Grades from the midterm exams. ( This may vary due to difficulty of lesson but in previous semesters sleep affected my exam grades significantly )

## Analysis Plan
The collected data will undergo statistical and visual analysis to uncover key aspects:

- **Correlation Analysis:** Determining whether there is strong link between sleep patterns and academic performance.
- **Sleep-Wake Pattern Evaluation:** Finding the best time to sleep and wake up for improved learning.
- **Data Visualization:** Using scatter plots, time-series graphs to present findings effectively.

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
The histogram below indicates that most common sleep durations fall between 7.5 and 9 hours. The distribution is slightly right-skewed, with a few days having notably shorter or longer sleep durations.

![Sleep Duration Histogram](Sleep%20Duration%20-%20Histogram.png)  
*Figure 2: Distribution of sleep hours.*

**Insight:** Typical sleep patterns appear healthy, but occasional deviations may impact productivity.

---

### 3. Distribution of Study Hours
The histogram shows study durations primarily clustering between 3 to 6 hours, peaking at around 4 hours. A slight right skew suggests occasional extended study sessions.

![Study Duration Histogram](Study%20Duration%20-%20Histogram.png)  
*Figure 3: Distribution of study hours.*

**Insight:** Most study sessions are moderate in length, possibly indicating optimal attention spans.

---

### 4. Relationship Between Sleep Duration and Study Duration

#### Scatter Plot
The scatter plot below assesses the relationship between sleep duration and study hours:

- No clear linear relationship observed.
- Study durations vary independently of sleep length, suggesting other factors like motivation or external obligations.

![Scatter: Sleep vs Study Hours](Study%20Duration%20-%20Sleep%20Duration.png)  
*Figure 4: Sleep duration versus study hours.*

**Insight:** Sleep duration alone is insufficient to explain study habits.

---

### 5. Sleep Quality vs Study Hours

#### Box Plot
This plot categorizes study hours by rounded sleep quality scores (1-10):

- Median study hours remain consistent across sleep quality levels.
- High variability in study durations across mid-to-high sleep quality scores.

![Boxplot: Sleep Quality vs Study Hours](Study%20Duration%20-%20Sleep%20Quality.png)  
*Figure 5: Boxplot of sleep quality versus study hours.*

**Insight:** Better sleep quality does not consistently translate into increased study hours.

---

### 6. Relationship Between Sleep Quality and Study Quality

#### Scatter Plot
This plot explores the relationship between sleep quality and perceived study quality:

- No strong linear relationship, though clusters suggest better sleep often accompanies higher perceived study quality.

![Scatter: Sleep Quality vs Study Quality](Study%20Quality%20-%20Sleep%20Quality.png)  
*Figure 6: Sleep quality versus study quality.*

**Insight:** Improved sleep quality might modestly enhance subjective study quality.

---

### 7. Sleep and Study Hours Over Time

#### Time Series
The time series below highlights trends in sleep and study habits:

- Sleep hours are relatively stable, while study hours show significant variability.
- Frequent dips in study duration suggest external influences or fluctuating motivation.

![Time Series: Sleep & Study Over Time](Study%20&%20Sleep%20Hours%20over%20Time.png)  
*Figure 7: Sleep and study hours over time.*

**Insight:** Stable sleep doesn't always lead to stable study habits.

---

### 8. Correlation & Hypothesis Testing

**Research Question:**  
*Does sleep duration significantly correlate with study duration?*

To examine this relationship, a **Pearson correlation test** was conducted between the variables **Sleep Duration (SleepHours)** and **Study Duration (StudyHours)**.

**Hypotheses:**  
- **Null Hypothesis (H₀):** There is **no significant linear relationship** between sleep duration and study duration.
- **Alternative Hypothesis (H₁):** There is a **significant linear relationship** between sleep duration and study duration.

**Test Results:**  
- **Correlation coefficient (r):** `0.066`  
  *(Indicating a very weak positive linear correlation between sleep and study durations.)*
  
- **P-value:** `> 0.05` *(Not statistically significant)*

**Interpretation:**  
- The calculated Pearson correlation coefficient (`r = 0.066`) suggests only a negligible relationship between sleep duration and study duration.
- The resulting p-value exceeding 0.05 means we **fail to reject** the null hypothesis at the 5% significance level.

**Conclusion:**  
- Based on this analysis, there is **no statistically significant linear relationship** between sleep duration and study duration in the collected data.
- These findings suggest that the amount of sleep alone does not directly influence

---

