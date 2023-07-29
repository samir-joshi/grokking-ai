
"""
A trivial neuron - one input, one output
"""

class Neuron:
    
    def __init__ (self, w) :
        self.weight = w

    def predict(self, input):
        return input * self.weight

    def update_weight(self, w):
        self.weight = w

def main():
    weight = 0.5
    lr = 0.001
    input = 200
    correct_answer = 2
    error = 1
    accetaple_error = 0.01

    the_neuron = Neuron(weight)
    
    counter = 25000

    # Learning loop
    while error > accetaple_error and counter > 0:
        counter -= 1

        # Predict
        answer = the_neuron.predict(input)
        print(f" With input {input}, weight {weight} , prediction is : {answer}")

        # Measure error and update weight
        error = (answer - correct_answer) ** 2
        print(f" New error is  {error} ")

        if error > accetaple_error:
            error_up = (correct_answer - (input*(weight + lr)) ) ** 2
            error_dn = (correct_answer - (input*(weight - lr)) ) ** 2
            
            if error > error_up:
                weight += lr
            elif error > error_dn:
                weight -= lr
            
            print(f" New weight is  {weight} ")

            the_neuron.update_weight(weight)
        else:
            print (" Done - the error is in the acceptable range !")
            break



print(f" __name__ is {__name__}. What did you expect ?")

if __name__ == "__main__" :
    main()
