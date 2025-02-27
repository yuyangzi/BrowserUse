#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@CreateTime    : 2025/2/26 12:30
@Author  : wang yi ming
@file for: 
"""
from browser_use.browser.browser import Browser, BrowserConfig
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from browser_use import Agent
from pydantic import SecretStr
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
from dotenv import load_dotenv

load_dotenv()

# Initialize the model
# llm = ChatOllama(model="deepseek-r1", num_ctx=32000)

# api_key = os.getenv("DASHSCOPE_API_KEY")
api_key = os.getenv("DEEPSEEK_API_KEY")

print(api_key)
# base_url = 'https://dashscope.aliyuncs.com/compatible-mode/v1'
base_url = 'https://api.siliconflow.cn/v1'
llm = ChatOpenAI(base_url=base_url, model='Qwen/Qwen2.5-32B-Instruct', api_key=SecretStr(api_key))

# llm = ChatOllama(model='deepseek-r1:14b')

browser = Browser(
    config=BrowserConfig(
        # NOTE: you need to close your chrome browser - so that this can open your browser in debug mode
        # d:\Learning\AI-related\browser-use-demo\.env注意：您需要关闭您的Chrome浏览器，以便此操作可以在调试模式下打开您的浏览器
        chrome_instance_path=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    )
)


# task = (
#     "1. Go to http://www.csrc.gov.cn/csrc/xwfb/index.shtml"
#     "2. search for '四川银行' in the search box"
#     "3. click on the first article link"
#     "4. 提取文章正文内容，并加以整理和精简."
#     "5. Go to https://outlook.live.com/mail/0/"
#     "6. click 'New mail' button"
#     "7. To：'wangyiming19950222@gmail.com'"
#     "8. Add a subject：'四川银行新闻'"
#     "9. 将的提取到的内容以中文形式写入邮件正文部分"
#     "10. click 'Send' button 发送邮件"
# ),


# task = ("1. Open 'https://10.9.4.111/v1/main-userSetting/home'"
#         "2. If need to log in in between, username: wym, password: lb202020202020"
#         "3. Open 'https://10.9.4.111/v1/bts-other/associated-settings/group-management'"
#         "4. search for '中国建设银行' in the search box"
#         "5. click first row link"
#         "6. search for '上海' in the search box"
#         "7. click '已注销' button"
#         "8. clear search filter"
#         "9. click '存续' button"
#         ),

async def main():
    agent = Agent(
        task=("1. Compare the price of gpt-4o and DeepSeek-V3"
              "2. 将对比结果整理成易于观看的内容"
              "5. Go to https://outlook.live.com/mail/0/"
              "6. click 'New mail' button"
              "7. To：'wangyiming19950222@gmail.com'"
              "8. Add a subject：'Compare the price of gpt-4o and DeepSeek-V3'"
              "9. 将整理后的内容以中文形式写入邮件正文部分"
              "10. click 'Send' button 发送邮件"
              ),
        llm=llm,
        browser=browser,
        use_vision=False
    )

    result = await agent.run()

    print('=========================================')
    print(result)


asyncio.run(main())
