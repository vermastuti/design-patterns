package behavioural.strategy.classes;

import behavioural.strategy.interfaces.QuackBehavior;

public class Squeak implements QuackBehavior {
    @Override
    public void quack() {
        System.out.println("Squeak");
    }
    
}
