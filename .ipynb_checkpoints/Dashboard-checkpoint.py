import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Function

def correlation(x,y):
    corelation = x.corr(y)
    if corelation>0 and corelation<0.5:
        print(f"Weak Positive Correlation {corelation}")
    elif corelation>0.5:
        print(f"Positive Correlation {corelation}")
    elif corelation<0 and corelation>0.5:
        print(f"Weak Negative Correlation {corelation}")
    else:
        print(f"Negative Correlation {corelation}")

st.title('Student Performance Analysis')
st.subheader("Data Dictionary")

file_path = r"StudentPerformanceFactors.csv"

try:
    data = pd.read_csv(file_path)
    df = data.copy()
    st.write(data)
except FileNotFoundError:
    st.write("File not found")


col1,col2 = st.columns(2)

with col1:
    st.write("**Number of Missing Values**",data.isnull().sum())
with col2:
    st.write("**Percent of Missing Values**",round(data.isnull().sum()/data.shape[0]*100,2).astype(str)+"%")

#st.header("Analysis")
st.markdown("<h1 style='text-align: center;'>Analysis</h1>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Correlation Calculator")

cor1 = st.sidebar.selectbox("Select the first variable",df.columns)
cor2 = st.sidebar.selectbox("Select the second variable",df.columns)

if cor1 == cor2:
    st.sidebar.write("Please select different columns")
elif df[cor1].dtype == 'O':
    cor1_codes = df[cor1].astype('category').cat.codes
    st.sidebar.write("Correlation between" ,cor1, "and" ,cor2, " is", round(cor1_codes.corr(df[cor2]),4))
elif df[cor2].dtype == 'O':
    cor2_codes = df[cor2].astype('category').cat.codes
    st.sidebar.write("Correlation between" ,cor1, " and" ,cor2, "is", round(df[cor1].corr(cor2_codes),4))
else:
    st.sidebar.write("Correlation between " ,cor1, "and " ,cor2, " is", round(df[cor1].corr(df[cor2]), 4))

# Question 1
st.write("**1. How does the number of hours studied correlate with exam scores?**")

corelation = round(df['Hours_Studied'].corr(df['Exam_Score']),4)
st.write("Correlation between Hours Studied and Exam Score is",corelation)

# Question 2
st.write("**2. Is there a relationship between attendance and exam performance?**")
try:
    attendance = df['Attendance']
    exam_score = df['Exam_Score']

    fig,ax =plt.subplots(figsize=(10, 6))
    ax.scatter(attendance,exam_score)
    ax.set_xlabel('Attendance')
    ax.set_ylabel('Exam Score')
    ax.set_title('Attendance vs Exam Score')
    
    st.pyplot(fig)

    correlation_result = round(attendance.corr(exam_score),4)
    st.write("Correlation between attendance and exam performance",correlation_result)  

except FileNotFoundError:
    st.write("File not found") 

# Question 3
st.write("**3. How does parental involvement affect exam scores?**")
try:
    df['Parental_Involvement_Codes'] = df['Parental_Involvement'].astype('category').cat.codes
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df['Parental_Involvement'],y=df['Exam_Score'])
    ax.set_xlabel('Parental Involvement')
    ax.set_ylabel('Exam Score')
    ax.set_title('Exam Scores by Level of Parental Involvement')
    
    st.pyplot(fig)

    st.write("Correlation between parental involvement affect exam scores",round(df['Parental_Involvement_Codes'].corr(df['Exam_Score']),4))
except FileNotFoundError:
    st.write("File not found")

# Question 4
try:
    st.write("**4. Does access to resources significantly impact students' exam scores?**")
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=df['Access_to_Resources'],y=df['Exam_Score'])
    ax.set_xlabel('Access to Resources')
    ax.set_ylabel('Exam Score')
    ax.set_title('Exam Scores by Access to Resources')

    st.pyplot(fig)

    acess_to_resource_codes = df['Access_to_Resources'].astype('category').cat.codes
    correlation = round(acess_to_resource_codes.corr(df['Exam_Score']),4)
    st.write("Correlation between Access_to_Resources and Exam Score ",  correlation)
except FileNotFoundError:
    st.write("File not Found")

# Question 5
st.write("**5. Analyze the impact of extracurricular activities on exam performance?**")

