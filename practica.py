import requests

url = "https://myacademy.oracle.com/player/play"
params = {
    'in_sessionid': '229A393539012232',
    'classroom_id': '72576717',
    'in_lp_id': '72456973',
    'in_from_module': 'CLMSCHANNEL.PRVIEW~CLMSLEARNINGPATHDETAILS.PRMAIN',
    'in_filter': '%26in_offeringId%3D1280703384'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("Solicitud exitosa")
    # Puedes imprimir o manejar la respuesta aquí
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")