import numpy as np
import joblib
from keras.preprocessing import image
from keras.applications import vgg16

def extract(p):
    # Path to folders with training data
    symptoms_path = p / "symptoms"
    no_symptoms_path = p / "nosymptoms"

    images = []
    labels = []

    no_symptoms_indices = np.arange(0, 1467)
    no_symptoms_sample = np.random.choice(no_symptoms_indices, 90)

    i = 0
    for img in no_symptoms_path.glob("*.jpeg"):
        if(i in no_symptoms_sample):
            # Load the image from disk
            img = image.load_img(img, target_size=(70, 60))

            # Convert the image to a numpy array
            image_array = image.img_to_array(img)

            # Add the image to the list of images
            images.append(image_array)

            # For each 'no symptoms' image, the expected value should be 0
            labels.append(0)
        i += 1

    symptoms_indices = np.arange(0, 595)
    symptoms_sample = np.random.choice(symptoms_indices, 60)

    j = 0
    for img in symptoms_path.glob("*.jpeg"):
        if(j in symptoms_sample):
            # Load the image from disk
            img = image.load_img(img, target_size=(70, 60))

            # Convert the image to a numpy array
            image_array = image.img_to_array(img)

            # Add the image to the list of images
            images.append(image_array)

            # For each 'symptoms' image, the expected value should be 1
            labels.append(1)
        j += 1

    # Create a single numpy array with all the images we loaded
    x_train = np.array(images)

    # Also convert the labels to a numpy array
    y_train = np.array(labels)

    # Normalize image data to 0-to-1 range
    x_train = vgg16.preprocess_input(x_train)

    # Load a pre-trained neural network to use as a feature extractor
    pretrained_nn = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(70, 60, 3))

    # Extract features for each image (all in one pass)
    features_x = pretrained_nn.predict(x_train)

    # Save the array of extracted features to a file
    joblib.dump(features_x, "x_train.dat")

    # Save the matching array of expected values to a file
    joblib.dump(y_train, "y_train.dat")