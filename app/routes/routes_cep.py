from app import app
from flask import jsonify, abort
from ..controllers.cep_controller import CEPController
from ..controllers.request_controller import ResquestAPI
from flasgger import swag_from

cep_controller = CEPController()
resquest_api   = ResquestAPI()

#Metodos do tipo GET
@app.route('/cep/<int:cep>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'cep',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'O Cep que deverá ser pesquisado'
        }
    ],
    'responses': {
        200: {
            'description': 'Informações do CEP',
            'schema': {
                'type': 'object',
                'properties': {
                    'cep': {
                        'type': 'string',
                        'description': 'O CEP'
                    },
                    'estado': {
                        'type': 'string',
                        'description': 'O estado'
                    },
                    'cidade': {
                        'type': 'string',
                        'description': 'A cidade'
                    },
                    'bairro': {
                        'type': 'string',
                        'description': 'O bairro'
                    },
                    'rua': {
                        'type': 'string',
                        'description': 'A rua'
                    }
                }
            }
        },
        404: {
            'description': 'CEP não encontrado!',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {
                        'type': 'string',
                        'description': 'CEP não encontrado!'
                    }
                }
            }
        }
    }
})
def traz_cep(cep):
    result = cep_controller.retorna_cep(cep)
    if result:
        return jsonify({
            'cep': result.cep,
            'estado': result.estado,
            'cidade': result.cidade,
            'bairro': result.bairro,
            'rua': result.rua
        })
    else:
        abort(404, description="CEP não encontrado")

#Metodos do tipo PUT
@app.route('/cep/<int:cep>/auto_repair', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'cep',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'O Cep que deverá ser consertado'
        }
    ],
    'responses': {
        200: {
            'description': 'Atualizado com Sucesso',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'description': 'CEP atualizado com sucesso!'
                    }
                }
            }
        },
        404: {
            'description': 'Falha ao localizar CEP',
            'schema': {
                'type': 'object',
                'properties': {
                    'erro': {
                        'type': 'string',
                        'description': 'CEP não encontrado!'
                    }
                }
            }
        }
    }
})
def conserta_cep(cep):
    result = cep_controller.retorna_cep(cep)
    if not result:
        return jsonify({
            'erro' : 'CEP não encontrado!'    
        }), 404
    else:
        cep_controller.deleta_cep(cep)
        result = resquest_api.resquest_cep(cep)
        if result:
            return jsonify({
                'message' : 'CEP atualizado com sucesso!'    
            })
