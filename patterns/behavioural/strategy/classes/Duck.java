package behavioural.strategy.classes;
import behavioural.strategy.interfaces.FlyBehavior;
import behavioural.strategy.interfaces.QuackBehavior;

class Duck{
    /*  The strategy pattern is used to define a family of algorithms, 
        encapsulate each one, and make them interchangeable. 
        Strategy lets the algorithm vary independently from clients that use it.

        Design Principles:
        1. Identify the aspects of your application that vary and separate them from what stays the same. Encapsulate what varies.
        2. Program to an interface, not an implementation.
        3. Favor composition over inheritance.

    */

    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;
    
    public void performFly(){
        flyBehavior.fly();
    }

    public void performQuack(){
        quackBehavior.quack();
    }


    public void swim(){
        System.out.println("Swim");
    }

    public void display(){
        System.out.println("Display");
    }

    public void setFlyBehavior(FlyBehavior fb) {
        flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb) {
        quackBehavior = qb;
    }

}