"""
This module execute the judge generated
"""
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pipeline.judge import Judge
load_dotenv()

if __name__ == "__main__":

    US_ORIGINAL = """
    GIVEN a user views the Deviations landing page 
    WHEN he searches selecting type emergency and may 21st 2001 as end 
    THEN an error an error is showed"""

    US_ENRICHED_1 = """
    GIVEN a user is on the Deviations landing page, 
    WHEN they select 'EMERGENCY' as the 'Deviation Type' and '05/21/2001' 
    as the 'Effective End Date', and click the 'GO' button, 
    THEN no deviations should be displayed in the results section, 
    indicating there are no Emergency Deviations before May 21st, 2002."""
    llm = ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile")
    judge = Judge()
    result = judge.judge_pair(llm, US_ORIGINAL, US_ENRICHED_1)
    print(result.content)
