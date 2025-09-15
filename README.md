Variação da taxa de aprendizado e da quantidade de épocas

Ao variar a taxa de aprendizado e o número de épocas, podemos observar comportamentos diferentes no treinamento:

Épocas (epochs): representam quantas vezes o algoritmo percorre todos os exemplos de treino.

Taxa de aprendizado: define o tamanho do passo que o perceptron dá a cada ajuste de peso.

Com uma taxa de aprendizado de 1.0 e 500 épocas, o perceptron consegue atualizar os pesos de forma mais rápida e alcançar o resultado esperado em menos tempo de execução. Isso deixa o código mais leve e eficiente.

2. Teste com a porta AND

Para treinar o perceptron com a porta lógica AND, alterei os valores de saída (outputs) da seguinte forma:

De:

[0], [1], [1], [1]


Para:

[0], [0], [0], [1]


Assim o perceptron passa a aprender o comportamento da porta AND.

3. Alterando para a função Degrau

Para utilizar a função Degrau no lugar da Sigmoid, criei um novo método de ativação e adaptei a função predict.

A Sigmoid tenta ser mais “suave” e detalhada: retorna valores entre 0 e 1, fazendo previsões mais graduais, como se desse um palpite probabilístico.

A Degrau é mais “direta”: se a soma ultrapassa um limite, retorna 1; caso contrário, retorna 0.
