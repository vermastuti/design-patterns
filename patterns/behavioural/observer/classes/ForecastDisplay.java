package behavioural.observer.classes;

import behavioural.observer.interfaces.Observer;

public class ForecastDisplay implements Observer{


    private float temperature;
    private float humidity;
    private WeatherData weatherData;

    public ForecastDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        this.weatherData.registerObserver(this);
    }


    @Override
    public void update(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;   

        // Implement the logic to display the forecast based on the updated weather data
        System.out.println("Forecast: " + this.temperature + "F degrees and " + this.humidity + "% humidity");
    }
   

}
