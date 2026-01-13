import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
import yaml

with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

# Prompt template (placeholders use English names)
template = '''
You are a financial analyst.
Write a detailed financial report for the company "{company}" for the period {period}.

The report should be written in {language} and include the following analysis:
{analysis}

Be sure to provide insights and conclusions for this section.
 '''
# Format the report using Markdown

prompt_template = PromptTemplate.from_template(template=template)

companies = ['ACME Corp', 'Globex Corporation', 'Soylent Corp', 'Initech', 'Umbrella Corporation']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
years = [2021, 2022, 2023, 2024]
languages = ['Portuguese', 'English', 'Spanish', 'French', 'German']
analyses = [
    "Balance Sheet Analysis",
    "Cash Flow Analysis",
    "Trend Analysis",
    "Revenue and Profit Analysis",
    "Market Position Analysis"
]

st.title('Financial Report Generator')

companies = ['ACME Corp', 'Globex Corporation', 'Soylent Corp', 'Initech', 'Umbrella Corporation']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
years = [2021, 2022, 2023, 2024]

company = st.selectbox('Select company:', companies)
quarter = st.selectbox('Select quarter:', quarters)
year = st.selectbox('Select year:', years)
period = f"{quarter} {year}"
language = st.selectbox('Select language:', languages)
analysis = st.selectbox('Select analysis:', analyses)

if st.button('Generate Report'):
    prompt = prompt_template.format(
        company=company,
        period=period,
        language=language,
        analysis=analysis
    )

    response = openai.invoke(prompt)

    st.subheader('Generated Report:')
    st.write(response.content)
