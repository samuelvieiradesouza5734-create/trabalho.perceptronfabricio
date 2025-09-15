import numpy as np

class Perceptron:
    def __init__(self):
        pass
    
    # Função de ativação: degrau
    def ativacao_funcao(self, x):
        return 1 if x >= 0 else 0

    # Treinamento do perceptron
    def train(self, inputs, outputs, learning_rate=1.0, epochs=500):
        self.inputs = inputs
        self.outputs = outputs
        self.learning_rate = learning_rate
        self.epochs = epochs

        # Inicialização dos pesos e bias
        w1 = np.random.rand(1,)
        w2 = np.random.rand(1,)
        bias = np.random.rand(1,)

        for i in range(epochs):
            for j in range(len(inputs)):
                z = w1 * inputs[j][0] + w2 * inputs[j][1] + bias
                prediction = self.ativacao_funcao(z)

                # Atualização dos pesos
                error = outputs[j][0] - prediction
                w1 = w1 + learning_rate * error * inputs[j][0]
                w2 = w2 + learning_rate * error * inputs[j][1]
                bias = bias + learning_rate * error

        return w1, w2, bias

    # Predição
    def predict(self, weights, x1, x2):
        z = x1 * weights[0] + x2 * weights[1] + weights[2]
        return self.ativacao_funcao(z)
        

# Execução principal
if __name__ == "__main__":
    inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
    outputs = [[0], [0], [0], [1]]  # Porta AND

    perceptron = Perceptron()

    # Treinamento
    weights = perceptron.train(inputs, outputs, learning_rate=1.0, epochs=500)

    # Teste da predição
    prediction = perceptron.predict(weights, 1, 1)

    print("Predição para (1, 1):", prediction)
    print("Predição para (0, 0):", perceptron.predict(weights, 0, 0))
    print("Predição para (0, 1):", perceptron.predict(weights, 0, 1))
    print("Predição para (1, 0):", perceptron.predict(weights, 1, 0)) 
    print("Predição para (1, 1):", perceptron.predict(weights, 1, 1))