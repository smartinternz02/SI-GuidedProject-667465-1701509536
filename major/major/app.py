


#         # Now you can use these variables with your model for prediction
#         # For example:


# from flask import Flask, render_template, request
# import pickle

# app = Flask(__name__, template_folder='templates')

# # Load the model
# model = pickle.load(open("C:\\Users\\Ganesh\\Desktop\\major\\flask\\liver.pkl", "rb"))

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/pred")
# def index():
#     return render_template("index.html")

# @app.route("/out", methods=['POST', 'GET'])
# def predict():
#     if request.method == 'POST':
#         # ... (your existing code for handling form data)
           
#         AGE = float(request.form['AGE'])
#         Gender = float(request.form['Gender'])
#         Place = float(request.form["Place (Location where the patient lives)"])
#         Duration_of_alcohol_consumption = float(request.form["Duration of alcohol consumption"])
#         Quantity_of_alcohol_consumption = float(request.form["Quantity of alcohol consumption"])
#         Type_of_alcohol_consumed = float(request.form["Type of alcohol consumed"])
#         Blood_pressure = float(request.form["Blood pressure (mmhg)"])
#         Obesity = float(request.form["Obesity"])
#         Family_history_of_cirrhosis_hereditary = float(request.form["Family history of cirrhosis"])
#         Hemoglobin = float(request.form["Hemoglobin (g/dL)"])
#         PCV = float(request.form["PCV (X)"])
#         RBC = float(request.form["RBC (million cells/microliter)"])
#         MCV = float(request.form["MCV (femtoliters/cell)"])
#         MCH = float(request.form["MCH (picograms/cell)"])
#         MCHC = float(request.form["MCHC (grams/deciliter)"])
#         Total_Count = float(request.form["Total Count"])
#         Polymorphs = float(request.form["Polymorphs (X)"])
#         Lymphocytes = float(request.form["Lymphocytes (X)"])
#         Monocytes = float(request.form["Monocytes (X)"])
#         Eosinophils = float(request.form["Eosinophils (X)"])
#         Basophils = float(request.form["Basophils (%)"])
#         Platelet_Count = float(request.form["Platelet Count (lakhs/mm)"])
#         Direct = float(request.form["Direct    (mg/dl)"])
#         Indirect = float(request.form["Indirect     (mg/dl)"])
#         Total_Protein = float(request.form["Total Protein     (g/dl)"])
#         Albumin = float(request.form["Albumin   (g/dl)"])
#         Globulin = float(request.form["Globulin  (g/dl)"])
#         AL_Phosphatase = float(request.form["AL.Phosphatase      (U/L)"])
#         SGOT_AST = float(request.form["SGOT/AST      (U/L)"])
#         USG_Abdomen = float(request.form["USG Abdomen (diffuse liver or  not)"])
#         Outcome = float(request.form["Predicted Value(Out Come-Patient suffering from liver  cirrosis or not)"])

#         prediction = model.predict([[AGE, Gender, Place, Duration_of_alcohol_consumption, Quantity_of_alcohol_consumption,
#                                     Type_of_alcohol_consumed, Blood_pressure, Obesity,
#                                     Family_history_of_cirrhosis_hereditary, Hemoglobin, PCV, RBC, MCV, MCH, MCHC,
#                                     Total_Count, Polymorphs, Lymphocytes, Monocytes, Eosinophils,
#                                     Basophils, Platelet_Count, Direct, Indirect, Total_Protein,
#                                     Albumin, Globulin, AL_Phosphatase, SGOT_AST, USG_Abdomen, Outcome]])
#         result_text = "The person is suffering from liver cirrhosis." if prediction[0] == 1 else "The person is not suffering from liver cirrhosis."
#         return render_template("result.html", prediction=result_text)

#     return render_template("home.html")

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='templates')

# Load the model
model = pickle.load(open("C:\\Users\\Ganesh\\Desktop\\major\\flask\\liver1.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/pred")
def index():
    return render_template("index.html")

@app.route("/out", methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        try:
            # ... (your existing code for handling form data)
           
            # Convert numeric form inputs to float
            Age = float(request.form["Age"])
            Bilirubin = float(request.form["Bilirubin"])
            Cholesterol = float(request.form["Cholesterol"])
            Albumin = float(request.form["Albumin"])
            # Convert other attributes to appropriate types
            Drug = request.form['Drug']
            Sex = float(request.form['Sex'])
            Ascites = request.form["Ascites"]
            Hepatomegaly = request.form["Hepatomegaly"]
            Spiders = request.form["Spiders"]
            Edema = request.form["Edema"]
            Copper = float(request.form["Copper"])
            Alk_Phos = float(request.form["Alk_Phos"])
            SGOT = float(request.form["SGOT"])
            Tryglicerides = float(request.form["Tryglicerides"])
            Platelets = float(request.form["Platelets"])
            Prothrombin = float(request.form["Prothrombin"])
            Stage = float(request.form["Stage"])

            # Use the form data to make predictions
            prediction = model.predict([[Age, Sex, Ascites, Hepatomegaly, Spiders, Edema,
                                          Bilirubin, Cholesterol, Albumin, Copper, Alk_Phos,
                                          SGOT, Tryglicerides, Platelets, Prothrombin, Stage]])
            result_text = "The person is suffering from liver cirrhosis." if prediction[0] == 1 else "The person is not suffering from liver cirrhosis."
            return render_template("result.html", prediction=result_text)
        except ValueError as e:
            # Handle the error when converting non-numeric values to float
            error_message = "Error: " + str(e)
            return render_template("error.html", error_message=error_message)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
