The world file is [this one](ConveyorImport/conveyor_world.sdf) and it contains all 3 conveyor types and the [plate](ConveyorImport/plate).
Intertias of the models are not tunned yet, so most are using a standart value (standard from AI). 

In the conveyor import there are 3 different conveyor models in .obj format.

1) Straight conveyor with a 1 m leght [in this folder](ConveyorImport/straight_1m/meshes)
2) 90 deg. to the left conveyor with a 1 m leght [in this folder](ConveyorImport/left_1m/meshes)
3) 90 deg. to the right conveyor with a 1 m leght [in this folder](ConveyorImport/right_1m/meshes)

Also some other stls from the task to test out the camera.

Looking at the [left turning conveyor](ConveyorImport/left_1m) we can see that there are 2 models description files 
[with camera and lights](ConveyorImport/left_1m/model_camera.sdf) and 
[without camera and lights](ConveyorImport/left_1m/model.sdf). To change between one or the other we need to change the code 
[here](ConveyorImport/left_1m/model.config). like so "model_camera.sdf" <-> "model.sdf".

Файл мира [здесь](ConveyorImport/conveyor_world.sdf), и он содержит все 3 типа конвейеров и [плиту](ConveyorImport/plate).

Инерции моделей пока не настроены, поэтому у большинства используется стандартное значение (стандартное от ИИ).

В импорте конвейеров есть 3 различные модели конвейеров в формате .obj.

Прямой конвейер длиной 1 м [in this folder](ConveyorImport/straight_1m/meshes)

Конвейер с поворотом на 90° влево длиной 1 м [in this folder](ConveyorImport/left_1m/meshes)

Конвейер с поворотом на 90° вправо длиной 1 м [in this folder](ConveyorImport/right_1m/meshes)

Также есть несколько других STL-файлов из задания для тестирования камеры.

Глядя на конвейер с поворотом [влево](ConveyorImport/left_1m) , видно, что есть 2 файла описания моделей:
[с камерой и освещением](ConveyorImport/left_1m/model_camera.sdf) и [без камеры и освещения](ConveyorImport/left_1m/model.sdf). - 
без камеры и освещения. Чтобы переключаться между ними, нужно изменить код
[here](ConveyorImport/left_1m/model.config), например так: "model_camera.sdf" <-> "model.sdf".
