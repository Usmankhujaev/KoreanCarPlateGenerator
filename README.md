# KoreanCarPlateGenerator
Korean Car Plate Generator
------------------------
This project is automatically generate synthetic Korean car license plates.
We separated by types accordingly to their shape and background color.
You can see the types in following image

The license plates of Korea are as follows.
![Alt text](/image/table.jpg)

Please read the Notification_on_standards_such_as_registration_plates_for_Cars.pdf for detailed legal information.

How to use the generator
Before running a code make sure you create a folder named train/test 

python licensePlateType.py -t train/test -n int(number) -p int(Type(1~6))
