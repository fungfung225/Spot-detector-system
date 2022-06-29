# Spot-detector-system

Medical face masks are made of multiple(usually 3~5) layers of nonwoven fabric. During the production of nonwoven fabric, inevitably, some dust or even insects may fall on the fabric.

Although masks are manufactured in a dust-free environment, there are still chances that some masks are defective due to the contamination which comes with the raw material. For bacteria, the fabric is irradiated under UVC light on the automated production line right before it is used to manufacture masks. However, it is difficult to get rid of large specks. When multiple layers of fabric are stacked and become 
masks, it is extremely hard for the QC inspector to pick out the contaminated masks. To maintain the quality of masks, the factory put a worker at each production line by the raw material shelf and manually checks if there's dust or insect. Whenever the worker finds something unexpected, the whole production line must stop and wait for the worker to cut off the contaminated part and replace the fabric. You can imagine how tedious this job can be watching 3 ~ 4 layers of fabric for hours. On the other hand, because of Covid-19, the face mask market has extended to the general public. Conventional surgical masks are usually solid-colored like white, blue, or green. These masks are fine being used in the hospital but they are hard to be accepted by normal people, especially when people wear masks on a daily basis. Therefore, many mask manufacturers introduce some fashion into their products by using fabrics with graphic patterns as the surface layer. As a result, it's nearly impossible for a person to find dust specks on a fast-moving fabric like that.

## System design
To solve the problem, we, the R&D team, designed and implemented a fabric defects detection system leveraging the power of computer vision and machine learning.

![螢幕擷取畫面 2022-06-29 224408](https://user-images.githubusercontent.com/90837134/176465800-18428ee7-1d89-4abe-aaf9-dd8d3979878e.png)

The figure above shows the main hardware components in the system. Basically, the fabric goes through the lightbox where there's a camera constantly watching the fabric.

![螢幕擷取畫面 2022-06-29 224559](https://user-images.githubusercontent.com/90837134/176466189-bc6db7f2-408c-45f6-9c72-159272dccdf9.png)


The application core serves as a control layer coordinating threads and different modules so that the system works together efficiently with limited resources(number of CPU cores, RAM size, computational power, etc.).
The power manager will communicate with the UPS(Uninterruptible Power Supply). In case of a power outage of the production line, it will notify the application core and the corresponding event log will be recorded and uploaded to the cloud. Then the nano will turn itself off safely.
GPIO Handler is responsible for sending and receiving signals from our custom-made PCB. For example, it can turn on and off the lightbox, start/stop the alarm, and communicate with the MCU.
The frame processing engine contains the core functions. It will capture the video feed, pre-process each frame, detect abnormalities, render result images and send them to the user interface.
Logger is a daemon thread that runs in the background recording the system status. The Cloud handler is in charge of exchanging data between the nano and Google Cloud.

## Result
![螢幕擷取畫面 2022-06-30 004111](https://user-images.githubusercontent.com/90837134/176490648-99df6bd7-9887-4625-8dad-80811e65c423.png)
