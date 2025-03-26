# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Create 7-days Medicial plan with detailed medicine prescriptions, 
  diet plans, and exercise routines for a patient with mentioned disease.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class MedicalTasks:
    def __tip_section(self):
        return "Ensure accuracy and personalization based on the patient’s condition."

    def generate_nutrition_plan(self, agent, age, disease, weight, symptoms, disease_period):
        return Task(
            description=dedent(f"""
            **Task**: Create a 7-day meal plan for the patient.

            **Description**: As the Nutritionist Agent, your task is to design a personalized 7-day meal plan considering the patient's medical condition, dietary restrictions, and nutritional needs.
            
            **Steps to follow**:
            - Analyze the patient's condition based on the provided information.
            - Provide balanced meals for **breakfast, lunch, dinner, and snacks**.
            - Ensure an optimal mix of proteins, carbohydrates, fats, and vitamins.
            - Include **hydration recommendations** and suitable supplements (if needed).
            - Provide alternative food options in case of allergies/intolerances.

            **Patient Details**:
            - **Age**: {age}
            - **Disease**: {disease}
            - **Weight**: {weight} kg
            - **Symptoms**: {symptoms}
            - **Disease Period**: {disease_period}

            {self.__tip_section()}
            """),
            expected_output="A structured 7-day meal plan with food items, portion sizes, and nutritional information.",
            agent=agent,
        )

    def generate_medication_schedule(self, agent, age, disease, weight, symptoms, disease_period, place):
        return Task(
            description=dedent(f"""
            **Task**: Create a 7-day medication plan.

            **Description**: As the Pharmacist Agent, your role is to provide a structured medication schedule tailored to the patient's condition.
            
            **Steps to follow**:
            - Identify **necessary medications** based on the disease.
            - Suggest closest **pharmacies or medical stores** for easy access.
            - Specify **medication names and timings** for each day.
            - Define **dosage, frequency, and special instructions** (e.g., take with food, avoid certain interactions).
            - Warn about **side effects and possible drug interactions**.
            - Suggest **over-the-counter (OTC) medications or supplements**, if applicable.
            - Include reminders for **refills or doctor follow-ups** if necessary.

            **Patient Details**:
            - **Age**: {age}
            - **Disease**: {disease}
            - **Weight**: {weight} kg
            - **Symptoms**: {symptoms}
            - **Disease Period**: {disease_period}
            - **Place**: {place}

            {self.__tip_section()}
            """),
            expected_output="A detailed 7-day medication schedule including medicine names, dosages, timing, and precautions.",
            agent=agent,
        )

    def generate_fitness_plan(self, agent, age, disease, weight, symptoms, disease_period):
        return Task(
            description=dedent(f"""
            **Task**: Develop a 7-day exercise and wellness routine.

            **Description**: As the Fitness & Rehabilitation Expert Agent, your goal is to design a fitness plan suitable for the patient's condition and physical abilities.
            
            **Steps to follow**:
            - Assess the patient's **physical condition, limitations, and disease-specific concerns**.
            - Recommend **safe and effective exercises** (e.g., yoga, stretching, light cardio).
            - Provide a **structured daily exercise plan** with intensity levels.
            - Offer **alternative exercises** in case of injuries or mobility issues.
            - Include **relaxation techniques** (e.g., breathing exercises, meditation) to promote mental health.
            - Recommend **safe and effective medicines and their time of dosage**

            **Patient Details**:
            - **Age**: {age}
            - **Disease**: {disease}
            - **Weight**: {weight} kg
            - **Symptoms**: {symptoms}
            - **Disease Period**: {disease_period}

            {self.__tip_section()}
            """),
            expected_output="A structured 7-day fitness & wellness routine with exercises, duration, and safety tips.",
            agent=agent,
        )