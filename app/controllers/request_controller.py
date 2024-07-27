import requests

class RequestAPI():
    def request_cep(self, _cep):
        from .cep_controller import CEPController
        controller_cep = CEPController()
        response = requests.get(f'https://brasilapi.com.br/api/cep/v1/{_cep}')
        if response.status_code == 200:
            obj_json = response.json()
            cep = controller_cep.incluir_cep(
                _cep         = obj_json['cep'],
                _estado      = obj_json['state'],
                _cidade      = obj_json['city'],
                _bairro      = obj_json['neighborhood'],
                _rua         = obj_json['street'],
                _atualizacao = 'Atualizacao Automatica'
            )
            return cep
        else:
            response = requests.get(f'https://viacep.com.br/ws/{_cep}/json')
            if response.status_code == 200:
                obj_json = response.json()
                cep = controller_cep.incluir_cep(
                    _cep         = obj_json['cep'],
                    _estado      = obj_json['uf'],
                    _cidade      = obj_json['localidade'],
                    _bairro      = obj_json['bairro'],
                    _rua         = obj_json['logradouro'],
                    _atualizacao = 'Atualizacao Automatica - Via CEP'
                )
                return cep
            else:
                return None
