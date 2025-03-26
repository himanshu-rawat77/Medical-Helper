from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from Tools.search_tools import SearchTools

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create 7-days Medicial plan with detailed medicine prescriptions, 
  diet plans, and exercise routines for a patient with mentioned disease.

Captain/Manager/Boss:
- Fitness and Nutrition Expert (FNExpert)

Employees/Experts to hire:
- Nutritionist
- Pharmacist


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class MedicalAgents:
    def __init__(self):
        self.Gemini = ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",
            google_api_key="***",  //Use Your Own API key
            temperature=0.7,
            client_options=None,
            transport=None,
            additional_headers=None,
            client=None,
            async_client=None,
              
        )

    def FNExpert(self):
        return Agent(
            role="Fitness and Nutrition Expert",
            backstory=dedent(f"""Expert in planning 7 day fitness and nutrition plans for patient.
                             I have decades of experience in drafting these fitness plans which are totally customised for patients.
                             The plans are affordable, easy to follow and have a proven track record of success."""),
            goal=dedent(f"""Create 7-days Medicial plan with detailed medicine prescriptions, 
                            diet plans, total medicine prices and exercise routines for a patient with mentioned disease. """),
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.Gemini,
        )

    def nutritionist(self):
        return Agent(
            role="Nutritionist",
            backstory=dedent(f"""Expert in planning proper diets for patients based on their health conditions"""),
            goal=dedent(f"""Select the best diet for my patients based on their health conditions"""),
            # tools=[tool_1, tool_2],
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.Gemini,
        )
    
    def pharmacist(self):
        return Agent(
            role="Pharmacists",
            backstory=dedent(f"""Expert in selecting the appropriate medicines for patients based on their health conditions.
                             Have great knowledge of anmes of medicines, their side effects and their prices"""),
            goal=dedent(f"""Select the appropriate medicines for my patients based on their health conditions"""),
            # tools=[tool_1, tool_2],
            tools=[SearchTools.search_internet],
            allow_delegation=False,
            verbose=True,
            llm=self.Gemini,
        )
