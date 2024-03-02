import requests
import json

class Gemeni:

     def __init__(self, token):
        self.token = token
        self.url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + self.token

     
     def generateContent(self, text):
            headers = {'Content-Type': 'application/json'}
            data = {
               'contents': [{
                     'parts': [{
                      'text': text
                     }]
               }]
            }
            json_data = json.dumps(data)
            response = requests.post(self.url, headers=headers, data=json_data)
            response = response.json()
            try:
               return response['candidates'][0]['content']['parts'][0]['text']
            except KeyError as e:
               print(f"Error: La clave {e} no está presente en el diccionario.")
               return "Algo salió mal :("

            return response['candidates'][0]['content']['parts'][0]['text']
            # print(response['candidates'][0]['content']['parts'][0]['text'])
