
import tkinter as tk
from tkinter import filedialog

import numpy as np
import tensorflow as tf
import cv2

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

root = tk.Tk()

# input
label1 = tk.Label(root, text='SelectPath：')
label1.grid(row=0, column=0)
label2 = tk.Label(root, text='Prediction：')
label2.grid(row=1, column=0)

# Filepath
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('FangSong', 10), width=50, state='readonly')
entry.grid(row=0, column=1, padx=20, pady=15)

entry_text2 = tk.StringVar()
entry2 = tk.Entry(root, textvariable=entry_text2, font=('FangSong', 10), width=50, state='readonly')
entry2.grid(row=1, column=1, padx=20, pady=15)

"""
# Imageshow
fig = plt.figure(figsize=(10,4),dpi=100)#图像比例
f_plot =fig.add_subplot(111)#划分区域
canvas_spice = FigureCanvasTkAgg(fig,root)
canvas_spice.get_tk_widget().place(x=20,y=200)

t = tk.Text(root, width=30, height=1.5)
t.grid(row=8, column=3, padx=10, pady=5)
#t.pack()
"""

# Button SelectPath
def get_path():
    global path
    path = filedialog.askopenfilename(title='Please Select the File')
    entry_text.set(path)
    """
    image=cv2.imread(path)
    image_resized= cv2.resize(image, (224,224))
    
    f_plot.clear()
    plt.imshow(image)
    canvas_spice.draw()
    """

# Button Prediction
def show():
    # 加载模型
    model = tf.keras.models.load_model('./model/my_model.h5')
    # 图片读取路径
    
    
    image=cv2.imread(path)
    image_resized= cv2.resize(image, (224,224))
    image=np.expand_dims(image_resized,axis=0)
    # 预测环节
    # prediction
    pred=model.predict(image)
    pred = np.int(np.round(pred))
    # load dataset
    def load_data(data_dir='./used',split_rate=0.2,batch_size=32,image_size=(224,224),seed=123):
        train_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            color_mode="rgb",
            validation_split=split_rate,
            subset="training",
            seed=seed,
            batch_size=batch_size,
            image_size=image_size)

        val_ds = tf.keras.preprocessing.image_dataset_from_directory(
            data_dir,
            color_mode="rgb",
            validation_split=split_rate,
            subset="validation",
            seed=seed,
            batch_size=batch_size,
            image_size=image_size)
        return train_ds, val_ds
    train_ds, val_ds = load_data('./data/used')
    
    # output the prediction result of the image with probability
    def transfer_names(val_ds):
        class_names = []
        for name in val_ds.class_names:
            if name=='front':
                class_names.append('criminal')
            else:
                class_names.append('Not criminal')
        return class_names
    class_names = transfer_names(val_ds)
    output_class=class_names[int(pred)]
    
    string_1 = 'Predicted as '+output_class+' with prob '+str(model.predict(image)[0][0])
    entry_text2.set(string_1)
    
    


button1 = tk.Button(root, text='SelectPath', command=get_path).grid(row=17, column=1,
                                            sticky=tk.W, padx=30, pady=5)
button2 = tk.Button(root, text='Prediction', command=show).grid(row=27, column=1,
                                            sticky=tk.W, padx=30, pady=5)
button3 = tk.Button(root, text='Exit', command=root.quit).grid(row=37, column=1,
                                          sticky=tk.E, padx=30, pady=5)

tk.mainloop()

