from g4f.client import Client
from main_api.main_api.ml_model.prompts.analyze_user_loan_classification_prompt_text import analyze_user_loan_classification_prompt_text
import pandas as pd
import json


class Chatbot:
    def __init__(self):
        self.client = Client()

        self.analyze_user_loan_classification_prompt = analyze_user_loan_classification_prompt_text
        self.column_descriptions = pd.read_excel('./variables_description.xlsx').to_dict('records')

        self.retries = 0

        self.MAX_RETRIES = 3

    def get_response(self,
                     prediction: int,
                     data: dict,
                     tree_rules: str):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": self.analyze_user_loan_classification_prompt.format(
                    column_descriptions=self.column_descriptions,
                    prediction=prediction,
                    data=data,
                    tree_rules=tree_rules
                )}],
            )

            return json.loads(response.choices[0].message.content)

        except Exception as e:
            self.retries += 1
            if self.retries < self.MAX_RETRIES:
                return self.get_response(prediction=prediction,
                                         data=data,
                                         tree_rules=tree_rules
                                         )
            else:
                return {"error": f"Failed to get response from the chatbot. Error: {e}"}
