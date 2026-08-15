def greet(input):
    if "hello" in input:
        return "hello, there "
    else:
        return "I'm not sure what you mean"

greeting = greet("hello, computer")
print(greeting + "Julien")
