import joblib


model = joblib.load('housing-ml.joblib')

#inputs
rooms = int(input("number of rooms: "))
baths = int(input("number of bathrooms: "))
landsize = int(input("landsize: "))
lat = float(input("lattitude: "))
lon = float(input("longitude: "))


#predictions
prediction = model.predict([[rooms, baths, landsize, lat, lon]])
print(f"the price should be: {prediction}")
