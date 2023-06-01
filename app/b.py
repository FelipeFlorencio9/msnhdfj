from flask import Flask,jsonify,make_response,request

app = Flask(__name__)

@app.route("/addsemenete",methods=['POST'])
def return_seeds():

  seed_name = request.json["name_seed"]
  per_week_recommended_amount_of_water = request.json["recommended_amount_of_water_per_week"]
  per_week_amount_of_wateringper_week_amount_of_watering = request.json["amount_of_waterimg_per_week"]
  advice = request.json["recomendations"]


  return make_response(
        jsonify(
    
            status = "adicionada",
            name_seed = seed_name,
            recommended_amount_of_water_per_week = per_week_recommended_amount_of_water,
            amount_of_waterimg_per_week = per_week_amount_of_wateringper_week_amount_of_watering,
            recomendations = advice
            
        )
    )

app.run(debug=True, port=8080)