
"""
A trivial neuron - one input, one output
"""

class Neuron:
    
    def __init__ (self, w) :
        self.weight = w

    def predict(self, input):
        return input * self.weight

def main():
    weight = 0.5
    input = 1200
    the_neuron = Neuron(weight)
    answer = the_neuron.predict(input)
    print(f" With input {input}, weight {weight} , prediction is : {answer}")

print(f" __name__ is {__name__}. What did you expect ?")

if __name__ == "__main__" :
    main()
