from app.models.cep import CEP
from app import db

class CEPController(): 
    def incluir_cep(self, _cep, _estado, _cidade, _bairro, _rua, _atualizacao):
        novo_cep = CEP(cep=_cep, estado=_estado, cidade=_cidade, 
                       bairro=_bairro, rua=_rua, atualizacao=_atualizacao)
        db.session.add(novo_cep)
        db.session.commit()
        return novo_cep
    
    def retorna_cep(self, _cep):
        from .request_controller import ResquestAPI
        request_api = ResquestAPI()
        cep = CEP.query.get(_cep)
        if not cep:
            cep = request_api.resquest_cep(_cep)
        return cep
    
    def atualiza_cep(self, _cep, _estado, _cidade, _bairro, _rua, _atualizacao):
        cep             = CEP.query.get(_cep)
        cep.estado      = _estado
        cep.cidade      = _cidade
        cep.bairro      = _bairro
        cep.rua         = _rua
        cep.atualizacao = _atualizacao
        db.session.commit()
        return cep
    
    def deleta_cep(self, _cep):
        cep = CEP.query.get(_cep)
        db.session.delete(cep)
        db.session.commit()
        return cep
    