class State:
    """Base state class defining the interface for all concrete states."""
    def handle(self, context):
        raise NotImplementedError("Subclasses must implement this method")


class ConcreteStateA(State):
    """A concrete state implementation."""
    def handle(self, context):
        print("State A handling request and transitioning to State B")
        context.state = ConcreteStateB()


class ConcreteStateB(State):
    """Another concrete state implementation."""
    def handle(self, context):
        print("State B handling request and transitioning to State A")
        context.state = ConcreteStateA()


class Context:
    """The context class that maintains a reference to the current state."""
    def __init__(self, state: State):
        self.state = state

    def request(self):
        """Delegate the request to the current state."""
        self.state.handle(self)


if __name__ == "__main__":
    # Initialize context with a concrete state
    initial_state = ConcreteStateA()
    context = Context(initial_state)

    # Simulate state transitions
    context.request()  # State A -> State B
    context.request()  # State B -> State A
    context.request()  # State A -> State B