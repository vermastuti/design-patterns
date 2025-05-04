package behavioural.observer.interfaces;

public interface Subject {

    void notifyObservers();
    void registerObserver(Observer o);
    void removeObserver(Observer o);
    
}
