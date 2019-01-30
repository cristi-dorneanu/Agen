from keras.models import Model
from keras.layers import Conv2D, MaxPooling2D, Input, Dense, Flatten


class CnnNetwork:
    def __init__(self, input_shape):
        self.input_shape = input_shape

    def get_model(self, num_of_filters=224, filter_size=(3, 3), conv_stride_size=(1, 1), pool_size=(2, 2),
                  pool_stride_size=(2, 2)):
        input_image = Input(shape=self.input_shape)

        conv_layer = Conv2D(num_of_filters, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            input_image)
        conv_layer = MaxPooling2D(pool_size, pool_stride_size)(conv_layer)

        conv_layer = Conv2D(num_of_filters, filter_size, strides=conv_stride_size, padding='same', activation='relu')(
            conv_layer)
        conv_layer = MaxPooling2D(pool_size, pool_stride_size)(conv_layer)

        flatten = Flatten()(conv_layer)
        fc_layer = Dense(2, activation='softmax')(flatten)

        return Model(inputs=input_image, outputs=fc_layer)
