package behavioural.strategy.classes;


class MallardDuck extends Duck{

    public MallardDuck(){
        flyBehavior = new FlyWithWings();
        quackBehavior = new Quack();
    }
    
    @Override
    public void display(){
        System.out.println("Display Mallard Duck");
    }
}