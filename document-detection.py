from ultralytics import YOLO

model= YOLO("weights/best.pt")

docs_path=["docs/1413.jpg",
           "docs/d.jpg",
           "docs/yurt-disi-egitim.jpg",
           "docs/sahis-ornegi-1.jpg",
           "docs/Makbuz-Ornegi.jpg",
           "docs/muhur.jpg"]

# Run batched inference on a list of images
results = model(docs_path, conf=0.4)  # return a list of Results objects

i=0
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    print(boxes.xyxy, boxes.cls, boxes.conf)
    result.show()  # display to screen
    result.save(filename=f"{"result/"+docs_path[i].split("/")[-1]}")  # save to disk
    print(f"{"result/"+docs_path[i].split("/")[-1]}")
    i+=1
