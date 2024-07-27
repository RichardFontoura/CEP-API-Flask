from app import app
from flask import jsonify, abort
from ..controllers.cep_controller import CEPController
from ..controllers.request_controller import RequestAPI
from flasgger import swag_from

cep_controller = CEPController()
resquest_api   = RequestAPI()

#Metodos do tipo GET
@app.route('/cep/<string:cep>', methods=['GET'])
@swag_from({
    'parameters': [
        {
            'name': 'cep',
            'in': 'path',
            'type': 'string',
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
    cep = cep.replace("-", "")
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
@app.route('/cep/<string:cep>/auto_repair', methods=['PUT'])
@swag_from({
    'parameters': [
        {
            'name': 'cep',
            'in': 'path',
            'type': 'string',
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
    cep = cep.replace("-", "")
    result = cep_controller.retorna_cep(cep)
    if not result:
        return jsonify({
            'erro' : 'CEP não encontrado!'    
        }), 404
    else:
        cep_controller.deleta_cep(cep)
        result = resquest_api.request_cep(cep)
        if result:
            return jsonify({
                'message' : 'CEP atualizado com sucesso!'    
            })

#Exception
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Route not found. You cannot use this route."), 404

@app.errorhandler(405)
def page_not_found(e):
    return jsonify(error="The method is not allowed for the requested URL."), 405
