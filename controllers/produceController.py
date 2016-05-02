import os
from main import app
from models import Produce, Image, Farm, Address,

class ProduceController:

    def add_produce(farm_id):
            errors = []
            if request.method == 'POST':
                name = request.form.get('name', '')
                description = request.form.get('description', '')
                category = request.form.get('category', '')
                selected_units = request.form.get('units', '')
                prices = {}
                for sel_unit in selected_units:
                    prices[sel_unit] = request.form.get('price' + selected_units)
                file = request.files['prod_image']
                if not name:
                    errors.append('Name cannot be empty')
                if not description:
                    errors.append('Description cannot be empty')
                if not category:
                    errors.append('Please choose a category for the produce')
                if not selected_units:
                    errors.append('Please choose the units you wish to sell in')
                if len(prices) < len(selected_units):
                    errors.append('Please enter the prices for the produce')
                if not file or not utilities.allowed_file(file.filename):
                    errors.append("Please upload 'png', 'jpg', 'jpeg' or 'gif' image for produce")
                if not errors:
                    directory = os.path.join(app.config['UPLOAD_FOLDER'], 'produce/' + str(farm_id) + '/')
                    os.makedirs(os.path.dirname(directory), exist_ok=True)
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(directory, filename))
                    img = Image('produce/' + str(farm_id) + '/' + filename)
                    db.session.add(img)
                    db.session.flush()
                    prod = Produce(name, description, category, img.id)
                    db.session.add(prod)
                    db.session.flush()
                    db.session.add(Grows(farm_id, prod.id))
                    for p in prices:
                        db.session.add(Price(prod.id, p, prices[p]))
                        db.session.flush()
                    db.session.commit()
                    return 'Success'
            units = Unit.query.all()
            current_farm = Farm.query.get(farm_id)
            if not current_farm:
                abort(404)
            farm_address = Address.query.get(current_farm.address_id)
            return render_template('add_produce.html', units=units, farm=current_farm, address=farm_address, errors=errors)
