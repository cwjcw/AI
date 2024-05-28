import os
from openai import OpenAI
import pandas as pd

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
MODEL = "gpt-4o-2024-05-13"

file_path = r'C:\Users\Administrator\Desktop\临时文件\损益SQL数据.xlsx'
df = pd.read_excel(file_path)

response = client.chat.completions.create(
  model=MODEL,
  messages=[
    {"role": "system", "content": "你是一个数据分析师，对输入的dataframe格式的数据进行分析,并输出你分析之后的结果,结果不需要包含"},
    {"role": "user", "content":f"{df}" }
  ]
)
print(response.choices[0].message.content)