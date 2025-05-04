package behavioural.observer.classes;

import behavioural.observer.interfaces.Observer;

public class StatisticsDisplay implements Observer{


    private float temperature;
    private float humidity;
    private float pressure;
    private WeatherData weatherData;

    public StatisticsDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        this.weatherData.registerObserver(this);
    }

    @Override
    public void update(float temperature, float humidity, float pressure) {
        // Implement the logic to display the statistics based on the updated weather data
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        System.out.println("Statistics: " + this.temperature + "F degrees and " + this.humidity + "% humidity" 
                + " and " + this.pressure + " hPa");
    }

   

}
