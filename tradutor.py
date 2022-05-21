import os, requests, uuid, json



class Tradutor():
    def __init__(self,chaveApi,regiao):
        self.resource_key = chaveApi
        self.region = regiao
        self.endpoint = 'https://api.cognitive.microsofttranslator.com/'
       
        self.headers = {
                'Ocp-Apim-Subscription-Key': self.resource_key,
                'Ocp-Apim-Subscription-Region': self.region,
                'Content-type': 'application/json',
                'X-ClientTraceId': str(uuid.uuid4())
            }

    def traduzir(self,de,para,texto):
        try:
            path = '/translate?api-version=3.0'
            params = f'&from={de}&to={para}&'
            constructed_url = self.endpoint + path + params
            body = [{
                    'text' : f'{texto}'
                }]
            request = requests.post(constructed_url, headers=self.headers, json=body)
            response = request.json()
            if 'error' in response:
                raise Exception
            return response[0]
        except Exception as e:
            return self.traduzir('en','pt-br', response['error']['message'])
    
    def detectarIdioma(self,texto):
        path = '/detect?api-version=3.0'
        constructed_url = self.endpoint + path
        body = [{
            'text' : f'{texto}'
        }]
        request = requests.post(constructed_url, headers=self.headers, json=body)
        response = request.json()
        return response
