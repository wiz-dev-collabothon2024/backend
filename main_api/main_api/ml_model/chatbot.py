from g4f.client import Client
from main_api.main_api.ml_model.prompts.analyze_user_loan_classification_prompt_text import analyze_user_loan_classification_prompt_text
import pandas as pd


class Chatbot:
    def __init__(self):
        self.client = Client()

        self.analyze_user_loan_classification_prompt = analyze_user_loan_classification_prompt_text
        self.column_descriptions = pd.read_excel('./variables_description.xlsx').to_dict('records')

    def get_response(self,
                     prediction: int,
                     data: dict,
                     tree_rules: str):
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": self.analyze_user_loan_classification_prompt.format(
                column_descriptions=self.column_descriptions,
                prediction=prediction,
                data=data,
                tree_rules=tree_rules
            )}],
        )

        return response
