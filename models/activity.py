from shared import db


class Activity(db.Model):
    __tablename__ = 'activity'
    id = db.Column('id', db.Integer, primary_key=True)
    description = db.Column('description', db.String(255), nullable=False)
    farm_id = db.Column('farm_id', db.Integer, db.ForeignKey('farm.id'), nullable=False)
    date = db.column('date', db.Date, nullable=False)
    resource = db.comumn('resource', db.String(255), db.ForeignKey('resource.id') nullable=False)

    def __init__(self, name, address_id):
        self.description = description
        self.farm_id = farm_id
        self.date = date
        self.resource = resource
