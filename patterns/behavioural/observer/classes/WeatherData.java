package behavioural.observer.classes;

import java.util.List;

import behavioural.observer.interfaces.Observer;
import behavioural.observer.interfaces.Subject;

public class WeatherData implements Subject{

    /* The Observer Pattern defines a one-to-many dependency between objects so that when one object changes state,
     * all its dependents are notified and updated automatically.
     * 
     * Design Principles:
     * 1. Strive for loosely coupled designs between objects that interact.
     */

    // instance variables declaration
    List<Observer> observers;
    private float temperature;
    private float humidity;     
    private float pressure;
    
    // Constructor
    public WeatherData() {
        observers = new java.util.ArrayList<>();
    }

    public void measurementsChanged() {
        // Notify all observers about the change in measurements
        notifyObservers();
    }

    public void setMeasurements(float temperature, float humidity, float pressure) {
        this.temperature = temperature;
        this.humidity = humidity;
        this.pressure = pressure;
        measurementsChanged();
    }

    public float getTemperature() {
        return this.temperature;
    }
    public float getHumidity() {
        return this.humidity;
    }
    public float getPressure() {
        return this.pressure;
    }

    @Override
    public void registerObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(getTemperature(), getHumidity(), getPressure());
        }
    }


    
}
