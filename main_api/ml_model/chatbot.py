from g4f.client import Client
from g4f.Provider import Airforce, RetryProvider, Bing, Blackbox
from ml_model.prompts.analyze_user_loan_classification_prompt_text import analyze_user_loan_classification_prompt_text
import pandas as pd
import json


class Chatbot:
    def __init__(self):
        self.client = Client(
            provider=RetryProvider([Blackbox,
                                    Bing]))

        self.analyze_user_loan_classification_prompt = analyze_user_loan_classification_prompt_text
        self.column_descriptions = pd.read_excel('./ml_model/variables_description.xlsx').to_dict('records')

        self.retries = 0

        self.MAX_RETRIES = 3

    def get_response(self,
                     prediction: int,
                     data: dict,
                     tree_rules: str):
        response = None
        try:
            print('invoking the chatbot')
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user",
                           "content": self.analyze_user_loan_classification_prompt.format(
                               column_descriptions=self.column_descriptions,
                               prediction=prediction,
                               data=data,
                               tree_rules=tree_rules
                           )}],
            )

            if response is not None:
                print(response.choices[0].message.content)
                self.retries = 0

            return json.loads(response.choices[0].message.content)

        except Exception as e:
            self.retries += 1
            if self.retries < self.MAX_RETRIES:
                response = self.get_response(prediction=prediction,
                                         data=data,
                                         tree_rules=tree_rules
                                         )

                self.retries = 0

                return response

            else:
                self.retries = 0
                return {"error": f"Failed to get response from the chatbot. Error: {e}"}
