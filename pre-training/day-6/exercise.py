# Part 1: Single neuron. A neuron takes inputs (list of floats), has weights and a bias, computes: output = activation(sum(w*x) + bias). Implement sigmoid and ReLU as activation functions.
# Part 2: Layer of neurons. A DenseLayer takes n_inputs and n_neurons. Forward pass produces n_neurons outputs from 1 set of inputs.
# Part 3: Tiny network. Stack 2 layers: Layer(3 inputs, 4 neurons) -> Layer(4 inputs, 2 neurons). Manually set weights (no training). Pass in sample input [0.5, -0.3, 0.8] and print the output. Part 4: Explain it. In comments/README: what does each weight represent? What does the bias do? What changes if you use ReLU vs sigmoid?

import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def relu(x):
  return max(0, x)

# PART 1: Single Neuron Logic

def compute_neuron(inputs, weights, bias, activation_fn):
  total = 0

  for i in range(len(inputs)):
    input_val = inputs[i]
    weight_val = weights[i]
    total = total + (input_val * weight_val)

    z = total + bias
    return activation_fn(z)

# PART 2: The Layer of Neurons

def dense_layer(inputs, weights_matrix, biases, activation_fn):
  layer_outputs = []

  for i in range(len(weights_matrix)):
    neuron_weights = weights_matrix[i]
    neuron_bias = biases[i]

    output = compute_neuron(inputs, neuron_weights, neuron_bias, activation_fn)
    layer_outputs.append(output)

  return layer_outputs

# PART 3: The Tiny Network (Stacking Layers)

l1_weights = [
    [0.1, 0.2, 0.3], [0.4, 0.5, 0.6],
    [0.7, 0.8, 0.9], [-0.1, -0.2, -0.3]
]
l1_biases = [0.5, 0.5, 0.5, 0.5]

l2_weights = [
    [0.5, 0.2, -0.3, 0.1],
    [0.1, -0.4, 0.8, 0.2]
]
l2_biases = [0.1, 0.1]

sample_input = [0.5, -0.3, 0.8]

hidden_layer_out = dense_layer(sample_input, l1_weights, l1_biases, relu)

final_prediction = dense_layer(hidden_layer_out, l2_weights, l2_biases, sigmoid)

print(f"Layer 1 Output (4 neurons): {hidden_layer_out}")
print(f"Final Network Output (2 neurons): {final_prediction}")
