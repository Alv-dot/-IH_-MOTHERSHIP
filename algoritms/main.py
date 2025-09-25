from ultralytics import YOLO
import os

def main():
    # Load a model
    model = YOLO("yolo11n.pt")  # pretrained YOLO11n model

    img_list = [f"./image_data/{image}" for image in os.listdir("./image_data/")]
    # Run batched inference on a list of images
    results = model(img_list)  # return a list of Results objects
    # Process results list
    i = len(img_list)
    for result in results:
        human_boxes = result.boxes[result.boxes.cls == 0]

        if len(human_boxes) > 0:  # Only save if humans are detected
            # Replace boxes in the result with only human boxes
            result.boxes = human_boxes
            masks = result.masks  # Masks object
            keypoints = result.keypoints  # Keypoints object
            probs = result.probs  # Probs object for classification
            obb = result.obb  # Oriented boxes object for OBB outputs
            # result.show()  # display to screen
            result.save(filename=f"./results/result{i}.jpg")
            i -= 1

if __name__ == "__main__":
    main()
