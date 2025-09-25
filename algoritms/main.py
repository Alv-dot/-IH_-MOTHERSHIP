import asyncio
import concurrent.futures
from ultralytics import YOLO
import os
import json

# Load a model
model = YOLO("yolo11m.pt")

image_data = [f"./image_data/{image}" for image in os.listdir("./image_data/")]
# suppose 25



def yolo_processing(img_list: list, batch_id: int):
    results = model(source=img_list, conf=0.15)
    image_data = {}
    i = len(img_list)
    for result in results:
        coords = []
        human_boxes = result.boxes[result.boxes.cls == 0]
        if len(human_boxes) > 0:  # Only save if humans are detected
            for j in range(len(human_boxes)):
                xyxy = human_boxes.xyxy[j].tolist()  # [x1, y1, x2, y2]
                conf = float(human_boxes.conf[j].item())
                #print(f"Image: {i}, Human {j + 1}: BBox = {xyxy}, Confidence = {conf:.2f}")
                coords.append(xyxy)
                image_data[f"img{i}"] = {"coords": coords, "confidence": f"{conf:.2f}",}
            # Replace boxes in the result with only human boxes
            result.boxes = human_boxes
            # result.show()  # display to screen
            result.save(filename=f"./results/result{i}.jpg")
            i -= 1
    with open(f"./metadata/batch{batch_id}.json", "w") as f:
        json.dump(image_data, f)

    #print(image_data)

async def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        chunk_size = 5
        loop = asyncio.get_running_loop()
        task_list = [image_data[i:i + chunk_size] for i in range(0, len(image_data), chunk_size)]
        tasks = []
        batch_id = 1
        for batch in task_list:
            tasks.append(loop.run_in_executor(executor, yolo_processing, batch, batch_id))
            batch_id += 1
        results = await asyncio.gather(*tasks)
        print("tasks completed", results)


if __name__ == "__main__":
    asyncio.run(main())

