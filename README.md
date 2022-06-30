# Spot-detector-system

Medical face masks are constructed from numerous layers of nonwoven fabric, often 3–5. Unavoidably, some dust may fall on the nonwoven fabric during production.

Despite being produced in a dust-free atmosphere, there is always a potential that some masks will be faulty because of contamination in the raw materials. On the automated production process, the cloth is exposed to UVC radiation to kill bacteria before being utilized to make masks. However, it is challenging to remove noticeable flecks. It is quite challenging for the QC inspector to identify the contaminated masks when numerous layers of fabric are piled and used to create masks.

The firm placed a person at each manufacturing line at the raw material shelf to manually check for dust or insects in order to maintain the quality of the masks. Every time a worker discovers an unexpected item, the entire production line must stop while it waits for the worker to remove the contaminated material and replace it. You can imagine how tedious this job can be watching 3 ~ 4 layers of fabric for hours. On the other hand, because of Covid-19, the face mask market has extended to the general public. Conventional surgical masks are usually solid-colored like white, blue, or green. These masks are fine being used in the hospital but they are hard to be accepted by normal people, especially when people wear masks on a daily basis. As a result, several mask producers use textiles with graphic patterns as the surface layer of their goods to add a touch of fashion. Because of this, it is extremely difficult to detect dust flecks on a moving fabric.

## System design
To solve the problem, our team designed and implemented a defects detection system leveraging the power of computer vision and machine learning.

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
