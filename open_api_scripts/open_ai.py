import os
import openai
openai.api_key = os.getenv("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")
openai.Model.list()


print(openai.Model.list())