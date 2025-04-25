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

## Findings

### 1. Correlation Matrix
The heatmap below visualizes the correlation between four key variables: Sleep Duration (SleepHours), Sleep Quality, Study Duration (StudyHours), and Study Quality. The color gradient from blue (negative correlation) to red (positive correlation) highlights the strength and direction of these relationships.

- **SleepHours** and **SleepQuality** are highly correlated (0.84), suggesting that longer sleep often coincides with better self-reported quality.
- **StudyHours** shows a weak negative correlation with sleep-related metrics but has a moderate positive correlation with **StudyQuality** (0.36).

![Correlation Matrix](Correlation%20Matrix.png)

---

### 2. Distribution of Sleep Hours
The histogram below shows that the most common sleep duration falls between 7.5 and 9 hours. The distribution is slightly right-skewed, indicating that most days have adequate sleep duration, with a few nights of significantly shorter or longer sleep.

![Sleep Duration Histogram](Sleep%20Duration%20-%20Histogram.png)

---

### 3. Distribution of Study Hours
Study durations tend to cluster between 3 to 6 hours, with a notable peak around 4 hours. The KDE curve suggests a relatively normal distribution, but with a slight tail toward higher study durations.

![Study Duration Histogram](Study%20Duration%20-%20Histogram.png)

---

### 4. Sleep Duration vs Study Duration (Scatter Plot)
This scatter plot visualizes the relationship between sleep duration and study hours.

- There is no strong visible linear relationship.
- Some high study durations occur at both high and low sleep durations, indicating other factors may influence study habits.

![Scatter: Sleep vs Study Hours](Study%20Duration%20-%20Sleep%20Duration.png)

---

### 5. Sleep Quality vs Study Hours (Box Plot)
The box plot groups study hours based on rounded sleep quality scores (1-10). Median study hours remain fairly consistent across quality levels, but outliers appear frequently in both high and low sleep quality levels.

- Highest variance in study hours is observed around mid-to-high sleep quality.
- Lower sleep quality sometimes still resulted in relatively high study hours.

![Boxplot: Sleep Quality vs Study Hours](Study%20Duration%20-%20Sleep%20Quality.png)

---

### 6. Sleep Quality vs Study Quality (Scatter Plot)
This scatter plot explores the connection between self-reported sleep quality and study quality. Although no strong linear relationship is evident, clusters of high sleep quality generally align with high study quality.

![Scatter: Sleep Quality vs Study Quality](Study%20Quality%20-%20Sleep%20Quality.png)

---

### 7. Sleep and Study Hours Over Time (Time Series)
The time series graph illustrates trends in sleep and study habits across several weeks. It highlights gaps in study sessions as well as dips in sleep during busy periods.

- Sleep hours are more stable over time, while study hours fluctuate dramatically.
- Some days with very little study time coincide with consistent sleep hours, potentially indicating low motivation or outside obligations.

![Time Series: Sleep & Study Over Time](Study%20&%20Sleep%20Hours%20over%20Time.png)

---

### 8. Correlation & Hypothesis Test Result
Using `pearsonr` test to assess the relationship between sleep duration and study duration:

- **Correlation Coefficient (r)**: ~0.066 — very weak positive correlation.
- **P-Value**: > 0.05 — not statistically significant.

> Conclusion: There is no significant linear relationship between sleep duration and study hours in this dataset.

---

### 9. Regression Summary (Sleep Hours -> Study Hours)
An OLS regression was conducted to examine if sleep duration can predict study hours:

- The regression summary shows a non-significant coefficient for SleepHours.
- R-squared value is close to zero, indicating little explanatory power.

> Conclusion: Sleep duration does not meaningfully predict study time in this sample. Future analysis may consider interaction with additional lifestyle or environmental factors.

