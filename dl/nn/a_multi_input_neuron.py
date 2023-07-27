
"""
A trivial neuron - multiple inputs, multiple weights ->  one output
"""

class Neuron:
    
    def __init__ (self, w) :
        self.weight = w

    def predict(self, input):
        if len(input) == 0:
            return "Inputt length is 0"
        if len(input) != len(self.weight):
            return "Number of input elements do not match the weights initialized with"
        output = []
        for i in range(len(input)):
            output.append( input[i] * self.weight[i])
        return output

def main():
    weight = [0.5, 0.3, 2, 0, 1.5]
    input = [1200, 100, 10, 12, 2]
    the_neuron = Neuron(weight)
    answer = the_neuron.predict(input)
    print(f" With input {input}, weight {weight} , prediction is : {answer}")

print(f" __name__ is {__name__}. What did you expect ?")

if __name__ == "__main__" :
    main()
