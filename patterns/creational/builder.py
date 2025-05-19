class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show_parts(self):
        return ", ".join(self.parts)


class Builder:
    def build_part_a(self):
        raise NotImplementedError

    def build_part_b(self):
        raise NotImplementedError

    def get_result(self):
        raise NotImplementedError


class ConcreteBuilder(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA")

    def build_part_b(self):
        self.product.add_part("PartB")

    def get_result(self):
        return self.product


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()


# Client code
if __name__ == "__main__":
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    print("Product parts:", product.show_parts())