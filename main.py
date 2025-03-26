import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


from textwrap import dedent
from agents import MedicalAgents
from tasks import MedicalTasks



class MedicalCrew:
    def __init__(self, age, disease, weight, symptoms, disease_period, place):
        self.age = age
        self.disease = disease
        self.weight = weight
        self.symptoms = symptoms
        self.disease_period = disease_period
        self.place = place

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = MedicalAgents()
        tasks = MedicalTasks()

        # Define your custom agents and tasks here
        FNAgent = agents.FNExpert()
        nut_agent = agents.nutritionist()
        phar_agent = agents.pharmacist()

        # Custom tasks include agent name and variables as input
        nut_task = tasks.generate_nutrition_plan(
            nut_agent, 
            self.age, 
            self.disease,
            self.weight,
            self.symptoms,
            self.disease_period
        )

        phar_task = tasks.generate_medication_schedule(
            phar_agent,
            self.age,
            self.disease,
            self.weight,
            self.symptoms,
            self.disease_period, 
            self.place
        )

        FN_task = tasks.generate_fitness_plan(
            FNAgent,
            self.age,
            self.disease,
            self.weight,
            self.symptoms,
            self.disease_period
        )

        # Define your custom crew here
        crew = Crew(
            agents=[FNAgent, nut_agent, phar_agent],
            tasks=[nut_task, phar_task, FN_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    age = input(dedent("""Enter Age : """))
    disease = input(dedent("""Enter disease : """))
    weight = input(dedent("""Enter weight : """))
    symptoms = input(dedent("""Enter Symptoms that you have : """))
    disease_period = input(dedent("""For how long have you had this disease : """))
    place = input(dedent("""Enter your location : """))
    custom_crew = MedicalCrew(age, disease, weight, symptoms, disease_period, place)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is your 7 Day Fitness Plan :")
    print("########################\n")
    print(result)
