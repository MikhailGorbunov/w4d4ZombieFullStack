from flask import Blueprint, Flask, redirect, render_template, request
import repositories.biting_repository as biting_repository
from models.biting import Biting
import repositories.human_repository as human_repository
import repositories.zombie_repository as zombie_repository
import pdb


bitings_blueprint = Blueprint("bitings", __name__)

# INDEX
@bitings_blueprint.route("/bitings")
def bitings():
    bitings = biting_repository.select_all()
    return render_template("bitings/index.html", bitings=bitings)


# NEW

@bitings_blueprint.route("/bitings/new")
def new_bitings():
    human = human_repository.select_all()
    zombie = zombie_repository.select_all()
    return render_template("bitings/new.html", humans=human, zombies=zombie)




# CREATE
@bitings_blueprint.route("/bitings", methods= ["POST"])
def create_biting():
    
    #pdb.set_trace()
    human = human_repository.select(request.form["human_id"])
    zombie = zombie_repository.select(request.form["zombie_id"])

    new_biting= Biting(human, zombie)
    biting_repository.save(new_biting)
    return redirect("/bitings")




# EDIT

@bitings_blueprint.route("/bitings/<id>/edit")
def edit_biting(id):
    biting = biting_repository.select(id)
    human = human_repository.select_all()
    
    zombie = zombie_repository.select_all()
    return render_template('bitings/edit.html',zombies=zombie, humans=human, biting=biting)



# UPDATE
@bitings_blueprint.route("/bitings/<id>", methods= ['POST'])
def update_biting(id):
    human1 = human_repository.select_all()
    zombie1 = zombie_repository.select_all()
    human = human_repository.select(request.form["human_id"])
    zombie = zombie_repository.select(request.form["zombie_id"])
    biting= Biting(human, zombie, id)
    biting_repository.update(biting)
    return redirect("/bitings")




# DELETE


@bitings_blueprint.route("/bitings/<id>/delete", methods=["POST"])
def delete_biting(id):
    biting_repository.delete(id)
    return redirect("/bitings")