try:
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x =df['Extracurricular_Activities'],y=df['Exam_Score'])
    ax.set_xlabel('Extracurricular Activities')
    ax.set_ylabel('Exam Score')
    ax.set_title('Exam Scores by Extracurricular Activities')
    
    st.pyplot(fig)

    Extracurricular_Activities_code = df['Extracurricular_Activities'].astype('category').cat.codes
    correlation = round(Extracurricular_Activities_code.corr(df['Exam_Score']),4)
    st.write("Correlation between Extracurricular_Activities and Exam Score ", correlation)
except:
    pass

# Question 6

st.write("**6. How does the number of sleep hours affect exam scores?**")

try:
    fig,ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=df['Sleep_Hours'],y=df['Exam_Score'])
    ax.set_title('Sleep Hours vs Exam Score')
    ax.set_xlabel('Sleep Hours')
    ax.set_ylabel('Exam Score')
    ax.grid(linestyle='--',color='gray',linewidth=0.5)
    
    st.pyplot(fig)

    correlation = round(df['Sleep_Hours'].corr(df['Exam_Score']),4)
    st.write("Correlation between Sleep Hours and Exam Score ", correlation)

except FileNotFoundError:
    st.write("File not Found")

# Question 7

st.write("**7. How does motivation level correlate with exam results?**")

try:
    fig,ax = plt.subplots(figsize=(10, 6))
    # barchart
    sns.barplot(x=df['Motivation_Level'],y=df['Exam_Score'])
    # line chart
    sns.lineplot(x=df['Motivation_Level'],y=df['Exam_Score'],color='red',markers="O")
    ax.set_xlabel('Motivation Level')
    ax.set_ylabel('Exam Score')
    ax.grid()


    st.pyplot(fig)

    Motivation_Level_code = df['Motivation_Level'].astype('category').cat.codes
    correlation = round(Motivation_Level_code.corr(df['Exam_Score']),4)
    st.write("Correlation between Motivation_Level and Exam Score ", correlation)

except FileNotFoundError:
    st.write("File not Found")


# Question 8


st.write("**8. Is there a significant difference in exam scores between students with and without internet access?**")

try:
    fig, ax = plt.subplots(figsize=(10, 6))
    # bar chart
    sns.barplot(x=df['Internet_Access'], y=df['Exam_Score'], ax=ax)
    # line chart
    sns.lineplot(x = df["Internet_Access"], y = df["Exam_Score"], color = 'red', markers = 'o', ax=ax)
    ax.set_title('Exam Scores by Internet Access')
    ax.set_xlabel('Internet Access')
    ax.set_ylabel('Exam Score')

    st.pyplot(fig)

    Interet_Acess_code = df["Internet_Access"].astype('category').cat.codes
    correlation = round(Interet_Acess_code.corr(df["Exam_Score"]),4)
    st.write("Correlation between Internet Access and Exam Score ", correlation)

except FileNotFoundError:
    st.write("File not Found")


# Question 9

st.write("**9. How do tutoring sessions influence exam performance?**")
try:
    fig,ax = plt.subplots(figsize=(10, 6))
    # bar chart
    sns.barplot(x=df['Tutoring_Sessions'],y=df['Exam_Score'])
    # line chart
    sns.lineplot(x=df['Tutoring_Sessions'],y=df['Exam_Score'],color='red',markers='o')
    ax.set_title("Tutoring_Sessions vs Exam_Score")
    ax.set_xlabel('Tutoring Sessions')
    ax.set_ylabel('Exam Score')
    ax.grid()
    
    st.pyplot(fig)

    correlation = round(df['Tutoring_Sessions'].corr(df['Exam_Score']),4)
    st.write("Correlation between Tutoring Sessions and Exam Score ", correlation)
except FileNotFoundError:
    st.write("File not Found")


# Question 10

st.write("**10. Examine the effect of family income on students exam scores.**")

try:
    fig,ax = plt.subplots(figsize=(10, 6))
    # bar chart
    sns.barplot(x=df['Family_Income'],y=df['Exam_Score'])
    # line chart
    sns.lineplot(x=df['Family_Income'],y=df['Exam_Score'],color='red',markers='o')
    ax.set_title("Family Income vs Exam Score")
    ax.set_xlabel('Family Income')
    ax.set_ylabel('Exam Score')
    ax.grid()

    st.pyplot(fig)

    Family_Income_code = df["Family_Income"].astype('category').cat.codes
    correlation = round(Family_Income_code.corr(df['Exam_Score']),4)
    st.write("Correlation between Family Income and Exam Score ", correlation)

except FileNotFoundError:
    st.write("File not Found")




