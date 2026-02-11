# Video Game Success Analysis - Ice Store

## 📊 Project Overview
This project analyzes historical video game sales data from Ice, a global online video game store, to identify the key factors that determine a game’s commercial success.
Using data on user reviews, critic reviews, genres, platforms, age ratings, and regional sales, the analysis aims to uncover patterns that help guide marketing strategies and forecast future product performance.
The project focuses on data cleaning, preprocessing, exploratory data analysis (EDA), and statistical hypothesis testing, transforming raw historical data into actionable business insights to support the 2017 advertising campaign planning.

## 📊 Dataset Description
The dataset contains historical video game data up to December 2016, including:
- Global and regional sales (NA, EU, JP, Other)
- Platform information
- Genre classification
- ESRB rating categories
- Critic scores and user scores
- Release year data
This dataset enables market segmentation analysis and identification of commercial success drivers across regions.

## ⚙️ Methodology
The project follows a structured data analysis workflow:
1.	Data Preprocessing
-	Standardized missing values and corrected inconsistent entries
-	Converted data types for numerical analysis
-	Replaced "tbd" user score values with NaN
-	Handled missing critic and user score data
-	Filtered relevant data period for forecasting

2.	Exploratory Data Analysis
-	Platform life cycle and market trend evaluation
-	Sales distribution across regions
-	Genre popularity and profitability analysis
-	Correlation analysis between scores and sales

3.	Statistical Hypothesis Testing
-	Compared average user ratings across platforms
-	Evaluated rating differences between genres
-	Applied statistical testing using SciPy

## 🔍 Data Preparation Highlights
The preprocessing stage addressed several real-world data challenges:
- Missing Score Data
    - Significant missing values found in critic_score and user_score
    - Standardized "tbd" entries as missing values
- Data Type Conversion
    - Converted user scores into numeric values for statistical analysis
- Relevant Time Period Selection
    - Platform lifecycle analysis showed consoles typically remain commercially active for 5–7 years
    - Only data from 2012–2016 was used for 2017 forecasting, improving predictive relevance

## 📈 Project Highlights
-	Conducted real-world data cleaning and preprocessing
-	Performed multi-regional market segmentation analysis
-	Applied statistical hypothesis testing for business decision validation
-	Identified platform lifecycle trends
-	Generated data-driven marketing strategy recommendations

## 📈 Results
1.	Platform Market Trends
- Legacy platforms (PS3, X360) showed clear decline by 2016
- Platforms with highest growth potential for 2017:
    - PlayStation 4 (PS4)
    - Xbox One (XOne)

2.	Sales Success Drivers
- Critic Scores
    - Moderate positive correlation with global sales (0.51)
    - Reliable indicator of commercial success
- User Scores
    - No significant correlation with global sales (-0.03)

3.	Most Profitable Genres
Globally successful genres during the analyzed period:
- Action
- Shooter
- Role-Playing

4.	Regional Market Profiles
North America (US) & Europe (EU)
- Preferred Platforms: PS4 / XOne
- Preferred Games: Action / Shooter
- Preferred Rating: “M” (Mature)

Japan Market (JP)
- Preferred Platforms: Nintendo 3DS / PlayStation Vita (PSV)
- Preferred Games: Role-Playing
- Preferred Rating: “E” (Everyone)

5.	Hypothesis Testing Results
- Platform Rating Comparison
    - Null hypothesis accepted
    - Average user ratings between XOne and PC are not statistically different (p-value > 0.05)
- Genre Rating Comparison
    - Null hypothesis rejected
    - Average user ratings between Action and Sports genres are significantly different 
      (p-value < 0.05)

## 💼 Strategic Business Recommendations (2017 Campaign)
North America & Europe Strategy
- Focus advertising on:
    - Action and Shooter games
    - High critic-rated titles
    - PS4 and XOne platforms

Japan Strategy
- Focus advertising on:
    - Role-Playing games
    - Nintendo 3DS platform

## ▶️ How to Run the Project
1.	Clone this repository: git clone https://github.com/alangudi417/videogames-sales-success.git
2.	Navigate to the project folder: cd videogames-sales-success
3.	Create and activate virtual environment: python -m venv venv venv\Scripts\activate # Windows source venv/bin/activate # Mac/Linux
4.	Install dependencies: pip install -r requirements.txt
5.	Launch Jupyter Notebook: jupyter notebook
6.	Open notebooks/videogames_sales_analysis.ipynb