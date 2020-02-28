from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, BatchNormalization
from keras.layers.advanced_activations import LeakyReLU

def build_model(width, height, LR, output):

    model = Sequential()
    model.add(Conv2D(32, (3, 3), input_shape=(3, 150, 150)))
    model.add(LeakyReLU(alpha=.01))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())

    model.add(Conv2D(32, (3, 3)))
    model.add(LeakyReLU(alpha=.01))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())

    model.add(Conv2D(64, (3, 3)))
    model.add(LeakyReLU(alpha=.01))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(BatchNormalization())

    model.add(Flatten())
    model.add(Dense(4096))
    model.add(LeakyReLU(alpha=.01))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(512))
    model.add(LeakyReLU(alpha=.01))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))

    model.add(Dense(output))
    model.add(LeakyReLU(alpha=.01))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))




    model.optimizer('adam')

    return model