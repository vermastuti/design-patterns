package behavioural.observer.classes;

import behavioural.observer.interfaces.Observer;

public class CurrentConditionsDisplay implements Observer {

    private float temperature;
    private float humidity;
    private float pressure;
    private WeatherData weatherData;

    public CurrentConditionsDisplay(WeatherData weatherData) {
        this.weatherData = weatherData;
        this.weatherData.registerObserver(this);
    }

    @Override
    public void update(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        System.out.println("Current conditions: " + this.temperature + "°C, " + this.humidity + "% humidity, " + this.pressure + " hPa");

    }

    
}
