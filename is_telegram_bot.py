import numpy

class BotChecker(object):
    def __init__(self, weights: numpy.array):
        self.weights = weights
    
    def is_bot(self, user_input_data: list) -> float:
        return 1 / (1 + numpy.exp(-numpy.dot(numpy.array(user_input_data), self.weights)))
    
    def save_weights(self, filename: str):
        numpy.save(filename, self.weights)
    
    @classmethod
    def detect(cls, inputs: list, outputs: list, num = 20000):
        weights = 2 * numpy.random.random((len(inputs[0]), 1)) - 1

        inputs = numpy.array(inputs)
        outputs = numpy.array(outputs).T

        for _ in range(num):
            output = 1 / (1 + numpy.exp(-numpy.dot(inputs, weights)))
            error = outputs - output
            adjustment = numpy.dot(inputs.T, error * output * (1 - output))
            weights += adjustment
        
        return cls(weights)
    
    @classmethod
    def load_from_file(cls, filename):
        return cls(numpy.load(filename))
