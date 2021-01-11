## Korean Car Plate Generator

This project randomly generates synthetic images of Korean car license plates.
We separated by types accordingly to their shape and background color.
You can see the types in following image

### The license plates of Korea are as follows.
![Table](/table.jpg)

Please read the [Car plate notification on standards file](https://github.com/Usmankhujaev/KoreanCarPlateGenerator/blob/master/Notification%20on%20standards%20such%20as%20registration%20plates%20for%20Cars.pdf) for detailed legal information.

## How to use the generator.
Make sure you have [OpenCV](https://opencv.org/) installed on your computer.

Before running a code make sure you create a folder named **train/test**. Run the python code to see the results, you should indicate the -t -> train/test to save them in the proper folder, -n -> the number of images to be generated, -p -> type of plate to be generated.  

```bash
python licensePlateType.py -t train/test -n int(number) -p int(Type(1~6))
```
