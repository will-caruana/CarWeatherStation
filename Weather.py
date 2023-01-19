import obd

# Connect to the OBD-II adapter
connection = obd.OBD()

# Get barometric pressure
pressure_cmd = obd.commands.BAROMETRIC_PRESSURE
pressure_response = connection.query(pressure_cmd)
pressure = pressure_response.value.magnitude

# Get temperature
temperature_cmd = obd.commands.AMBIANT_AIR_TEMP
temperature_response = connection.query(temperature_cmd)
temperature = temperature_response.value.magnitude

# Create and fit linear regression model
model = LinearRegression()
model.fit(np.array(pressure).reshape(-1,1), np.array(temperature))

# Predict temperature for a given pressure
pressure_test = 1019
temperature_pred = model.predict(np.array(pressure_test).reshape(-1,1))
print("Predicted temperature: {:.2f} C".format(temperature_pred[0]))
