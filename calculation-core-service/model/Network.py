from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D, Input, Dense, Flatten, Dropout, Multiply, \
    BatchNormalization


class CnnNetwork:
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def get_model(self, output_type, num_of_filters=64, filter_size=(3, 3), conv_stride_size=(1, 1), pool_size=(2, 2),
                  pool_stride_size=(2, 2)):
        input_image = Input(shape=self.input_shape)

        conv_layer = Conv2D(64, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            input_image)
        conv_layer = MaxPooling2D(pool_size, pool_stride_size)(conv_layer)

        conv_layer = Conv2D(64, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            conv_layer)
        conv_layer = MaxPooling2D(pool_size, pool_stride_size)(conv_layer)

        conv_layer = Conv2D(128, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            conv_layer)

        conv_layer = Conv2D(128, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            conv_layer)
        conv_layer = MaxPooling2D(pool_size, pool_stride_size)(conv_layer)

        conv_layer = BatchNormalization()(conv_layer)

        flatten = Flatten()(conv_layer)

        output_layer = None

        if output_type == 'age':
            output_layer = Dense(units=11, activation='softmax', kernel_initializer='random_uniform')(flatten)
        elif output_type == 'gender':
            output_layer = Dense(units=2, activation='softmax', kernel_initializer='random_uniform')(flatten)

        return Model(inputs=input_image, outputs=output_layer)
