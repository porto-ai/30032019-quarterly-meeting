from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.layers import Input, Dropout, Dense, BatchNormalization, \
    Activation, concatenate, GRU, LSTM, Embedding, Flatten, Bidirectional
from keras.layers import GlobalAveragePooling1D, GlobalMaxPooling1D, concatenate, SpatialDropout1D, Conv1D
from keras.models import Model
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping, TensorBoard
from keras import backend as K
from keras import optimizers
from keras.preprocessing.sequence import pad_sequences
from keras import initializers
import tensorflow as tf
from keras import backend as K
import pandas as pd
import sys


LABELS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
try:
    test_labels = pd.read_csv('test_labels.csv')[LABELS]
except:
    print("Failed to load test_labels.csv. ")
    print("Please follow the instructions in the README.md file to download Kaggle data.")
    sys.exit()


def auc(y_true, y_pred):
    auc = tf.metrics.auc(y_true, y_pred)[1]
    K.get_session().run(tf.local_variables_initializer())
    return auc


def get_keras_data(X):
    return {'input_features': X}


def get_score_on_kaggle_test_set(X, model):
    assert X.shape[0] == test_labels.shape[0], "Input has to have %s samples" % test_labels.shape[0]
    _, accuracy, auc = model.evaluate(X, test_labels)
    print("You got a %.3f accuracy and a %.3f ROC-AUC" % (accuracy, auc))
    print("Check Kaggle's leaderboard at https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/leaderboard")


def get_MLP_features_model(number_feats):
    raise NotImplementedError("Implement MLP model")


def get_shallow_features_model(number_feats):
    # Inputs
    input = Input(shape=[number_feats], name="input_features")

    # output
    output = Dense(6, activation='sigmoid')(input)

    # model
    model = Model([input], output)
    model.compile(loss="binary_crossentropy",
                  optimizer='adam', metrics=['accuracy', auc])
    return model


def get_embeddings_model(input_len, num_words, embeddings_dim):
    # Inputs
    input = Input(shape=(input_len,), name="comment_words_idx")

    # Embedding layer
    x = Embedding(num_words, embeddings_dim)(input)
    x = Flatten()(x)

    # Classification head
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.25)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.1)(x)

    # output
    output = Dense(6, activation='sigmoid')(x)

    # model
    model = Model([input], output)
    model.compile(loss="binary_crossentropy",
                  optimizer='adam', metrics=['accuracy', auc])
    return model


def get_pretrained_embeddings_model(input_len, num_words, embeddings_dim, embeddings_matrix):
    # Inputs
    input = Input(shape=(input_len,), name="comment_words_idx")

    # Embedding layer
    x = Embedding(num_words, embeddings_dim, weights=[embeddings_matrix])(input)
    x = Flatten()(x)

    # Classification head
    x = Dense(512, activation='relu')(x)
    x = Dropout(0.25)(x)
    x = Dense(64, activation='relu')(x)
    x = Dropout(0.1)(x)

    # output
    output = Dense(6, activation='sigmoid')(x)

    # model
    model = Model([input], output)
    model.compile(loss="binary_crossentropy",
                  optimizer='adam', metrics=['accuracy', auc])
    return model


def get_recurrent_model(input_len, num_words, embeddings_dim):
    raise NotImplementedError("Implement recurrent model")
