'''
@Description: 人脸识别
@Version: 1.0
@Autor: lhgcs
@Date: 2019-10-23 12:12:22
@LastEditors: lhgcs
@LastEditTime: 2019-10-23 14:55:21
'''

# 预训练
'''
@description: 该函数将读取所有的训练图像，从每个图像检测人脸并将返回两个相同大小的列表，分别为脸部信息和标签
@param {type} 
@return: 
'''
def prepare_training_data(data_folder_path):
    # 获取数据文件夹中的目录（每个主题的一个目录）
    dirs = os.listdir(data_folder_path)

    # 两个列表分别保存所有的脸部和标签
    faces = []
    labels = []

    # 浏览每个目录并访问其中的图像
    for dir_name in dirs:
        # dir_name(str类型)即标签
        label = int(dir_name)
        # 建立包含当前主题主题图像的目录路径
        subject_dir_path = data_folder_path + "/" + dir_name
        # 获取给定主题目录内的图像名称
        subject_images_names = os.listdir(subject_dir_path)

        # 浏览每张图片并检测脸部，然后将脸部信息添加到脸部列表faces[]
        for image_name in subject_images_names:
            # 建立图像路径
            image_path = subject_dir_path + "/" + image_name
            # 读取图像
            image = cv2.imread(image_path)
            # 显示图像0.1s
            cv2.imshow("Training on image...", image)
            cv2.waitKey(100)

            # 检测脸部
            face, rect = detect_face(image)
            # 我们忽略未检测到的脸部
            if face is not None:
                #将脸添加到脸部列表并添加相应的标签
                faces.append(face)
                labels.append(label)

    cv2.waitKey(1)
    cv2.destroyAllWindows()
    #最终返回值为人脸和标签列表
    return faces, labels


# 使用opencv自带的识别器来进行训练了
#调用prepare_training_data（）函数
faces, labels = prepare_training_data("training_data")

#创建LBPH识别器并开始训练，当然也可以选择Eigen或者Fisher识别器
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(faces, np.array(labels))



'''
@description: 根据给定的（x，y）坐标标识出人名
@param {type} 
@return: 
'''
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (128, 128, 0), 2)



# 训练完毕后就可以进行预测了，在这之前我们可以设定一下预测的格式，包括用矩形框框出人脸并标出其名字，当然最后别忘了建立标签与真实姓名直接的映射表：

#建立标签与人名的映射列表（标签只能为整数）
subjects = ["jiaju", "jiaqiang"]

# 此函数识别传递的图像中的人物并在检测到的脸部周围绘制一个矩形及其名称
def predict(test_img):
    #生成图像的副本，这样就能保留原始图像
    img = test_img.copy()
    #检测人脸
    face, rect = detect_face(img)
    #预测人脸
    label = face_recognizer.predict(face)
    # 获取由人脸识别器返回的相应标签的名称
    label_text = subjects[label[0]]

    # 在检测到的脸部周围画一个矩形
    draw_rectangle(img, rect)
    # 标出预测的名字
    draw_text(img, label_text, rect[0], rect[1] - 5)
    #返回预测的图像
    return img

