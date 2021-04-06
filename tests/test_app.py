def test_verifica_a_pagina_inicial(client):
   
    with client.test_client() as test_client:
        
        response = test_client.get('/home')
        assert response.status_code == 200
        
        texto = b'Pagina'
        assert texto in response.data

def test_verifica_pagina_que_nao_existe(client):
    with client.test_client() as test_client:
        response = test_client.get('/testando')
        assert response.status_code == 404
