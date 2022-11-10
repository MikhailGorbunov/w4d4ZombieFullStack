from db.run_sql import run_sql
# from models.human import Human
# from models.zombie import Zombie 
from models.biting import Biting
import repositories.zombie_repository as zombie_repository  
import repositories.human_repository as human_repository  

def save(biting):
    sql = "INSERT INTO bitings (zombie_id, human_id) VALUES (%s, %s) RETURNING id"
    values = [biting.zombie.id, biting.human.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id


def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)
    for result in results:
        zombie = zombie_repository.select(result["zombie_id"])
        human = human_repository.select(result["human_id"])
        biting = Biting(zombie, human, result["id"])
        bitings.append(biting)
        
    return bitings



def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        zombie = zombie_repository.select(result["zombie_id"])
        human = human_repository.select(result["human_id"])       
        biting= Biting(zombie, human, result["id"])
    return biting


def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(biting):
    sql = "UPDATE bitings SET (zombie_id, human_id) = (%s, %s) WHERE id = %s"
    values = [biting.zombie.id, biting.human.id, biting.id]
    run_sql(sql, values)

    

   