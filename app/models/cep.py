from app import db

class CEP(db.Model):
    cep         = db.Column(db.String(8), nullable=False, primary_key=True)
    estado      = db.Column(db.String(2), nullable=False)
    cidade      = db.Column(db.String(50), nullable=False)
    bairro      = db.Column(db.String(50), nullable=False)
    rua         = db.Column(db.String(200), nullable=False)
    atualizacao = db.Column(db.String(20), nullable=False)