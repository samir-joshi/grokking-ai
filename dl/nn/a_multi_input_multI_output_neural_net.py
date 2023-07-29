
"""
A trivial neuron network - multiple inputs, multiple neurons each having its own weight set ->  multiple outputs (one for each neuron)
"""


class Neuron:
    
    def __init__ (self, w) :
        self.weight = w

    def predict(self, input):
        if len(input) == 0:
            print( "Inputt length is 0")
            return
        if len(input) != len(self.weight):
            print ( "Number of input elements do not match the weights initialized with")
            return
        output = 0
        for i in range(len(input)):
            output +=  input[i] * self.weight[i]
        return output
    

class NeuralNet:
    def __init__ (self, neurons):
        self.neurons = neurons

    def predict(self, input):
        if len(input) == 0:
            return "Inputt length is 0"
        
        output = []
        for i in range(len(self.neurons)):
            output.append(  self.neurons[i].predict( input) )
        return output




def main():
    weights = [ [0.5, 0.3, 2, 0, 1.5],
                [0.1, 0.2, 1, 10, -1.5],
                [0, 1.3, 0.2, 1.1, 0.5]
               ]
    input = [1200, 100, 10, 12, 2]
    the_neurons = [ Neuron(weights[0]), Neuron(weights[1]), Neuron(weights[2]) ]
    the_neural_network = NeuralNet(the_neurons)
    answer = the_neural_network.predict(input)
    print(f" With input {input}, weight {weights} , prediction is : {answer}")


if __name__ == "__main__" :
    main()
