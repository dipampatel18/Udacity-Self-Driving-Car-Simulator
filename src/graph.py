#!/usr/bin/env python3

# Plotting the Graph of Training - Validation Loss & Accuracy for all the Epochs

# Importing Library
import matplotlib.pyplot as plt

# Initializing the x and y values
x_epoch = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_train_loss = [0.0476, 0.0297, 0.0283, 0.0263, 0.0265, 0.0253, 0.0254, 0.0254, 0.0238, 0.0236]
y_train_acc = [0.3331, 0.3290, 0.3166, 0.3187, 0.3224, 0.3317, 0.3292, 0.3336, 0.3282, 0.3260]
y_val_loss = [0.0221, 0.0190, 0.0236, 0.0178, 0.0217, 0.0167, 0.0214, 0.0194, 0.0210, 0.0245]
y_val_acc = [0.7800, 0.8150, 0.7950, 0.7950, 0.8137, 0.8087, 0.7963, 0.8213, 0.8050, 0.7925]

# Plotting 
plt.plot(x_epoch, y_train_loss, label='Training Loss')
plt.plot(x_epoch, y_train_acc, label='Training Accuracy')
plt.plot(x_epoch, y_val_loss, label='Validation Loss')
plt.plot(x_epoch, y_val_acc, label='Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
