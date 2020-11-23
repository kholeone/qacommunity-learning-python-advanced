@app.route('/')
@app.route('/animal/name' methods=['GET','POST'])

def animal_name():
    animal_list=["orca","big cat","wolf","crocodile","bear"]
    data = random.choice(animal_list)
    return Response(data, mimetype='text/plain')

@app.route('/animal/noise' methods=['GET','POST'])
def animal_noise():
    response=request.data.decode('utf-8')
    if response == "orca":
        noise = "eeuuuuuuuuuwwwww!"
    elif response == "big cat":
        noise = "rawr!"
    elif response == "wolf":
        noise = "owuuuuu!"
    elif response == "crocodile":
        noise = "grrr"
    elif response == "bear":
        noise = "rauugh!"
    else:
        noise = "wind noises"
    return Response(noise, mimetype='text/plain')
