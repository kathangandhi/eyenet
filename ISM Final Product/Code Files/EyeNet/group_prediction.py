from keras.models import model_from_json
from pathlib import Path
from keras.preprocessing import image
import numpy as np
from keras.applications import vgg16, vgg19

def sample_testing(p):
    # Load the json file that contains the model's structure
    f = Path("model_structure.json")
    model_structure = f.read_text()

    # Recreate the Keras model object from the json data
    model = model_from_json(model_structure)

    # Re-load the model's trained weights
    model.load_weights("model_weights.h5")

    # Path to folders with testing data
    symptoms_path = p / "symptoms"
    no_symptoms_path = p / "nosymptoms"

    images = []
    expected = np.concatenate([np.zeros(10), np.ones(10)])
    output = []

    no_symptoms_indices = np.arange(0, 1467)
    no_symptoms_sample = np.random.choice(no_symptoms_indices, 10)

    i = 0
    for img in no_symptoms_path.glob("*.jpeg"):
        if (i in no_symptoms_sample):
            # Load an image file to test, resizing it to _____ pixels (as required by this model)
            img = image.load_img(img, target_size=(70, 60))

            # Convert the image to a numpy array
            image_array = image.img_to_array(img)

            # Add a forth dimension to the image (since Keras expects a bunch of images, not a single image)
            images = np.expand_dims(image_array, axis=0)

            # Normalize the data
            images = vgg16.preprocess_input(images)

            # Use the pre-trained neural network to extract features from our test image (the same way we did to train the model)
            feature_extraction_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(70, 60, 3))
            features = feature_extraction_model.predict(images)

            # Given the extracted features, make a final prediction using our own model
            results = model.predict(features)

            # Since we are only testing one image with possible class, we only need to check the first result's first element
            single_result = results[0][0]

            # Predict actual result
            if (int(single_result * 100) <= 50):
                #print("This image indicates: NO SYMPTOMS")
                output.append(0)
            else:
                #print("This image indicates: SYMPTOMS")
                output.append(1)

        i += 1

    symptoms_indices = np.arange(0, 595)
    symptoms_sample = np.random.choice(symptoms_indices, 10)

    j = 0
    for img in symptoms_path.glob("*.jpeg"):
        if (j in symptoms_sample):
            # Load an image file to test, resizing it to _____ pixels (as required by this model)
            img = image.load_img(img, target_size=(70, 60))

            # Convert the image to a numpy array
            image_array = image.img_to_array(img)

            # Add a forth dimension to the image (since Keras expects a bunch of images, not a single image)
            images = np.expand_dims(image_array, axis=0)

            # Normalize the data
            images = vgg16.preprocess_input(images)

            # Use the pre-trained neural network to extract features from our test image (the same way we did to train the model)
            feature_extraction_model = vgg16.VGG16(weights='imagenet', include_top=False, input_shape=(70, 60, 3))
            features = feature_extraction_model.predict(images)

            # Given the extracted features, make a final prediction using our own model
            results = model.predict(features)

            # Since we are only testing one image with possible class, we only need to check the first result's first element
            single_result = results[0][0]

            # Predict actual result
            if (int(single_result * 100) <= 50):
                #print("This image indicates: NO SYMPTOMS")
                output.append(0)
            else:
                #print("This image indicates: SYMPTOMS")
                output.append(1)

        j += 1

    print(expected)
    print(output)
    return int(sum(np.equal(expected, output))/20 * 100)