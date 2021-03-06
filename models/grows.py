from shared import db


class Grows(db.Model):

    __tablename__ = 'grows'
    __table_args__ = (
        db.PrimaryKeyConstraint('farm_id', 'produce_id', name='OneFarmOneProduceOneEntry_CK'),
    )

    farm_id = db.Column('farm_id', db.Integer, db.ForeignKey("farms.id"))
    produce_id = db.Column('produce_id', db.Integer, db.ForeignKey('produces.id'))

    def __init__(self, farm_id, produce_id):
        self.farm_id = farm_id
        self.produce_id = produce_id
