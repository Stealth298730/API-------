from db import Table, Session


def add_table(ceo, club):
    with Session() as session:
        table = table(ceo=ceo, club=club)
        session.add(table)
        session.commit()
        session.refresh(table)
        return table.id
    
def get_tables():
    with Session() as session:
        return session.query(Table).all()


def get_table(id):
    with Session() as session:
        return session.query(Table).where(Table.id == id).first()

def update_table(id, author, text):
    with Session() as session:
        table = session.query(Table).filter_by(id=id).first()
        table.author = author
        table.text = text
        session.commit()
        return "Стіл успішно заказано"
    

def delete_table(id):
    with Session() as session:
        table = session.query(Table).filter_by(id=id).first()
        session.delete(Table)
        session.commit()
        return "Стіл успішно видалено"
