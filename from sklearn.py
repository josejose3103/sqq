from sklearn.metrics import mean_squared_error
from prophet import Prophet

df = pd.read_csv('https://raw.githubusercontent.com/facebook/prophet/main/examples/example_wp_log_peyton_manning.csv')

model = Prophet()
model.fit(df)
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)
fig = model.plot(forecast)
plt.show()