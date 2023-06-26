# Image-Based Search Engine
It is similar to one of the features of Google, where you can input an image to search for similar products.

The search engine functions based on the principles of feature extraction. We utilized the pre-trained architecture of ResNet-50 to accomplish this task. The functionality is straightforward: when an image is inputted, its features are extracted layer by layer, starting from the basic to the most advanced, using Convolutional Neural Networks (CNN). The code for feature extraction can be found in `feature_extractor.py`.

In the process, an image is inputted and processed to obtain its features. The inputting of the image is demonstrated in `request.py`. The image is then processed in `server_base_64.py`, which involves converting the image to the required file format (in our case, JPG) and subsequently converting it to the base64 format. After making the image compatible, it is saved and sent for feature extraction.

On the other hand, `offline.py` is responsible for extracting the features of all the images existing in our database. These images represent the products we are selling. This task is performed offline, as the images are already stored in the "Images" directory within the static directory. The features of these images are converted to JSON format and stored in the "Features" directory, also located within the static directory.

Now, let's return to the input image part. When an image is inputted, `server_base_64.py` processes it, extracts the features, converts them to JSON format, and compares them with all the features stored in the "Features" folder. The comparison process is based on the "Manhattan distance measure." The differences between the stored features and the input feature are calculated, and the top 30 features with the least difference compared to the inputted feature are chosen.

Each of these features is assigned a unique image ID, which is identified within `server_base_64.py`. These IDs serve as addresses to the corresponding images. Therefore, upon inputting an image into our system, we retrieve the top 30 similar images. This api which I created has been incorporated into the company's website and is referred to as the Image-Based Search Engine.





